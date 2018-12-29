import os
import subprocess

#Starting and enabling docker service on the server machine.
os.system('systemctl start docker')
os.system('systemctl enable docker')

#Now the docker service is running so we need to start the docker container image
#Which we have pulled from DockerHub containing CentOS along with necessary machine learning tools.

os.system('docker run -it -privileged centosforML:latest')
