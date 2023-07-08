import sys
class color_print():
    green = "\033[1;32m"
    blue = "\033[1;34m"
    yellow = "\033[1;33m"
    red = "\033[1;31m"
    purple = "\033[1;35m"
    def  print_green(self,text):
        print(self.green + text + "\033[0m")
    def print_blue(self,text):
        print(self.blue + text + "\033[0m")
    def print_yellow(self,text):
        print(self.yellow + text + "\033[0m")
    def print_red(self, text):
        print(self.red + text + "\033[0m")
    def print_purple(self,text):
        print(self.purple + text + "\033[0m")

    def print_Binline(self, text):
        print(self.blue + text + "\033[0m", end='\r')
        sys.stdout.flush()
    def print_Rinline(self, text):
        print(self.red + text + "\033[0m", end='\r')
        sys.stdout.flush()
    def print_Ginline(self, text):
        print(self.green + text + "\033[0m", end='\r')
        sys.stdout.flush()