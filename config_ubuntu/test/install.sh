#!/bin/bash

installSoftWare(){
    sudo apt-get install $1
    if [ $?==0 ]
    then 
        echo "$1 installed successfully!\n" >> $2
    else
        echo "$1 installed unsuccessfully!\n " >> $2
    fi
}

installSomeSoftWare(){
    for software in $*
    do
        installSoftWare $software $1
    done
}

b(){
    echo "get args $2" >> $1
}

a(){
    logfile= $1
    index= 2
    while (($index<=$#))
    do
        b $logfile $($index)
    done
}


a install.log 1 2 3 4 5