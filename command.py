import unittest, random
from string_command import remove_words, remove_function, process


class MyTestCase(unittest.TestCase):
    def test_chrome(self):
        command = "can you please open chrome for me".split()
        app = process(command)
        return self.assertEqual(app, "chrome")

    def test_text_editor(self):
        command = "Open text editor".split()
        app = process(command)
        return self.assertEqual(app, "text editor")

    def test_custom_apps(self):
        com = ["can you please open ", "open for me ", "start new ", "i need ", "start ", "need to work on "]
        apps = ["chrome", "firefox", "atom", "notepad", "pycharm"]
        app_arg = random.choice(apps)
        command = (random.choice(com) + app_arg).split()
        app = process(command)
        return self.assertEqual(app, app_arg)


if __name__ == '__main__':
    unittest.main()
