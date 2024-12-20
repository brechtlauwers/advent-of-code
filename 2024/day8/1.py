import numpy as np

with open("input.txt") as file_in:
    m = []
    for line in file_in:
        m.append(list(*line.split()))
        
m = np.array(m)


example_input = ["............","........0...",".....0......",".......0....","....0.......","......A.....","............","............","........A...",".........A..","............","............"]

#m = []
#for line in example_input:
#    m.append(list(line))
    
m = np.array(m)
m_len = m.shape[0]
result = set()

for i in range(m_len):
    for j in range(m_len):
        if m[i][j] != ".":
            symbol = m[i][j]
            # TODO only search from the found symbol -> end instead of full matrix
            other_symbols = np.where(m == symbol)
            other_ij = list(zip(other_symbols[0], other_symbols[1]))
            other_ij.remove((i,j))

            for other_index in other_ij:
                diff = other_index[0] - (i,j)[0], other_index[1] - (i,j)[1]
                antinode1 = (i,j)[0] - diff[0], (i,j)[1] - diff[1]
                antinode2 = other_index[0] + diff[0], other_index[1] + diff[1]

                if 0 <= antinode1[0] < m_len and 0 <= antinode1[1] < m_len:
                    result.add(antinode1)
                if 0 <= antinode2[0] < m_len and 0 <= antinode2[1] < m_len:
                    result.add(antinode2)


#print(result)
print(len(result))
