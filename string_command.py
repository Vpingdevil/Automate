# coding: utf-8
import os
import re
from urllib.parse import quote as encoder


# create a list with all helping words
# Examples:  please, sorry etc
helping_words = ['please', 'but', 'sorry', "for", "me"]

# words for the command such as open, close, new file, new tab
functional_words = ['open', 'start', 'execute']
# custom apps: which can be opened with start command
custom_apps = ["chrome", "firefox", "atom", "pycharm", "notepad"]


def remove_words(command):
    for word in helping_words:
        if word in command:
            command.remove(word)


def remove_function(command):
    function_index = -1
    for function in functional_words:
        try:
            function_index = command.index(function)
            break
        except ValueError:
            pass
    return ' '.join(command[function_index + 1:])


def open_app(service):
    installed = False
    try:
        os.system("start " + service)
        installed = True

    except Exception as e:
        print(e.__str__())
        os.system(service)
        installed = True
    
    finally:
        if not installed:
            print("Unable to process command, try using different keywords")
        confirm = input(f"Type yes to show web results for {command} or press any other key to continue")
        if confirm or confirm in ["yes", "yeah", "yup"]:
            os.system("start www.google.com/search?q="+encoder(service))


def process(command):
    global custom_apps
    if all(["text" in command, "editor" in command]):
        return "text editor"

    for app in custom_apps:
        if app in command:
            return app

    remove_words(command)
    return remove_function(command)


if __name__ == '__main__':
    while True:
        in_command = input("what's your command?\n")
        command = in_command.lower().split()
        if any(["quit" in command, "exit" in command, "terminate" in command]):
            break
        command = process(command)
        if re.search(r"[\w\d-]+\.[\w]+(\.[\w]+)?", command):
            if "www" not in command:
                command = "www." + command
            print(command)
            os.system("start " + command)
            continue
        if re.search(r"^[\d+\-\*\/\%]+$", command):
            print(eval(command))
            continue

        open_app(command)
