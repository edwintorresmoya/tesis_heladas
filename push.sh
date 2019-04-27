#!/bin/bash
export dia=`date`
echo ${dia}
git add --all
git commit -m "${dia}"
git push -u origin master
