import tkinter as tk
from PIL import Image, ImageTk

class AdventureGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Adventure Game")
        self.geometry("420x420")
        self.config(bg="#fae5b1")

    
    def create_widgets(self):
        self.text_label = tk.Label(self, text="Welcome to the Lost Library Adventure!", font=("Helvetica", 20), wraplength=600)
        self.text_label.pack()

        self.image_label = tk.Label(self)
        self.image_label.pack()

        self.button1 = tk.Button(self, text="1", command=self.next_stage(1))
        self.button2 = tk.Button(self, text="2", command=self.next_stage(2))

        self.button1.pack(pady=10)
        self.button2.pack(pady=10)


    def next_stage(self, choice):
        if self.current_stage in self.next_stages:
            self.current_stage = self.next_stages[self.current_stage][choice - 1]
        else:
            self.current_stage += 1

        self.update_story()


    def display_image(self, image_path):
        img = Image.open(image_path)
        img = img.resize((150, 150))
        img = ImageTk.PhotoImage(img)

        self.image_label.config(image=img)
        self.image_label.image = img

if __name__ == "__main__":
    app = AdventureGame()
    app.mainloop()