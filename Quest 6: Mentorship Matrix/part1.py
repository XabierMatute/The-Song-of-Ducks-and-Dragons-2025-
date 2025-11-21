notes= """
ABCCbaCBcBbAacCAbcCCCacAAaBcBCbABcCBaAbACAaABabACacBCbcaaCBBaCbbcABbbaaCbaaCaBaAaBBABBcABabcAcbBcBbAbCabaBbaCBBCa
"""

possible_pairs = 0
for index, letter in enumerate(notes):
    # if letter.islower():
    if letter == 'a':
        novice = letter
        for profesional in notes[:index]:
            if profesional.isupper() and profesional.lower() == letter:
                possible_pairs += 1

print(possible_pairs)