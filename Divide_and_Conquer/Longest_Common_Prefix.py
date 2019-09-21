



def LongestCommmon(a):
    if (len(a) == 1):
        return a[0]
    mid=len(a)//2
    lp = LongestCommmon(a[:mid])
    rp = LongestCommmon(a[mid:])

    return CommonPrefix([lp,rp])





def CommonPrefix(a):
    s1 = a[0]
    s2 = a[1]
    l = min(len(s1),len(s2))
    s = ""
    for i in range (l):
        if(s1[i]==s2[i]):
            s+=s1[i]
        else:
            break
    print("common prefix of ",a[0]," and ",a[1]," is  = ",s)
    return  s


def main():
    a = ["Hello","Hell","Hellelo","Hellooo"]
    s = LongestCommmon(a)
    print("the longest prefix is  = ",s)

main()