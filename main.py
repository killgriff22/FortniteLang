file = open("input.fortnite","r").readlines()

variables = {}
#in order to add a jump instruction we have to switch from a for loop to a while loop
#as a for loop abstracts away (hides) the index, even if we use enumerate, the "i" variable
#is immutable (cannot be changed) 
#i also removed all the continues and replaced them with else statements
program_counter= 0 # the index into the file
while program_counter < len(file): # loop until we reach then end of the file
  line = file[program_counter]
  data = line.split(" ")
  instruction = data.pop(0)
  data[-1] = data[-1].strip()
  match instruction:
    case "crank":#Print
      if data[0] in variables:
        #i tried to run my test program and found that 1 & 0 output true & false
        #i can also see that "if not x" also means "if x == False" so i changed "if not x" to "if x == None"
        if type(variables[data[0]]) in [bool,None]:
          if variables[data[0]] == True:
            print("bullet")
          elif variables[data[0]] == False:
            print("reboot")
          elif variables[data[0]] == None:
            print("bust")
        else:
          print(variables[data[0]])
      else:
        data = " ".join(data)
        print(data)
    case "pump":#Add
      if data[0] in variables:
        a = variables[data[0]]
      else:
        a = int(data[0])
      if data[1] in variables:
        b = variables[data[1]]
      else:
        b = int(data[1])
      if len(data) == 3:
        variables[data[2]] = a+b
      else:
        print(a+b)
    case "down":#Subtract
      if data[0] in variables:
        a = variables[data[0]]
      else:
        a = int(data[0])
      if data[1] in variables:
        b = variables[data[1]]
      else:
        b = int(data[1])
      if len(data) == 3:
        variables[data[2]] = a-b
      else:
        print(a-b)
    case "res":#write a variable
      name = data.pop(0)
      data_str = " ".join(data)
      variables[name] = " ".join(data)
      if len(data) == 0 or data[0] == "bust":
        variables[name] = None
      elif data[0].isdigit():
        variables[name] = int(data[0])
      elif "[" in data_str or "{" in data_str:
        variables[name] = eval(data_str)
      elif data[0] == "bullet":
        variables[name] = True
      elif data[0] == "reboot":
        variables[name] = False
    case "jump":#jump
      #only using the first argument, data[0] is the index to jump to
      #we subtract 1 because we want to be able to reference the line number provided by our IDE, not the index
      #(IDE line numbers count from 1, while indexs count from 0, so we must decrement)
      #if data[0] is an existing var, and that var is a number, set the program counter to the number stored in the variable
      if data[0] in variables and type(variables[data[0]]) == int:
        program_counter = variables[data[0]]-1 if not variables[data[0]]-1 < 0 else variables[data[0]]
        #inline if statement says that if the number-1 is less than 0 then just use the variable
        #this lets us use negative indexes and have 0 & 1 both represent the beginning of the program
      #otherwise, if its a number, then set the program counter to that number 
      elif data[0].isdigit():
        program_counter = int(data[0])-1 if not int(data[0])-1 < 0 else int(data[0])
      continue #this should only be used to skip the increment that currently comes right after this line.
  program_counter += 1 # increment the program counter