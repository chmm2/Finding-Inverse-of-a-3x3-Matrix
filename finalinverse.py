

l1 = []
l2 = []
l3 = []

#Building the Matrix

for i in range(3):
    t = int(input("Enter a number for first row: "))
    l1.append(t)

for c in range(3):
    u = int(input("Enter a number for second row: "))
    l2.append(u)

for d in range(3):
    v = int(input("Enter a number for third row: "))
    l3.append(v)
print("\nGiven Matrix is: ")
print("\n",l1[0],"\t",l1[1],"\t",l1[2],"\n",l2[0],"\t",l2[1],"\t",l2[2],"\n",l3[0],"\t",l3[1],"\t",l3[2])

p1 = (l2[1]*l3[2])-(l3[1]*l2[2])
p4 = (l3[0]*l2[2])-(l3[2]*l2[0])
p7 = (l2[0]*l3[1])-(l3[0]*l2[1])
p2 = (l1[2]*l3[1])-(l1[1]*l3[2])
p5 = (l1[0]*l3[2])-(l1[2]*l3[0])
p8 = (l1[1]*l3[0])-(l1[0]*l3[1])
p3 = (l2[2]*l1[1])-(l1[2]*l2[1])
p6 = (l2[0]*l1[2])-(l2[2]*l1[0])
p9 = (l2[1]*l1[0])-(l1[1]*l2[0])

#The Adjoint
print("\nAdjoint of the Matrix is: ")
print("\n",p1,"\t",p2,"\t",p3,"\n",p4,"\t",p5,"\t",p6,"\n",p7,"\t",p8,"\t",p9)

#Finding Det
x= l1[0]*((l2[1]*l3[2])-(l3[1]*l2[2])) + (-l1[1]*((l2[0]*l3[2])-(l3[0]*l2[2]))) + l1[2]*((l2[0]*l3[1])-(l3[0]*l2[1]))

#Final Inverse Matrix
print("\nInverse of the Matrix is: ")
print("\n",p1/x,"\t",p2/x,"\t",p3/x,"\n",p4/x,"\t",p5/x,"\t",p6/x,"\n",p7/x,"\t",p8/x,"\t",p9/x,"\n")