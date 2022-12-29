import string


drivers_name=["lEwis_HaMiLton","MaX_vERsTapPen","SebASTIan_vEtTeL","ChaRleS_IEcLeRc"]
print(list(enumerate(drivers_name)))
indices=[]
driver=[]

for c,d in enumerate(drivers_name):
    indices.append(c)
    driver.append(d)
for i in range(0,4):
    print(indices[i]) 
    print(driver[i])
for i in range (0,4):
    driver[i]=driver[i].lower()
    
    driver[i]=driver[i].replace("_"," ")
    print(driver[i])
length = lambda val : len(val)
temp=list(map(length,driver))
print(f"{driver}")
print(f"{temp}")
z=zip(driver,temp)
print(list(z))
indices=[sum(i) for i in zip(indices,temp)]
print(indices)
indices.sort(reverse=True)
print(indices)
F1_drivers=dict(zip(indices,driver))
print(F1_drivers)
