# OpenSW-Team-Kim-da-bin-

Team name : Kim Da Bin (김다빈)

| Name    | Student Number | 
|---------|-----|
| 손인화  | 202334484  |
| 김다빈  | 202334424  |
| 리시웬  | 202334461  |
| 박세렴  | 202334469  |

This is a simple project that uses the OpenCV library to capture video from a camera, detects faces using a Haar cascade classifier, and displays the locations where a "ball" is drawn.


## Getting Started


To, set up and run this prohect on your local machine for development and testing purposes, follow these instructions.


- Install OpenCV
- Clone the Reopository
- Navigate to Project Directory
- Run the Python Script
- Interact with the Program
- Adjustments and Modifications


### Prerequisites

To run the provided Python script using OpenCV, you'll need to install Python and the OpenCV library on your machine.


### Installing

Python Downloads. 

Install OpenCV 
ex) pip install opencv-python

Clone or Download out script
ex) git clone [https://github.com/hwm31/OpenSW-Team-Kim-da-bin-]



### Code

Here are the main components and functionalities of the code

1) 'draw_ball_location' function: A function that draws lines on the image to visually represent the location of a ball.

2) 'cap' object: A VideoCapture object used to capture video from the camera.

3) 'list_ball_location' and 'history_ball_locations': Lists that store the current and previous center coordinates of detected faces.

4) 'isDraw' variable: A flag indicating whether to draw the location of the ball.

5) 'face_cascade': A Haar cascade face classifier used to detect faces.

6) Main loop: Reads frames from the camera, flips the image, detects faces, draws a circle at the center of each detected face, and records or displays the location of the "ball."

7) Key event handling: Performs actions such as toggling drawing mode, clearing locations, and exiting the program based on key events.





## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments




