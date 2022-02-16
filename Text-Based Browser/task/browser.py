import os
import sys
import requests
from bs4 import BeautifulSoup
from colorama import Fore


def read_data(file_name):
    pref = 'https://'
    if pref in file_name:
        url = file_name
    else:
        url = pref + file_name
    try:
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                     "Chrome/70.0.3538.77 Safari/537.36"
        r = requests.get(url, headers={'User-Agent': user_agent})
        soup = BeautifulSoup(r.content, 'html.parser')

        for tag in soup.find_all('a'):
            a_text = str(tag.text.strip())
            if a_text:
                tag.string = Fore.BLUE + tag.text + Fore.RESET

        content = soup.find_all(tags)
        text = ''
        for s in content:
            s1 = s.text.strip()
            if s1:
                text += s1 + '\n'
        return text
    except requests.exceptions.ConnectionError:
        print("Incorrect URL")
        return ""


def get_file_name(url):
    fn = url.replace('https://', '')
    fn = fn.rsplit('.')
    return '_'.join(fn[:-1])


def write_data(data, url):
    f_name = get_file_name(url)
    path = dir_name + '/' + f_name
    if not os.path.exists(path):
        with open(path, 'w', encoding='utf-8') as file:
            file.write(data)
    if not f_name in files:
        files.append(f_name)
    print(data)


dir_name = sys.argv[1]
files = []
stack = []
file_name = ''
current_name = ''
tags = ['p', 'a', 'h1', 'h2', 'ul', 'ol', 'li']
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

while True:
    cmd = input()
    if cmd == 'exit':
        break
    if cmd == 'back':
        if stack:
            file_name = stack.pop()
        else:
            continue
    else:
        current_name = file_name
        file_name = cmd

    content = read_data(file_name)

    if current_name and file_name != current_name:
        stack.append(current_name)
    text = '\n'.join([s for s in content.split('\n') if s])
    write_data(content, file_name)

