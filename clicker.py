'''
clicker game
make a gold counter
make a button
you earn gold for every click
when you have enough gold you can unlock new nodes to automatically generate gold!
'''


import functools
from ursina import *

app = Ursina()
window.color = color._20

gold = 0
counter = Text(text='0', y=.25, z=-1, scale=2, origin=(0,0), background=True)
button = Button(text='+', color=color.azure, scale= .125)

def button_click():
    print("Getting 1 gold")
    global gold
    gold += 1
    counter.text = str(gold)

button.on_click = button_click



button_2 = Button(cost=10, generate=1, x=.2, scale=.125, color=color.dark_gray, disabled=True)
button_2.tooltip = Tooltip(f'<gold>Gold Generator\n<default>Earn 1 gold every second.\nCosts {button_2.cost} gold.')

button_3 = Button(cost=50, generate=5, x=.4, scale=.125, color=color.light_gray, disabled=True)
button_3.tooltip = Tooltip(f'<gold>Huge Gold Generator\n<default>Earn 5 gold every second.\nCosts {button_3.cost} gold.')

button_4 = Button(cost=1000, generate=100, x=.6, scale=.125, color=color.gray, disabled=True)
button_4.tooltip = Tooltip(f'<gold>Ultra Gold Generator\n<default>Earn 100 gold every second.\nCosts {button_4.cost} gold.')

mines = [button_2, button_3, button_4]

def buy_auto_gold(button: Button):
    print("Want to buy auto gold")
    global gold
    print(f"I have {gold} gold")
    print(f"Cost is {button.cost} gold")
    if gold >= button.cost:
        print(button.cost)
        gold -= button.cost
        counter.text = str(gold)
        invoke(auto_generate_gold, button, 1)

for button in mines:
    button.on_click = functools.partial(buy_auto_gold, button)



def auto_generate_gold(button: Button, interval=1):
    global gold
    gold += button.generate
    counter.text = str(gold)
    button.animate_scale(.125 * 1.1, duration=.1)
    button.animate_scale(.125, duration=.1, delay=.1)
    invoke(auto_generate_gold, button, delay=interval)


def update():
    global gold
    for b in mines:
        if gold >= b.cost:
            b.disabled = False
            b.color = color.green
        else:
            b.disabled = True
            b.color = color.gray



app.run()