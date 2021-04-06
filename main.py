import os
import sys
import requests
from bs4 import BeautifulSoup
from colorama import Fore

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

websites = {'bloomberg.com': bloomberg_com, 'nytimes.com': nytimes_com}
args = sys.argv
dir_name = args[1]
stack = []
tags = ["p", 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li']
try:
    os.mkdir(dir_name)
except FileExistsError:
    print('Error: File already exists')


def main(url):
    if '.' in url:
        if url.startswith('https://') == False:
            url = 'https://' + url
        r = requests.get(url)
        if r:
            soup = BeautifulSoup(r.text, 'html.parser')
            page = ''
            for tag in soup.find_all(tags):
                if tag.find('a'):
                    page += (Fore.BLUE + tag.get_text())
                else:
                    page += tag.text.strip()
            try:
                with open(f"./{dir_name}/{url[9:url.rfind('.')]}", 'w') as f2:
                    f2.write(page)
                    print(page)
            except KeyError:
                print('error')
    else:
        try:
            with open(f"./{dir_name}/{url}", 'r') as f2:
                f2.read()
            print(f2)
        except FileNotFoundError:
            print('error')


while True:
    user_input = input()
    if user_input == 'exit':
        break
    elif user_input == 'back':
        if stack != []:
            stack.pop()
            main(stack.pop())
    else:
        stack.append(user_input)
        main(user_input)


