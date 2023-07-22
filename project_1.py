"""
project_1.py: první projekt do Engeto Online Python Akademie

author: Václav Zmuda
email: vaclav.zmuda@gmail.com
discord: vaclav5301
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]


USERS = {
    "bob": "123", 
    "ann": "pass123", 
    "mike": "password123", 
    "liz": "pass123"
}

separator = 40 * "="

title = 0
upper = 0
lower = 0
numeric = 0
numeric_total = 0

graph_value = {}

print("Welcome to our text analazer. Please log in.")
# žádost přihlášení

username = input("username: ").lower()
password = input("password: ")

#ověření přihlášení
if username not in USERS or password != USERS[username]:

    #pokud není registrovaný, upozorni jej a ukonči program
    print("unregistered user or wrong password, terminating the program...")
    exit()
#pokračování po přihlášení

print(separator)
print(f"Welcome to the app, {username}") 
print(f"We have 3 texts to be analyzed.\n{separator}")

#Výběr textu
choice = input("Enter a number btw. 1 and 3 to select: ")

#Ověření vstupních dat
if not choice.isdigit() or not(int(choice)-1 in range(len(TEXTS))):
    print("Your choice is not correct, terminating the program...")
    exit()

#pročištění textu
select_text = TEXTS[int(choice)-1]
translate_table = select_text.maketrans(",-", "  ", ".")
clear_list = select_text.translate(translate_table).split()

for word in clear_list:
    #hodnoty pro graf
    len_word = len(word)
    if len_word in graph_value:
        graph_value[len_word] += 1
    else:
        graph_value[len_word] = 1
    
    #počet slov s prvním velkým písmenem
    if word.istitle():
        title += 1
    
    #počet slov velkými písmeny
    elif word.isupper():
        upper += 1
    
    #počet slov malými písmeny
    elif word.islower():
        lower += 1
    
    #počet čísel 
    #sumu všech čísel v textu
    elif word.isnumeric():
        numeric += 1
        numeric_total += int(word)

print(separator)

# textová statistika
print(f"There are {len(clear_list)} words in the selected text.")    

#výpis ostatních statistik
print(f"There are {title} titlecase words.")
print(f"There are {upper} uppercase words.")
print(f"There are {lower} lowercase words.")
print(f"There are {numeric} numeric strings.")
print(f"The sum of all the numbers {numeric_total}.\n{separator}")  

#šířka pro sloupcový graf
if len("LEN") > len(str(sorted(graph_value.keys()).pop())):
    max_len = len("LEN")
else:
    max_len = len(str(sorted(graph_value.keys()).pop()))        

if len("OCCURENCES") > sorted(graph_value.values()).pop():
    max_number = len("OCCURENCES") + 2
else:
    max_number = sorted(graph_value.values()).pop() + 2

#hlavička grafu
print(f"{'LEN':>{max_len}}|{'OCCURENCES':^{max_number}}|number.\n{separator}")

#vytvoření grafu
for key, value in sorted(graph_value.items()):
    print(f"{key:>{max_len}}|{'*'*value:<{max_number}}|{value}")
