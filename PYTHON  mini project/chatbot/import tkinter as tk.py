import tkinter as tk
from tkinter import scrolledtext, messagebox
import random

class Chatbot:
    def __init__(self, master):
        self.master = master
        master.title("Advanced Chatbot")

        self.chat_area = scrolledtext.ScrolledText(master, state='disabled', wrap=tk.WORD)
        self.chat_area.pack(padx=10, pady=10)

        self.user_input = tk.Entry(master, width=48)
        self.user_input.pack(padx=10, pady=10)
        self.user_input.bind('<Return>', self.send_message)

        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.pack(pady=10)

        self.setup()

    def setup(self):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, "Bot: Hello! I'm here to chat. How can I help you today?\n")
        self.chat_area.config(state='disabled')

    def send_message(self, event=None):
        user_message = self.user_input.get()
        if not user_message.strip():
            messagebox.showwarning("Warning", "Please enter a message.")
            return
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, "You: " + user_message + "\n")
        self.chat_area.insert(tk.END, "Bot: " + self.get_response(user_message) + "\n")
        self.user_input.delete(0, tk.END)
        self.chat_area.config(state='disabled')
        self.chat_area.yview(tk.END)

    def get_response(self, user_message):
        user_message = user_message.lower()
        responses = {
            'hello': "Hello! How can I assist you today?",
            'how are you': "I'm just a computer program, but thanks for asking!",
            'bye': "Goodbye! Have a great day!",
            'help': "I can help you with general inquiries. Ask me anything!"
        }
        return responses.get(user_message, "I'm sorry, I don't understand that.")

if __name__ == "__main__":
    root = tk.Tk()
    chatbot = Chatbot(root)
    root.mainloop()
