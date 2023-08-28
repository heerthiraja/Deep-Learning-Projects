import os
os.chdir('D:\\MasterClass\\Artificial_Intelligence\\Day12\\Code\\simple_images\\thanosMarvel\\')
i=1
for file in os.listdir():
    src=file
    dst="2"+"_"+str(i)+".jpg"
    os.rename(src,dst)
    i+=1

