import os
import sys


def read_data(file_name):
    text = ''
    if file_name == 'bloomberg':
        text = bloomberg_com
    elif file_name == 'nytimes':
        text = nytimes_com
    return text


def get_file_name(url):
    fn = url.replace('https://', '')
    fn = fn.rsplit('.')
    return '_'.join(fn[:-1])


def write_data(data, f_name):
    # f_name = get_file_name(url)
    path = dir_name + '/' + f_name
    if not os.path.exists(path):
        with open(path, 'w', encoding='utf-8') as file:
            file.write(data)
    if not f_name in files:
        files.append(f_name)
    print(data)


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

dir_name = sys.argv[1]
files = []
sites = ["bloomberg.com", "nytimes.com"]
file_name = ''

if not os.path.exists(dir_name):
    os.mkdir(dir_name)

while True:
    cmd = input()
    if cmd == 'exit':
        break
    if cmd in files:
        content = read_data(cmd)
        print(content)
        continue
    if cmd not in sites:
        print("Error: Incorrect URL")
        continue

    file_name = get_file_name(cmd)

    content = read_data(file_name)
    # text = '\n'.join([s for s in content.split('\n') if s])
    write_data(content, file_name)

