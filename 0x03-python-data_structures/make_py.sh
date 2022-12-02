#!/bin/bash

import_modules () {
	echo "Would you like to import any module? "
	read modules
	while [ "$modules" != "nvm" ]; do
		if [[ "$modules" == *"from"* ]]; then
			echo "$modules" >> $file_name.py
		else
			echo -e "import $modules" >> $file_name.py
		fi
		read modules
	done

	if [ "$modules" == "nvm" ]; then
		echo -e "\n" >> $file_name.py
	fi
}

add_comments () {
	echo "Would you like to add any comments? "
	read comment
	if [ "$comment" != "nvm" ]; then
		echo -e "\"\"\"$comment\"\"\"" >> $file_name.py
	else 
		echo -e "\n" >> $file_name.py
	fi
	echo "$comment" > comment.txt
}
check_style () {
	echo -e "You might have not adhered to PEP8 regulations,\n
	If no messages follow this message, all is good!
        "
        pycodestyle $file_name.py
	echo -e "Did you spot any errors, If so, "
        echo "Rectify: "
        read req
        if [ "$req" == "y" ]; then
        	vim $file_name.py
                pycodestyle $file_name.py
                echo "Done? "
                read assert2
                if [ "$assert2" == "y" ]; then
                	git add $file_name.py
                        git commit -m "Rectified coding style, PEP8"
		else
			check_style
		fi
	fi
}

init_file () {
	echo "What is the name of the file you would like to create:
Do not add the .py extension!"
	read file_name
	echo -e "#!/usr/bin/python3\n" > $file_name.py
	import_modules
	add_comments
	edit_file
	check_style
}
edit_file () {
	vim $file_name.py
	chmod a+x $file_name.py
	echo "Would you like to run the file $file_name.py you just created:
Type y to run any other key to skip: "
	read query
	if [ "$query" == "y" ]; then
		./$file_name.py
		echo "Did it run correctly? Would you like to stage and commit? "
		read response
		if [ "$response" == "y" ]; then
			git add $file_name.py
			default_message=`cat comment.txt`
			echo -e "Type your commit message for $file_name.py: The default is set to\n $default_message"
			read commit_message
			if [ "$commit_message" == "K" ]; then
				commit_message=$default_message
				echo "$commit_message"
			fi
			echo "You are about to commit with the message	$commit_message"
			read assert
			if [ "$assert" == "y" ]; then
				git commit -m "$commit_message"
			fi
		fi
	fi
}
init_file
