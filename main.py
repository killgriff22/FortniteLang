file = open("input.fortnite","r").readlines()

variables = {}

for line in file:
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