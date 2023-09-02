import tkinter as tk
import time
import winsound
from PIL import Image, ImageTk

def set_alarm():
    try:
        alarm_time = entry.get()
        time.strptime(alarm_time, '%H:%M:%S')  # Validate the format
    except ValueError:
        label.config(text="Invalid time format")
        return
    
    def check_time():
        current_time = time.strftime('%H:%M:%S')
        if current_time == alarm_time:
            winsound.PlaySound("tone.mp3", winsound.SND_ASYNC)
            label.config(text="Alarm!")
        else:
            label.config(text="")
            root.after(1000, check_time)  # Check again after 1 second
        
    check_time()

root = tk.Tk()
root.title("Alarm Clock")

image = Image.open("alarm.png")
image = image.resize((150, 150), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=photo)
image_label.pack()

label = tk.Label(root, text="Enter alarm time (HH:MM:SS):")
entry = tk.Entry(root)
set_button = tk.Button(root, text="Set Alarm", command=set_alarm)

label.pack()
entry.pack()
set_button.pack()

root.mainloop()
