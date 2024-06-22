from tkinter import *
from tkinter import messagebox


def submit_form():
    messagebox.showinfo("Information", f"Регистрация прошла успешно!")


window = Tk()
window.geometry("550x800")
window.title("Рома | Вариант 32")

header_text = Label(text="ALL FIELDS FORM", fg='blue', font=("Times", 17))
header_text.grid(row=0, column=0, padx=10, pady=10)

text_file = Label(text="Textfield", font=('Times', 12))
text_file.grid(row=1, column=0, padx=5, pady=10)
text_file_entry = Entry(bg='white', width=42)
text_file_entry.grid(row=1, column=1, padx=5, pady=10)

text_area = Label(text="Textarea", font=('Times', 12))
text_area.grid(row=2, column=0, padx=10, pady=1)
text_area_text = Text(height=6, width=30)
text_area_text.grid(row=2, column=1, padx=10, pady=30, sticky='w', columnspan=3)

email_address = Label(text="Email Address", font=('Times', 12))
email_address.grid(row=3, column=0, padx=5, pady=10)
email_address_entry = Entry(bg='white', width=42)
email_address_entry.grid(row=3, column=1, padx=5, pady=10)

dropdown = Label(text="Dropdown", font=('Times', 12))
dropdown.grid(row=4, column=0, padx=10, pady=10)
dropdown_text_option = StringVar(value="Option 1")
option_menu_dropdown = OptionMenu(
    window,
    dropdown_text_option,
    "Ростов-на-Дону", "Респ. Дагестан, г. Дербент",
    "Респ. Дагестан, Махачкала", "Респ. Дагестан, пос. Белиджи",
    "Респ. Дагестан, село Кабир"
)
option_menu_dropdown.grid(row=4, column=1, padx=10, pady=5, columnspan=3)

radio_button = Label(text="Radio Button", font=('Arial bold', 12))
radio_button.grid(row=5, column=0, padx=10, pady=10)
radio_button_activate = StringVar(value="task_option_one")
task_option_one = Radiobutton(text="Option 1", variable=radio_button_activate, value="task_option_one")
task_option_one.grid(row=5, column=1, padx=10, pady=5)
task_option_one = Radiobutton(text="Option 2", variable=radio_button_activate, value="task_option_one")
task_option_one.grid(row=6, column=1, padx=10, pady=5)

checkbox = Label(text="Checkbox", font=('Times', 12))
checkbox.grid(row=7, column=0, padx=10, pady=10)
checkbox_option_one = Checkbutton(text="Option 1")
checkbox_option_one.grid(row=7, column=1, padx=10, pady=5)
checkbox_option_two = Checkbutton(text="Option 2")
checkbox_option_two.grid(row=8, column=1, padx=10, pady=5)
checkbox_option_tree = Checkbutton(text="Option 3")
checkbox_option_tree.grid(row=9, column=1, padx=10, pady=5)

password = Label(text="Password", font=('Arial bold', 12))
password.grid(row=10, column=0, padx=10, pady=10)
entry_password = Entry(show='*', bg='#dbdbdb', width=42)
entry_password.grid(row=10, column=1, padx=10, pady=10, columnspan=3)

number_filed = Label(text="Number Field", font=('Times', 12))
number_filed.grid(row=11, column=0, padx=5, pady=10)
number_filed_entry = Entry(bg='#dbdbdb', width=12)
number_filed_entry.grid(row=11, column=1, padx=5, pady=10)

mathematical_captcha = Label(text="Mathematical\nCaptcha", font=('Times', 12))
mathematical_captcha.grid(row=12, column=0, padx=5, pady=10)
mathematical_captcha_text = Label(text="6 + 8 =", font=('Times', 12))
mathematical_captcha_text.grid(row=12, column=1, padx=5, pady=10)
mathematical_captcha_entry = Entry(bg='#dbdbdb', width=5)
mathematical_captcha_entry.grid(row=12, column=2, padx=5, pady=10)

google_captcha = Label(text="Google Captcha", font=('Times', 12))
google_captcha.grid(row=13, column=0, padx=10, pady=10)
google_captcha_check = Checkbutton(text="I'm not a robot", bg='#dbdbdb', font=('Times', 12), width=25)
google_captcha_check.grid(row=13, column=1, padx=10, pady=5)

btn = Button(text="Submit", bg='blue', fg='white', command=submit_form)
btn.grid(row=14, column=0, padx=10, pady=10)

window.mainloop()
