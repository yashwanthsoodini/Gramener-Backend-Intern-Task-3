def CommonElements(l1,l2):  #Function that returns the list containing the common elements in l1 and l2
    l1.sort()               #We will first sort the two lists using sort()
    l2.sort()
    ce = []                 #ce is the list that will contain the common elements in l1 and l2
    i=0                     #We will use indexes i and j to access elements from lists l1 and l2 respectively
    j=0                     #i and j are initially set to zero
    while(True):
        if(i>=len(l1) or j>=len(l2)):                   #We break the while loop if one or both of the indexes overflow
            break
        if(l1[i]==l2[j]):                               #If l1[i] and l2[j] are equal, we append any of them to ce and increment both i and j
            if(len(ce)==0 or ce[len(ce)-1]!=l1[i]):
                ce.append(l1[i])
            i = i+1
            j = j+1
        else:
            if(l1[i]<l2[j]):                            #If l1[i] is smaller than l2[j], then we increment i
                i = i+1
            else:                                       #If l1[i] is greater than l2[j], then we increment j
                j = j+1
    return ce

def Minus(l1,l2):                        #Function that returns the list containing elements in l1 but not in l2
    l1.sort()                            #We will first sort the two lists using sort()
    l2.sort()
    l = []                              #l is the list that will contain the elements present in l1 but not in l2
    ce = CommonElements(l1,l2)          #ce is the list that will contain the common elements in l1 and l2
    i=0                                 #We will use indexes i and j to access elements from lists l1 and ce respectively
    j=0                                 #i and j are initially set to zero
    while(True):
        if(i>=len(l1)):                     #We break the while loop if index i overflows
            break
        if(j>=len(ce)):                     #If index j overflows, we add all the remaining elements in l1 to l
            for k in range(i,len(l1)):
                l.append(l1[k])
            break
        if(l1[i]==ce[j]):                   #If l1[i] and l2[j] are equal, then we increment i
            i = i+1
        else:
            if(l1[i]<ce[j]):                #If l1[i] is smaller than l2[j], then we append l1[i] to l and increment i
                l.append(l1[i])
                i = i+1
            else:                            #If l1[i] is greater than l2[j], then we increment j
                j = j+1
    return l

L1 = ['a','b','c']          #The given lists L1 and L2
L2 = ['b','d']

print("Common Elements in L1 and L2 : ")
print(CommonElements(L1,L2))
print("Elements present in L1 but not in L2 : ")
print(Minus(L1,L2))
