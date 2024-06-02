This Python script utilizes OpenCV, PyCaw, and a custom Hand Tracking Module to control the system volume using hand gestures. The webcam captures video, and the script processes the video frames to detect hand gestures. Specifically, the distance between the thumb and index finger is used to adjust the volume.

Features
Hand Detection:

Utilizes a custom HandDetector from the Hand_Tracking_Module to detect and track hand landmarks in real-time.
Volume Control:

Uses the PyCaw library to interface with the system's audio controls.
Maps the distance between the thumb and index finger to the system volume range.
Visual Feedback:

Displays the current volume level as a vertical bar on the screen.
Shows the percentage of the current volume.
Provides real-time feedback by drawing circles and lines on the detected hand landmarks.
Performance:

Displays the current frames per second (FPS) for performance monitoring.
