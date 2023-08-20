
import os
import argparse
import webbrowser
import subprocess

# Check for docker and docker and docker_compose if not present install for more information refer to addtional information section in ReadMe file 
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
 # Create word press container for more information refer to addtional information section in ReadMe file
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
MYSQL_ROOT_PASSWORD=wordpress
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

# Manage WordPress Site for more iformation refer to addtional information section in ReadMe file
class WordPressSiteManager:
    def __init__(self, site_name):
        self.site_name = site_name

    def enable(self):
        os.chdir("wordpress")
        subprocess.run(["docker-compose", "start"])

    def disable(self):
        os.chdir("wordpress")
        subprocess.run(["docker-compose", "stop"])

    def delete(self):
        os.chdir("wordpress")
        subprocess.run(["docker-compose", "down"])
        os.system(f"sudo rm -rf wordpress/")
        os.system(f"sudo sed -i /{self.site_name}/d /etc/hosts")
        
# Main function of the program for more iformation refer to addtional information section in ReadMe file
def main():
    parser = argparse.ArgumentParser(description='Create, enable, disable, or delete a WordPress site using Docker')
    subparsers = parser.add_subparsers(dest='command')

    create_parser = subparsers.add_parser('create', help='Create a new WordPress site')
    create_parser.add_argument('site_name', help='Name of the site')

    enable_parser = subparsers.add_parser('enable', help='Enable a WordPress site')
    enable_parser.add_argument('site_name', help='Name of the site')

    disable_parser = subparsers.add_parser('disable', help='Disable a WordPress site')
    disable_parser.add_argument('site_name', help='Name of the site')

    delete_parser = subparsers.add_parser('delete', help='Delete an existing WordPress site')
    delete_parser.add_argument('site_name', help='Name of the site')

    args = parser.parse_args()
    
    if args.command == 'create':
        DockerHelper().is_present()
        WordPressSiteCreator(args.site_name).create()
    elif args.command == 'enable':
        WordPressSiteManager(args.site_name).enable()
    elif args.command == 'disable':
        WordPressSiteManager(args.site_name).disable()
    elif args.command == 'delete':
        WordPressSiteManager(args.site_name).delete()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

