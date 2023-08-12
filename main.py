
import os
import argparse
import webbrowser
import subprocess

class DockerHelper:
    def __init__(self):
        self.docker = "docker"
        self.docker_compose = "docker-compose"

    def is_present(self):
        if os.system(f"{self.docker} --version") == 0:
            print("Docker is already installed on the system")
        else:
            print("Docker is not installed on the system")
            os.system("curl -fsSL https://get.docker.com -o get-docker.sh")
            os.system("sh get-docker.sh")
            print("Docker is installed on the system")
            os.remove("get-docker.sh")

        if os.system(f"{self.docker_compose} --version") == 0:
            print("Docker-compose is already installed on the system")
        else:
            print("Docker-compose is not installed on the system")
            os.system("sudo apt install docker-compose")
            print("Docker-compose is installed on the system")

class WordPressSiteCreator:
    def __init__(self, site_name):
        self.site_name = site_name

    def create(self):
        os.system("mkdir wordpress")
        os.system("cp -r s1.py wordpress/")
        os.chdir("wordpress")
        os.system("touch docker-compose.yml")
        with open("docker-compose.yml", "w") as f:
            f.write(
                """
version: '3'
services:
  db:
    image: mysql:5.7
    restart: always
    environment:
      MYSQL_RANDOM_ROOT_PASSWORD: 1
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: wordpress
    volumes:
      - db_data:/var/lib/mysql
  wordpress:
    depends_on:
      - db
    image: wordpress:latest
    restart: always
    ports:
      - '8080:80'
    environment:
      WORDPRESS_DB_HOST: db:3306
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: wordpress
      WORDPRESS_DB_NAME: wordpress
    volumes:
      - wordpress:/var/www/html
volumes:
  db_data:
  wordpress:
                """
            )

        os.system("touch .env")
        with open(".env", "w") as f:
            f.write(
                """
MYSQL_ROOT_PASSWORD=somewordpress
MYSQL_DATABASE=wordpress
MYSQL_USER=wordpress
MYSQL_PASSWORD=wordpress
                """
            )

        subprocess.run(["docker-compose", "up", "-d"])
        with open("/etc/hosts", "a") as f:
            f.write(f"\n127.0.0.1 {self.site_name}")

        print(f"WordPress site is now running, access it with http://{self.site_name}:8080")
        webbrowser.open(f"https://{self.site_name}:8080")

