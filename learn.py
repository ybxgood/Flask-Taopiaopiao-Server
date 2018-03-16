

def play(f):
    def sleep():
        print('sleep  sleep')
        f()
        print('gogogo')
    return sleep



def game():
    print('chiji')


if __name__ == '__main__':
    g = play(game)
    g()





