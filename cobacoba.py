import cv2
import numpy as np
from tkinter import *
from PIL import Image, ImageTk

# Create a window
window = Tk()
window.title("Face Recognition App")

# Create a canvas to display the webcam feed
canvas = Canvas(window, width=640, height=480)
canvas.pack()

# Create a button to capture the photo
capture_button = Button(window, text="Capture!")
capture_button.pack()

# Initialize the webcam
cap = cv2.VideoCapture(0)

def capture_photo():
    # Capture the photo from the webcam
    ret, frame = cap.read()

    # Convert the frame to PIL Image format
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)

    # Display the captured image on the canvas
    canvas.image = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor=NW, image=canvas.image)

# Bind the capture_photo function to the button click event
capture_button.configure(command=capture_photo)

# Start the main event loop
window.mainloop()