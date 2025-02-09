import cv2
import os
import datetime
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, Toplevel
from PIL import Image, ImageTk, ImageFilter
from detect_number import detect_number_plate
from vehicle_db import get_vehicle_details, add_vehicle_details

# Constants
UPLOAD_FOLDER = "uploads"
ICON_FOLDER = "icons"
BACKGROUND_IMAGE = "background.jpg"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
if not os.path.exists(ICON_FOLDER):
    os.makedirs(ICON_FOLDER)

class ANPRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Automatic Number Plate Recognition (ANPR) System")
        self.root.geometry("900x700")
        self.root.configure(bg="#F0F8FF")

        # Load background image with blur
        self.bg_label = tk.Label(self.root)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.set_background()

        # Heading
        heading_label = tk.Label(root, text="Automatic Number Plate Recognition System", font=("Arial", 18, "bold"), bg="#F0F8FF", fg="#003366")
        heading_label.pack(pady=10)

        # Buttons Frame
        self.button_frame = tk.Frame(root, bg="#F0F8FF")
        self.button_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Load Icons
        self.load_icons()

        # Buttons
        self.create_buttons()
        
        self.image_path = None
        self.cap = None

    def create_buttons(self):
        button_data = [
            (" Open Camera", self.camera_icon, self.open_camera),
            (" Upload Image", self.upload_icon, self.upload_image),
            (" Detect Plate", self.detect_icon, self.process_image),
            (" Admin Panel", self.admin_icon, self.admin_login),
            (" Fetch Details", None, self.fetch_details)
        ]
        for text, icon, command in button_data:
            btn = tk.Button(self.button_frame, text=text, image=icon, compound=tk.LEFT, command=command, font=("Arial", 14, "bold"), bg="#007BFF", fg="white", padx=10, relief="raised", bd=4)
            btn.pack(pady=10, ipadx=20, ipady=5, fill=tk.X)
        
        self.number_entry = tk.Entry(self.button_frame, font=("Arial", 14))
        self.number_entry.pack(pady=10, ipadx=20, ipady=5, fill=tk.X)

    def set_background(self):
        if os.path.exists(BACKGROUND_IMAGE):
            bg = Image.open(BACKGROUND_IMAGE).resize((900, 700)).filter(ImageFilter.GaussianBlur(5))
            self.bg_image = ImageTk.PhotoImage(bg)
            self.bg_label.config(image=self.bg_image)

    def load_icons(self):
        def load_icon(filename):
            path = os.path.join(ICON_FOLDER, filename)
            return ImageTk.PhotoImage(Image.open(path).resize((40, 40))) if os.path.exists(path) else None
        
        self.camera_icon = load_icon("camera.png")
        self.upload_icon = load_icon("upload.png")
        self.detect_icon = load_icon("detect.png")
        self.admin_icon = load_icon("admin.png")

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
        if file_path:
            self.image_path = file_path
            messagebox.showinfo("Success", "Image uploaded successfully!")

    def open_camera(self):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            messagebox.showerror("Error", "Failed to open camera!")
            return
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow("Camera", frame)
            key = cv2.waitKey(1)
            if key == 32:
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                image_path = os.path.join(UPLOAD_FOLDER, f"captured_{timestamp}.jpg")
                cv2.imwrite(image_path, frame)
                self.image_path = image_path
                messagebox.showinfo("Success", "Image captured successfully!")
                break
            elif key == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

    def process_image(self):
        if not self.image_path:
            messagebox.showerror("Error", "No image selected!")
            return
        plate_number = detect_number_plate(self.image_path)
        if plate_number:
            messagebox.showinfo("Success", f"Detected Number Plate: {plate_number}")
        else:
            messagebox.showerror("Error", "Number plate not detected!")

    def fetch_details(self):
        vehicle_number = self.number_entry.get().strip()
        if not vehicle_number:
            messagebox.showerror("Error", "Please enter a vehicle number!")
            return
        details = get_vehicle_details(vehicle_number)
        if details:
            messagebox.showinfo("Vehicle Details", f"Vehicle: {details}")
        else:
            messagebox.showerror("Error", "Vehicle details not found!")

    def admin_login(self):
        if simpledialog.askstring("Admin Login", "Enter Admin Password:", show="*") == "admin123":
            self.open_admin_form()
        else:
            messagebox.showerror("Error", "Incorrect password!")

    def open_admin_form(self):
        admin_window = Toplevel(self.root)
        admin_window.title("Add Vehicle Details")
        admin_window.geometry("400x300")
        labels = ["Vehicle Number", "Owner Name", "Vehicle Model", "Registration Year"]
        entries = {label: tk.Entry(admin_window) for label in labels}
        for label, entry in entries.items():
            tk.Label(admin_window, text=f"{label}:").pack()
            entry.pack()
        
        def submit_details():
            data = {label: entry.get().strip() for label, entry in entries.items()}
            if all(data.values()):
                add_vehicle_details(data["Vehicle Number"], data["Owner Name"], data["Vehicle Model"], data["Registration Year"])
                messagebox.showinfo("Success", "Vehicle details added successfully!")
                admin_window.destroy()
            else:
                messagebox.showerror("Error", "All fields are required!")
        
        tk.Button(admin_window, text="Submit", command=submit_details, bg="#28A745", fg="white").pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = ANPRApp(root)
    root.mainloop()
