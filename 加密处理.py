import cv2
import numpy
def secret(name,number):
    arr=[]
    arr2=[]
    arr3=[]
    arr4=[]
    arr5=[]
    arr6=[]
    count=0
    img=cv2.imread(name)
    x=int(len(img[0])/number)
    y=int(len(img)/number)
    for i2 in range(0,number):
        for i3 in range(0,number):
            for i in range(i2*y,y+(i2*y)):
                for a in range(i3*x,x+(i3*x)):
                    arr.append(img[i][a])
                arr2.append(arr)
                arr=[]
            arr3.append(arr2)
            arr2=[]
        arr4.append(arr3)
        arr3=[]
    for i4 in range(0,number):
        for i5 in range(0,i4+1):
            arr5.append(arr4[i4-i5][i5])
            count+=1
            if (count)%number==0:
                end = numpy.concatenate(arr5, axis=1)
                arr6.append(end)
                arr5=[]
    for i6 in range(1,number):
        for i7 in range(i6,number):
            arr5.append(arr4[number-i7+i6-1][i7])
            count += 1
            if (count) % number == 0:
                end = numpy.concatenate(arr5, axis=1)
                arr6.append(end)
                arr5 = []
    end2=numpy.concatenate(arr6,axis=0)
    cv2.imshow("kk",end2)
    cv2.imwrite(name,end2)
    cv2.waitKey(0)
def desecret(name,number):
    arr = []
    arr2 = []
    arr3 = []
    arr4=[]
    arr5 = []
    arr6 = []
    count = 0
    num=0
    down=number-1
    downbody=int((number*number/2)+(number/2))-1
    recorddown=down
    img = cv2.imread(name)
    x = int(len(img[0]) / number)
    y = int(len(img) / number)
    for l2 in range(0, number):
        for l3 in range(0, number):
            for l in range(l2 * y, y + (l2 * y)):
                for b in range(l3 * x, x + (l3 * x)):
                    arr.append(img[l][b])
                arr2.append(arr)
                arr = []
            arr3.append(arr2)
            arr2 = []
    for l4 in range(0,number):
        count += l4
        for l5 in range(2+l4,number+2):
            arr5.append(arr3[num+count])
            num+=l5
        num=0
        arr6.append(arr5)
        arr5=[]
    for l7 in range(0,number-1):
        for l6 in range(1,recorddown+1):
            arr6[number-l6].append(arr3[downbody+1])
            downbody+=1
        recorddown+=-1
    for l8 in range(0,len(arr6)):
        end = numpy.concatenate(arr6[l8], axis=1)
        arr4.append(end)
    end2 = numpy.concatenate(arr4, axis=0)
    cv2.imshow("kk", end2)
    cv2.imwrite(name,end2)
    cv2.waitKey(0)
desecret("lofer lz/1-1.jpg",80)