"""

l5 = []
l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]
l3 = []
l4 = []
if len(l1) > len(l2):
    a = l1[len(l2):]
    l3.extend(a)
    print(a)
    b = l1[:len(l2)]
    l4.extend(b)
if len(l2) > len(l1):
    a = l1[len(l1):]
    l3.extend(a)
    print(a)
    b = l1[:len(l1)]
    l4.extend(b)
print(l3)
print(l4)

c = 0
d = 0
if len(l1) != len(l2):
    for i in l4:
        e = 0
        for j in l2:
            if d == e:
                if c != 0:
                    a = str(c + i + j)
                    a = list(a)
                    c = c -c
                    if len(a) > 1:
                        print(a[1])
                        l5.append(a[1])
                        c = c + int(a[0])
                    else:
                        print(a[0])
                        l5.append(a[0])
                else:
                    a = str(i + j)
                    a = list(a)
                    if len(a) > 1:
                        print(a[1])
                        l5.append(a[1])
                        c = c + int(a[0])
                    else:
                        print(a[0])
                        l5.append(a[0])
            e += 1
        d += 1
        
    
else:
    for i in l1:
        e = 0
        for j in l2:
            if d == e:
                if c != 0:
                    a = str(c + i + j)
                    a = list(a)
                    c = c -c
                    if len(a) > 1:
                        print(a[1])
                        l5.append(a[1])
                        c = c + int(a[0])
                    else:
                        print(a[0])
                        l5.append(a[0])
                else:
                    a = str(i + j)
                    a = list(a)
                    if len(a) > 1:
                        print(a[1])
                        l5.append(a[1])
                        c = c + int(a[0])
                    else:
                        print(a[0])
                        l5.append(a[0])
            e += 1
        d += 1


    
if not l3:
    pass
else:
    
    for k in l3:
        if c != 0 :
            a = str(k + c)
            c = c- c
            a = list(a)
            if len(a) > 1:
                print(a[1])
                l5.append(a[1])
                c = c + int(a[0])
            else:
                print(a[0])
                l5.append(a[0])
        else:
            a = str(k)
            a = list(a)
            if len(a) > 1:
                print(a[1])
                l5.append(a[1])
                c = c + int(a[0])
            else:
                print(a[0])
                l5.append(a[0])
if c != 0:
    print(c)
    l5.append(c)
print(l5)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
    
        
        l1 = list(l1)
        l2 = list(l2)
        l5 = []
        #l1 = [9, 9, 9, 9, 9, 9, 9]
        #l2 = [9, 9, 9, 9]
        l3 = []
        l4 = []
        if len(l1) > len(l2):
            a = l1[len(l2):]
            l3.extend(a)
            print(a)
            b = l1[:len(l2)]
            l4.extend(b)
        if len(l2) > len(l1):
            a = l1[len(l1):]
            l3.extend(a)
            print(a)
            b = l1[:len(l1)]
            l4.extend(b)
        print(l3)
        print(l4)

        c = 0
        d = 0
        if len(l1) != len(l2):
            for i in l4:
                e = 0
                for j in l2:
                    if d == e:
                        if c != 0:
                            a = str(c + i + j)
                            a = list(a)
                            c = c -c
                            if len(a) > 1:
                                print(a[1])
                                l5.append(a[1])
                                c = c + int(a[0])
                            else:
                                print(a[0])
                                l5.append(a[0])
                        else:
                            a = str(i + j)
                            a = list(a)
                            if len(a) > 1:
                                print(a[1])
                                l5.append(a[1])
                                c = c + int(a[0])
                            else:
                                print(a[0])
                                l5.append(a[0])
                    e += 1
                d += 1
                
            
        else:
            for i in l1:
                e = 0
                for j in l2:
                    if d == e:
                        if c != 0:
                            a = str(c + i + j)
                            a = list(a)
                            c = c -c
                            if len(a) > 1:
                                print(a[1])
                                l5.append(a[1])
                                c = c + int(a[0])
                            else:
                                print(a[0])
                                l5.append(a[0])
                        else:
                            a = str(i + j)
                            a = list(a)
                            if len(a) > 1:
                                print(a[1])
                                l5.append(a[1])
                                c = c + int(a[0])
                            else:
                                print(a[0])
                                l5.append(a[0])
                    e += 1
                d += 1


            
        if not l3:
            pass
        else:
            
            for k in l3:
                if c != 0 :
                    a = str(k + c)
                    c = c- c
                    a = list(a)
                    if len(a) > 1:
                        print(a[1])
                        l5.append(a[1])
                        c = c + int(a[0])
                    else:
                        print(a[0])
                        l5.append(a[0])
                else:
                    a = str(k)
                    a = list(a)
                    if len(a) > 1:
                        print(a[1])
                        l5.append(a[1])
                        c = c + int(a[0])
                    else:
                        print(a[0])
                        l5.append(a[0])
        if c != 0:
            print(c)
            l5.append(c)
        print(l5)
        return l5
g = Solutio() 
print(g.addTwoNumbers(l1, l2))
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
c = ""
d = ""
for i in l1:
    c = c + str(i)
for j in l2 :
    d = d + str(j)
print(d)
print(c)
e = str(int(d) + int(c))
e[::-1]
e = list(e)
return e
"""