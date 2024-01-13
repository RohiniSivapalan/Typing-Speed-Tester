#Typing Speed Test by ROHINI S
import time
import random
import tkinter as tk
from tkinter import messagebox

def get_random_sentence():
    sentences = [
        "Coding is fun and challenging at the same time.",
        "The journey of a thousand miles begins with a single step.",
        "Innovation distinguishes between a leader and a follower.",
        "Be the change that you wish to see in the world.",
        "Life is what happens when you're busy making other plans.",
        "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "The only limit to our realization of tomorrow will be our doubts of today."
        "The sun sets, casting a warm glow on the horizon.",
        "Coding challenges develop problem-solving skills and enhance programming proficiency.",
        "Incredible journeys begin with a single step and relentless determination.",
        "Practice regularly, and your skills will steadily improve over time.",
        "Nature's beauty surrounds us, offering moments of peace and inspiration.",
        "Creativity flourishes when guided by passion and fueled by perseverance.",
        "Unlock your potential, embrace challenges, and achieve extraordinary accomplishments.",
        "Balancing work and life requires mindfulness, priorities, and effective time management.",
        "Adaptability is the key to thriving in an ever-changing world.",
        "Positive thoughts breed positive actions, creating a path to success."
    ]
    return random.choice(sentences)

class TypingSpeedTestApp:
    def __init__(self, master):
        self.master = master
        master.title("Typing Speed Test")

        # Increased window size
        master.geometry("500x400")

        # Background color
        master.configure(bg="light blue")

        self.sentence_label = tk.Label(master, text="", font=("Arial", 12), bg="light blue")
        self.sentence_label.pack(pady=10)

        self.text_entry = tk.Text(master, wrap="word", width=40, height=2, font=("Arial", 12))
        self.text_entry.pack(pady=10)

        self.text_entry.bind("<KeyRelease>", self.adjust_text_area)
        self.text_entry.bind("<Return>", self.show_result)

        self.result_label = tk.Label(master, text="", font=("Arial", 12), bg="light blue")
        self.result_label.pack(pady=10)

        self.start_test()

    def start_test(self):
        self.start_time = time.time()
        sentence = get_random_sentence()
        self.sentence_label.config(text=f"Type the following sentence : \n\n\n{sentence}")

        self.text_entry.delete(1.0, tk.END)  # Clear the text area
        self.result_label.config(text="")
        self.adjust_text_area()

    def show_result(self, event):
        typed_text = self.text_entry.get(1.0, tk.END).strip()

        accuracy = calculate_accuracy(self.sentence_label.cget("text"), typed_text)
        end_time = time.time()
        time_taken = end_time - self.start_time
        words_per_minute = calculate_speed(len(typed_text.split()), time_taken)
        score = calculate_score(words_per_minute, accuracy)

        result_text = f"Your Typing Speed : {words_per_minute:.2f} Words per Minute\n\nAccuracy : {accuracy:.2f}%"
        self.result_label.config(text=result_text)

    def adjust_text_area(self, event=None):
        self.text_entry.config(height=self.text_entry.get("1.0", "end-1c").count("\n") + 2)

def calculate_accuracy(original, typed):
    min_len = min(len(original), len(typed))
    correct_chars = sum(c1 == c2 for c1, c2 in zip(original[:min_len], typed[:min_len]))
    accuracy = (correct_chars / max(len(original), len(typed))) * 100 if len(original) != 0 else 0
    return accuracy



def calculate_speed(words_typed, time_taken):
    return (words_typed / time_taken) * 60 if time_taken != 0 else 0

def calculate_score(words_per_minute, accuracy):
    return (words_per_minute * accuracy) / 100

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()
