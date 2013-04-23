#Verify if the matrix is consistent on each row or empty
def verifyMatrix(matrix):
  
  if (len(matrix) == 0): #empty matrix is invalid
    return False 
    
  rowSize = len(matrix[0])
  for i in (0, len(matrix)-1):
    if len(matrix[i]) != rowSize:
      return False
  return True

#Verify if the elements have all been printed
#Could have cheated and wrapped the whole while loop in a try/catch 
def checkBounds(current, upperBound):
  return current >= upperBound


#Takes a MxN matrix and prints in a spiral form
def spiralPrinter(matrix):
  
  #Verify is Matrix is printable
  if not verifyMatrix(matrix):
    raise Exception('Invalid matrix')
    
  totalElements = len(matrix)*len(matrix[0]) #get total elements
  resultString = ''
  printedElements = 0 #counter for printer elements
  #current position at matrix
  row = 0
  column = 0
  
  #cache all the values that get calculated repeatedly
  rowSize = len(matrix)
  columnSize = len(matrix[0]) 
  
  while True:
    #print top
    for column in range(column, columnSize + column):
      resultString += str(matrix[row][column]) + ', '
      printedElements += 1
    
    #print right
    row += 1
    rowSize -= 1
    if checkBounds(printedElements, totalElements):
      break
    for row in range(row, rowSize + row):
      resultString += str(matrix[row][column]) + ', '
      printedElements += 1
    
    #print bottom
    column -= 1
    columnSize -= 1
    if checkBounds(printedElements, totalElements):
      break
    for column in range(column, column - columnSize, -1):
      resultString += str(matrix[row][column]) + ', ' 
      printedElements += 1 
    
    #print left
    row -= 1
    rowSize -= 1
    if checkBounds(printedElements, totalElements):
      break
    for row in range(row, rowSize - row, -1):
      resultString += str(matrix[row][column]) + ', '
      printedElements += 1

    #cleanup for next iteration
    if checkBounds(printedElements, totalElements):
      break    
    column += 1
    columnSize -= 1
    
  return resultString[:-2:] #remove last ', '
