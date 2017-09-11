    #!/bin/sh

sudo apt-get install python2.7 python2.7-dev
sudo apt-get install build-essential libssl-dev libevent-dev libjpeg-dev libxml2-dev libxslt-dev

# 安装 pip
sudo apt-get install python-pip
if [ $?!=0 ]
then 
    echo "install pip is successfully----"
fi
# 安装 virtualenv
sudo pip install virtualenv
if [ $?!=0 ]
then 
    echo "install virtualenv is successfully----"
fi