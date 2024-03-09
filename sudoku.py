def sudoku(puzzle):
    S = []
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            S.append(puzzle[i][j])
    while True:
        def dictor(S):
            D = {}
            D_L = {}
            D_C = {}
            D_B = {}

            L = []
            C = []
            B = []
            for i in range(len(S)//9):
                C.append([])
            c = 0
            for i in range(len(S)//9):
                L.append(S[9*i: 9*(i+1)])
                for i in range(len(S)):
                    if i % 9 == c:
                        C[c].append(S[i])
                else:
                    c += 1
            for i in range(9):
                for j in range(len(L)):
                    if L[j][i *3 : (i + 1)*3] != []:
                        B.append(L[j][i *3 : (i + 1)*3])
            buf = []
            for i in range(9):
                buf.append(B[i *3 : (i + 1)*3])
            B = buf
            B[1],B[2],B[3],B[5],B[6],B[7],B[8] = B[3],B[6],B[1],B[7],B[2],B[5],B[8]
            for i in range(len(B)):
                B[i] = B[i][0] + B[i][1] + B[i][2]
            N = range(len(S))
            N_L = range(len(L))
            N_C = range(len(C))
            for z,p in zip(N, S):
                D[z] = p
            for z,p in zip(N_L, L):
                D_L[z] = p
            for z,p in zip(N_C, C):
                D_C[z] = p
            for z,p in zip(N_L, B):
                D_B[z] = p

            return D, D_L,D_C,D_B
        D,D_L,D_C,D_B = dictor(S)
        for i in S:
            if i == 0:
                break
        else:
            break
        def deter(n):
            det = 0
            if n < 27:
                for i in range(9):
                    if n in range(i * 0, (i+1) * 3) or n in range(i + 9, (i + 4) * 3) or n in range(i + 18, (i + 7) * 3):
                        det = i
                        break
            elif n < 54:
                n = n % 27
                for i in range(9):
                    if n in range(i * 0, (i+1) * 3) or n in range(i + 9, (i + 4) * 3) or n in range(i + 18, (i + 7) * 3):
                        det = i + 3
                        break
            elif n < 81:
                n = n % 27
                for i in range(9):
                    if n in range(i * 0, (i+1) * 3) or n in range(i + 9, (i + 4) * 3) or n in range(i + 18, (i + 7) * 3):
                        det = i + 6
                        break
            return det
        def isinbox(n):
            box = [1,2,3,4,5,6,7,8,9]
            for i in range(9):
                if D_B[deter(n)][i] in box:
                    box.remove(D_B[deter(n)][i])
            return box
        def isinline(n):
            line = [1,2,3,4,5,6,7,8,9]
            for i in range(9):
                if D_L[n//9][i] in line:
                    line.remove(D_L[n//9][i])
            return line                          
        def isincolumn(n):
                colum = [1,2,3,4,5,6,7,8,9]
                for i in range(9):
                    if D_C[n % 9][i] in colum:
                        colum.remove(D_C[n%9][i])
                return colum
        def numeral(n):
            numeral = []
            for i in range(1, 10):
                if i in isinbox(n) and i in isinline(n) and i in isincolumn(n):
                    numeral.append(i)
            return numeral
        for i in range(81):
            if S[i] == 0:
                if len(numeral(i)) == 1:
                    S[i] = numeral(i)[0]

                    
    res = []
    for i in range(9):
        res.append(D_L[i])
    return res
puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]
for i in range(9):
    print(sudoku(puzzle)[i])