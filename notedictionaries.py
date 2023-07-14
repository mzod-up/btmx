# Dictionaries for each of the notes containing MusicXML values for step, octave, and alter.

E1 = {'step':'E', 'octave':1, 'alter':0}
F1 = {'step':'F', 'octave':1, 'alter':0}
Gb1 = {'step':'G', 'octave':1, 'alter':-1}
G1 = {'step':'G', 'octave':1, 'alter':0}
Ab1 = {'step':'A', 'octave':1, 'alter':-1}
A1 = {'step':'A', 'octave':1, 'alter':0}
Bb1 = {'step':'B', 'octave':1, 'alter':-1}
B1 = {'step':'B', 'octave':1, 'alter':0}
C2 = {'step':'C', 'octave':2, 'alter':0}
Db2 = {'step':'D', 'octave':2, 'alter':-1}
D2 = {'step':'D', 'octave':2, 'alter':0}
Eb2 = {'step':'E', 'octave':2, 'alter':-1}
E2 = {'step':'E', 'octave':2, 'alter':0}
F2 = {'step':'F', 'octave':2, 'alter':0}
Gb2 = {'step':'G', 'octave':2, 'alter':-1}
G2 = {'step':'G', 'octave':2, 'alter':0}
Ab2 = {'step':'A', 'octave':2, 'alter':-1}
A2 = {'step':'A', 'octave':2, 'alter':0}
Bb2 = {'step':'B', 'octave':2, 'alter':-1}
B2 = {'step':'B', 'octave':2, 'alter':0}
C3 = {'step':'C', 'octave':3, 'alter':0}
Db3 = {'step':'D', 'octave':3, 'alter':-1}
D3 = {'step':'D', 'octave':3, 'alter':0}
Eb3 = {'step':'E', 'octave':3, 'alter':-1}
E3 = {'step':'E', 'octave':3, 'alter':0}
F3 = {'step':'F', 'octave':3, 'alter':0}
Gb3 = {'step':'G', 'octave':3, 'alter':-1}
G3 = {'step':'G', 'octave':3, 'alter':0}
Ab3 = {'step':'A', 'octave':3, 'alter':-1}
A3 = {'step':'A', 'octave':3, 'alter':0}
Bb3 = {'step':'B', 'octave':3, 'alter':-1}
B3 = {'step':'B', 'octave':3, 'alter':0}
C4 = {'step':'C', 'octave':4, 'alter':0}

# Lists for each bass string.
# Note Name: Index numbers are the fret numbers - each holding their corresponding note.

G = [G2, Ab2, A2, Bb2, B2, C3, Db3, D3, Eb3, E3, F3, Gb3, G3, Ab3, A3, Bb3, B3, C4]
D = [D2, Eb2, E2, F2, Gb2, G2, Ab2, A2, Bb2, B2, C3, Db3, D3, Eb3, E3, F3, Gb3, G3]
A = [A1, Bb1, B1, C2, Db2, D2, Eb2, E2, F2, Gb2, G2, Ab2, A2, Bb2, B2, C3, Db3, D3]
E = [E1, F1, Gb1, G1, Ab1, A1, Bb1, B1, C2, Db2, D2, Eb2, E2, F2, Gb2, G2, Ab2, A2]

# Left - fret numbers (0 = open string). Right - MIDI values for each fret-string value combination.
MidiG = {'0':'43', '1':'44', '2':'45', '3':'46', '4':'47', '5':'48', '6':'49', '7':'50', '8':'51', '9':'52', '10':'53', '11':'54', '12':'55', '13':'56', '14':'57', '15':'58', '16':'59', '17':'60'}
MidiD = {'0':'38', '1':'39', '2':'40', '3':'41', '4':'42', '5':'43', '6':'44', '7':'45', '8':'46', '9':'47', '10':'48', '11':'49', '12':'50', '13':'51', '14':'52', '15':'53', '16':'54', '17':'55'}
MidiA = {'0':'33', '1':'34', '2':'35', '3':'36', '4':'37', '5':'38', '6':'39', '7':'40', '8':'41', '9':'42', '10':'43', '11':'44', '12':'45', '13':'46', '14':'47', '15':'48', '16':'49', '17':'50'}
MidiE = {'0':'28', '1':'29', '2':'30', '3':'31', '4':'32', '5':'33', '6':'34', '7':'35', '8':'36', '9':'37', '10':'38', '11':'39', '12':'40', '13':'41', '14':'42', '15':'43', '16':'44', '17':'45'}

# Left - MIDI values. Right - Note names.
MidiGNote = {'43':'G2', '44':'Ab2', '45':'A2', '46':'Bb2', '47':'B2', '48':'C3', '49':'Db3', '50':'D3', '51':'Eb3', '52':'E3', '53':'F3', '54':'Gb3', '55':'G3', '56':'Ab3', '57':'A3', '58':'Bb3', '59':'B3', '60':'C4'}
MidiDNote = {'38':'D2', '39':'Eb2', '40':'E2', '41':'F2', '42':'Gb2', '43':'G2', '44':'Ab2', '45':'A2', '46':'Bb2', '47':'B2', '48':'C3', '49':'Db3', '50':'D3', '51':'Eb3', '52':'E3', '53':'F3', '54':'Gb3', '55':'G3'}
MidiANote = {'33':'A1', '34':'Bb1', '35':'B1', '36':'C2', '37':'Db2', '38':'D2', '39':'Eb2', '40':'E2', '41':'F2', '42':'Gb2', '43':'G2', '44':'Ab2', '45':'A2', '46':'Bb2', '47':'B2', '48':'C3', '49':'Db3', '50':'D3'}
MidiENote = {'28':'E1', '29':'F1', '30':'Gb1', '31':'G1', '32':'Ab1', '33':'A1', '34':'Bb1', '35':'B1', '36':'C2', '37':'Db2', '38':'D2', '39':'Eb2', '40':'E2', '41':'F2', '42':'Gb2', '43':'G2', '44':'Ab2', '45':'A2'}