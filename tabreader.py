import os

def process_tab(filename):
  g = []
  d = []
  a = []
  e = []
  with open(filename) as txt_file:
    # First, split each bass string. 
    for line in txt_file:
      if line.startswith('G'):
        g.append(line)
      elif line.startswith('D'):
        d.append(line)
      elif line.startswith('A'):
        a.append(line)
      elif line.startswith('E'):
        e.append(line)
      else:
        pass
    if check_valid(g,d,a,e,filename):
      g_measures = clean_measures(g)
      d_measures = clean_measures(d)
      a_measures = clean_measures(a)
      e_measures = clean_measures(e)
      print(g_measures)
      print(d_measures)
      print(a_measures)
      print(e_measures)
      return("Imported File: {}".format(os.path.split(filename)[1]))
    else:
      return("{} does not contain bass tabs!\nPlease select a valid .txt file.".format(os.path.split(filename)[1]))

def check_valid(g,d,a,e,filename):
  if len(g) < 1 or (len(d) < 1) or (len(a) < 1) or (len(e) < 1):
    print("{} does not contain bass tabs!\nPlease select a valid .txt file.".format(os.path.split(filename)[1]))
    return(False)
  else:
    print("Imported File: {}".format(os.path.split(filename)[1]))
    return(True)

def has_numbers(str_input):
  return any(char.isdigit() for char in str_input)

def has_hyphen(str_input):
  return any(char in '-' for char in str_input)

def only_hyphen(str_input):
  return all(char in '-' for char in str_input)

def clean_measures(string):
  measures = [measure.replace('\n','') for measure in string]
  measures = [measure.split('|') for measure in measures] #splitting measure by measure symbol |
  measures = [line for measure in measures for line in measure] #flattening list of lists into list
  for i in range(len(measures)):
    if has_hyphen(measures[i]): #only keeping elements containing hyphens
      pass
    else:
      measures[i] = ''
  measures = [x for x in measures if x] #removing empty string
  return(measures)


