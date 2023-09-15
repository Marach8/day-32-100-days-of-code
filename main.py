list = ['Good morning!', 'Bonjour!', '¿Qué tal?', 'Zdravstvuyte!', 'Nǐn hǎo!', 'Salve!', 'Konnichiwa!', 'Guten Tag!', 'Olá!', 'Anyoung haseyo!']
import random
a = random.randint(0, 10)
print(f'\033[1;33m{list[a]:^50}.')