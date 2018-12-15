import os
import shutil

path = 'E:/MOVIES'
a=os.listdir(path)
movie_folder=a[:]
count=1
for name in range(len(movie_folder)):
    if(os.path.isdir(path+'/'+movie_folder[name])!=True):
        x=movie_folder[name]
        x=x[0:len(x)-4]
        p1=path+'/'+x
        if os.path.exists(path+'/'+x):
            os.makedirs(path+'/'+x+str(count))
            count+=1
            shutil.move(path+'/'+movie_folder[name],path+'/'+x+str(count))
        else:
            os.makedirs(path+'/'+x)
            shutil.move(path+'/'+movie_folder[name],path+'/'+x)
