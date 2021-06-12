#!/usr/bin/python3
import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
vol = mydata.getvalue("vol")
name = mydata.getvalue("name")
image = mydata.getvalue("image")
version = mydata.getvalue("version")
port = mydata.getvalue("port")
defaultport = mydata.getvalue("defaultport")
networkname = mydata.getvalue("networkname")
mount = mydata.getvalue("mount")
giturl = mydata.getvalue("giturl")

if networkname == None:
    if (vol and mount)==None:
            print("mount and vol none")
            cmd2 = "sudo docker run -dit  --name {0}  -p {1}:{2} {3}:{4}".format(name,port,defaultport,image,version)
            output2 = subprocess.getoutput(cmd2)
            print("your container id is:" + output2)
    else:        
            cmd1 = "sudo docker volume create {}".format(vol)
            output1 = subprocess.getoutput(cmd1)
            print("your volume name is:" + vol)
            if giturl:
                mkdir = subprocess.getoutput("sudo docker volume create {}".format(vol))
                git = subprocess.getoutput("sudo git clone {}  /var/lib/docker/volumes/{}/_data/".format(giturl,vol))
                print("your github repo URL is:" + git)
                print("Cloned!!!")
            cmd2 = "sudo docker run -dit -v{0}:{6} --name {1}  -p {2}:{3} {4}:{5}".format(vol,name,port,defaultport,image,version,mount)
            output2 = subprocess.getoutput(cmd2)
            print("your container id is:" + output2)

elif (vol and mount)==None:
        mount="/var"
        vol="test25"
        cmd3 = "sudo docker network create --driver bridge {}".format(networkname)
        output3 = subprocess.getoutput(cmd3)
        print("your networkname is:" + networkname)
        cmd2 = "sudo docker run -dit  --name {} --network {} -p {}:{} {}:{}".format(name,networkname,port,defaultport,image,version)
        output2 = subprocess.getoutput(cmd2)
        print("your container id is:" + output2)

if giturl:
        cmd3 = "sudo docker network create --driver bridge {}".format(networkname)
        output3 = subprocess.getoutput(cmd3)
        print("your networkname is:" + networkname)
        remove = subprocess.getoutput("sudo rm -frv /var/lib/docker/volumes/{}".format(vol))
        mkdir = subprocess.getoutput("sudo docker volume create {}".format(vol))
        print("your volume name is:" + vol)
        git = subprocess.getoutput("sudo git clone {}  /var/lib/docker/volumes/{}/_data/".format(giturl,vol))
        print("your github repo URL is:" + git)
        print("Cloned!!!")
        cmd2 = "sudo docker run -dit -v {0}:{7} --name {1} --network {6} -p {2}:{3} {4}:{5}".format(vol,name,port,defaultport,image,version,networkname,mount)
        output2 = subprocess.getoutput(cmd2)
        print("your container id is:" + output2)

elif giturl==None:
        print("giturl none")
        cmd3 = "sudo docker network create --driver bridge {}".format(networkname)
        output3 = subprocess.getoutput(cmd3)
        print("your networkname is:" + networkname)
        mkdir = subprocess.getoutput("sudo docker volume create {}".format(vol))
        print("your volume name is:" + vol)
        cmd2 = "sudo docker run -dit -v {0}:{7} --name {1} --network {6} -p {2}:{3} {4}:{5}".format(vol,name,port,defaultport,image,version,networkname,mount)
        output2 = subprocess.getoutput(cmd2)
        print("your container id is:" + output2)

else: 
    print("Enter compulsory fields")
