from os import system, name
from random import randint
import keyboard

DIFF_MENU = ('Easy', 'Medium', 'Hard', 'Back to Main Menu', ' CHOOSE DIFFICULTY ')
MAIN_MENU = ('Play game', 'Choose difficulty', 'Instructions', 'Exit game', ' MAIN MENU ')
SECONDARY_MENU = ('Play again', 'Back to Main Menu', 'Exit game', ' MENU ')
INSTRUCTIONS_MENU = ('Back to Main Menu', 'Exit game', ' MENU ')
EASY = 4
MEDIUM = 5
HARD = 6

global numbers
numbers = []


def main_title():
  clear_screen()
  print(
"""···················································
:      _   _                 _                    :
:     | \ | |_   _ _ __ ___ | |__   ___ _ __      :
:     |  \| | | | | '_ ` _ \| '_ \ / _ \ '__|     :
:     | |\  | |_| | | | | | | |_) |  __/ |        :
:     |_| \_|\__,_|_| |_| |_|_.__/ \___|_|        :
:    ____ _           _ _                         :
:   / ___| |__   __ _| | | ___ _ __   __ _  ___   :
:  | |   | '_ \ / _` | | |/ _ \ '_ \ / _` |/ _ \  :
:  | |___| | | | (_| | | |  __/ | | | (_| |  __/  :
:   \____|_| |_|\__,_|_|_|\___|_| |_|\__, |\___|  :
:                                    |___/        :
···················································
"""
  )


def secondary_title():
  clear_screen()
  print(
"""···················································
: ┌┐┌┬ ┬┌┬┐┌┐ ┌─┐┬─┐  ┌─┐┬ ┬┌─┐┬  ┬  ┌─┐┌┐┌┌─┐┌─┐ :
: ││││ ││││├┴┐├┤ ├┬┘  │  ├─┤├─┤│  │  ├┤ ││││ ┬├┤  :
: ┘└┘└─┘┴ ┴└─┘└─┘┴└─  └─┘┴ ┴┴ ┴┴─┘┴─┘└─┘┘└┘└─┘└─┘ :
···················································
"""
  )


def print_instructions():
  print('-=-'*17)
  print(
"""
Instructions here!
"""
)
  print('-=-'*17)
  print()


def print_difficultys():
  diff_levels = {
    EASY: 'Easy',
    MEDIUM: 'Medium',
    HARD: 'Hard'
  }

  print('-=-'*17)
  print(
f"""
           Easy   = Sequence of \033[1m{EASY}\033[m numbers
           Medium = Sequence of \033[1m{MEDIUM}\033[m numbers 
           Hard   = Sequence of \033[1m{HARD}\033[m numbers
"""
)
  difficulty = diff_levels.get(len(numbers))
  print(f'             Currently difficulty: {difficulty}')
  print('-=-'*17)
  print()


def print_scoreboard():
  print('-=-'*17)
  print(
"""
Scoreboard here!
"""
)
  print('-=-'*17)
  print()


def clear_screen():
  system('cls' if name == 'nt' else 'clear')


def draw_numbers(difficulty):
  global numbers
  numbers = []
  for i in range(difficulty):
    numbers.append(randint(1,9))
    if i == difficulty - 1:
      print(numbers[i])
    else:
      print(numbers[i], end='')


def print_menu(menu, selected):
  if not menu == MAIN_MENU:
    secondary_title()
    if menu == INSTRUCTIONS_MENU:
      print_instructions()
    elif menu == DIFF_MENU:
      print_difficultys()
    elif menu == SECONDARY_MENU:
      print_scoreboard()
  else:
    main_title()
  
  print(f'{menu[-1]:=^51}')
  for i, option in enumerate(menu):
    if i == selected:
      print(f'\033[1m  {option:^47}  \033[m')
    elif not i == len(menu) - 1:
      print(f'  {option:^47}  ')
  print('='*51)

  for i, number in enumerate(numbers):
    print(number, end='')



def get_pressioned_key(menu):
  selected = 0

  print_menu(menu, selected)

  while True:
    event = keyboard.read_event(suppress=True)
    if event.event_type == 'down':
      size = len(menu) - 1
      if event.name == 'up':
        selected = (selected - 1) % size
        print_menu(menu, selected)
      elif event.name == 'down':
        selected = (selected + 1) % size
        print_menu(menu, selected)
      elif event.name == 'enter':
        return menu[selected] 


def choice_processement(choice):
  menus = {
    'main': MAIN_MENU,
    'difficulty': DIFF_MENU,
    'secondary': SECONDARY_MENU,
    'instructions': INSTRUCTIONS_MENU
  }

  for name, menu in menus.items():
    if choice in menu:
      which_menu = name
      break

  if which_menu == 'main':
    if choice == 'Play game':
      return 'Você escolheu Play game'
    elif choice == 'Choose difficulty':
      choice = get_pressioned_key(DIFF_MENU)
      return choice_processement(choice)
    elif choice == 'Instructions':
      choice = get_pressioned_key(INSTRUCTIONS_MENU)
      return choice_processement(choice)
    elif choice == 'Exit game':
      main_title()
      print('Até logo!')
      return

  elif which_menu == 'difficulty':
    if choice == 'Easy':
      draw_numbers(EASY)
      choice = get_pressioned_key(DIFF_MENU)
      return choice_processement(choice)
    elif choice == 'Medium':
      draw_numbers(MEDIUM)
      choice = get_pressioned_key(DIFF_MENU)
      return choice_processement(choice)
    elif choice == 'Hard':
      draw_numbers(HARD)
      choice = get_pressioned_key(DIFF_MENU)
      return choice_processement(choice)
    elif choice == 'Back to Main Menu':
      choice = get_pressioned_key(MAIN_MENU)
      return choice_processement(choice)
    
  elif which_menu == 'secondary':
    if choice == 'Play again':
      return 'Você escolheu Play again'
    elif choice == 'Back to Main Menu':
      choice = get_pressioned_key(MAIN_MENU)
      return choice_processement(choice)
    elif choice == 'Exit game':
      main_title()
      print('Obrigado por jogar! Até logo!')
      return
  
  elif which_menu == 'instructions':
    if choice == 'Back to Main Menu':
      choice = get_pressioned_key(MAIN_MENU)
      return choice_processement(choice)
    elif choice == 'Exit game':
      main_title()
      print('Até logo!')
      return
  return


def run():
  main_title()
  draw_numbers(EASY)
  choice = get_pressioned_key(MAIN_MENU)
  print(choice_processement(choice))
  print(numbers)


if __name__ == '__main__':
  run()