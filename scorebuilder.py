import re
from notedictionaries import MidiGNote, MidiDNote, MidiANote, MidiENote

def to_note(g_sliced, d_sliced, a_sliced, e_sliced):

    for i, a in enumerate(g_sliced):
        for j, c in enumerate(a):
            if c != '-':
                g_sliced[i][j] = MidiGNote[c]

    for i, a in enumerate(d_sliced):
        for j, c in enumerate(a):
            if c != '-':
                d_sliced[i][j] = MidiDNote[c]

    for i, a in enumerate(a_sliced):
        for j, c in enumerate(a):
            if c != '-':
                a_sliced[i][j] = MidiANote[c]

    for i, a in enumerate(e_sliced):
        for j, c in enumerate(a):
            if c != '-':
                e_sliced[i][j] = MidiENote[c]

    return g_sliced, d_sliced, a_sliced, e_sliced

def slicer(g_midi, d_midi, a_midi, e_midi):
    flattened, g_sep, d_sep, a_sep, e_sep = ([] for i in range(5))

    # Splitting up midi-fied arrays by hyphen/midi-value so that instead of containing a whole string, each individual char is an element in the array
    for line in g_midi:
        g_sep.append(re.findall(r'\d+|\-',line))

    for line in d_midi:
        d_sep.append(re.findall(r'\d+|\-',line))

    for line in a_midi:
        a_sep.append(re.findall(r'\d+|\-',line))

    for line in e_midi:
        e_sep.append(re.findall(r'\d+|\-',line))

    return g_sep, d_sep, a_sep, e_sep
