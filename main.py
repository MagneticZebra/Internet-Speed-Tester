import tkinter as tk
from PIL import Image, ImageTk
import speedtest
import threading

# Runs speed test and updates labels
def speed_test():
    loading_label.config(text="Running test...")

    test = speedtest.Speedtest()

    test.get_servers() # get list of servers that are available for speed test

    download_result = test.download() # Runs download speed test
    upload_result = test.upload() # Runs upload speed test

    download_result = round(download_result / (10**6), 2) # Converts to Mbps
    upload_result = round(upload_result / (10**6), 2) # Converts to Mbps

    down_label.config(text="Download Speed: " + str(download_result) + " Mbps")
    up_label.config(text="Upload Speed: " + str(upload_result) + " Mbps")

    # Places download and upload speed labels
    down_label.place(x=250, y=530)
    up_label.place(x=250, y=565)

    loading_label.place_forget() # Hides loading label

# Creates a seperate thread to handle the speed testing
def update_text():
    loading_label.place(x=345, y=300)
    threading.Thread(target=speed_test).start()

# Handles the animation in the background (runs on main thread)
def update_frame(frame_number):
    frame = gif_frames[frame_number]
    gif_label.config(image=frame)
    root.after(100, update_frame, (frame_number+1) % len(gif_frames))


root = tk.Tk()
root.title("Internet Speed Tester") # Title of window
root.resizable(False, False)  # Disable resizing in both directions

gif_path = "C:\\Portfolio\\InternetSpeedTester\\img\\rocket.gif" # You will need to update this path
gif_frames = []

with Image.open(gif_path) as gif:
    for frame in range(gif.n_frames):
        gif.seek(frame)
        frame_image = ImageTk.PhotoImage(gif.copy())
        gif_frames.append(frame_image)

gif_label = tk.Label(root)
gif_label.pack()

update_frame(0)

# Creates button and customizes it
button = tk.Button(root, text="Run Speed Test", command = update_text, width=50, height=2, font=("Verdana", 12, "bold"), 
                   borderwidth=4, 
                   relief="raised",
                   cursor="hand2")
button.place(x=125, y=50)

# Customising labels
loading_label = tk.Label(root, text="", font=("Helvetica", 12, "italic"), 
                              fg="green", 
                              bg="black", 
                              padx=10, 
                              pady=10, 
                              borderwidth=2, 
                              relief="sunken")

down_label = tk.Label(root, text="", font=("Arial", 14, "bold"), 
                      fg="white", 
                      bg="#0078D7",  
                      padx=10, 
                      pady=5, 
                      borderwidth=2, 
                      relief="raised")

up_label = tk.Label(root, text="", font=("Arial", 14, "bold"), 
                    fg="white", 
                    bg="#00B294",  
                    pady=5, 
                    borderwidth=2, 
                    relief="raised")

# Initialy hides labels
loading_label.place_forget()
down_label.place_forget()
up_label.place_forget()


root.mainloop()
