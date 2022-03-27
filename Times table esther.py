num1=1
num2=2
num3=3
num4=4
num5=5
num6=6
num7=7
num8=8
num9=9
num10=10
num11=11
num12=12

#for the top row, the first 6 tables
#iterate 12 times from j = 1 to 12
for j in range(1,13):
    print(j,'x',num1,'=',num1*j,'  ',j,'x',num2,'=',num2*j,'  ',j,'x',num3,'=',num3*j,'  ',j,'x',num4,'=',num4*j,'  ',j,'x',num5,'=',num5*j,'  ',j,'x',num6,'=',num6*j) 

#space inbetween rows
print('      ')


#for the bottom row, the last 6 tables
#iterate 12  times from j = 1 to 12
for j in range(1,13):
    print(j,'x',num7,'=',num7*j,'  ',j,'x',num8,'=',num8*j,'  ',j,'x',num9,'=',num9*j,'  ',j,'x',num10,'=',num10*j,'  ',j,'x',num11,'=',num11*j,'  ',j,'x',num12,'=',num12*j) 
