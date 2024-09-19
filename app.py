import tkinter as tk
from dvd_menu_app import DVDMenuApp
from tkinter import filedialog
from dvd_creation import DVDCreation  # Certifique-se de que o módulo está disponível

class DVDMenuGUI:
    def __init__(self, root):
        self.app = DVDMenuApp()
        self.root = root
        self.root.title("DVD Menu Creator")

        # Botão para criar o menu
        create_menu_button = tk.Button(root, text="Create Menu", command=self.app.create_menu)
        create_menu_button.pack(pady=10)

        # Botão para navegar para capítulos
        navigate_button = tk.Button(root, text="Navigate to Chapters", command=lambda: self.app.navigate_menu('Chapters'))
        navigate_button.pack(pady=10)

        # Botão para importar vídeos
        import_videos_button = tk.Button(root, text="Import Videos", command=self.import_videos)
        import_videos_button.pack(pady=10)

        # Botão para definir o vídeo de "First Play"
        first_play_button = tk.Button(root, text="Set First Play Video", command=self.set_first_play_video)
        first_play_button.pack(pady=10)

        # Botão para pré-visualizar o menu
        preview_button = tk.Button(root, text="Preview Menu", command=self.preview_menu)
        preview_button.pack(pady=10)

        # Botão para gravar o DVD
        burn_button = tk.Button(root, text="Burn DVD", command=self.burn_dvd)
        burn_button.pack(pady=10)

    def import_videos(self):
        # Função para importar vídeos
        video_files = filedialog.askopenfilenames(title="Select Videos", filetypes=[("Video Files", "*.mp4;*.avi;*.mkv")])
        if video_files:
            print("Videos imported:", video_files)
            # Armazena os vídeos importados na instância do DVDMenuApp
            self.app.videos = video_files
        else:
            print("No videos selected.")

    def set_first_play_video(self):
        # Função para definir o vídeo de "First Play"
        video_file = filedialog.askopenfilename(title="Select First Play Video", filetypes=[("Video Files", "*.mp4;*.avi;*.mkv")])
        if video_file:
            print(f"First play video set to: {video_file}")
            # Define o vídeo de "First Play" na lógica do DVDMenuApp
            self.app.first_play_video = video_file
        else:
            print("No video selected for First Play.")

    def preview_menu(self):
        # Função para pré-visualizar o menu
        if hasattr(self.app, 'menu_structure'):
            self.app.preview_menu(self.app.menu_structure)
        else:
            print("Menu not created yet.")

    def burn_dvd(self):
        # Função para gravar o DVD
        if hasattr(self.app, 'videos') and self.app.videos:
            dvd_creator = DVDCreation(self.app.videos)
            dvd_creator.burn_dvd()
        else:
            print("No videos selected for DVD creation.")

if __name__ == "__main__":
    root = tk.Tk()
    gui = DVDMenuGUI(root)
    root.mainloop()
