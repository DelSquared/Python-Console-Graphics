import numpy as np 
import os
import time

x=60
y=30 #canvas dims

def Draw(): #draw loop
  A = np.zeros((x,y),dtype=np.str)
  A[np.random.randint(0,x),np.random.randint(0,y)] = 'X'
  return A
  
#------Frame handling-------

screen = np.zeros((x,y),dtype=np.str)

while True:
  os.system('cls')
  screen[:,:]=Draw()
  screenstr = (x+2)*'-'+'\n'
  for i in range(y):
    screenstr+='|'
    for j in range(x):
      if screen[j,i]=='':
        screenstr+=' '
      elif screen[j,i]=='X':
        screenstr+='X'
    screenstr+='|\n'
  screenstr += (x+2)*'-'+'\n'
  print(screenstr,flush=True)
  time.sleep(0.5)
