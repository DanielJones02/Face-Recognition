# Auto installs modules not installed
try:
    import cv2
    from colorama import Fore
    import matplotlib.pyplot as plt
    import face_recognition
    import numpy
except ModuleNotFoundError:
    import time
    import os
    os.system('pip install opencv-python')
    os.system('pip install colorama')
    os.system('pip install matplotlib')
    os.system('pip install numpy')
    os.system('pip install face_recognition')
    print("\n")
    print("Requirements Installed.\n\n")
    time.sleep(0.5)

# Imports Libraries
import os, time
from pathlib import Path
import cv2
import matplotlib.pyplot as plt
import numpy
import face_recognition

# Changes terminal colour and title
os.system(f'title Face Recognition Software')
os.system('color 3')
os.system('cls')

# Main Class
class image:
    def __init__(self):
        self.img
        self.gray_image
        self.face
        self.img_rgb

    @staticmethod
    def validator(imagePath):
        os.system('color 7')

        check_filePath = Path(imagePath)

        if check_filePath.is_file():
            pass
        else:
            print("Image path does not exist\n\n")

            input("[Press Enter to exit...]:> ")
            exit()


    def read_image(self, imagePath):
        # Reads Image
        self.img = cv2.imread(imagePath)
        self.img = cv2.resize(self.img, (4000, 2667))
    

    def gray(self):
        # Makes image Gray to improve efficency
        self.gray_image = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        #self.gray_image.shape(4000, 2667)
    

    def face_recognition(self):
        face_classifier = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )

        self.face = face_classifier.detectMultiScale(
            self.gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
        )
    
    def draw_box(self):
        for (x, y, w, h) in self.faces:
            cv2.rectangle(self.frame, (x, y), (x + w, y + h), (173, 216, 230), 1)  # Light Blue (RGB: 173, 216, 230)

    
    def display_image(self):
        img_rgb = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)

        plt.figure(figsize=(20,10))
        plt.imshow(img_rgb)
        plt.axis('off')


# Detect Faces in Real time (video capture/webcam)
class real_time:
    def detect_and_recognize_faces():
        video_capture = cv2.VideoCapture(0)
        face_classifier = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )

        while True:
            ret, frame = video_capture.read()
            
            # Convert frame to grayscale for face detection
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # Detect faces using Haar Cascade
            faces = face_classifier.detectMultiScale(
                gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(60, 60)
            )
            
            light_blue_bgr = (255, 255, 0)

            # Draw a box around each detected face
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), light_blue_bgr, 1) 

            
            cv2.imshow('Face Recognition software', frame)
            
            # Press 'q' to exit the loop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        video_capture.release()
        cv2.destroyAllWindows()       

if __name__ == "__main__":
    print("------------------LOADING XRECOGNITION------------------\n")

    # Options
    print("""
    1. Find Faces/numbers in an image
    2. Recognise Faces via Webcam
    3. Find Faces/Numbers in a video
    """)

    choice = int(input("[Enter a choice]:> "))
    
    if choice == 1:
        # Location to your image
        imagePath = input("[Enter the path to your image e.g /images/image.jpg]:> ")
        print(Fore.RESET)
        image.validator(imagePath=imagePath)  # Calls function to check if the location is correct

        app = image()
        app.read_image(imagePath=imagePath)  # Calls function to read image
        app.gray()  # Calls function to make the image gray for improved efficiency
        app.face_recognition()  # Recognizes Faces
        app.draw_box()  # Draws a box around the person's face
        app.display_image() # Displays Image
        os.system('color 7')
    elif choice == 2:
        app = real_time()

        real_time.detect_and_recognize_faces()
    elif choice == 3:
        pass
    else:
        print("Invalid option please enter: 1, 2 or 3\n")
        
        input("[Press Enter to exit...]:> ")
        exit()

    # Resets terminal color to White
    #os.system('color 7')