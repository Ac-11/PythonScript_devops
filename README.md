# rtCamp DevOps Engineer Assignment

## Description
Welcome to the Dockerized WordPress LEMP Stack Script using python.
This script aims to simplify the process of setting up and managing WordPress sites using a LEMP stack within Docker containers.  With support of Pyhton as scripting language and a range of features including dependency management, site creation, enabling/disabling, and deletion.


## Outlines of Assigment
- Task 1: Check if docker and docker-compose is installed on the system. If not present, install the missing packages.
- Task 2: The script should be able to create a WordPress site using the latest WordPress Version. Please provide a way for the user to provide the site name as a command-line argument.
- Task 3: It must be a LEMP stack running inside containers (Docker) and a docker-compose file is a must.
- Task 4: Create a /etc/hosts entry for example.com pointing to localhost. Here we are assuming the user has provided example.com as the site name.
- Task 5: Prompt the user to open example.com in a browser if all goes well and the site is up and healthy.
- Task 6: Add another subcommand to enable/disable the site (stopping/starting the containers)
- Task 7: Add one more subcommand to delete the site (deleting containers and local files).


## Explanation in detail with screenshots

### Development Details
- Langauge Used: Pyhton
- Code Editor Used: VsCode
- Development Platform: Windows 11
- Testing Platform: Ubuntu 20.04.2 LTS

### How to run the script
1. Start by clicking the "Fork" button at the top right corner of the repository page to create your own copy of the repository on your GitHub account.
2. Open the terminal and use the following command to clone the repository. This will automatically create a folder named "PYTHONSCRIPT_DEVOPS" or use your preferred folder name.
`git clone https://github.com/Ac-11/PythonScript_devops.git`
3. Go to the directory and run the script
`cd PYTHONSCRIPT_DEVOPS`

#### Task 1: Check if docker and docker-compose is installed on the system. If not present, install the missing packages.

```bash
#Run the python script to execute
sudo python3 script.py create example.com
```
![u](Ss_readme/u.png)

#### Task 2: The script should be able to create a WordPress site using the latest WordPress Version. Please provide a way for the user to provide the site name as a command-line argument.

```bash
#to create wordpress site
sudo python3 script.py create "SiteNameyouWant"

#to create a wordpress site named example.com
sudo python3 script.py create example.com
```
![u](Ss_readme/u1.png)

#### Task 3:  It must be a LEMP stack running inside containers (Docker) and a docker-compose file is a must.
```bash
#Docker compose file specifications
version: '3'
services:
  db:
    image: mysql:5.7
    restart: always
    environment:
      MYSQL_RANDOM_ROOT_PASSWORD: 1
      MYSQL_DATABASE: wordpress_database
      MYSQL_USER: yourname
      MYSQL_PASSWORD: yourpassword
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
```
#### Task 4: Create a /etc/hosts entry for example.com pointing to localhost. Here we are assuming the user has provided example.com as the site name.

![u](Ss_readme/u3.png)

#### Task 5: Prompt the user to open example.com in a browser if all goes well and the site is up and healthy.

![u](Ss_readme/u4.png)

![u](Ss_readme/u5.png)