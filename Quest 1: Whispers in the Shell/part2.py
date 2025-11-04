names = "Sarnnix,Zormal,Quirzrak,Zyrgyth,Briveldrin,Ascaleon,Skarfeth,Durnpyros,Calasis,Vyrkris,Arakwyris,Shaemdren,Krynnalar,Sillith,Zynardith,Draithnar,Tarlparth,Kazaxar,Ilmarnar,Nylthyris"

moves = "L5,R7,L14,R11,L15,R13,L11,R14,L19,R7,L5,R12,L5,R19,L5,R13,L5,R11,L5,R18,L7,R11,L11,R10,L16,R6,L9,R6,L15"

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
       pos = pos + int(move[1:])
    if move[0] == 'L':
       pos = pos - int(move[1:])
    print(pos)
    
    
print(names[pos])