from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
couple_words = {}
to_learn = {}


try:
    words = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    words = pandas.read_csv("data/table_words_en_ru.csv")
else:
    all_words = words.to_dict(orient="records")

def answer_to_card():
    canvas.itemconfig(card_bg, image=card_back)
    canvas.itemconfig(tittle_card, text="Russian", fill="white")
    canvas.itemconfig(words_card, text=couple_words['ru'], fill="white")

def random_en_word():
    global couple_words, timer_flip
    window.after_cancel(timer_flip)
    couple_words = choice(all_words)
    canvas.itemconfig(card_bg, image=card_front)
    canvas.itemconfig(tittle_card, text="English", fill="black")
    canvas.itemconfig(words_card, text=couple_words['en'], fill="black")
    timer_flip = window.after(3000, answer_to_card)

def right_button_func():
    all_words.remove(couple_words)
    new_data = pandas.DataFrame(all_words)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    random_en_word()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer_flip = window.after(3000, answer_to_card)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
right_answer = PhotoImage(file="images/right.png")
wrong_answer = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_bg = canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)
tittle_card = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
words_card = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

wrong_button = Button(image=wrong_answer, bg=BACKGROUND_COLOR, highlightthickness=0, command=random_en_word)
wrong_button.grid(column=0, row=1)

right_button = Button(image=right_answer, bg=BACKGROUND_COLOR, highlightthickness=0, command=right_button_func)
right_button.grid(column=1, row=1)

random_en_word()

window.mainloop()


