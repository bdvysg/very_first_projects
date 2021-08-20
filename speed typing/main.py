from tkinter import *
from random import choice
import time
import threading


right = 0
wrong = 0

right_len = 0
wrong_len = 0


def get_word_list():
    with open('projects\speed typing\en.txt', 'r') as words:
        word_list = [word[:-1] for word in words]
        return word_list


def set_new_words(*args):
    count_right_and_wrong()
    current_word.config(text= next_word.cget('text'))
    next_word.config(text= choice(word_list))
    entry_field.delete(0, END)
    

def start_test(*args):
    finish_score.config(text='')
    
    global right, right_len
    global wrong, wrong_len
    right = 0
    right_len = 0
    wrong = 0
    wrong_len = 0
    rights_count.config(text='Correct  - ' + str(right))
    wrongs_count.config(text='Incorrect - ' + str(wrong))

    current_word.config(text= choice(word_list))
    next_word.config(text= choice(word_list))
    button.config(text='Try again')
    entry_field.delete(0, END)
    thread = threading.Thread(target=timer, args=('0:20', ))
    thread.start()



def end_test(*args, **kwargs):
    finish_score = Label(text=f'Correct char - {str(right_len)}\nIncorrect char - {str(wrong_len)}')
    finish_score.place(relx=0.5, rely=0.2, anchor='c', width=130, height=90)
    



def timer(time_value=str, *args, **kwargs):
    separator_index = time_value.find(':')
    seconds = int(time_value[:separator_index]) * 60 + int(time_value[separator_index + 1:])
    for sec in range(seconds, 0, -1):
        if sec < 10:
            time_label.config(text=f'0:0{str(sec)}')
        elif sec < 60:
            time_label.config(text=f'0:{str(sec)}')
        elif (sec - (sec // 60) * 60) < 10:
            time_label.config(text=f'{str(sec // 60)}:0{str(sec % 60)}')
        else:
            time_label.config(text=f'{str(sec // 60)}:{str(sec % 60)}')
        time.sleep(1)
    time_label.config(text='0:00')
    end_test()


def count_right_and_wrong(*args, **kwargs):
    global right, right_len
    global wrong, wrong_len
    if entry_field.get().replace(' ', '', 10) == current_word.cget('text'):
        right += 1
        right_len += len(current_word.cget('text'))
        rights_count.config(text='Correct - ' + str(right))
    else:
        wrong += 1
        wrong_len += len(current_word.cget('text'))
        wrongs_count.config(text='Incorrect - ' + str(wrong))

            

word_list = get_word_list()

# config window
window = Tk()
window.title('Speed typing test')
window.geometry('500x500')
#window.iconbitmap(r'icon.ico')


# config labels
current_word = Label(text='')
next_word = Label(text='')
time_label = Label(text='0:00')
wrongs_count = Label(text='0')
wrongs_len = Label(text='')
rights_count = Label(text='0')
rights_len = Label(text='')  
finish_score = Label(text='')


# config entry
word = StringVar()
entry_field = Entry(justify='center', textvariable=word)
entry_field.bind('<space>', lambda *args: set_new_words())


# config button
button = Button(text='Start', command= lambda: start_test())


# place elements
button.place(relx=0.5, rely=0.5, anchor='c', width=100, height=30)
entry_field.place(relx=0.5, rely=0.3, anchor='c', width=90, height=25)
current_word.place(relx=0.5, rely=0.4, anchor='c', width=100, height=15)
next_word.place(relx=0.7, rely=0.4, anchor='c', width=100, height=15)
time_label.place(relx=0.3, rely=0.4, anchor='c', width=25, height=15)
wrongs_count.place(relx=0.2, rely=0.6, anchor='c', width=100, height=15)
rights_count.place(relx=0.2, rely=0.7, anchor='c', width=100, height=15)


window.mainloop()