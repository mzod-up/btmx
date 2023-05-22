import re
from notedictionaries import MidiGNote, MidiDNote, MidiANote, MidiENote

def to_note(g_sliced, d_sliced, a_sliced, e_sliced):
    # replacing midi values in sliced midi arrays with note names

    for i, a in enumerate(g_sliced):
        for j, c in enumerate(a):
            if c != '-':
                g_sliced[i][j] = MidiGNote[c]
    #print("new G: {}",format(len(g_sliced)))
    #print(g_sliced)

    for i, a in enumerate(d_sliced):
        for j, c in enumerate(a):
            if c != '-':
                d_sliced[i][j] = MidiDNote[c]
    #print("new D: {}",format(len(d_sliced)))
    #print(d_sliced)

    # for a in d_sliced:
    #     for c in a:
    #         if c != '-':
    #             c = MidiDNote[c]
    # print("new D:")
    # print(d_sliced)

    for i, a in enumerate(a_sliced):
        for j, c in enumerate(a):
            if c != '-':
                a_sliced[i][j] = MidiANote[c]
    #print("new A: {}",format(len(a_sliced)))
    #print(a_sliced)

    for i, a in enumerate(e_sliced):
        for j, c in enumerate(a):
            if c != '-':
                e_sliced[i][j] = MidiENote[c]
    #print("new E: {}",format(len(e_sliced)))
    #print(e_sliced)

    return g_sliced, d_sliced, a_sliced, e_sliced

# slicing midi arrays into arrays of hyphens & midi values
def slicer(g_midi, d_midi, a_midi, e_midi):
    #print("FLATTENED:\n")
    flattened, g_sep, d_sep, a_sep, e_sep = ([] for i in range(5))

    # splitting up midi-fied arrays by hyphen/midi-value

    for line in g_midi:
        # print('line:{}'.format(line))
        g_sep.append(re.findall(r'\d+|\-',line))
    #print("\nG string")
    #print(g_sep)

    for line in d_midi:
        d_sep.append(re.findall(r'\d+|\-',line))
    #print("\nD string")
    #print(d_sep)

    for line in a_midi:
        a_sep.append(re.findall(r'\d+|\-',line))
    #print("\nA string")
    #print(a_sep)

    for line in e_midi:
        e_sep.append(re.findall(r'\d+|\-',line))
    #print("\nE string")
    #print(e_sep)
    
    # for i in range(0, len(g_midi)-1):
    #     for j in range(0, len(g_midi[i])-1):
    #         print([g_midi[i][j], d_midi[i][j], a_midi[i][j], e_midi[i][j]])
    #         flattened.append([g_midi[i][j], d_midi[i][j], a_midi[i][j], e_midi[i][j]])

    # print("THIS IS FLATTENED:")
    # print(flattened)

    return g_sep, d_sep, a_sep, e_sep
