#!/bin/bash

salts=( "chusmail@126.com"
	  )

hash_sha1_saved='d09d60441c42c4a87e750a378398d88125297a95'
###############################################################
read -p "Type your password:" -s password
hash=`echo -n ${password}|sha1sum`
if [[ ! ${hash} =~ ${hash_sha1_saved} ]];then
    echo "Password is NOT matched!!!"
    exit
fi

echo -e "\r\n"
echo "############### Windy Albert's PASSWORD ####################"
for salt in "${salts[@]}"
do
	result=`strongpwd --salt ${salt} --password ${password}`
	echo "${salt} ${result}" | awk '{printf("%-35s%s\033[1;32m%s\033[0m\n\n",$1,$2,$3)}'
done
echo "############################################################"
