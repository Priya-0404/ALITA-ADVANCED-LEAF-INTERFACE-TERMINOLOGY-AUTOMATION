import cv2
import os

image = input("Enter name of image\n")
l = os.listdir("Data")
name=""
name1=""
match = 0.0
for i in range(0, len(l)):
    path = l[i]
    l1 = os.listdir(f"Data/{path}")
    img = cv2.imread(image)
    if(img.shape[0] != 518 or img.shape[1] != 200):
        img = img [150:3000, 100:1200]
        r = 200.0 / img.shape[1]
        dim = (200, int(img.shape[0] * r))
        img = cv2.resize(img, dim)
    m = 0
    m1 = 0
    for j in range(1, len(l1)):
        img1 = cv2.imread(f"Data/{path}/{j}.jpg")
        a = img.shape[0]
        b = img.shape[1]
        c = img.shape[2]
        m = (a+b+c)/3
        match1 = 0
        match2 = 0
        match3 = 0
        for i in range(0, a):
            arr = img[i,1,1]
            arr1 = img1[i,1,1]
            ab = abs(int(arr)-int(arr1))
            if(ab <= 50):
                match1 += 1
        for i in range(0, b):
            arr = img[1,i,1]
            arr1 = img1[1,i,1]
            ab = abs(int(arr)-int(arr1))
            if(ab <= 50):
                match2 += 1
        for i in range(0, c):
            arr = img[1,1,i]
            arr1 = img1[1,1,i]
            ab = abs(int(arr)-int(arr1))
            if(ab <= 50):
                match3 += 1

        m1=(match1+match2+match3)/3
        r = m1/m * 100.0
        if (r>match):
            match = r
            name1 = path+"/"+str(j)+".jpg"
            name = path

if (match>70.0):
    print(name, name1)
