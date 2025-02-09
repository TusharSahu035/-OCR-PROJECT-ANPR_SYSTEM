# Automatic Number Plate Recognition (ANPR) System - User Guide

## Introduction
This guide provides detailed instructions on how to install, set up, and use the ANPR System. The application is designed to recognize vehicle number plates using a webcam or uploaded images, fetch vehicle details, and manage records through an admin panel.

---

## 1. Installation Guide

### **1.1 Prerequisites**
Ensure you have the following installed on your system:
- **Python 3.8+** (Download from [python.org](https://www.python.org/))
- **pip (Python package manager)**
- **OpenCV** for image processing
- **Tkinter** for GUI (comes pre-installed with Python)
- **Pillow** for handling images

### **1.2 Install Required Libraries**
Open the terminal or command prompt and run the following command:
```bash
pip install opencv-python numpy pillow tkinter
```

---

## 2. Running the Application

### **2.1 Clone or Download the Project**
If you are using Git:
```bash
git clone https://github.com/your-repo/ANPR.git
cd ANPR
```
Or manually download the project and extract it to a directory.

### **2.2 Run the Application**
Navigate to the project folder and execute:
```bash
python main.py
```

If everything is set up correctly, the **ANPR System GUI** will open.

---

## 3. Features & Usage

### **3.1 Open Camera & Capture Image**
- Click the **"Open Camera"** button to start the webcam.
- Press **Spacebar** to capture an image.
- Press **'q'** to close the camera.

### **3.2 Upload an Image**
- Click the **"Upload Image"** button to select an image from your computer.

### **3.3 Detect Number Plate**
- Click **"Detect Plate"** after capturing or uploading an image.
- The system will extract the number plate and display the result.

### **3.4 Fetch Vehicle Details**
- Enter a vehicle number in the input field.
- Click **"Fetch Details"** to retrieve stored records.

---

## 4. Admin Panel

### **4.1 Access Admin Panel**
- Click **"Admin Panel"**.
- Enter the **admin password** (Default: `admin123`).

### **4.2 Add Vehicle Details**
- Enter **Vehicle Number, Owner Name, Model, and Registration Year**.
- Click **Submit** to save the details.

---

## 5. Troubleshooting

### **5.1 Camera Not Opening**
- Ensure your webcam is connected and accessible.
- Try restarting the application and checking your camera permissions.

### **5.2 Image Upload Fails**
- Ensure the image is in **.jpg, .jpeg, or .png** format.

### **5.3 Number Plate Not Detected**
- Ensure the image is clear and the plate is visible.
- Try with another image.

### **5.4 Forgot Admin Password?**
- Modify the `main.py` file and change the password manually in the `admin_login()` function.

---

## 6. Additional Notes
- The application saves images in the `uploads/` folder.
- Future updates will include **database integration** for better record management.

---

## 7. Support & Contact
For issues or suggestions, contact the developer at **tusharsahu035@gmail.com** or visit the GitHub repository.

Enjoy using the **ANPR System**!

