#!/usr/bin/env python3

import shutil
import os

# First change to the HOME student directory
os.chdir('/home/student/mycode/')

# Copy the file, sdn_network.txt
shutil.copy('5g_research/sdn_network.txt', '5g_research/sdn_network.txt.copy')

#This creates the directory if it does not exist already
shutil.copytree('5g_research/', '5g_research_backup/')
