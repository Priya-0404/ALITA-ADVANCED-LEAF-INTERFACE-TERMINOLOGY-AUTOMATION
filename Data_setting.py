import os
import cv2

def setit(a, b, path):
    m = b
    for j in range(a, b):
        img = cv2.imread(f"Data/{path}/{j}.jpg")
        img = img [150:3000, 100:1200]
        r = 200.0 / img.shape[1]
        dim = (200, int(img.shape[0] * r))
        img = cv2.resize(img, dim)
        cv2.imwrite(f"Data/{path}/{j}.jpg", img)
        img = cv2.rotate(img, cv2.cv2.ROTATE_180)
        cv2.imwrite(f"Data/{path}/{m}.jpg", img)
        m += 1
    l = m-1
    with open(f"Data/{path}/data_count.txt", "w") as f:
        f.write(str(l))
        
with open("tree_count.txt" , "r") as file:
    curr_data = list(file.read().split("\n"))
data = os.listdir("Data")
difference = set(data) - set(curr_data)
data = list(difference)
if (len(data)>0):
    with open("tree_count.txt" , "a") as file:
        file.write("\n"+"\n".join(data))
    for i in range(0,len(data)):
        path = data[i]
        q = 1
        for j in os.listdir(f"Data/{path}"):
            source = f"Data/{path}/" + str(j)
            destination = f"Data/{path}/" + str(q) + ".jpg"
            os.rename(source, destination)
            q += 1
        l = len(os.listdir(f"Data/{path}"))
        setit(1, l+1, path)


for i in range(0,len(curr_data)):
    path = curr_data[i]
    l = len(os.listdir(f"Data/{path}"))-1
    with open(f"Data/{path}/data_count.txt", "r") as f:
        l1 = int(f.read())
        li = []
        w = l1+1
        for k in range(1,l1+1):
            li.append(str(k)+".jpg")
        lis = os.listdir(f"Data/{path}")
        lis.remove("data_count.txt")
        li = list(set(lis)-set(li))
        for j in range(0, len(li)):
            source = f"Data/{path}/" + str(li[j])
            destination = f"Data/{path}/" + str(w) +".jpg"
            os.rename(source, destination)
            w += 1
    if (l != l1):
        setit(l1+1, l+1, path) 
    
