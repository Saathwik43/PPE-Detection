# Real-time PPE Detection System

Advanced Personal Protective Equipment (PPE) detection system using YOLOv8 and OpenCV for workplace safety monitoring and compliance.

## 🚀 Features

- **Real-time Detection** 
  - Multiple PPE items tracking
  - Support for both webcam and video files
  - High-performance processing
- **Smart Alerts**
  - Color-coded detection boxes
  - Confidence score display
  - Multi-class detection
- **Flexible Input**
  - Webcam support
  - Video file processing
  - Adjustable confidence thresholds

## 🎯 Detection Classes

### Safety Equipment
- ✅ Hardhat
- ✅ Safety Vest
- ✅ Mask

### Safety Violations
- ⚠️ NO-Hardhat
- ⚠️ NO-Safety Vest
- ⚠️ NO-Mask

### Additional Objects
- 👥 Person
- 🔺 Safety Cone
- 🏗️ Machinery
- 🚗 Vehicle

## 🛠️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/Saathwik43/ppe-detection.git
cd ppe-detection
```

2. **Install dependencies**
```bash
pip install ultralytics opencv-python cvzone
```

3. **Download model**
- Download the `ppe.pt` model file
- Place it in the project root directory

## 💻 Usage

### Running with Webcam
```python
# Modify main.py - Change video source to webcam
cap = cv2.VideoCapture(0)
```

### Running with Video File
```python
# Modify main.py - Specify video file path
cap = cv2.VideoCapture('Samples/your_video.mp4')
```

### Execute the Program
```bash
python main.py
```

## ⚙️ Configuration

```python
# Adjust detection confidence (in main.py)
if conf > 0.5:  # Change 0.5 to desired threshold

# Color codes
- Green (0, 255, 0): Compliant PPE
- Red (0, 0, 255): Safety violations
- Blue (255, 0, 0): Other objects
```

## 🎮 Controls

- **Q key**: Exit program
- **Any other key**: Continue processing

## 🎨 Visual Indicators

- 🟢 **Green Box**: Detected proper PPE
- 🔴 **Red Box**: Safety violation detected
- 🔵 **Blue Box**: Other detected objects
- 📊 **Confidence Score**: Shown for each detection

## 🔧 System Requirements

- Python 3.8+
- GPU recommended for optimal performance
- Webcam (for live detection)
- Required packages:
  - ultralytics
  - opencv-python
  - cvzone

## 🔍 Performance Optimization

- Use GPU acceleration when available
- Adjust confidence threshold (default: 0.5)
- Optimize video resolution for real-time processing


## 🤝 Contributing

Feel free to submit issues and enhancement requests!

---

*Last updated: September 2025*
