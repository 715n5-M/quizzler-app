from tkinter import *
from tkinter import messagebox
from data import question_data
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("QUIZZLER")
        self.window.config(pady=20, padx=20, bg= THEME_COLOR)

        self.score_l = Label(text="Score: 0 ", highlightthickness=0, bg= THEME_COLOR, fg='white',
                             font=("Ariel", 12, "bold"))
        self.score_l.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text=self.canvas.create_text(150, 125, text= "question_data",
                                                   font=("Arial", 15, "italic"), fill=THEME_COLOR, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_b_img = PhotoImage(file="images/true.png")
        self.true_b = Button(image=true_b_img, highlightthickness=0, command=self.true_pressed)
        self.true_b.grid(row=3, column=0)

        false_b_img = PhotoImage(file="images/false.png")
        self.false_b = Button(image=false_b_img, highlightthickness=0, command=self.false_pressed)
        self.false_b.grid(row=3, column=1)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            self.score_l.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the game")
            self.true_b.config(state="disabled")
            self.false_b.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
