import tkinter as tk
from dvd_menu_app import DVDMenuApp
from tkinter import filedialog

class DVDMenuGUI:
    def __init__(self, root):
        self.app = DVDMenuApp()
        self.root = root
        self.root.title("DVD Menu Creator")

        create_menu_button = tk.Button(root, text="Create Menu", command=self.app.create_menu)
        create_menu_button.pack(pady=10)

        navigate_button = tk.Button(root, text="Navigate to Chapters", command=lambda: self.app.navigate_menu('Chapters'))
        navigate_button.pack(pady=10)

       
        import_videos_button = tk.Button(root, text="Import Videos", command=self.import_videos)
        import_videos_button.pack(pady=10)

    def import_videos(self):
        
        video_files = filedialog.askopenfilenames(title="Select Videos", filetypes=[("Video Files", "*.mp4;*.avi;*.mkv")])
        if video_files:
            print("Videos imported:", video_files)
        else:
            print("No videos selected.")

if __name__ == "__main__":
    root = tk.Tk()
    gui = DVDMenuGUI(root)
    root.mainloop()
