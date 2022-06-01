import cv2
# if you ran this before, make sure you delete output.rbxlx first!
imgname = "example.png" #the name of the image here

a = cv2.resize(cv2.imread(imgname,1), (0,0), fx = 0.5, fy = 0.5)
cv2.imshow("the image",a)
re = open("output.rbxlx", "a")
re.write('<roblox xmlns:xmime="http://www.w3.org/2005/05/xmlmime" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.roblox.com/roblox.xsd" version="4"><External>null</External><External>nil</External><Item class="Workspace" referent="Workspace">')
main = ""
def part(pos,color):
    re.write('<Item class="Part" referent="RBXC8461F5915A74687B9F4247BB8A46776"><Properties><bool name="Anchored">true</bool><Vector3 name="size"><X>1</X><Y>1</Y><Z>1</Z></Vector3>')
    re.write('<bool name="CastShadow">false</bool><CoordinateFrame name="CFrame"><X>'+str(pos[0])+'</X><Y>'+str(pos[1])+'</Y><Z>'+str(pos[2])+'</Z><R00>1</R00><R01>0</R01><R02>0</R02><R10>0</R10><R11>1</R11><R12>0</R12><R20>0</R20><R21>0</R21><R22>1</R22></CoordinateFrame>')
    re.write('<Color3 name="Color"><R>'+str(color[0])+'</R><G>'+str(color[1])+'</G><B>'+str(color[2])+'</B></Color3>')
    re.write('</Properties></Item>')

l = len(a)
p = 0
for i in a:
    l -= 1
    p = 0
    for u in i:
        p += 1
        part([p,l,0],[u[2]/255,u[1]/255,u[0]/255]) #RGB -> BGR
re.write('</Item></roblox>')
re.close()
print("Finished!")
cv2.waitKey(0)
