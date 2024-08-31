# Advanced Gesture Recognition

### Real-Time Gesture Recognition with MediaPipe and OpenCV

## 📈 Overview

This project demonstrates real-time gesture recognition using MediaPipe and OpenCV. The application can detect and classify gestures such as Closed Fist, Thumbs Up, and Peace Sign, enhancing the potential for intuitive and interactive user experiences. 

## ✨ Features

- **Real-Time Gesture Detection**: Recognizes hand gestures in real-time using a webcam.
- **Gesture Classification**: Detects specific gestures like:
  - Closed Fist
  - Thumbs Up
  - Peace Sign
- **Face Detection (Optional)**: Integrate face detection to enhance interaction.
- **Visual Feedback**: Provides on-screen feedback by drawing landmarks and connections for hands.

## 🛠️ Technologies Used

- **Python**
- **MediaPipe**: For hand and face landmark detection.
- **OpenCV**: For image processing and real-time video capture.

## 🚀 Getting Started

### Prerequisites

Make sure you have Python installed. You can install the required libraries using pip:

```bash
pip install opencv-python mediapipe numpy
```
Running the Application

```bash
git clone https://github.com/Philani56/Advanced-Gesture-Recognition
```

```bash
python main.py
```
- Ensure your webcam is connected and working.

## Using the Application:

The application will open a window that captures video from your webcam. Move your hand into the frame, and the application will detect and classify the gestures in real-time.

## Example Output

- Number of Fingers: Displays the number of fingers detected.
- Detected Gestures: Displays the recognized gesture (e.g., "Thumbs Up", "Closed Fist").
- Face Detection (Optional): If enabled, detects and marks faces in the video feed.


## 📄 Code Explanation
### Main Components:

- gesture_recognition.py: The core script that captures video, processes frames, and detects gestures.
- count_fingers(): Function to count the number of fingers raised.
- detect_gestures(): Function to classify gestures based on hand landmarks.

- Extending the Project
- Add New Gestures: You can extend the detect_gestures() function to recognize more gestures.
- Integrate Face Detection: Enhance the project by integrating face detection features.

## 🤝 Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📧 Contact

For any inquiries, questions, or feedback, please reach out to:

- Email: khumalophilani580@gmail.com
- LinkedIn: https://www.linkedin.com/in/nhlakanipho-philani-khumalo-679726224/

Feel free to connect with me on social media or via email for more information!














