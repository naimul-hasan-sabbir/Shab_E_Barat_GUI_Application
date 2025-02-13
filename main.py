import tkinter as tk
import datetime
import math
import time
import random
from PIL import Image, ImageTk

class ShabeBaratPoster:
    def __init__(self, root):
        self.root = root
        self.root.title("Shab-e-Barat")
        self.width = 800
        self.height = 600
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.configure(bg="#03045e")

        self.canvas = tk.Canvas(
            self.root, width=self.width, height=self.height, bg="#03045e", highlightthickness=0
        )
        self.canvas.pack()

        self.stars = []
        self.create_stars(50)

        try:
            self.moon_image = Image.open("crescent_moon.jpg")
            self.moon_image = self.moon_image.resize((150, 150))
            self.moon_photo = ImageTk.PhotoImage(self.moon_image)
            self.moon = self.canvas.create_image(self.width // 2, 100, image=self.moon_photo)
        except FileNotFoundError:
            print("Error: crescent_moon.png not found")
            self.moon = self.canvas.create_oval(
                self.width//2 - 50, 50, self.width//2 + 50, 150, fill="gold", outline="gold"
            )
        self.moon_glow_radius = 80
        self.moon_glow = self.canvas.create_oval(
             self.width//2 - self.moon_glow_radius, 100 - self.moon_glow_radius,
             self.width//2 + self.moon_glow_radius, 100 + self.moon_glow_radius,
             fill="", outline="gold", width=2
         )
        self.moon_glow_opacity = 1.0
        self.moon_glow_direction = -1

        self.mosque_coords = [
            50, self.height - 50, 150, self.height - 150, 250, self.height - 150,
            300, self.height - 100, 500, self.height - 100, 550, self.height - 150,
            650, self.height - 150, 750, self.height - 50, self.width - 50, self.height - 50,
            self.width - 50, self.height, 50, self.height
        ]
        self.mosque = self.canvas.create_polygon(
            self.mosque_coords, fill="#001219", outline="#001219"
        )

        self.pattern_start_y = self.height - 50
        self.pattern_height = 50
        self.create_geometric_pattern()

        self.title_text = self.canvas.create_text(
            self.width // 2, 220, text="Shab-e-Barat", font=("Arial", 48, "bold"),
            fill="gold", state=tk.HIDDEN
        )
        self.subtitle_text = self.canvas.create_text(
            self.width // 2, 280, text="The Night of Forgiveness", font=("Arial", 24, "italic"),
            fill="white", state=tk.HIDDEN
        )
        self.dua_text = self.canvas.create_text(
            self.width // 2, 350, text="Allahumma innaka `Afuwwun \nTuhibbul `Afwa fa`fu `annee",
            font=("Arial", 16), fill="white", state=tk.HIDDEN, justify=tk.CENTER
        )
        self.dua_translation_text = self.canvas.create_text(
            self.width // 2, 400, text="O Allah, You are Forgiving and love forgiveness, so forgive me",
            font=("Arial", 12, "italic"), fill="white", state=tk.HIDDEN, justify=tk.CENTER
        )
        self.date_text = self.canvas.create_text(
            self.width // 2, 450, text="February 14, 2025",
            # self.width // 2, 450, text=self.calculate_shab_e_barat_date(),
            font=("Arial", 14, "bold"), fill="gold", state=tk.HIDDEN
        )

        self.animation_stage = 0
        self.animation_delay = 50
        self.animate()

        self.lanterns = []
        self.create_lanterns(7)

    def create_stars(self, num_stars):
        for _ in range(num_stars):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.randint(1, 3)
            star = self.canvas.create_oval(
                x, y, x + size, y + size, fill="white", outline="white"
            )
            self.stars.append((star, size))

    def create_lanterns(self,num_lanterns):
        for _ in range(num_lanterns):
            x = random.randint(50, self.width-50)
            y = random.randint(self.height - 90, self.height -60)
            size = random.randint(10,15)
            lantern = self.canvas.create_oval(x,y,x+size, y+size, fill="orange", outline = "darkorange")
            self.lanterns.append((lantern, x, y, size, random.uniform(0.5, 1.5)))
            self.canvas.itemconfig(lantern, state=tk.HIDDEN)

    def animate_stars(self):
        for star, size in self.stars:
            opacity = random.uniform(0.5, 1.0)
            self.canvas.itemconfig(star, fill=f"#{int(255*opacity):02x}FFFF")

    def animate_moon_glow(self):
        self.moon_glow_opacity += 0.05 * self.moon_glow_direction
        if self.moon_glow_opacity <= 0.1 or self.moon_glow_opacity >= 1.0:
            self.moon_glow_direction *= -1
        opacity_hex = hex(int(self.moon_glow_opacity * 255))[2:].zfill(2)
        glow_color = f"#FFD700{opacity_hex}"
        self.canvas.itemconfig(self.moon_glow, outline=glow_color)

    def animate_lanterns(self):
        for i, (lantern, x, y, size, speed) in enumerate(self.lanterns):
            if self.canvas.itemcget(lantern, "state") == tk.HIDDEN:
                continue
            y -= speed
            x += math.sin(time.time() * 5) * 2
            self.canvas.coords(lantern, x, y, x + size, y + size)
            if y + size < 0:
                x = random.randint(50, self.width-50)
                y = random.randint(self.height - 90, self.height -60)
                speed = random.uniform(0.5, 1.5)
                self.canvas.coords(lantern, x, y, x+size, y+size)
            self.lanterns[i] = (lantern, x, y, size, speed)

    def animate(self):
        if self.animation_stage == 0:
            self.animation_stage = 1
        elif self.animation_stage == 1:
            self.canvas.itemconfig(self.title_text, state=tk.NORMAL)
            self.animation_stage = 2
        elif self.animation_stage == 2:
            self.canvas.itemconfig(self.subtitle_text, state=tk.NORMAL)
            self.animation_stage = 3
        elif self.animation_stage == 3:
            for lantern,_,_,_,_ in self.lanterns:
                self.canvas.itemconfig(lantern, state = tk.NORMAL)
            self.animation_stage = 4
        elif self.animation_stage == 4:
             self.canvas.itemconfig(self.dua_text, state=tk.NORMAL)
             self.canvas.itemconfig(self.dua_translation_text, state=tk.NORMAL)
             self.animation_stage = 5
        elif self.animation_stage == 5:
            self.canvas.itemconfig(self.date_text, state= tk.NORMAL)
            self.animation_stage = 6
        elif self.animation_stage == 6:
            self.animate_stars()
            self.animate_moon_glow()
            self.animate_lanterns()
        self.root.after(self.animation_delay, self.animate)

    def calculate_shab_e_barat_date(self):
        current_year = datetime.date.today().year
        base_date = datetime.date(2024, 2, 11)
        year_diff = current_year - 2024
        approx_days_offset = year_diff * 354
        approx_shaban_start = base_date + datetime.timedelta(days=approx_days_offset)
        shab_e_barat_date = approx_shaban_start + datetime.timedelta(days=14)
        return shab_e_barat_date.strftime("%B %d, %Y")

    def draw_square(self, x, y, size, color):
        self.canvas.create_rectangle(x, y, x + size, y + size, fill=color, outline=color)

    def draw_eight_pointed_star(self, x, y, size, color):
        half_size = size / 2
        sqrt2_2 = 0.7071
        offset = half_size * sqrt2_2
        points = [
            x + half_size, y,
            x + size - offset, y + offset,
            x + size, y + half_size,
            x + size - offset, y + size - offset,
            x + half_size, y + size,
            x + offset, y + size - offset,
            x, y + half_size,
            x + offset, y + offset,
        ]
        self.canvas.create_polygon(points, fill=color, outline=color)

    def create_geometric_pattern(self):
        star_size = 50
        square_size = star_size * 0.7071

        x = 0
        while x < self.width:

            self.draw_eight_pointed_star(x, self.pattern_start_y, star_size, "#FFD700")
            self.draw_square(x + star_size * 0.7071 / 2, self.pattern_start_y + star_size * 0.7071 / 2 , square_size, "#03045e")

            x += star_size * 0.7071 + star_size/2

            if x < self.width:
              self.draw_eight_pointed_star(x, self.pattern_start_y, star_size, "#03045e")
              self.draw_square(x + star_size * 0.7071 / 2, self.pattern_start_y + star_size * 0.7071 / 2 , square_size, "#FFD700")
              x += star_size * 0.7071 + star_size/2


if __name__ == "__main__":
    root = tk.Tk()
    poster = ShabeBaratPoster(root)
    root.mainloop()