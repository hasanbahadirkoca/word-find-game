import os # Import os module for get os language
import json # Import json module for json file

TRANSLATION_FILE = "translate.json" # Set the translation file path
SIZE = 80


def clear_screen(): # Clear screen function 
    print("\033c", end="")

def get_screen_size(): # Get screen size function 
    return os.get_terminal_size().columns

def get_os_lang(): # Get language code from os function 
    return os.environ['LANG'].split('_')[0]

class GetTranslations: # Class for get translations
    
    # Functions for get file path and language code
    def __init__(self, file_path, lang_code=get_os_lang()):
        self.lang_code = lang_code
        self.file_path = file_path

    # Function for get translations from file
    def get_translation(self, param):
        with open(self.file_path, 'r') as file:
            data = file.read()
            data = json.loads(data)
            return data[self.lang_code][param]

def set_color(color="default"): # Set color function
    if 'green':
        print('\033[1;32m', end='')
    elif 'red':
        print('\033[1;31m', end='')
    elif 'yellow':
        print('\033[1;33m', end='')
    elif 'blue':
        print('\033[1;34m', end='')
    elif 'purple':
        print('\033[1;35m', end='')
    elif 'cyan':
        print('\033[1;36m', end='')
    elif 'white':
        print('\033[1;37m', end='')
    elif 'default':
        print('\033[0m', end='')

def print_blank(unit=1): # Print blank line function
    for i in range(unit):
        print('')

def print_line(): # Print line function
    set_color("green")
    print(('#' * SIZE).center(get_screen_size())) # Print line
    set_color("default")

def print_border(text=""): # Print border function
    if not len(text) % 2 == 0: # Check if text length is even
        text += ' ' # Add space to text
    
    characters = len(text) + 2 # Get text length
    space = ' ' * (int((SIZE - characters)/2)) # Set space
    
    set_color("green")
    screen_size = get_screen_size() # Get screen size
    print(('#' + space + text + space + '#').center(screen_size)) # Print border
    set_color("default")

def print_header(): # Print header function
    TITLE = translation.get_translation('title') # Get title from translation file
    set_color("green")
    print_line() # Print line
    print_border() # Print border
    print_border(TITLE) # Print border with title
    print_border()
    print_line()
    set_color("default")
    

def print_lines(word): # Print lines for word function
    word_length = len(word) # Get word length
    set_color("red")
    lines = " ____ " * word_length # Set lines
    print(lines.center(get_screen_size(), ' '))



if __name__ == '__main__': # Main function
    clear_screen() # Clear screen
    translation = GetTranslations(TRANSLATION_FILE) # Get translations
    print_header() # Print header
    print_lines("hasan") # Print lines

