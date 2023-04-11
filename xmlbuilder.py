from xml.dom import minidom
import xml.etree.ElementTree as ET
from notedictionaries import *

def clean_notes(g_notes, d_notes, a_notes, e_notes):
    flat = []
    temp = []
    for i in range(0,len(g_notes)):
        temp = []
        for j in range(0,len(g_notes[i])):
            # print("{} at {} {}".format(g_notes[i][j],i,j))
            # print("{} at {} {}".format(d_notes[i][j],i,j))
            # print("{} at {} {}".format(a_notes[i][j],i,j))
            # print("{} at {} {}".format(e_notes[i][j],i,j))
            if g_notes[i][j] == '-':
                if j < len(d_notes[i]):
                    if d_notes[i][j] == '-':
                        if j < len(a_notes[i]):
                            if a_notes[i][j] == '-':
                                if j < len(e_notes[i]):
                                    if e_notes[i][j] == '-': pass
                                    else: temp.append(e_notes[i][j])
                                else: pass
                            else: temp.append(a_notes[i][j])
                        else: pass
                    else: temp.append(d_notes[i][j])
                else: pass
            else: temp.append(g_notes[i][j])               
        print(temp)
        flat.append(temp)
    print(flat)
    return flat

def xml_build(seq):
    m_count = 1

    base = ET.parse('template.xml')
    root = base.getroot() #<score-partwise>
    part = ET.SubElement(root,'part')
    part.set('id', 'P1')

    for m in seq:
        measure = ET.SubElement(part, 'measure')
        measure.set('number', '{}'.format(m_count))
        if m_count == 1:
            attributes = ET.SubElement(measure, 'attributes')
            ET.SubElement(attributes, 'divisions').text = '1'
            time = ET.SubElement(attributes, 'time')
            ET.SubElement(time, 'beats').text = '4'
            ET.SubElement(time, 'beat-type').text = '4'
            clef = ET.SubElement(attributes, 'clef')
            ET.SubElement(clef, 'sign').text = 'F'
            ET.SubElement(clef, 'line').text = '4'
            m_count += 1
        else: m_count += 1
        for n in m:
            print("building {}".format(globals()[n]['step']))
            note = ET.SubElement(measure, 'note')
            pitch = ET.SubElement(note, 'pitch')
            step = ET.SubElement(pitch, 'step')
            step.text = '{}'.format(globals()[n]['step'])
            octave = ET.SubElement(pitch, 'octave')
            octave.text = '{}'.format(globals()[n]['octave'])
            ET.SubElement(note, 'duration').text = '1'
            ET.SubElement(note, 'stem').text = 'none'

    #https://stackoverflow.com/questions/28813876/how-do-i-get-pythons-elementtree-to-pretty-print-to-an-xml-file
    prettier = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
    with open("scratch.xml", "w") as f:
        f.write(prettier)