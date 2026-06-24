# Team 20, Members: Mohammad Alkhaledi (Group Leader), Hanan Alshatti, Liamm Mirza, Farazi Kabir
# Milestone 3
# Date of Submission: 2nd April 2020

from Cimpl import load_image, create_image, copy, get_width, get_height, get_color, set_color, save_as, save, set_zoom, show, create_color, distance, choose_file, choose_save_filename

# Function Definitions

def red_channel(image):
    """ Written By: 'Mohammad Alkhaledi'
    
    (Cimpl.Image) -> Cimpl.Image
    
    Returns the chosen image filtered red by removing all the green and blue components of each pixel, while preserving the red component.
    
    >>> image = load_image(choose_file())
        filtered_image = red_channel(image)
        *displays image with red filter applied*
    
    """
    
    new_image = copy(image)     # Creates a copy of the file to work with.
    for pixel in new_image:     # Loops through each pixel in this image.
        x, y, (r, g, b) = pixel # Unpacks every pixel tuple into its corresponding components.
        new_color = create_color(r, 0, 0)       # Creates a new color which consists of only the red component of that particular pixel location, making the blue and green components zero.
        set_color(new_image, x, y, new_color)   # Assigns this new color to that same pixel.
    return new_image                            # Returns the filtered image.

def green_channel(image):
    """ Written By: 'Hanan Alshatti'
    
    (Cimpl.Image) -> Cimpl.Image
    
    Returns the chosen image filtered green by removing all the red and blue components of each pixel, while preserving the green component.
    
    >>> image = load_image(choose_file())
        filtered_image = green_channel(image)
        *displays image with green filter applied*
    
    """
    
    new_image = copy(image)     # Creates a copy of the file to work with.
    for pixel in new_image:     # Loops through each pixel in this image.
        x, y, (r, g, b) = pixel # Unpacks every pixel tuple into its corresponding components.
        new_color = create_color(0, g, 0)       # Creates a new color which consists of only the green component of that particular pixel location, making the red and blue components zero.
        set_color(new_image, x, y, new_color)   # Assigns this new color to that same pixel.
    return new_image                            # Returns the filtered image.

def blue_channel(image):
    """ Written By: 'Liamm Mirza'
    
    (Cimpl.Image) -> Cimpl.Image
    
    Returns the chosen image filtered blue by removing all the red and green components of each pixel, while preserving the blue component.
        
    >>> image = load_image(choose_file())
        filtered_image = blue_channel(image)
        *displays image with blue filter applied*
    
    """
    
    new_image = copy(image)     # Creates a copy of the file to work with.
    for pixel in new_image:     # Loops through each pixel in this image.
        x, y, (r, g, b) = pixel # Unpacks every pixel tuple into its corresponding components.
        new_color = create_color(0, 0, b)       # Creates a new color which consists of only the blue component of that particular pixel location, making the red and green components zero.
        set_color(new_image, x, y, new_color)   # Assigns this new color to that same pixel.
    return new_image                            # Returns the filtered image.

def combine(red_image, green_image, blue_image):
    """ Written By: 'Farazi Kabir'
    
    (Cimpl.Image, Cimpl.Image, Cimpl.Image) -> Cimpl.Image
    
    Returns the combination of the three images inputted, with each pixel containing that appropriate red, green and blue components retrived from that same pixel location in each of the images.
    
    >>> red_image = load_image(choose_file())
        green_image = load_image(choose_file())
        blue_image = load_image(choose_file())
        combined_image = combine(red_image, green_image, blue_image)
        *displays combined image*
    
    """
    
    new_red_image = copy(red_image)             # Creates a copy of the first file (red) to work with.
    new_green_image = copy(green_image)         # Creates a copy of the second file (blue) to work with.
    new_blue_image = copy(blue_image)           # Creates a copy of the third file (green) to work with.
    
    filtering_image = copy(red_image)           # Creates a copy of the first file to apply the filter to.
    
    for pixel in filtering_image:                       # Loops through each pixel in this image.
        x, y, (r,g,b) = pixel                           # Unpacks every pixel tuple into its corresponding components.
        from_red_image = get_color(new_red_image,x,y)   # Retrives the color of each pixel location in the red image file.
        r1,g1,b1 = from_red_image                       # Unpacks every pixel tuple in the red image into its corresponding components.
        red = r1                                        # Stores the red component as a variable.
        from_green_image = get_color(new_green_image,x,y)   # Retrives the color of each pixel location in the green image file.
        r2,g2,b2 = from_green_image                         # Unpacks every pixel tuple in the green image into its corresponding components.
        green = g2                                          # Stores the green component as a variable.
        from_blue_image = get_color(new_blue_image,x,y)         # Retrives the color of each pixel location in the blue image file.
        r3,g3,b3 = from_blue_image                              # Unpacks every pixel tuple in the blue image into its corresponding components.
        blue = b3                                               # Stores the blue component as a variable.
        combined_color = create_color(red,green,blue)   # Creates a new color which consists of these components for that particular pixel location.
        set_color(filtering_image,x,y,combined_color)   # Assigns this new color to that same pixel.
    return filtering_image                              # Returns the combined image.

def two_tone(image, color1, color2):
    """ Written By: 'Farazi Kabir'
    
    (Cimpl.Image, str, str) -> Cimpl.Image
    
    Returns the chosen image filtered to have only the two color tones that are specified in the function by calculating the brightness of the pixel and if the brightness is between 0 and 127 the pixel is set to the first color and if the brightness is between 128 and 255 the pixel is set to the second color.
    
    >>> image = load_image(choose_file())
        filtered_image = two_tone(image, 'black', 'white')         # The color names must be entered as a string.
        *displays image with two tone filter applied*
    
    """
    new_image = copy(image)                              # Creates a copy of the file to work with.
    
    # Creating new tuples with the first element of the tuple being the name of the colors and the second element being the color itself.
    
    black = ('black', create_color(0, 0, 0))
    white = ('white', create_color(255, 255, 255))
    red = ('red', create_color(255, 0, 0))
    lime = ('lime', create_color(0, 255, 0))
    blue = ('blue', create_color(0, 0, 255))
    yellow = ('yellow', create_color(255, 255, 0))
    cyan = ('cyan', create_color(0, 255, 255))
    magenta = ('magenta', create_color(255, 0, 255))
    gray = ('gray', create_color(128, 128, 128))

    colors = [black, white, red, lime, blue, yellow, cyan, magenta, gray]   # Arranging the tuples into a list.
    
    tone1 = create_color(0, 0, 0)                                           # Creating a default color variables for color1.
    tone2 = create_color(0, 0, 0)                                           # Creating a default color variables for color2.
    
    for elem in colors:         # Loops through each tuple in the list.
        name, color = elem      # Unpacks each tuple to get the name and color components.
        if name == color1:      # Compares the name with the first color name inputted in the function.
            tone1 = color
        elif name == color2:    # Compares the name with the second color name inputted in the function.
            tone2 = color
            
    for pixel in new_image:     # Loops through each pixel in this image.
        x, y, (r, g, b) = pixel # Unpacks every pixel tuple into its corresponding components.
        brightness = (r + g + b) // 3   # Calculates the brightness of each pixel.
        
        if 0 <= brightness <= 127:
            new_color = tone1
            set_color(new_image, x, y, new_color)
        elif 128 <= brightness <= 255:
            new_color = tone2
            set_color(new_image, x, y, new_color)
            
    return new_image            # Returns the filtered image.

def three_tone(image, color1, color2, color3):
    """ Written By: 'Farazi Kabir'
    
    (Cimpl.Image, str, str, str) -> Cimpl.Image
    
    Returns the chosen image filtered to have only the three color tones that are specified in the function by calculating the brightness of the pixel and if the brightness is between 0 and 84 the pixel is set to the first color, if the brightness is between 85 and 170 the pixel is set to the second color and if the brightness is between 171 and 255 the pixel is set to the third color.
    
    >>> image = load_image(choose_file())
        filtered_image = three_tone(image, 'black', 'white', 'grey')         # The color names must be entered as a string.
        *displays image with three tone filter applied*
    
    """
    new_image = copy(image)                              # Creates a copy of the file to work with.
    
    # Creating new tuples with the first element of the tuple being the name of the colors and the second element being the color itself.
    
    black = ('black', create_color(0, 0, 0))
    white = ('white', create_color(255, 255, 255))
    red = ('red', create_color(255, 0, 0))
    lime = ('lime', create_color(0, 255, 0))
    blue = ('blue', create_color(0, 0, 255))
    yellow = ('yellow', create_color(255, 255, 0))
    cyan = ('cyan', create_color(0, 255, 255))
    magenta = ('magenta', create_color(255, 0, 255))
    gray = ('gray', create_color(128, 128, 128))

    colors = [black, white, red, lime, blue, yellow, cyan, magenta, gray]   # Arranging the tuples into a list.
    
    tone1 = create_color(0, 0, 0)                                           # Creating a default color variables for color1.
    tone2 = create_color(0, 0, 0)                                           # Creating a default color variables for color2.
    tone3 = create_color(0, 0, 0)                                           # Creating a default color variables for color3.
    
    for elem in colors:         # Loops through each tuple in the list.
        name, color = elem      # Unpacks each tuple to get the name and color components.
        if name == color1:      # Compares the name with the first color name inputted in the function.
            tone1 = color
        elif name == color2:    # Compares the name with the second color name inputted in the function.
            tone2 = color
        elif name == color3:    # Compares the name with the third color name inputted in the function.
            tone3 = color
            
    for pixel in new_image:     # Loops through each pixel in this image.
        x, y, (r, g, b) = pixel # Unpacks every pixel tuple into its corresponding components.
        brightness = (r + g + b) // 3   # Calculates the brightness of each pixel.
        
        if 0 <= brightness <= 84:
            new_color = tone1
            set_color(new_image, x, y, new_color)
        elif 85 <= brightness <= 170:
            new_color = tone2
            set_color(new_image, x, y, new_color)
        elif 171 <= brightness <= 255:
            new_color = tone3
            set_color(new_image, x, y, new_color)        
            
    return new_image            # Returns the filtered image.

def extreme_contrast(image):
    """ Written By: 'Mohammad Alkhaledi'
    
    (Cimpl.Image) -> Cimpl.Image
    
    Returns the chosen image filtered to maximize the contrast between pixels. It looks at each component of the pixel, if the component is between 0 and 127 then the component is set to 0 and if the component is between 128 and 255 then the component is set to 255.
    
    >>> image = load_image(choose_file())
        filtered_image = extreme_contrast(image)
        *displays image with extreme contrast filter applied*
    
    """
    new_image = copy(image)                              # Creates a copy of the file to work with.
    
    VALUE1 = 0
    VALUE2 = 255
    
    for pixel in new_image:     # Loops through each pixel in this image.
        x, y, (r,g,b) = pixel # Unpacks every pixel tuple into its corresponding components.
            
        if 0 <= r <= 127:
            red = VALUE1
        elif 128 <= r <= 255:
            red = VALUE2
            
        if 0 <= g <= 127:
            green = VALUE1
        elif 128 <= g <= 255:
            green = VALUE2
            
        if 0 <= b <= 127:
            blue = VALUE1
        elif 128 <= b <= 255:
            blue = VALUE2
            
        new_color = create_color(red, green, blue)
        set_color(new_image, x, y, new_color)
        
    return new_image            # Returns the filtered image.

def sepia(image):
    """ Written By: 'Hanan Alshatti'
    
    (Cimpl.Image) -> Cimpl.Image
    
    Returns the chosen image filtered to have a sepia tint. It first changes each pixel to grayscale and then adjusts the red and blue components of this grayscale image to achieve this.
    
    >>> image = load_image(choose_file())
        filtered_image = sepia(image)
        *displays image with sepia filter applied*
    
    """
    new_image1 = copy(image)                              # Creates a copy of the file to work with.
    new_image2 = grayscale(new_image1)
    
    for pixel in new_image2:     # Loops through each pixel in this image.
        x, y, (r,g,b) = pixel # Unpacks every pixel tuple into its corresponding components.
            
        if r < 63:
            red = 1.1 * r
            green = g
            blue = 0.9 * b
            
        elif 63 <= r <= 191:
            red = 1.15 * r
            green = g
            blue = 0.85 * b
        
        elif r > 191:
            red = 1.08 * r
            green = g
            blue = 0.93 * b
        
        new_color = create_color(red, green, blue)
        set_color(new_image2, x, y, new_color)
        
    return new_image2            # Returns the filtered image.

def grayscale(image):
    """
    
    (Cimpl.Image) -> Cimpl.Image
    
    Return a grayscale copy of image.
   
    >>> image = load_image(choose_file())
    >>> gray_image = grayscale(image)
    >>> show(gray_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:

        # Use the pixel's brightness as the value of RGB components for the 
        # shade of gray. These means that the pixel's original colour and the
        # corresponding gray shade will have approximately the same brightness.
        
        brightness = (r + g + b) // 3
        
        # or, brightness = (r + g + b) / 3
        # create_color will convert an argument of type float to an int
        
        gray = create_color(brightness, brightness, brightness)
        set_color(new_image, x, y, gray)      
    return new_image

def posterize(image):
    """ Written By: 'Liamm Mirza'
    
    (Cimpl.Image) -> Cimpl.Image
    
    Returns the chosen image with the posterize filter applied. It first checks r,g,b component of each pixel and determines which quadrant the component lies in using a helper function. It then adjusts the components accordingly to produce the posterized image.
    
    >>> image = load_image(choose_file())
        filtered_image = posterize(image)
        *displays image with posterize filter applied*
    
    """
    new_image = copy(image)                              # Creates a copy of the file to work with.
    
    for pixel in new_image:     # Loops through each pixel in this image.
        x, y, (r,g,b) = pixel # Unpacks every pixel tuple into its corresponding components.
        
        red = _adjust_component(r)
        green = _adjust_component(g)
        blue = _adjust_component(b)
        
        new_color = create_color(red, green, blue)
        set_color(new_image, x, y, new_color)
        
    return new_image            # Returns the filtered image.

def _adjust_component(component: int) -> int:
    """ Written By: 'Liamm Mirza'
    
    (int) -> int
    
    Returns the midpoint value of the quadrant that the given component lies in.
    
    >>> _adjust_component(120)
        95
    >>> _adjust_component(220)
        223
    
    """    
    
    VALUE1 = 31
    VALUE2 = 95
    VALUE3 = 159
    VALUE4 = 223
    
    if 0 <= component <= 63:
        return VALUE1
    elif 64 <= component <= 127:
        return VALUE2
    elif 128 <= component <= 191:
        return VALUE3
    elif 192 <= component <= 255:
        return VALUE4

def detect_edges(image, threshold):
    """ Written By: 'Farazi Kabir'
    
    (Cimpl.Image, int) -> Cimpl.Image
    
    Returns the chosen image filtered by the edge detection algorithm. This is done by comparing the brightness of every pixel with the pixel below it to determine the contrast between the pixels. If the contrast is high then the top pixel is set to black and if the contrast is low then the top pixel is set to white. The resulting image is black and white.
    
    The threshold must be a positive integer.
    
    >>> image = load_image(choose_file())
        filtered_image = detect_edges(image, 10)
        *displays image with edge detection filter applied*
    
    """
    new_image = copy(image)                              # Creates a copy of the file to work with.
    
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    
    for x, y, (r,g,b) in new_image:      # Loops through each pixel in this image.
        brightness1 = (r + g + b) // 3   # Calculates the brightness of each pixel.
        if y < get_height(new_image) - 1:
            color_of_pixel_below = get_color(new_image, x, y+1)     # Gets the color of the pixel below the current pixel.
            r1, g1, b1 = color_of_pixel_below                       # Unpacks the tuple for this color.
            brightness2 = (r1 + g1 + b1) // 3                       # Calculates the brightness of each pixel below the original pixel.
            contrast = abs(brightness1 - brightness2)               # Calculates the contrast between the two pixels.
            if contrast > threshold:
                set_color(new_image, x, y, black)
            else:
                set_color(new_image, x, y, white)
        else: 
            set_color(new_image, x, y, white)                       # Sets the last row of pixels to white.

            
    return new_image            # Returns the filtered image.

def detect_edges_better(image, threshold):
    """ Written By: 'Mohammad Alkhaledi'
    
    (Cimpl.Image, int) -> Cimpl.Image
    
    Returns the chosen image filtered by the improved edge detection algorithm. This is done by comparing the brightness of every pixel with the pixel below as well as to the right of it to determine the contrast between the pixels. If the contrast is high between the pixel and the one below it or to the right of it, then the pixel is set to black, otherwise the contrast is low then the top pixel is set to white. The resulting image is black and white.
    
    The threshold must be a positive integer.
    
    >>> image = load_image(choose_file())
        filtered_image = detect_edges_better(image, 10)
        *displays image with edge detection filter applied*
    
    """
    new_image = copy(image)                              # Creates a copy of the file to work with.
    
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    
    for x, y, (r,g,b) in new_image:      # Loops through each pixel in this image.
        brightness1 = (r + g + b) // 3   # Calculates the brightness of each pixel.
        if y < get_height(new_image) - 1 and x < get_width(new_image) - 1:
            
            color_of_pixel_below = get_color(new_image, x, y+1)     # Gets the color of the pixel below the current pixel.
            r1, g1, b1 = color_of_pixel_below                       # Unpacks the tuple for this color.
            brightness2 = (r1 + g1 + b1) // 3                       # Calculates the brightness of each pixel below the original pixel.
            contrast_below = abs(brightness1 - brightness2)         # Calculates the contrast between the two pixels.
            
            color_of_pixel_right = get_color(new_image, x+1, y)     # Gets the color of the pixel on the right to the current pixel.
            r2, g2, b2 = color_of_pixel_right                       # Unpacks the tuple for this color.
            brightness3 = (r2 + g2 + b2) // 3                       # Calculates the brightness of each pixel to the right of the original pixel.
            contrast_right = abs(brightness1 - brightness3)         # Calculates the contrast between the two pixels.
            
            if contrast_below > threshold or contrast_right > threshold:
                set_color(new_image, x, y, black)
            else:
                set_color(new_image, x, y, white)
                
        else: 
            set_color(new_image, x, y, white)                       # Sets the last row and last column of pixels to white.

    return new_image            # Returns the filtered image.

def flip_vertical(image):
    """ Written By: 'Hanan Alshatti'
    
    (Cimpl.Image) -> Cimpl.Image
    
    Returns the chosen image flipped on its central vertical axis.
    
    >>> image = load_image(choose_file())
        filtered_image = flip_vertical(image)
        *displays image filpped vertically*
    
    """
    new_image = copy(image)                              # Creates a copy of the file to work with.
    temp_image = copy(image)                             # Creates another copy of the image to iterate through.
    temp_width = get_width(image) - 1
    
    for pixel in temp_image:                             # Loops through each pixel in this image.
        
        x, y, color = pixel                              # Unpacks the tuple.
        set_color(new_image, temp_width - x, y, color)
        
    return new_image                                     # Returns the filtered image.

def flip_horizontal(image):
    """ Written By: 'Liamm Mirza'
    
    (Cimpl.Image) -> Cimpl.Image
    
    Returns the chosen image flipped on its central horizontal axis.
    
    >>> image = load_image(choose_file())
        filtered_image = flip_horizontal(image)
        *displays image filpped horizontally*
    
    """
    new_image = copy(image)                              # Creates a copy of the file to work with.
    temp_image = copy(image)                             # Creates another copy of the image to iterate through.
    temp_height = get_height(image) - 1
    
    for pixel in temp_image:                             # Loops through each pixel in this image.
        
        x, y, color = pixel                              # Unpacks the tuple.
        set_color(new_image, x, temp_height - y, color)
        
    return new_image                                     # Returns the filtered image.

