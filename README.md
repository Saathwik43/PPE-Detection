# PPE Detection System

Real-time Personal Protective Equipment (PPE) detection using YOLOv8 for workplace safety monitoring.

## Features

- **Real-time PPE Detection** - Hardhat, Mask, Safety Vest detection
- **Safety Violation Detection** - Identifies missing PPE items
- **Color-coded Alerts** - Green for compliance, Red for violations
- **Webcam & Video Support** - Works with live camera or video files
- **Custom Model Support** - Uses trained PPE detection model

## Detected Classes

- ✅ **Compliant**: Hardhat, Mask, Safety Vest, Person, Safety Cone, Machinery, Vehicle
- ❌ **Violations**: NO-Hardhat, NO-Mask, NO-Safety Vest

## Installation

1. **Install dependencies**
```bash
pip install -r requirements.txt
```

2. **Download PPE model**
```bash
# Download the pre-trained PPE detection model
wget https://github.com/ultralytics/assets/releases/download/v0.0.0/ppe.pt
```
Or download manually: [ppe.pt model file](https://github.com/ultralytics/assets/releases/download/v0.0.0/ppe.pt)

Place the downloaded `ppe.pt` file in this directory

## Usage

### Webcam Detection
```bash
python YoloWebCam.py
```

### Video File Detection
Edit the video path in `main.py`:
```python
cap = cv2.VideoCapture('../Videos/ppe1.mp4')
```

## Configuration

### Model Selection
- Replace `ppe.pt` with your custom PPE model
- Update `classNames` list to match your model's classes

### Detection Sensitivity
- Adjust confidence threshold in the model call
- Modify box colors in `myColor` variables

## Controls

- **Any key** - Continue processing
- **Close window** - Exit application

## Color Coding

- 🟢 **Green boxes** - PPE compliance detected
- 🔴 **Red boxes** - Safety violations (missing PPE)

## Requirements

- Python 3.8+
- OpenCV
- Ultralytics YOLO
- CVZone
- Custom PPE model file

## Model Training

To train your own PPE detection model:
1. Collect and label PPE images
2. Use Ultralytics YOLO training pipeline
3. Replace `ppe.pt` with your trained model
4. Update `classNames` list accordingly

## Performance Tips

- Use GPU acceleration for better performance
- Reduce video resolution for real-time processing
- Adjust confidence threshold based on accuracy needs
