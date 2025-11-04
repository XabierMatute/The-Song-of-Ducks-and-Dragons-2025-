names = "Braeorath,Malpyros,Kazphor,Gareldrin,Cragzar,Aeorxelor,Wyrynn,Ballith,Laziradarin,Ascallyr,Vaeldra,Marallyr,Shaelxelor,Fyrzyph,Tirzal,Drazaris,Hyrapyros,Arvynn,Tharnural,Cynvarzorin,Harnimar,Kazdin,Lazgryph,Selthel,Pylarris,Axaladir,Ilmarmir,Brelaxar,Norakvoran,Valquin"

moves = "L36,R39,L9,R47,L34,R24,L27,R22,L44,R28,L18,R18,L8,R43,L26,R12,L30,R48,L29,R10,L5,R45,L5,R13,L5,R28,L5,R24,L5,R39,L5,R7,L5,R36,L5,R8,L5,R28,L5,R42,L32,R48,L23,R11,L48,R7,L26,R31,L46,R25,L12,R21,L8,R32,L20,R14,L10,R35,L15"

print(names);
print(moves);

names = names.split(",")
moves = moves.split(",")

print(names);
print(moves);

pos = 0

for move in moves:
    print(move)
    if move[0] == 'R':
       pos = 0 + int(move[1:])
    if move[0] == 'L':
       pos = 0 - int(move[1:])
    while pos > len(names):
        pos = pos - len(names)
    while pos < 0 - len(names):
        pos = pos + len(names)
    print(pos)
    names[0], names[pos] = names[pos], names[0]
    
pos = 0
    
print(names[pos])