#!/bin/bash

account=(1 2 3 5 8)
subject=("tiktok" "google")
prefix="beta"

hash_sha1_saved="03cfd743661f07975fa2f1220c5194cbaff48451"
###############################################################
read -p "Type your password:" -s password
hash=`echo ${password}|sha1sum`
if [[ ! ${hash} =~ ${hash_sha1_saved} ]];then
    echo "Password is NOT matched!!!"
    exit
fi

echo -e "\r\n"
echo "##########################################################"
for sub in "${subject[@]}"
do
    echo "Subject : ${sub}"
	for user in "${account[@]}"
	do
		salt="${prefix}${user}@bianxingji.top/${sub}"
		result=`strongpwd --salt ${salt} --password ${password}`
        echo ${salt} ${result}
	done
done
echo "##########################################################"
