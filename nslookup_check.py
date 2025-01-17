# Script Name		: nslookup_check.py
# Author				: Craig Richards
# Created				: 5th January 2012
# Last Modified		:
# Version				: 1.0

# Modifications		:

# Description			: This very simple script opens the file server_list.txt and then does a nslookup for each one to check the DNS entry

import subprocess  # Import the subprocess module
from security import safe_command

for server in open("server_list.txt"):  # Open the file and read each line
    safe_command.run(subprocess.Popen, ("nslookup " + server)
    )  # Run the nslookup command for each server in the list
