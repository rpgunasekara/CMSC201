"""
File: minor_key.py
Author: Ravindu Gunasekara
Setion: 44
E-mail: rgunase1@umbc.edu
Date: 10/18/2023
Description:
    Asks user for an input, determines
    if the input is a valid musical note,
    then gives the harmonic minor scale for
    that note.
"""
MUSICAL_NOTES = ["C", "D\u266d", "D", "E\u266d", "E", "F", "G\u266d", "G", "A\u266d", "A", "B\u266d", "B"]

# Determines if the input is a valid note, then asks for the scale.
def is_note(note):
    if "flat" in note:
        note = note[0] + "\u266d"

        if note in MUSICAL_NOTES:
            minor_scale(note)
        else:
            print("There is no starting note " + note + ".")
    else:
        note = note[0]

        if note in MUSICAL_NOTES:
            minor_scale(note)
        else:
            print("There is no starting note " + note + ".")

# Once determined a valid note, finds the list that starts with the note and prints it out to give the scale.
def minor_scale(note):
    harmonic_1 = ["C", "D", "E\u266d", "F", "G", "A\u266d", "B", "C"]
    harmonic_2 = ["D\u266d", "E\u266d", "E", "G\u266d", "A\u266d", "A", "C", "D\u266d"]
    harmonic_3 = ["D", "E", "F", "G", "A", "B\u266d", "D\u266d", "D"]
    harmonic_4 = ["E\u266d", "F", "G\u266d", "A\u266d", "B\u266d", "B", "D", "E\u266d"]
    harmonic_5 = ["E", "G\u266d", "G", "A", "B", "C", "E\u266d", "E"]
    harmonic_6 = ["F", "G", "A\u266d", "B\u266d", "C", "D\u266d", "E", "F"]
    harmonic_7 = ["G\u266d", "A\u266d", "A", "B", "D\u266d", "D", "F", "G\u266d"]
    harmonic_8 = ["G", "A", "B\u266d", "C", "D", "E\u266d", "G\u266d", "G"]
    harmonic_9 = ["A\u266d", "B\u266d", "B", "D\u266d", "E\u266d", "E", "G", "A\u266d"]
    harmonic_10 = ["A", "B", "C", "D", "E", "F", "A\u266d", "A"]
    harmonic_11 = ["B\u266d", "C", "D\u266d", "E\u266d", "F", "G\u266d", "A", "B\u266d"]
    harmonic_12 = ["B", "D\u266d", "D", "E", "G\u266d", "G", "B\u266d", "B"]

    if note == harmonic_1[0]:
        print(" ".join(harmonic_1))
    elif note == harmonic_2[0]:
        print(" ".join(harmonic_2))
    elif note == harmonic_3[0]:
        print(" ".join(harmonic_3))
    elif note == harmonic_4[0]:
        print(" ".join(harmonic_4))
    elif note == harmonic_5[0]:
        print(" ".join(harmonic_5))
    elif note == harmonic_6[0]:
        print(" ".join(harmonic_6))
    elif note == harmonic_7[0]:
        print(" ".join(harmonic_7))
    elif note == harmonic_8[0]:
        print(" ".join(harmonic_8))
    elif note == harmonic_9[0]:
        print(" ".join(harmonic_9))
    elif note == harmonic_10[0]:
        print(" ".join(harmonic_10))
    elif note == harmonic_11[0]:
        print(" ".join(harmonic_11))
    elif note == harmonic_12[0]:
        print(" ".join(harmonic_12))


if __name__ == "__main__":
    starting_note = input("Enter a starting note (C, D flat): ").strip()

    while starting_note != "quit":
        is_note(starting_note)
        starting_note = input("Enter a starting note (C, D flat): ").strip()
