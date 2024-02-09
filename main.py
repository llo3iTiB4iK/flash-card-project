from tkinter import *
import pandas as pd
BACKGROUND_COLOR = "#B1DDC6"
flip_timer = None
current_word_index = None

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/data.csv")


def new_card():
    global flip_timer, current_word_index
    if flip_timer:
        window.after_cancel(flip_timer)
    card = data.sample()
    current_word_index = card.index[0]
    canvas.itemconfig(word_label, text=card["en_word"].item(), fill="black")
    canvas.itemconfig(language_label, text="English", fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, flip_card, card)


def flip_card(card):
    canvas.itemconfig(word_label, text=card["uk_word"].item(), fill="white")
    canvas.itemconfig(language_label, text="Ukrainian", fill="white")
    canvas.itemconfig(card_background, image=card_back_image)


def word_is_known():
    data.drop(current_word_index, inplace=True)
    new_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
language_label = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_label = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bd=0, command=new_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bd=0, command=word_is_known)
right_button.grid(row=1, column=1)

new_card()

window.mainloop()

data.to_csv("data/words_to_learn.csv", index=False)
