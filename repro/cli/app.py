from repro.config import GREETING, SUBJECT


def greet():
    print(f'{GREETING}, {SUBJECT}!')


if __name__ == '__main__':
    greet()
