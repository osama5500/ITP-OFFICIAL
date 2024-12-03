

# This was created in a different file than the one here. Once it was completed, I simply copy/pasted the code into here


import tkinter as tk
from tkinter import PhotoImage #Import Tkinter and Python Image Library into the program for their uses

class ChooseYourOwnStory:
    def __init__(self, root):
        self.root = root
        self.root.title("The Adventures Against Nettspend")
        
        # Setup the main frame
        self.frame = tk.Frame(self.root, bg="lightblue") #The frame where all buttons and text will be displayed
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        # These are the actual choices and prompts that will eventually be displayed on the screen. I like to edit them a lot and make different stories, so I keep them as organized as I can.
        #The "next" is for the outcome of the choice made. For example, you see 1: 3: and so on, but you don't see 2. That's because 2 is in the right branch, or the other choice outcome.
        self.story = {
            "start": {
                "text": "You wake up in a mysterious cave. Do you up the ladder to your right or down the tunnel to your left?",
                "choices": ["Ladder", "Tunnel"],
                "next": ["Osa_Mason_bridge", "Lazer_Dim_ahead"]
            },
            "Osa_Mason_bridge": { #Left Branch
                "text": "Osa Mason is waiting for you outside. He says to take the bridge to the right, should you take it, or the bridge to the left?",
                "choices": ["Bridge to the right", "Bridge to the left"],
                "next": ["cabin_explore", "knock_or_not"]
            },
            "cabin_explore": {
                "text": "You find a mysterious abandoned cabin. Should you explore it or keep moving on?",
                "choices": ["Explore the cabin", "Keep moving"],
                "next": ["followed_by_Osa", "Osa_trapped"]
            },
            "knock_or_not": {
                "text": "You find a home, which seems to be occupied. Should you knock on the door or keep moving?",
                "choices": ["Knock", "Keep moving"],
                "next": ["Nettspend_servants", "good_ending_1"]
            },
            "followed_by_Osa": {"text": "You explore the cabin, unaware of Osa Mason following you, waiting for the perfect opportunity. This is the end for you.", "choices": [], "next": []},
            "Osa_trapped": {"text": "Osa Mason set up a trap for you, and unfortunately, you got caught. You will spend the rest of your life in prison.", "choices": [], "next": []},
            "Nettspend_servants": {"text": "The people at the door were servants of Nettspend. This didn't end well.", "choices": [], "next": []},
            "good_ending_1": {"text": "While you didn't make it to Nettspend's castle, you did escape with your life. At least you are alive.", "choices": [], "next": []},
            # Right branch
            "Lazer_Dim_ahead": {
                "text": "You use the hidden tunnel to make it outside Nettspend's legendary castle. Lazer Dim stands guard. Do you fight him or try to sneak in?",
                "choices": ["Fight", "Sneak"],
                "next": ["gate_or_not", "crown_of_Nettspend"]
            },
            "gate_or_not": {
                "text": "You narrowly defeat Lazer Dim. The gate is down. Should you enter through there?",
                "choices": ["Use gate", "Look for another way"],
                "next": ["lots_of_guards", "black_hole"]
            },
            "crown_of_Nettspend": {
                "text": "You sneak in through an open window. Nettspend's royal crown is sitting there, unattended. Do you take the crown or leave it?",
                "choices": ["Take the crown", "Leave the crown"],
                "next": ["Nettspend_mad", "Nettspend_happy"]
            },
            "lots_of_guards": {"text": "You rush in through the gates, only to meet thousands of guards. You are quickly dispatched.", "choices": [], "next": []},
            "black_hole": {"text": "You look for another way, but fall into Nettspend's pocket black hole. Crazy that he has one, right?", "choices": [], "next": []},
            "Nettspend_mad": {
                "text": "Before you can grab it, Nettspend appears. He yells 'How dare you try to steal my drank!' Should you fight or run?",
                "choices": ["Fight", "Run"],
                "next": ["prison_forever", "escape_barely"]
            },
            "Nettspend_happy": {
                "text": "Before you leave, Nettspend appears in front of you. He wants you to become the new king, because you didn't steal such a valuable item. Do you accept?",
                "choices": ["Accept his offer", "Reject his offer"],
                "next": ["underground_King", "myth_of_the_world"]
            },
            "prison_forever": {"text": "You fight valiantly, but Nettspend bests you and throws you in prison, forever.", "choices": [], "next": []},
            "escape_barely": {"text": "You manage to barely escape Nettspend's wrath. You have no idea where you are and are severely injured, but still alive.", "choices": [], "next": []},
            "underground_King": {"text": "You are the new king of the Underground. Congratulations!", "choices": [], "next": []},
            "myth_of_the_world": {"text": "You leave and become a myth, a powerful warrior who declined Nettspend and lived in the shadows, your stories told to this day. Congratulations!.", "choices": [], "next": []}
        }
        self.current_stage = 0
        self.user_choices = []  # To track the user's choices and see what's up
        
        # Label for the story, also works as the background in the actual story
        self.story_label = tk.Label(self.frame, text="", wraplength=400, bg="lightblue", font=("Arial", 14))
        self.story_label.pack(pady=20)
        
        # Buttons for choices
        self.button1 = tk.Button(self.frame, text="", command=lambda: self.next_step(0), font=("Arial", 12))
        self.button2 = tk.Button(self.frame, text="", command=lambda: self.next_step(1), font=("Arial", 12))
        self.button1.pack(pady=5)
        self.button2.pack(pady=5)
        
        self.update_choices()

    def update_choices(self):
        #Update UI with the choices
        stage = self.story[self.current_stage]
        self.story_label.config(text=stage["text"])
        
        if stage["choices"]:
            self.button1.config(text=stage["choices"][0], state=tk.NORMAL)
            self.button2.config(text=stage["choices"][1], state=tk.NORMAL)
        else:
            self.button1.pack_forget()
            self.button2.pack_forget()

    def next_step(self, choice):
        #Based on the user's decision, make the next choice
        stage = self.story[self.current_stage]
        if stage["choices"]:
            self.user_choices.append(stage["choices"][choice])
            self.current_stage = stage["next"][choice]
            self.update_choices()


# Create the tkinter window
root = tk.Tk()
app = ChooseYourOwnStory(root)
root.geometry("500x500")
root.mainloop()