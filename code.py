

morse_code_dict = { 'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.',
                    'f':'..-.', 'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-',
                    'l':'.-..', 'm':'--', 'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-',
                    'r':'.-.', 's':'...', 't':'-', 'u':'..-', 'v':'...-', 'w':'.--',
                    'x':'-..-', 'y':'-.--', 'z':'--..',
                    '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.','0':'-----',
                    ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-',
                    ' ': '//'}




try:
    user_time = float(input('Enter a unit of time(0-1): '))
    user_input = input('Enter a sentence: ').lower()

except ValueError:
    print('enter an integer for time')


# filters user input to include only morse code elements
def clean_user_input(user_input, morse_code_dict):
    filtered_list = []
    for char in user_input:
        for key in morse_code_dict.keys():
            if char == key:
                filtered_list.append(char)

    return filtered_list


#convert filtered list characters to morse code
def convert_input(filtered_list, morse_code_dict):
    output_list = []
    for char in filtered_list:
        for key in morse_code_dict.keys():
            if char == key:
                if char == ' ':
                    output_list += ["//"]
                else:
                    converted_char = list(morse_code_dict.get(char))
                    for x in converted_char:
                        output_list.append(x)
                    output_list += ["/", "/", "/"]
    return output_list

import time
from adafruit_circuitplayground import cp

def display_neopixels(input, lapsed):
    cp.pixels.brightness = 0.15
    for char in input:
        if char == '.':
            cp.pixels.fill((255, 0, 0))
            time.sleep(lapsed)
            cp.pixels.fill((0, 0, 0))
            time.sleep(lapsed)
        elif char == '-':
            cp.pixels.fill((255, 0, 0))
            time.sleep(lapsed*3)
            cp.pixels.fill((0, 0, 0))
            time.sleep(lapsed)
        elif char == '/':
            cp.pixels.fill((0, 0, 0))
            time.sleep(lapsed)
        else:
            cp.pixels.fill((0, 0, 0))
            time.sleep(lapsed*7)



filtered_input = clean_user_input(user_input, morse_code_dict)
output = convert_input(filtered_input, morse_code_dict)
display_neopixels(output, user_time)


