import jobsubmission.JobSub 
from jobsubmission.JobSub import *
#import JobSub

inFile="run.mac"
source = "/scratch1/darkmatter/ds20k/g4ds10_reBuild_1218/configDarkSide.sh"
workdir = "/scratch1/darkmatter/ds20k/g4ds10_reBuild_1218/Linux-g++"
command = "./g4ds"
myfile = "bob.mac"
errorfile = "errfile.txt"
logfile ="logfile.txt"
shellname = "LEDTEST"
jobdirname = "Testing 10"

#x = jobsubmission.jobSubmitter
print "creating object"
x = jobsubmission.jobSubmitter(source,"Test9",command,myfile,workdir)
print "here1"
#jobsubmission.jobSubmitter.writeJobBash(x)
#JobSub.jobSubmitter.writeJobBash(x)
#print "here2"
jobsubmission.jobSubmitter.jobSubmit(x,errorfile,logfile,"long","8gb")
