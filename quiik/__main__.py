import sys, os
from quiik import *
from argparse import ArgumentParser
from time import time
from fabulous.text import Text

parser = ArgumentParser()
parser.add_argument('-rk', '--righty-keys', help='Use IJKL instead of WASD for keys.', default=False, action='store_true')
parser.add_argument('-sm', '--skip-menu', help='Skip Intro', default=False, action='store_true')
args = parser.parse_args()

def main():
    try:
        game = Game(args.righty_keys)
        game.start_screen()
        while True:
            key = game.random_key()
            game.display_random_key(key)
            start = time()
            over = False
            while time() - start <  1:
                start1 = time()
                if wait_key() == key:
                    if (time() - start1) > 1:
                        over = True
                        break
                    else:
                        game.score += 1
                        over = False
                        break
                else:
                    over = True
                    break
                over = True
            if over:
                    break
        if 'win32' in sys.platform or 'win64' in sys.platform:
                os.system('cls')
        else:
            os.system('clear')
        if game.end_screen():
            main()
        else:
            pass
    except KeyboardInterrupt:
        print(Text('Goodbye!', color='#%02X%02X%02X' % (255, 50, 50), shadow=True))


def start():
    try:
        gamer = Game(args.righty_keys)
        if args.skip_menu == False:
            gamer.display_menu()
        main()
    except KeyboardInterrupt:
        print(Text('Goodbye!', color='#%02X%02X%02X' % (255, 50, 50), shadow=True))

if __name__ == "__main__":
    try:
        start()
    except KeyboardInterrupt:
        print(Text('Goodbye!', color='#%02X%02X%02X' % (255, 50, 50), shadow=True))