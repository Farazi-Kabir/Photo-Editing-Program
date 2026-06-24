# Photo-Editing-Program
ECOR 1051 IMAGE FILTERS PROJECT(R) Version 1.1  04/04/2020

Description:
------------------------

The project contains two programmes. One programme makes user of a batch file to read and execute commands, while the other presents the user with an
interactive user interface where the user can input commands and get the results in real time. Each programme makes use of nine distinct filters that 
can alter the colors, the tones and the contrast of an image, it can flip an image both horizontally and vertically and it can detect edges of an image 
with two different levels of accuracy without impacting the original image. These filtered images can then be saved by the user in the file type of their 
choice.

The project is composed of 3 files:

- T20_batch_ui.py: A python user interface which reads and executes commands from a batch file.

- T20_image_filters.py: A python script consisting of all the image filters which are imported by the user interfaces.

- T20_interactive_ui.py: A python interactive user interface where commands are executed following inputs from the user.

Installation:
------------------------

Python 3.8.1

Built-in python modules along with one external module is used in these programmes.

External modules which need to be installed:: Cimpl.py

This module is to be installed from the course website: 
https://culearn.carleton.ca/moodle/course/view.php?id=144561 > ECOR 1051 > Milestone 1 > 'P1 Task 4 - A folder containing Cimpl.py and Approved Sample Images-20200304'

Usage:
------------------------

> python T20_batch_ui.py

When prompted, enter the name of the batch file (along with its extension name) which contains the commands which are to be executed by the programme.
There is no error control for the batch user interface -- if the user enters a file which is not in the same folder that the programme is in or if the 
user enters the name of a batch file without its extension, then the programme ends.

> python T20_interactive_ui.py

When prompted, first load an image by entering 'L', then enter the number or letter corresponding to the filter you want to apply, following the displayed
options in the prompt. Then enter 'S' to save the image or 'Q' to end the programme. 
Additional prompts will appear if 'E' or 'I' is entered by the user, corresponding to the 'Edge Detection' or 'Improved Edge Detection' filters, this prompt 
will ask the user for a threshold value for edge detections. 
Additional prompt will appear if 'S' is entered, which corresponds to 'Save-as', this prompt will ask the user to enter the name they want give to the image 
they are currently saving along with its filetype extension.
There is error control present for the interactive user interface -- if the user enters an invalid command either before, or after loading an image 
then the programme lets the user know that there is no such command and prompts the user for a new command, if the user tries to apply a filter without 
first loading an image, then the programme lets the user know that there is no image loaded and prompts the user for a new command.

Credits:
------------------------

Team 20

Mohammad Alkhaledi - Recorded as author MA

- red_channel
- extreme_contrast
- detect_edges_better

Hanan Alshatti - Recorded as author HA

- green_channel
- sepia
- flip_vertical

Liamm Mirza - Recorded as author LM

- blue_channel
- posterize
- flip_horizontal
- _adjust_component

Farazi Kabir - Recorded as author FK

- combine
- two_tone
- three_tone
- detect_edges

Carleton University - Recorded as CU

- grayscale


Copyright 2020 Team 20 Corporation. All rights reserved.
ECOR 1051 IMAGE FILTERS PROJECT and its use are subject to a license agreement and are also subject to copyright, trademark, patent and/or other laws.
All other brand and product names are trademarks or registered.
