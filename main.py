
import os
import argparse
import webbrowser
import subprocess


class Docker_and_DockerCompose_Check:
    def __init__(self):
        self.docker="docker"
        self.docker_compose="docker-compose"

    def ifpresent(self):
        if os.system("docker --version") == 0:
            print("Docker already installed")
        else:
            print("Docker not installed")
            
            os.system("curl -fsSL https://get.docker.com -o get-docker.sh")
            os.system("sh get-docker.sh")
            print("Docker is installed")
            os.remove("get-docker.sh")
 
        if os.system("docker-compose --version") == 0:
            print("Docker compose is already installed")
        else:
            print("Docker compose is not installed")
            os.system("sudo apt install docker-compose")
            print("Docker compose is installed")