import JobSubwreplace as job
from JobSubwreplace import *

#sourceDir,workDir,cmd,jobName,inFile
inFile="text.txt"
source = "/scratch1/darkmatter/ds20k/g4ds10_reBuild_1218/configDarkSide.sh"
#source = "/scratch3/jpalmer/PhD/JP-LEDs2/BACCARAT/setup.sh"
workdir = "/scratch3/jpalmer/PhD/JP-LEDs2/BACCARAT"
command = "/scratch3/jpalmer/PhD/JP-LEDs2/BACCARAT/build.x86_64-slc6-gcc48-opt/bin/BACCARATExecutable"
myfile = "LEDTEST.mac"
errorfile = "errfile.txt"
logfile ="logfile.txt"
shellname = "LEDTEST"
jobdirname = "PythonTEST"
#x = jobSubmitter(source,workdir,command,"PythonTEST",myfile)
#jobSubmitter.writeJobBash(x)
#jobSubmitter.jobSubmit(x,errorfile,logfile)
for i in range(2,5,1):
    x = jobSubmitter(source,workdir,command,jobdirname,jobdirname+str(i),myfile)
    y = jobSubmitter.searchReplace(x,"/Bacc/source/set LEDPhotons TPCtop 1 1000","/Bacc/source/set LEDPhotons TPCtop "+str(i)+ " 1000",myfile,str(i))
    shellname = shellname + str(i)
    jobSubmitter.writeJobBash(x,y)
  
    
    shellname = "LEDTEST"
    
#source1 = "/scratch1/darkmatter/ds20k/g4ds10_reBuild_1218/configDarkSide.sh"
#wkDir = "/scratch1/darkmatter/ds20k/g4ds10_reBuild_1218/Linux-g++"
#cmd = "g4ds"
#myfile1 = "run.mac"

#y = jobSubmitter(source1,wkDir,cmd,"TestJob5", myfile1)
#jobSubmitter.writeJobBash(y)
#jobSubmitter.jobSubmit(y,errorfile,logfile) 