from tkinter import *
# from customtkinter import CTk


class UserInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Mini Games")

        self.min_width = 400
        self.min_height = 400
        self.max_width = 800
        self.max_height = 600

        self.window.wm_minsize(self.min_width, self.min_height)  # width, height
        self.window.wm_maxsize(self.max_width, self.max_height)

        self.buttons = []

    def create_button(self, button_name, button_function):

        button = Button(self.window, text=button_name, command=button_function)
        print(f"{button.size() = }")
        y_level = 0.4 + (0.1 * (len(self.buttons) + 1.0))
        print(f"{y_level = }")
        button.place(relx=0.5, rely=y_level, anchor='center')
        self.buttons.append(button)

    def rules_display(self):
        print("Displaying the rules")

    def multiplayer_screen(self):
        print("Going to multiplayer screen")

    def vs_ai(self):
        print("Going to Vs Ai Screen")

    def render(self):
        self.window.mainloop()


UI = UserInterface()
UI.create_button("Rules", UI.rules_display)
UI.create_button("Multiplayer", UI.multiplayer_screen)
UI.create_button("Vs AI", UI.vs_ai)
UI.render()
