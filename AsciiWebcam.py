# Import the necessary libraries
import cv2             # OpenCV library for computer vision, used to access the webcam
import curses          # Curses library for controlling terminal display
from curses import wrapper  # Wrapper function to manage the curses screen

# This variable controls the scale of the webcam image
scale = 0.1

def main(screen):
    # Prepare the terminal screen for displaying output
    screen.clear()
    
    # Capture video from the webcam; 0 indicates the default webcam
    cap = cv2.VideoCapture(0)

    # Check if the webcam stream is successfully opened
    if not cap.isOpened():
        raise IOError("Cannot open Webcam Stream.")
    
    while True:
        # Capture the current frame from the webcam
        ret, frame = cap.read()

        # Resize the frame to make it smaller, according to the scale factor
        frame = cv2.resize(frame, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
        
        # Determine the width of the frame (each pixel is displayed as two ASCII characters)
        width = len(frame[0]) * 2

        # Convert the frame to grayscale for easier ASCII conversion
        gscale = []  # List to store grayscale pixel values
        for i, b in enumerate(frame):
            for x, a in enumerate(b):
                sum = a[0] + a[1] + a[2]  # Sum the RGB values
                sum /= 3                   # Compute the average to get the grayscale value
                sum = int(sum)             # Convert to an integer
                gscale.append(sum)         # Add grayscale value to the list
                gscale.append(sum)         # Repeat it because each pixel will be converted to 2 characters

        # Initialize an empty list to store ASCII characters representing each pixel
        ascii_px = []

        # Iterate over each pixel's grayscale value in the gscale list
        for pixel in gscale:
            # Calculate the index for the corresponding ASCII character
            char_index = pixel // 25  # Dividing by 25 gives a value between 0 and 9 (since pixel values range from 0 to 255)
            
            # Get the ASCII character from the chars list using the calculated index
            ascii_character = chars[char_index]
            
            # Append the ASCII character to the ascii_px list
            ascii_px.append(ascii_character)

        # Define a list of ASCII characters to represent pixel brightness
        chars = ["@", "%", "&", "$", "#", "+", "-", ":", ".", " " ]
        chars.reverse()  # Reverse the list so that darker pixels have heavier characters

        # Initialize an empty list to store the lines of ASCII art
        ascii_frame = []

        # Iterate over the ascii_px list in chunks corresponding to the width of the frame
        for index in range(0, len(ascii_px), width):
            # Extract a slice of the ascii_px list that corresponds to one row of the image
            ascii_row = ascii_px[index: index + width]
            
            # Join the list of characters into a single string representing the row
            ascii_row_str = "".join(ascii_row)
            
            # Append the row string to the ascii_frame list
            ascii_frame.append(ascii_row_str)

        # Display the ASCII art in the terminal
        for l, x in enumerate(ascii_frame):
            try:
                screen.addstr(l, 0, x)  # Print each line at the correct position
            except:
                pass  # If an error occurs (e.g., terminal too small), just skip the line
        
        # Refresh the screen to show the updated frame
        screen.refresh()
    
    # Release the webcam resource when done
    cap.release()
    return

# Start the curses application, running the 'main' function
wrapper(main)












