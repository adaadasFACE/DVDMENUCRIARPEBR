import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from moviepy.editor import VideoFileClip

class DVDMenuApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Coleção de Filmes BG Produções")
        self.geometry("800x600")

        # Reproduzir vídeo de First Play
        self.play_first_play()

    def play_first_play(self):
        first_play_video = "first_play.mp4"  # Caminho do vídeo de First Play
        clip = VideoFileClip(first_play_video)
        clip.preview()
        clip.close()

        # Após a reprodução do vídeo, iniciar o menu principal
        self.create_main_menu()
    
    def create_main_menu(self):
        self.clear_frame()

        # Adicionar logo e título
        logo_label = tk.Label(self, text="BG PRODUÇÕES", font=("Arial", 24, "bold"))
        logo_label.pack(pady=20)

        title_label = tk.Label(self, text="Coleção de Filmes BG Produções", font=("Arial", 18))
        title_label.pack(pady=10)

        # Adicionar botões do menu
        buttons_frame = tk.Frame(self)
        buttons_frame.pack(pady=20)

        button_texts = [
            "Filme 1: Título do Filme 1",
            "Filme 2: Título do Filme 2",
            "Filme 3: Título do Filme 3",
            "Filme 4: Título do Filme 4",
            "Filme 5: Título do Filme 5",
            "Play All",
            "Configurações",
            "Extras"
        ]

        button_commands = [
            self.show_film_1_menu,
            self.show_film_2_menu,
            self.show_film_3_menu,
            self.show_film_4_menu,
            self.show_film_5_menu,
            self.play_all,
            self.show_settings,
            self.show_extras
        ]

        for text, command in zip(button_texts, button_commands):
            button = tk.Button(buttons_frame, text=text, command=command, width=30, height=2)
            button.pack(pady=5)

    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    def show_film_1_menu(self):
        self.clear_frame()
        self.create_film_submenu("Título do Filme 1", "scene1.png", "film1.mp4")

    def show_film_2_menu(self):
        self.clear_frame()
        self.create_film_submenu("Título do Filme 2", "scene2.png", "film2.mp4")

    def show_film_3_menu(self):
        self.clear_frame()
        self.create_film_submenu("Título do Filme 3", "scene3.png", "film3.mp4")

    def show_film_4_menu(self):
        self.clear_frame()
        self.create_film_submenu("Título do Filme 4", "scene4.png", "film4.mp4")

    def show_film_5_menu(self):
        self.clear_frame()
        self.create_film_submenu("Título do Filme 5", "scene5.png", "film5.mp4")

    def create_film_submenu(self, title, background_image, film_video):
        # Configurar imagem de fundo
        bg_image = Image.open(background_image)
        bg_image = bg_image.resize((800, 600), Image.ANTIALIAS)
        bg_photo = ImageTk.PhotoImage(bg_image)

        bg_label = tk.Label(self, image=bg_photo)
        bg_label.image = bg_photo
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Título do submenu
        title_label = tk.Label(self, text=title, font=("Arial", 18), bg="black", fg="white")
        title_label.pack(pady=10)

        # Opções do submenu
        buttons_frame = tk.Frame(self, bg="black")
        buttons_frame.pack(pady=20)

        button_texts = [
            "Play: Assistir ao Filme",
            "Cenas: Seleção de Cenas",
            "Voltar ao Menu Principal"
        ]

        button_commands = [
            lambda: self.play_film(film_video),
            self.show_scenes,
            self.create_main_menu
        ]

        for text, command in zip(button_texts, button_commands):
            button = tk.Button(buttons_frame, text=text, command=command, width=30, height=2)
            button.pack(pady=5)

    def play_film(self, film_video):
        clip = VideoFileClip(film_video)
        clip.preview()
        clip.close()

    def show_scenes(self):
        messagebox.showinfo("Seleção de Cenas", "Exibindo seleção de cenas...")

    def play_all(self):
        messagebox.showinfo("Reproduzir Todos os Filmes", "Reproduzindo todos os filmes")

    def show_settings(self):
        self.clear_frame()
        settings_label = tk.Label(self, text="Configurações", font=("Arial", 18))
        settings_label.pack(pady=10)

        back_button = tk.Button(self, text="Voltar", command=self.create_main_menu)
        back_button.pack(pady=20)

    def show_extras(self):
        self.clear_frame()
        extras_label = tk.Label(self, text="Extras", font=("Arial", 18))
        extras_label.pack(pady=10)

        back_button = tk.Button(self, text="Voltar", command=self.create_main_menu)
        back_button.pack(pady=20)

if __name__ == "__main__":
    app = DVDMenuApp(dvd_menu_app.py)
    app.mainloop()