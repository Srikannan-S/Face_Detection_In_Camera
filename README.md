📷 Real-Time Face Detection using OpenCV

This Python project uses OpenCV and Haar Cascade to detect faces in real-time through a webcam feed.

🔥 Features

1. Uses a pretrained Haar Cascade classifier to detect faces  
2. Processes live video feed from a webcam  
3. Draws green rectangles around detected faces in real time  
4. Exits cleanly when the Escape (Esc) key is pressed  

🚀 Technologies Used

1. Python – Programming language  
2. OpenCV – Library for real-time computer vision  
3. Haar Cascade – Pretrained face detection model  

⚙️ Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/realtime-face-detection.git
   cd realtime-face-detection
   ```

2. Install the required package:
   ```bash
   pip install opencv-python
   ```

3. Make sure the Haar Cascade file is in the project directory:
   - `haarcascade_frontalface_default.xml` (Download from [here](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml))

4. Run the script:
   ```bash
   python app.py
   ```

🛠️ How It Works

- Opens your system’s default webcam.  
- Converts each video frame to grayscale.  
- Detects faces in each frame using `detectMultiScale()`.  
- Draws rectangles around all detected faces.  
- Continues detecting until you press the `Esc` key.  

📂 Project Structure

📁 realtime-face-detection  
├── app.py                        # Main Python script  
├── haarcascade_frontalface_default.xml  # Face detection model  
└── README.md                     # Project documentation  
