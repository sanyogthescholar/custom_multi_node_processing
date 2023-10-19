

#solved state:
#s = "OOOOOOOOOGGGWWWBBBYYYGGGWWWBBBYYYGGGWWWBBBYYYRRRRRRRRR"
#print(len(s))

class Cube:
    def __init__(self,state):
        self.state = state
    
    def move(self,mov):
        if mov == "R":
            temp1,temp2,temp3 = self.state[2],self.state[5],self.state[8]
            self.state[2],self.state[5],self.state[8] = self.state[14],self.state[26],self.state[38]
            self.state[14],self.state[26],self.state[38] = self.state[47],self.state[50],self.state[53]
            self.state[47],self.state[50],self.state[53] = self.state[42],self.state[30],self.state[18]
            self.state[42],self.state[30],self.state[18] = temp1,temp2,temp3
            temp1,temp2,temp3 = self.state[15],self.state[16],self.state[17]
            self.state[15],self.state[16],self.state[17] = self.state[39],self.state[27],temp1
            self.state[39],self.state[27] = self.state[41],self.state[40]
            self.state[40] = self.state[29]
            self.state[29],self.state[41] = temp2,temp3
        if mov == "R'":
            temp1,temp2,temp3 = self.state[2],self.state[5],self.state[8]
            self.state[8],self.state[5],self.state[2] = self.state[18],self.state[30],self.state[42]
            self.state[18],self.state[30],self.state[42] = self.state[53],self.state[50],self.state[47]
            self.state[53],self.state[50],self.state[47] = self.state[38],self.state[26],self.state[14]
            self.state[38],self.state[26],self.state[14] = temp3,temp2,temp1
            temp1,temp2,temp3 = self.state[15],self.state[16],self.state[17]
            self.state[15],self.state[16],self.state[17] = temp3,self.state[29],self.state[41]
            self.state[29],self.state[41] = self.state[40],self.state[39]
            self.state[40] = self.state[27]
            self.state[39],self.state[27] = temp1,temp2
        if mov == "L":
            temp1,temp2,temp3 = self.state[0],self.state[3],self.state[6]
            self.state[0],self.state[3],self.state[6] = self.state[44],self.state[32],self.state[20]
            self.state[44],self.state[32],self.state[20] = self.state[45],self.state[48],self.state[51]
            self.state[45],self.state[48],self.state[51] = self.state[12],self.state[24],self.state[36]
            self.state[12],self.state[24],self.state[36] = temp1,temp2,temp3
            temp1,temp2,temp3 = self.state[9],self.state[10],self.state[11]
            self.state[9],self.state[10],self.state[11] = self.state[33],self.state[21],temp1
            self.state[33],self.state[21] = self.state[35],self.state[34]
            self.state[34] = self.state[23]
            self.state[23],self.state[35] = temp2,temp3
        if mov == "L'":
            temp1,temp2,temp3 = self.state[0],self.state[3],self.state[6]
            self.state[0],self.state[3],self.state[6] = self.state[12],self.state[24],self.state[36]
            self.state[12],self.state[24],self.state[36] = self.state[45],self.state[48],self.state[51]
            self.state[45],self.state[48],self.state[51] = self.state[44],self.state[32],self.state[20]
            self.state[44],self.state[32],self.state[20] = temp1,temp2,temp3
            temp1,temp2,temp3 = self.state[9],self.state[10],self.state[11]
            self.state[9],self.state[10],self.state[11] = temp3,self.state[23],self.state[35]
            self.state[23],self.state[35] = self.state[34],self.state[33]
            self.state[34] = self.state[21]
            self.state[33],self.state[21] = temp1,temp2
        if mov == "U":
            temp1,temp2,temp3 = self.state[9],self.state[10],self.state[11]
            self.state[9],self.state[10],self.state[11] = self.state[12],self.state[13],self.state[14]
            self.state[12],self.state[13],self.state[14] = self.state[15],self.state[16],self.state[17]
            self.state[15],self.state[16],self.state[17] = self.state[18],self.state[19],self.state[20]
            self.state[18],self.state[19],self.state[20] = temp1,temp2,temp3
            temp1,temp2,temp3 = self.state[0],self.state[1],self.state[2]
            self.state[0],self.state[1],self.state[2] = self.state[6],self.state[3],temp1
            self.state[3],self.state[6] = self.state[7],self.state[8]
            self.state[7] = self.state[5]
            self.state[5],self.state[8] = temp2,temp3
        if mov == "U'":
            temp1,temp2,temp3 = self.state[9],self.state[10],self.state[11]
            self.state[9],self.state[10],self.state[11] = self.state[18],self.state[19],self.state[20]
            self.state[18],self.state[19],self.state[20] = self.state[15],self.state[16],self.state[17]
            self.state[15],self.state[16],self.state[17] = self.state[12],self.state[13],self.state[14]
            self.state[12],self.state[13],self.state[14] = temp1,temp2,temp3
            temp1,temp2,temp3 = self.state[0],self.state[1],self.state[2]
            self.state[0],self.state[1],self.state[2] = temp3,self.state[5],self.state[8]
            self.state[5],self.state[8] = self.state[7],self.state[6]
            self.state[7] = self.state[3]
            self.state[3],self.state[6] = temp2,temp1
        if mov == "F":
            temp1,temp2,temp3 = self.state[6],self.state[7],self.state[8]
            self.state[6],self.state[7],self.state[8] = self.state[35],self.state[23],self.state[11]
            self.state[35],self.state[23],self.state[11] = self.state[47],self.state[46],self.state[45]
            self.state[47],self.state[46],self.state[45] = self.state[15],self.state[27],self.state[39]
            self.state[15],self.state[27],self.state[39] = temp1,temp2,temp3
            temp1,temp2,temp3 = self.state[12],self.state[13],self.state[14]
            self.state[12],self.state[13],self.state[14] = self.state[36],self.state[24],temp1
            self.state[36],self.state[24] = self.state[38],self.state[37]
            self.state[37] = self.state[26]
            self.state[38],self.state[26] = temp3,temp2
        if mov == "F'":
            temp1,temp2,temp3 = self.state[6],self.state[7],self.state[8]
            self.state[6],self.state[7],self.state[8] = self.state[15],self.state[27],self.state[39]
            self.state[15],self.state[27],self.state[39] = self.state[47],self.state[46],self.state[45]
            self.state[47],self.state[46],self.state[45] = self.state[35],self.state[23],self.state[11]
            self.state[35],self.state[23],self.state[11] = temp1,temp2,temp3
            temp1,temp2,temp3 = self.state[12],self.state[13],self.state[14]
            self.state[12],self.state[13],self.state[14] = temp3,self.state[26],self.state[38]
            self.state[26],self.state[38] = self.state[37],self.state[36]
            self.state[37] = self.state[24]
            self.state[36],self.state[24] = temp1,temp2
        if mov == "D":
            temp1,temp2,temp3 = self.state[33],self.state[34],self.state[35]
            self.state[33],self.state[34],self.state[35] = self.state[42],self.state[43],self.state[44]
            self.state[42],self.state[43],self.state[44] = self.state[39],self.state[40],self.state[41]
            self.state[39],self.state[40],self.state[41] = self.state[36],self.state[37],self.state[38]
            self.state[36],self.state[37],self.state[38] = temp1,temp2,temp3
            temp1,temp2,temp3 = self.state[45],self.state[46],self.state[47]
            self.state[45],self.state[46],self.state[47] = self.state[51],self.state[48],temp1
            self.state[51],self.state[48] = self.state[53],self.state[52]
            self.state[52] = self.state[50]
            self.state[53],self.state[50] = temp3,temp2
        if mov == "D'":
            temp1,temp2,temp3 = self.state[33],self.state[34],self.state[35]
            self.state[33],self.state[34],self.state[35] = self.state[36],self.state[37],self.state[38]
            self.state[36],self.state[37],self.state[38] = self.state[39],self.state[40],self.state[41]
            self.state[39],self.state[40],self.state[41] = self.state[42],self.state[43],self.state[44]
            self.state[42],self.state[43],self.state[44] = temp1,temp2,temp3
            temp1,temp2,temp3 = self.state[45],self.state[46],self.state[47]
            self.state[45],self.state[46],self.state[47] = temp3,self.state[50],self.state[53]
            self.state[50],self.state[53] = self.state[52],self.state[51]
            self.state[52] = self.state[48]
            self.state[51],self.state[48] = temp1,temp2
        if mov == "B":
            temp1,temp2,temp3 = self.state[0],self.state[1],self.state[2]
            self.state[0],self.state[1],self.state[2] = self.state[17],self.state[29],self.state[41]
            self.state[17],self.state[29],self.state[41] = self.state[53],self.state[52],self.state[51]
            self.state[53],self.state[52],self.state[51] = self.state[33],self.state[21],self.state[9]
            self.state[33],self.state[21],self.state[9] = temp1,temp2,temp3
            temp1,temp2,temp3 = self.state[18],self.state[19],self.state[20]
            self.state[18],self.state[19],self.state[20] = self.state[42],self.state[30],temp1
            self.state[42],self.state[30] = self.state[44],self.state[43]
            self.state[43] = self.state[32]
            self.state[44],self.state[32] = temp3,temp2
        if mov == "B'":
            temp1,temp2,temp3 = self.state[0],self.state[1],self.state[2]
            self.state[0],self.state[1],self.state[2] = self.state[33],self.state[21],self.state[9]
            self.state[33],self.state[21],self.state[9] = self.state[53],self.state[52],self.state[51]
            self.state[53],self.state[52],self.state[51] = self.state[17],self.state[29],self.state[41]
            self.state[17],self.state[29],self.state[41] = temp1,temp2,temp3
            temp1,temp2,temp3 = self.state[18],self.state[19],self.state[20]
            self.state[18],self.state[19],self.state[20] = temp3,self.state[32],self.state[44]
            self.state[32],self.state[44] = self.state[43],self.state[42]
            self.state[43] = self.state[30]
            self.state[42],self.state[30] = temp1,temp2

def list_to_string(cl):
    ans=''
    for i in cl:
        ans+=i
    return ans

def string_to_list(cs):
    ans=[]
    for i in cs:
        ans.append(i)
    return ans