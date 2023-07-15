import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class QuizGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("MCQ Quiz")
        self.master.geometry("600x400")
        
        # Quiz questions, options, and answers
        self.questions = [
            {
                "question": "Which of the following is liquid at room temperature?",
                "options": ["Carbon", "Sodium", "Oxygen", "Mercury"],
                "answer": 3
            },
            {
                "question": "What is the national game of India?",
                "options": ["Hockey", "Badminton", "Cricket", "Football"],
                "answer": 0
            },
            {
                "question": "How many states are there in India?",
                "options": ["27", "28", "30", "29"],
                "answer": 1
            }
        ]
        
        # Track current question and score
        self.current_question = 0
        self.score = 0
        
        # Create style for labels
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Arial", 18))
        
        # Create widgets
        self.question_label = ttk.Label(master, text="")
        self.question_label.pack(pady=20)
        
        self.option_var = tk.IntVar()
        
        self.option_radios = []
        for i in range(4):
            radio = ttk.Radiobutton(master, text="", variable=self.option_var, value=i)
            radio.pack(anchor=tk.W)
            self.option_radios.append(radio)
        
        self.submit_button = ttk.Button(master, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=20)
        
        self.score_label = ttk.Label(master, text="")
        self.score_label.pack()
        
        # Start the quiz
        self.show_question()
        
    def show_question(self):
        question_data = self.questions[self.current_question]
        
        self.question_label.config(text=question_data["question"])
        
        for i, option_radio in enumerate(self.option_radios):
            option_radio.config(text=question_data["options"][i])
        
        self.option_var.set(-1)  # Reset option selection
        
        self.submit_button.config(state=tk.NORMAL)  # Enable submit button
        
        self.score_label.config(text=f"Score: {self.score}/{self.current_question}")
    
    def check_answer(self):
        selected_option = self.option_var.get()
        correct_answer = self.questions[self.current_question]["answer"]
        
        if selected_option == -1:
            messagebox.showwarning("No Option Selected", "Please select an option.")
            return
        
        if selected_option == correct_answer:
            self.score += 1
        
        self.submit_button.config(state=tk.DISABLED)  # Disable submit button
        
        # Move to the next question or finish the quiz
        self.current_question += 1
        
        if self.current_question < len(self.questions):
            self.show_question()
        else:
            messagebox.showinfo("Quiz Finished", f"You have answered all the questions!\nYour score: {self.score}/{len(self.questions)}")
            self.master.destroy()  # Close the GUI window

# Create the main window
root = tk.Tk()

# Create the quiz GUI
quiz = QuizGUI(root)

# Start the main event loop
root.mainloop()
