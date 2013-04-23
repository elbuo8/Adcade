#Scheduler for priority queue of trucks
def paradeScheduler(parade):
  
  status = '' #contains the log of trials
  totalTrucks = 0 #counter to be updated with the total number of trucks to be organized
  
  for line in parade:
    
    if line.strip() == '0': #Exit clause
      return status[:-1:] #Remove unnecary \n at the end
      
    elif (len(line.strip()) == 1): #Store the amount of upcoming trucks
      totalTrucks = int(line)
      
    else:
      paradeQueue = map(int, line.strip().split(' ')) #Parse the trucks into a queue
      
      if (len(paradeQueue) != totalTrucks): #Verify that the number of trucks is consistent
        raise Exception('Inconsistent Number of Trucks')
        
      sideStreetStack = [] #Alley
      counter = 1 
      
      while True:
        #At the end of this iteration there will be one element in the queue||stack saving 1 iteration
        if(counter==totalTrucks): 
          status += 'yes\n'
          break
        #If there is an truck in queue and it =='s the counter, clear it
        elif(len(paradeQueue) > 0 and paradeQueue[0] == counter):
          paradeQueue.pop(0)
          counter += 1
        
        #If there is an truck in top of the stack and it =='s the counter, clear it 
        elif(len(sideStreetStack) > 0 and sideStreetStack[-1] == counter):
          sideStreetStack.pop()
          counter += 1
        
        #Here is the fun part. If the that is going to be pushed into the stack is bigger than
        #the current top, it won't be pushed and the code breaks on the else saving a bunch of iterations.
        elif(len(sideStreetStack) == 0 or paradeQueue[0] < sideStreetStack[-1]):
          sideStreetStack.append(paradeQueue.pop(0))
          
        else:
          status += 'no\n'
          break