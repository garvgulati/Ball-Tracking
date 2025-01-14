# Ball-Tracking
Real-Time Ball Tracking with OpenCV

This project demonstrates how to use OpenCV to track a specific colored object (in this case, a green ball) in real-time using a webcam. The program captures live video from the webcam, applies color filtering to detect the ball, and draws a path to show its movement across the screen.

Features: 

1. Real-time Object Tracking: Uses OpenCV to track the movement of a green ball in a webcam feed.
2. Path Visualization: The path of the ball is drawn on the screen as it moves.
3. HSV Color Filtering: The program uses the HSV (Hue, Saturation, Value) color space for more accurate color filtering and ball detection.
4. Live Webcam Feed: The program captures video from your webcam and processes it in real-time.
5. Track and Draw: The path of the ball is drawn using a deque to maintain the ball’s previous positions, creating a visual trail as it moves.
