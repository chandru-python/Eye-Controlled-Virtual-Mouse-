# 👁️ Eye-Controlled Virtual Mouse

<div align="center">

### Control Your Computer Using Only Your Eyes

A Computer Vision-based Virtual Mouse that enables cursor movement, scrolling, and mouse clicks using eye tracking and blink detection.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![Dlib](https://img.shields.io/badge/Dlib-Facial%20Landmarks-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

</div>

---

## 📌 Overview

Eye-Controlled Virtual Mouse is an intelligent Human-Computer Interaction (HCI) system that uses real-time eye tracking and blink detection to control mouse operations without physical contact.

Using a webcam, the system detects facial landmarks, tracks eye movement, and converts gaze direction into mouse cursor movement. Different blink durations are interpreted as mouse click actions.

---

## ✨ Features

✅ Real-Time Eye Tracking

✅ Cursor Movement Through Eye Position

✅ Smooth Mouse Navigation

✅ Automatic Scrolling

✅ Blink-Based Left Click

✅ Blink-Based Right Click

✅ Double Blink Detection

✅ Hands-Free Computer Control

✅ Accessibility Support

---

## 🛠️ Tech Stack

| Technology | Purpose                      |
| ---------- | ---------------------------- |
| Python     | Core Programming             |
| OpenCV     | Video Processing             |
| Dlib       | Face & Landmark Detection    |
| NumPy      | Mathematical Operations      |
| SciPy      | Eye Aspect Ratio Calculation |
| PyAutoGUI  | Mouse Control                |

---

## 🧠 System Architecture

```text
Webcam
   ↓
Face Detection
   ↓
Facial Landmark Detection
   ↓
Eye Landmark Extraction
   ↓
EAR Calculation
   ↓
Blink Detection
   ↓
Mouse Actions
```

---

## 🎯 Mouse Controls

| Eye Gesture         | Action       |
| ------------------- | ------------ |
| Eye Movement        | Move Cursor  |
| Blink (0.5 - 1 sec) | Left Click   |
| Blink (>1 sec)      | Right Click  |
| Double Blink        | Double Click |
| Look Up             | Scroll Up    |
| Look Down           | Scroll Down  |

---

## 📷 Working Principle

### Step 1: Face Detection

The webcam continuously captures frames and detects the user's face.

### Step 2: Eye Tracking

The system identifies eye landmarks using Dlib's 68-point facial landmark model.

### Step 3: Eye Aspect Ratio (EAR)

EAR is calculated to determine whether the eyes are open or closed.

### Step 4: Cursor Control

The eye center position is mapped to screen coordinates and used to move the mouse cursor.

### Step 5: Blink Recognition

Blink duration is analyzed to trigger mouse click events.

---

## 📂 Project Structure

```bash
Eye-Controlled-Virtual-Mouse/
│
├── app.py
├── shape_predictor_68_face_landmarks.dat
├── requirements.txt
├── README.md
│
└── screenshots/
    ├── demo1.png
    └── demo2.png
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/chandru-python/Eye-Controlled-Virtual-Mouse-.git
cd Eye-Controlled-Virtual-Mouse-
```

### Install Dependencies

```bash
pip install opencv-python
pip install dlib
pip install pyautogui
pip install numpy
pip install scipy
```

Or

```bash
pip install -r requirements.txt
```

---

## 📥 Download Landmark Model

Download:

shape_predictor_68_face_landmarks.dat

Place it inside the project directory before running the application.

---

## ▶️ Run Application

```bash
python app.py
```

Press:

```text
q
```

to exit the application.

---

## 🚀 Applications

### Accessibility Systems

Helping physically challenged users operate computers.

### Smart Human-Computer Interaction

Advanced touchless interaction systems.

### Research Projects

Computer Vision and AI-based interaction systems.

### Healthcare Solutions

Hands-free interfaces for medical environments.

---

## 📈 Future Improvements

* Deep Learning-Based Eye Tracking
* Iris Detection
* Multi-Monitor Support
* Gesture Recognition
* Voice Assistant Integration
* AI-Based Cursor Prediction

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to branch
5. Open a Pull Request

---

## 👨‍💻 Author

**Chandru M**

AI/ML Engineer | Computer Vision Developer | Deep Learning Enthusiast

GitHub: https://github.com/chandru-python

---

## ⭐ Support

If you found this project useful:

⭐ Star this repository

🍴 Fork this repository

📢 Share it with others

---

<div align="center">

### Built with ❤️ using Computer Vision and Artificial Intelligence

</div>
