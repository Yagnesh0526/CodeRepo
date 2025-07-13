import tkinter as tk
from tkinter import messagebox
import speedtest 

# Function to check internet speed
def check_speed():
    try:
        st = speedtest.Speedtest()
        st.download()  # Initializes server and download speed
        download_speed = st.results.download / 1_000_000  # Convert to Mbps
        upload_speed = st.results.upload / 1_000_000  # Convert to Mbps
        
        # Update the labels with speed values
        download_label.config(text=f"Download Speed: {download_speed:.2f} Mbps")
        upload_label.config(text=f"Upload Speed: {upload_speed:.2f} Mbps")
    except Exception as e:
        messagebox.showerror("Error", f"Could not check speed. Error: {e}")

# Initialize the main window
root = tk.Tk()
root.title("Internet Speed Test")
root.geometry("300x200")

# Create a button to check speed
check_button = tk.Button(root, text="Check Speed", command=check_speed)
check_button.pack(pady=20)

# Labels to display the speed results
download_label = tk.Label(root, text="Download Speed: - Mbps")
download_label.pack(pady=5)

upload_label = tk.Label(root, text="Upload Speed: - Mbps")
upload_label.pack(pady=5)

# Run the main loop
root.mainloop()
