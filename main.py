from sequance import SquareSequence as ss


def main():
    print('Enter (e) to exit loop')
    print('To continue, press [ENTER]')
    cont = ''
    while cont == '' or cont != 's':
        sequance = ss()
        sequance.print_equation()
        x = sequance.sequance_handler()
        print(x)

        print('\nStop or continue?')
        cont = input('>>>')


if __name__ == '__main__':
    main()
