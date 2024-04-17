import tkinter
from PIL import Image, ImageDraw
from tkinter import filedialog

# Window
window = tkinter.Tk()
window.title("Image Water Generator")
window.minsize(300, 10)
window.config(padx=60, pady=60, bg="#31363F")

# Canvas
canvas = tkinter.Canvas
my_canvas = canvas(width=60, height=60, bg="black", highlightthickness=0)

# Labels
label = tkinter.Label
title_label = label(text="image watermark generator".capitalize(), bg="#31363F", fg="white", font=("arial", 15, "bold"))
user_text_label = label(text="insert text".capitalize(), bg="#31363F", fg="white", font=("arial", 10, "bold"))
select_image_label = label(text="select an image".capitalize(), bg="#31363F", fg="white", font=("arial", 10, "bold"))

# text field
user_text_input = tkinter.Entry(width=14)


def image_select():
    user_text = user_text_input.get()
    selection = filedialog.askopenfilename(initialdir="/", title="Select a File")
    image_resolution = Image.open(selection).size
    print(f"Image Size: {image_resolution}")
    if image_resolution[0] > 1000:
        column = 4000
        row = 5000
        column_space = 500
        row_space = 200
        font_size = 80

    else:
        column = 2000
        row = 2000
        column_space = 200
        row_space = 50
        font_size = 25

    with Image.open(selection).convert("RGBA") as base:
        # make a blank image for the text, initialized to transparent text color
        txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

        # get a drawing context
        d = ImageDraw.Draw(txt)

        # draw text, half opacity
        for n in range(column)[100::column_space]:
            for row in range(row)[::row_space]:
                d.text((n, row), user_text, font_size=font_size, fill=(255, 255, 255, 60))

        out = Image.alpha_composite(base, txt)

        out.show()


# Button
button = tkinter.Button
select_button = button(text="Select Image", command=image_select)

# padding
title_label.config(padx=0, pady=0)
user_text_label.config(padx=0, pady=20)
select_image_label.config(padx=0, pady=20)

# Grid
title_label.grid(column=0, row=0)
user_text_label.grid(column=0, row=1)
user_text_input.grid(column=0, row=2)
select_image_label.grid(column=0, row=3)
select_button.grid(column=0, row=4)


window.mainloop()
