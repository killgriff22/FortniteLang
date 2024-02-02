file = open("input.fortnite","r").readlines()

variables = {}
#in order to add a jump instruction we have to switch from a for loop to a while loop
#as a for loop abstracts away (hides) the index, even if we use enumerate, the "i" variable
#is immutable (cannot be changed) 
program_counter= 0 # the index into the file
while program_counter < len(file): # loop until we reach then end of the file
  line = file[program_counter]
  data = line.split(" ")
  instruction = data.pop(0)
  data[-1] = data[-1].strip()
  match instruction:
    case "crank":#Print
      if data[0] in variables.keys():
        if variables[data[0]] == True:
          print("bullet")
        elif variables[data[0]] == False:
          print("reboot")
        elif not variables[data[0]]:
          print("bust")
        else:
          print(variables[data[0]])
        continue
      data = " ".join(data)
      print(data)
    case "pump":#Add
      if data[0] in variables.keys():
        a = variables[data[0]]
      else:
        a = int(data[0])
      if data[1] in variables.keys():
        b = variables[data[1]]
      else:
        b = int(data[1])
      if len(data) == 3:
        variables[data[2]] = a+b
        continue
      print(a+b)
    case "down":#Subtract
      if data[0] in variables.keys():
        a = variables[data[0]]
      else:
        a = int(data[0])
      if data[1] in variables.keys():
        b = variables[data[1]]
      else:
        b = int(data[1])
      if len(data) == 3:
        variables[data[2]] = a-b
        continue
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
      #if data[0] is an existing var, and that var is a number, set the program counter to the number stored in the variable
      if data[0] in variables.keys() and type(variables[data[0]]) == int:
        program_counter = variables[data[0]]
      #otherwise, if its a number, then set the program counter to that number 
      elif data[0].isdigit():
        program_counter = int(data[0])
  program_counter += 1 # increment the program counter