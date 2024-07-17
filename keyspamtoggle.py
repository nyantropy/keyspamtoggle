#A small script to continuously spam a single keypress - used in conjunction with autokey :)

import time
import threading
import os

#path to state file in tmp
state_file = "/tmp/spam_state.txt"
thread = None

#this is the key that is spammed during the toggle
key = "<f12>"

#keypress delay
delay = 0.1

#spam key defined above
def spam():
    while True:
        with open(state_file, 'r') as f:
            spamming = f.read().strip() == "1"
        if not spamming:
            break

        keyboard.send_key(key)
        time.sleep(delay)

#toggle spam state by using a tmp file
def toggle_spam():
    global thread
    # Read the current state
    if os.path.exists(state_file):
        with open(state_file, 'r') as f:
            current_state = f.read().strip()
    else:
        current_state = "0"

    #toggle the state
    new_state = "0" if current_state == "1" else "1"
    with open(state_file, 'w') as f:
        f.write(new_state)

    #start a thread if we need to start a spam thread - this will join automatically, since it probes the tmp file
    if new_state == "1":
        if thread is None or not thread.is_alive():
            thread = threading.Thread(target=spam)
            thread.start()

#toggle spam whenever script is run
toggle_spam()
