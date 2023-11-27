from tkinter import *
from Main import get_response, bot_name
import os
from gtts import gTTS
import pygame
import datetime
import re

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

class ChatApplication:
    
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
        self.tts_enabled = False
        
    def run(self):
        self.window.mainloop()
        
    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=700, height=700, bg=BG_COLOR)
        
        # head label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="Welcome", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)
        
        # tiny divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)
        
        # text widget
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        
        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)
        self.text_widget.config(yscrollcommand=scrollbar.set)
        
        # bottom label
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)
        
        # message entry box
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        
        # send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

    def sentence_contain_string_with_number(self, input_string):
        pattern = r'[0-9]+[a-zA-Z]+|[a-zA-Z]+[0-9]+'
        match = re.search(pattern, input_string)
        return match is not None

    #! When user click the button or press "Enter"
    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        if msg == "TTS ON":
            self.tts_enabled = True
            self._insert_message(msg, bot_name)
        elif msg == "TTS OFF":
            self.tts_enabled = False
            self._insert_message(msg, bot_name)
        else:
            self._insert_message(msg, "You")
        
    def _insert_message(self, msg, sender):
        if not msg:
            return
                        
        #! run when self.tts_enabled = True
        if self.tts_enabled:
            #Text_to_Speech
            speech_text = get_response(msg)
            speech = gTTS(speech_text)
            speech_file = "Audio.mp3"
            speech.save(speech_file)
            pygame.init()
            pygame.mixer.init()
            sound = pygame.mixer.Sound(speech_file)
            sound.play()
            while pygame.mixer.get_busy():
                pygame.time.Clock().tick(0)
            pygame.mixer.quit()
            os.remove(speech_file)

        #Clear the entry text field, and print the user response
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
            
        #Print Bot Response
        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        
        #!Write the output into txt file
        #(a = append) (w = overwrite) (r = read)
        current_datetime = datetime.datetime.now()
        format_datetime = current_datetime.strftime("%d-%m-%Y_%H-%M")
        output_filename = f"conversation_{format_datetime}.txt"
        file = open(output_filename, "a")
        file.write("\nYou : " + msg)
        file.write("\nBot : " + get_response(msg))
        file.close()
 
        self.text_widget.see(END)

if __name__ == "__main__":
        app = ChatApplication()
        app.run()