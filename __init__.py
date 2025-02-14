import tkinter as tk
from tkinter import font
import random


class ShabEBaratApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shab e Barat Celebration")
        self.root.configure(bg='#000033')
        self.root.geometry("800x600")

        self.create_ascii_art()
        self.create_text_content()
        self.create_interactive_elements()
        self.animate_moon()

    def create_ascii_art(self):
        # Mosque ASCII Art
        mosque_ascii = r"""
           /\
          /  \
         /____\
        /______\
        |  __  |
        | |  | |
        | |__| |
        |  __  |
        | |  |_|
        | |____ 
        |______|
        """
        self.mosque_label = tk.Label(self.root, text=mosque_ascii,
                                     font=('Courier', 12), fg='#00FF00', bg='#000033')
        self.mosque_label.pack(pady=10)

        # Moon ASCII Art
        self.moon_label = tk.Label(self.root, text="🌙",
                                   font=('Arial', 32), fg='white', bg='#000033')
        self.moon_label.place(x=50, y=50)

    def create_text_content(self):
        # Header
        header_font = font.Font(family='Arial', size=18, weight='bold')
        self.header = tk.Label(self.root, text="Shab e Barat Mubarak!",
                               font=header_font, fg='gold', bg='#000033')
        self.header.pack(pady=5)

        # Body Text
        body_text = """May Allah shower His blessings upon you and your family
Forgive all your sins and accept your prayers
May this Night of Forgiveness bring peace and happiness"""
        self.body = tk.Label(self.root, text=body_text,
                             font=('Arial', 12), fg='white', bg='#000033')
        self.body.pack(pady=10)

        # Decorative Stars
        self.stars = tk.Label(self.root, text="✦ ✦ ✦ ✦ ✦",
                              font=('Arial', 24), fg='white', bg='#000033')
        self.stars.pack(pady=5)

    def create_interactive_elements(self):
        # Dua Button
        self.dua_button = tk.Button(self.root, text="Click for Special Dua",
                                    command=self.show_dua, bg='#333399', fg='white')
        self.dua_button.pack(pady=10)

        # Dua Display
        self.dua_display = tk.Label(self.root, text="",
                                    font=('Arial', 12), fg='#00FF00', bg='#000033')
        self.dua_display.pack(pady=5)

    def show_dua(self):
        duas = [
            "O Allah, forgive our sins and grant us mercy!",
            "Ya Rabb, accept our prayers and good deeds!",
            "Allahumma bless us with Your infinite mercy!",
            "O Allah, protect us from the fire of Jahannam!",
            "Ya Arhamar Rahimin, shower us with Your blessings!"
        ]
        self.dua_display.config(text=random.choice(duas))

    def animate_moon(self):
        self.current_x = 50
        self.direction = 1
        self.move_moon()

    def move_moon(self):
        self.current_x += 5 * self.direction
        if self.current_x > 700:
            self.direction = -1
        elif self.current_x < 50:
            self.direction = 1
        self.moon_label.place(x=self.current_x, y=50)
        self.root.after(100, self.move_moon)

        # Add twinkle effect
        if random.random() < 0.2:
            self.moon_label.config(fg='gold')
        else:
            self.moon_label.config(fg='white')


if __name__ == "__main__":
    root = tk.Tk()
    app = ShabEBaratApp(root)

    # Add footer
    footer = tk.Label(root, text="May your prayers be accepted and sins forgiven! ✨",
                      font=('Arial', 10), fg='cyan', bg='#000033')
    footer.pack(side=tk.BOTTOM, pady=10)

    root.mainloop()