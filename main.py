import random
from tkinter import *

MOST_COMMON_WORDS = ['the', 'of', 'to', 'and', 'a', 'in', 'is', 'it', 'you', 'that', 'he', 'was', 'for', 'on', 'are',
                     'with', 'as', 'I', 'his', 'they', 'be', 'at', 'one', 'have', 'this', 'from', 'or', 'had', 'by',
                     'hot', 'but', 'some', 'what', 'there', 'we', 'can', 'out', 'other', 'were', 'all', 'your', 'when',
                     'up', 'use', 'word', 'how', 'said', 'an', 'each', 'she', 'which', 'do', 'their', 'time', 'if',
                     'will', 'way', 'about', 'many', 'then', 'them', 'would', 'write', 'like', 'so', 'these', 'her',
                     'long', 'make', 'thing', 'see', 'him', 'two', 'has', 'look', 'more', 'day', 'could', 'go', 'come',
                     'did', 'my', 'sound', 'no', 'most', 'number', 'who', 'over', 'know', 'water', 'than', 'call',
                     'first', 'people', 'may', 'down', 'side', 'been', 'now', 'find', 'any', 'new', 'work', 'part',
                     'take', 'get', 'place', 'made', 'live', 'where', 'after', 'back', 'little', 'only', 'round', 'man',
                     'year', 'came', 'show', 'every', 'good', 'me', 'give', 'our', 'under', 'name', 'very', 'through',
                     'just', 'form', 'much', 'great', 'think', 'say', 'help', 'low', 'line', 'before', 'turn', 'cause',
                     'same', 'mean', 'differ', 'move', 'right', 'boy', 'old', 'too', 'does', 'tell', 'sentence', 'set',
                     'three', 'want', 'air', 'well', 'also', 'play', 'small', 'end', 'put', 'home', 'read', 'hand',
                     'port', 'large', 'spell', 'add', 'even', 'land', 'here', 'must', 'big', 'high', 'such', 'follow',
                     'act', 'why', 'ask', 'men', 'change', 'went', 'light', 'kind', 'off', 'need', 'house', 'picture',
                     'try', 'us', 'again', 'animal', 'point', 'mother', 'world', 'near', 'build', 'self', 'earth',
                     'father', 'head', 'stand', 'own', 'page', 'should', 'country', 'found', 'answer', 'school', 'grow',
                     'study', 'still', 'learn', 'plant', 'cover', 'food', 'sun', 'four', 'thought', 'let', 'keep',
                     'eye', 'never', 'last', 'door', 'between', 'city', 'tree', 'cross', 'since', 'hard', 'start',
                     'might', 'story', 'saw', 'far', 'sea', 'draw', 'left', 'late', 'run', "don't", 'while', 'press',
                     'close', 'night', 'real', 'life', 'few', 'stop', 'open', 'seem', 'together', 'next', 'white',
                     'children', 'begin', 'got', 'walk', 'example', 'ease', 'paper', 'often', 'always', 'music',
                     'those', 'both', 'mark', 'book', 'letter', 'until', 'mile', 'river', 'car', 'feet', 'care',
                     'second', 'group', 'carry', 'took', 'rain', 'eat', 'room', 'friend', 'began', 'idea', 'fish',
                     'mountain', 'north', 'once', 'base', 'hear', 'horse', 'cut', 'sure', 'watch', 'color', 'face',
                     'wood', 'main', 'enough', 'plain', 'girl', 'usual', 'young', 'ready', 'above', 'ever', 'red',
                     'list', 'though', 'feel', 'talk', 'bird', 'soon', 'body', 'dog', 'family', 'direct', 'pose',
                     'leave', 'song', 'measure', 'state', 'product', 'black', 'short', 'numeral', 'class', 'wind',
                     'question', 'happen', 'complete', 'ship', 'area', 'half', 'rock', 'order', 'fire', 'south',
                     'problem', 'piece', 'told', 'knew', 'pass', 'farm', 'top', 'whole', 'king', 'size', 'heard',
                     'best', 'hour', 'better', 'TRUE', 'during', 'hundred', 'am', 'remember', 'step', 'early', 'hold',
                     'west', 'ground', 'interest', 'reach', 'fast', 'five', 'sing', 'listen', 'six', 'table', 'travel',
                     'less', 'morning', 'ten', 'simple', 'several', 'vowel', 'toward', 'war', 'lay', 'against',
                     'pattern', 'slow', 'center', 'love', 'person', 'money', 'serve', 'appear', 'road', 'map',
                     'science', 'rule', 'govern', 'pull', 'cold', 'notice', 'voice', 'fall', 'power', 'town', 'fine',
                     'certain', 'fly', 'unit', 'lead', 'cry', 'dark', 'machine', 'note', 'wait', 'plan', 'figure',
                     'star', 'box', 'noun', 'field', 'rest', 'correct', 'able', 'pound', 'done', 'beauty', 'drive',
                     'stood', 'contain', 'front', 'teach', 'week', 'final', 'gave', 'green', 'oh', 'quick', 'develop',
                     'sleep', 'warm', 'free', 'minute', 'strong', 'special', 'mind', 'behind', 'clear', 'tail',
                     'produce', 'fact', 'street', 'inch', 'lot', 'nothing', 'course', 'stay', 'wheel', 'full', 'force',
                     'blue', 'object', 'decide', 'surface', 'deep', 'moon', 'island', 'foot', 'yet', 'busy', 'test',
                     'record', 'boat', 'common', 'gold', 'possible', 'plane', 'age', 'dry', 'wonder', 'laugh',
                     'thousand', 'ago', 'ran', 'check', 'game', 'shape', 'yes', 'hot', 'miss', 'brought', 'heat',
                     'snow', 'bed', 'bring', 'sit', 'perhaps', 'fill', 'east', 'weight', 'language', 'among']


def start_testing():
    global rewrite_text
    rewrite_text = ""
    for _ in range(100):
        rewrite_text += f"{random.choice(MOST_COMMON_WORDS)} "

    canvas.itemconfig(text_area, text=f"{rewrite_text}", width=800)
    start.grid_forget()
    global text_input
    text_input = Text()
    text_input.grid(column=0, row=1)
    text_input.focus()
    window.after(60000, check_speed)


def check_speed():
    text_to_score = text_input.get("1.0", END)
    list_text_to_score = text_to_score.split(" ")
    list_rewrite_text = rewrite_text.split(" ")
    typos = 0
    index = 0
    for _ in list_text_to_score:
        if list_text_to_score[index] != list_rewrite_text[index]:
            typos += 1
        index += 1
    canvas.itemconfig(text_area, text=f"Your typing speed is {len(list_text_to_score)} words per minute."
                                      f"\nNumber of typos you made: {typos}.")
    text_input.grid_forget()
    start.grid(column=0, row=1)


window = Tk()

window.title("Type Speed Tester")
window.config(padx=20, pady=20)

canvas = Canvas(width=800, height=200)
text_area = canvas.create_text(400, 100, width=250, font=("Arial", 12, "bold"), fill="black", justify='center',
                               text='How fast can you type?\nPress "Start" button to start the timer, '
                                    'then write the words below.')
canvas.grid(column=0, row=0)

start = Button(text='Start', command=start_testing)
start.grid(column=0, row=1, pady=10)

window.mainloop()
