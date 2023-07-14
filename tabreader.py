import os
import re
from xml.dom import minidom
import xml.etree.ElementTree as ET
from notedictionaries import MidiG, MidiD, MidiA, MidiE
from scorebuilder import slicer, to_note
from xmlbuilder import clean_notes, xml_build

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
 
      # Converts tab note values to MIDI note values:
      g_midi, d_midi, a_midi, e_midi = to_midi(g_measures, d_measures, a_measures, e_measures)

      # Turns each measure into an array of hyphens and MIDI notes:
      g_sliced, d_sliced, a_sliced, e_sliced = slicer(g_midi, d_midi, a_midi, e_midi)

      # Converts MIDI note values to standard note names (e.g., Eb2):
      g_notes, d_notes, a_notes, e_notes = to_note(g_sliced, d_sliced, a_sliced, e_sliced)
      seq = clean_notes(g_notes, d_notes, a_notes, e_notes)
      xml_build(seq,filename)

      #Info text displayed in GUI underneath Import Tab button:
      print("Exported File: {}.xml".format(os.path.split(filename)[1][:-4]))
      return("File exported as: {}.xml".format(os.path.split(filename)[1][:-4]))
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
  measures = [measure.split('|') for measure in measures] #Splitting measure by measure symbol "|"
  measures = [line for measure in measures for line in measure] #Flattening list of lists into list
  for i in range(len(measures)):
    if has_hyphen(measures[i]): #Only keeping elements containing hyphens
      pass
    else:
      measures[i] = ''
  measures = [x for x in measures if x] #Removing empty strings
  measures = [x for x in measures ]
  
  regex = re.compile('[^\d\-]+') 
  #Replaces non-digits and non-hyphens with hyphens
  for i in range(len(measures)):
    measures[i] = regex.sub('-', measures[i])
  return(measures)

def to_midi(g_list, d_list, a_list, e_list):
  g_midi, d_midi, a_midi, e_midi = ([] for i in range(4))

  for m in g_list:
    g_midi.append(re.sub(r'\d+', lambda x: MidiG[x.group()], m))

  for m in d_list:
    d_midi.append(re.sub(r'\d+', lambda x: MidiD[x.group()], m))

  for m in a_list:
    a_midi.append(re.sub(r'\d+', lambda x: MidiA[x.group()], m))

  for m in e_list:
    e_midi.append(re.sub(r'\d+', lambda x: MidiE[x.group()], m))

  return g_midi, d_midi, a_midi, e_midi

