#!/bin/sh

removeSoftWare(){
    sudo apt-get remove $1
    if [ $?==0 ]
    then
        echo "$1 remove successfully\n" >> remove.log
    elif [ $?==100 ]
        echo "$1 can't finded\n'" >> remove.log
    fi
}

removeSomeSoftWare(){
    for software in $*
    do
        removeSoftWare $software
    done
}

installSoftWare(){
    sudo apt-get install $1
    if [ $?==0 ]
    then 
        echo "$1 installed successfully!\n" >> install.log
    else
        echo "$1 installed unsuccessfully!\n " >> install.log
    fi
}

installSomeSoftWare(){
    for software in $*
    do
        installSoftWare $software
    done
}

installDeb(){
    sudo dpkg -i $1
    if [ $?==0 ]
    then
        echo "$1 installed successfully!\n" >> install.log
    else 
        sudo apt-get install -f
        sudo dpkg -i $1
        if [ $?==0 ]
        then
            echo "$1 installed successfully!\n" >> install.log
        else 
            echo "$1 installed unsuccessfully!\n" >> install.log
        then
    fi
}

installPythonMoudle(){
    sudo pip install $1
    if [ $?==0 ]
    then
        echo "$1 install successfully\n" >> install.log
    else
        echo "$1 install successfully\n'" >> install.log
    fi
}


configPythonEnvironment(){
    # config python2.7 environment
    installSoftWare python2.7
    installSoftWare python2.7-dev
    installSoftWare python-pip
    installSoftWare virtualenv

    installSoftWare build-essential
    installSoftWare libssl-dev
    installSoftWare libevent-dev
    installSoftWare libjpeg-dev
    installSoftWare libxml2-dev
    installSoftWare libxslt-dev

    installSoftWare redis-cli

    # install some module
    installPythonMoudle pymongo
    installPythonMoudle redis
    installPythonMoudle BeautifulSoup4


}

installMongoDB(){
    tar -zxvf mongodb-linux-x86_64-ubuntu1604-3.4.3.tgz
    sudo mkdir /usr/local/mongodb
    sudo cp mongodb-linux-x86_64-ubuntu1604-3.4.3/ /usr/local/mongodb/
    sudo mkdir -p /data/db
    sudo mkdir -p /data/logs
    sudo touch /data/logs/mongodb.log
    sudo chmod 777 /data/*
}

installMacTheme(){
    #config mac theme
    sudo add-apt-repository ppa:noobslab/macbuntu
    sudo apt-get update
    installSoftWare macbuntu-os-icons-lts-v7
    installSoftWare macbuntu-os-ithemes-lts-v7
    installSoftWare unity-tweak-tool
}

installTLP(){
    sudo add-apt-repository ppa:linrunner/tlp
    sudo apt-get update
    removeSomeSoftWare tlp tlp-rdw
    # sudo tlp start
    # sudo tlp-stat
}


#install zsh  https://zhuanlan.zhihu.com/p/27052046
sudo apt-get install zsh
zsh --version
sudo chsh -s $(which zsh)
wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | sh



#remove some software
removeSoftWare libreoffice-common
removeSoftWare unity-webapps-common
removeSomeSoftWare onboard deja-dup
removeSomeSoftWare gnome-mines cheese transmission-common gnome-orca webbrowser-app gnome-sudoku  landscape-client-ui-install
removeSomeSoftWare thunderbird totem rhythmbox empathy brasero simple-scan gnome-mahjongg aisleriot


# install some software
installSoftWare vim
installSoftWare git
installSoftWare guake
installSomeSoftWare tpp cloc figlet

# change hosts
sudo cp hosts /etc/
installSoftWare nscd
sudo /etc/init.d/nscd restart
if [ $?!=0 ]
then
	echo "change hosts successfully!!!\n" >> install.log
fi

# install sougou
installSoftWare fcitx libssh2-1
installDeb sougou_64.deb


sudo apt-get install mysql-server
sudo apt-get install mysql-client







sudo apt-get install libboost-all-dev
sudo apt-get install aptitude
aptitude search boost
