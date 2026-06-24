# Team 20, Members: Mohammad Alkhaledi (Group Leader), Hanan Alshatti, Liamm Mirza, Farazi Kabir
# Milestone 3
# Date of Submission: 2nd April 2020
# Written By Mohammad Alkhaledi and Farazi Kabir

from Cimpl import load_image, create_image, copy, get_width, get_height, get_color, set_color, save_as, save, set_zoom, show, create_color, distance, choose_file, choose_save_filename

from T20_image_filters import two_tone, three_tone, extreme_contrast, sepia, posterize, detect_edges, detect_edges_better, flip_vertical, flip_horizontal   # Imports all the filter files for testing.

# Function Definitions

def prompt_answer() -> str:
    """
    
    Displays the available commands and prompts the user to enter a command.
    
    >>> prompt_answer()
    
    """
    print('L)oad image  S)ave-as', '2)-tone  3)- tone  X)treme contrast  T)int sepia  P)osterize', 'E)dge detect  I)mproved edge detect  V)ertical flip  H)orizontal flip', 'Q)uit', '', sep = '\n')
    command = input(': ')
    upper_command = command.upper()
    if upper_command in list_of_valid_commands:
        return upper_command

def prompt_threshold() -> int:
    """
    
    Prompts the user to enter a threshold value for the Edge Detection or the Improved Edge Detection filter.
    
    >>> prompt_threshold()
    
    """    
    threshold = int(input('Please enter the threshold value: '))
    return threshold

def prompt_filename() -> str:
    """
    
    Prompts the user to enter a filename.
    
    >>> prompt_filename()
    
    """    
    filename = input('Please enter a file name along with its extension: ')
    return filename

def loading_image():
    """
    
    Opens an external window and prompts the user to select an image from the window..
    
    >>> loading_image()
    
    """    
    loaded_image = load_image(choose_file())
    return loaded_image

def saving_image(image) -> None:
    """
    
    Saves a given image with a particular filename that it obtains by using the prompt_filename function to get a filename from the user.
    
    >>> saving_image(image)
    
    """    
    filename = prompt_filename()
    save_as(image, filename)

# Main Script

list_of_valid_commands = ['L', 'S', '2', '3', 'X', 'T', 'P', 'E', 'I', 'V', 'H', 'Q']
filter_image = create_image(1,1)     # Creates a default image for initialization purposes.
image = create_image(1,1)            # Creates a default image for initialization purposes.
command = ''
first_command = prompt_answer()      # Takes an initial command from the user.
state1 = True
state2 = True
while state1:                                   # The code enterd a while loop.
    
    state1 = True
    state2 = True
    
    if first_command != 'L' and first_command != 'Q':           # If the first command does not load an image or quit the programme the following errors are displayed based on the situation.
        
        if first_command not in list_of_valid_commands:             # If an invalid command is entered in the beginning, without an image loaded, then the programme lets the user know.
            print('\n','No such command','\n','', sep = '')
            first_command = prompt_answer()
        else:                                                       # If an image is not loaded in the first command, the programme lets the user know.
            print('\n','No image loaded','\n','', sep = '')
            first_command = prompt_answer()
            
    elif first_command == 'L':                  # If the first command loads an image, then code enters a while loop and the user is prompted with inputs unitl q is entered and the programme quits.
        
        image = loading_image()
        filter_image = copy(image)
        command = ''
        while command != 'Q' and state2:
            
            command = prompt_answer()    
            if command == '2':
                filter_image = two_tone(filter_image, 'yellow', 'cyan')
                show(filter_image)
            elif command == '3':
                filter_image = three_tone(filter_image, 'yellow', 'magenta', 'cyan')
                show(filter_image)
            elif command == 'X':
                filter_image = extreme_contrast(filter_image)
                show(filter_image)
            elif command == 'T':
                filter_image = sepia(filter_image)
                show(filter_image)
            elif command == 'P':
                filter_image = posterize(filter_image)
                show(filter_image)
            elif command == 'E':
                threshold = prompt_threshold()
                filter_image = detect_edges(filter_image, threshold)
                show(filter_image)
            elif command == 'I':
                threshold = prompt_threshold()
                filter_image = detect_edges_better(filter_image, threshold)
                show(filter_image)
            elif command == 'V':
                filter_image = flip_vertical(filter_image)
                show(filter_image)
            elif command == 'H':
                filter_image = flip_horizontal(filter_image) 
                show(filter_image)
            elif command == 'S':
                saving_image(filter_image)
            elif command not in list_of_valid_commands:             # If an invalid command is entered while applying the filters, then the programme lets the user know.
                print('\n','No such command','\n','', sep = '')
            elif command == 'L':                                    # The user is allowed to load and start working with a new image while already editing some other image.
                state2 = False
                
    if first_command == 'Q' or command == 'Q':              # If the first command entered is q or the user enters q any other time, the programme quits.
        state1 = False 
