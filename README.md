# Face-Recognition
Facial Recognition Software in Python
<h1 align="center">Hi 👋, I'm Daniel Jones</h1>
<h3 align="center">I'm a passionate Python and C++ developer</h3>
<h3 align="center">Welcome To my github project!👋</h3>

- 👨‍💻 All of my projects are available at [https://github.com/DanielJones02](https://github.com/DanielJones02)

# Installation And Usage

 - To use this software you will need Pip and Python 🐍 Installed on your PC

 - Clone the repository `git clone https://github.com/DanielJones02/Face-RecognitionPY` or download the latest release
   
 - Then all you have to do is execute run.bat and the requirements will automaticaly be installed
   
 - From there select Webcam or image
   
 - Have fun!

## Potential upcomming features

 - [ ] Add GUI Based version (tk)


## Preview of Code

```
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
```

> [!WARNING]
> This software has not been tested on linux, I have only tested it on windows.

<h3 align="left">Connect with me:</h3>
<p align="left">
</p>

<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://www.cprogramming.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/c/c-original.svg" alt="c" width="40" height="40"/> </a> <a href="https://www.w3schools.com/cpp/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/cplusplus/cplusplus-original.svg" alt="cplusplus" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>


