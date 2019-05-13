# counter

This tiny counter based on flask framework can show how many times you're visited genereted page. 

# Gettimg started 

run locally:
install python3.6
Ubuntu/Debian: 
sudo apt-get install python3.6 python3-pip
CentOS:
sudo yum install python36 python3-pip

Install python libs. 
pip install -r requirements.txt
At the .env file shuld be endpoint of your redis

run script:
python counter_app.py

Install redis
Ubuntu/Debian:  
sudo apt-get install redis-server
Centos: 
sudo yum install redis -y


To run in docker:
docker build -t counter .
At the .env file shuld be endpoint of your redis
docker-compose up -d
