# Team 20, Members: Mohammad Alkhaledi (Group Leader), Hanan Alshatti, Liamm Mirza, Farazi Kabir
# Milestone 3
# Date of Submission: 2nd April 2020
# Written By Hanan Alshatti and Liamm Mirza

from Cimpl import load_image, create_image, copy, get_width, get_height, get_color, set_color, save_as, save, set_zoom, show, create_color, distance, choose_file, choose_save_filename

import string

from T20_image_filters import two_tone, three_tone, extreme_contrast, sepia, posterize, detect_edges, detect_edges_better, flip_vertical, flip_horizontal   # Imports all the filter files for testing.

# Function Definitions

# Main Script

name_of_file = input('Please enter the name of the batch file along with its extension: ')

batch_file = open(name_of_file)             # Opens up the batch file.

for line in batch_file:                     # Iterates through each line of the batch file.
    list1 = line.split()                    # Slipts each component of the line into a list.
    filename = list1[0]                     # Saves thename of the file that will be edited as a seperate variable.
    saving_name = list1[1]                  # Saves the name of the file that will be given to the edited image as a seperate variable.
    repeat = len(list1)-2
    list_of_commands = []
    for elem in range(repeat):                              # Obtains the filter commands in each line of the batch file and saves it as a list of commands.
        list_of_commands += [(list1[len(list1)-repeat]).upper()]
        repeat -= 1
    image = load_image(filename)                            # Loads the image.
    filter_image = copy(image)                              # Makes a copy of the image to work with.
    for command in list_of_commands:                        # Iterates through the list of commands and applies the corresponding filters to the loaded image.
        if command == '2':
            filter_image = two_tone(filter_image, 'yellow', 'cyan')
        elif command == '3':
            filter_image = three_tone(filter_image, 'yellow', 'magenta', 'cyan')
        elif command == 'X':
            filter_image = extreme_contrast(filter_image)
        elif command == 'T':
            filter_image = sepia(filter_image)
        elif command == 'P':
            filter_image = posterize(filter_image)
        elif command == 'E':
            filter_image = detect_edges(filter_image, 10)
        elif command == 'I':
            filter_image = detect_edges_better(filter_image, 10)
        elif command == 'V':
            filter_image = flip_vertical(filter_image)
        elif command == 'H':
            filter_image = flip_horizontal(filter_image)
            
    save_as(filter_image, saving_name)                              # Saves the final image obtained after applying the filters from the list of commands.

batch_file.close()                                                  # Closes the batch file.
