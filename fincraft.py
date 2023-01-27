def longest_comon_substring(string1,string2):
    m=len(string1)
    n = len(string2)
    result=0
    end = 0
    length=[[0 for x in range(n+1) ] for y in range(m+1) ]

    for i in range(m+1):
        for j in range(n+1):
            if i ==0 or j==0:
                length[i][j] = 0
            elif string1[i-1]== string2[j-1]:
                length[i][j] = length[i-1][j-1] +1
                if length[i][j] > result:
                    result = length[i][j]
                    end = i-1
                else:
                    length[i][j]=0
    if length == 0:
        return ""
    return string1[end-result+1:end+1]

print(longest_comon_substring("abcdef","abc"))