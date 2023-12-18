#!/usr/bin/env bash

function backup {
	date=$(date "+%F")
	archive_name="$(basename $1)-$date.tar"
	tar -cvf $archive_name $1
	echo "done, your archive is $(realpath $archive_name)"
}

function help {
	echo '''Usage
-----------------
help - print this message;
backup <directory name> - make an archive of the directory
'''
}

$1 $2 || help
