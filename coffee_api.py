import requests

error_string = 'Invalid Coffee\nPlease refer to list below\n\ncaffè macchiato\ncortado\ncafé au lait\ncold brew'


def coffee(coffee_type):
    # All statistics are found using the coffee API https://github.com/JACKZHENGELA/Coffee-Server.git
    return requests.get(f'http://10.6.21.80:8000/coffee_stock/{coffee_type}?api_key=071113', auth=('user', 'pass')).json()


def stock(coffee_type=None):
    if coffee_type is None:
        return 'invalid'
    else:
        return coffee(coffee_type)['stock']


def ranking(coffee_type=None):
    if coffee_type is None:
        return 'invalid'
    else:
        return coffee(coffee_type)['ranking']

run = True
while run:
    answer = input('Would you like to find the ranking or the stock of a coffee?\nR = Ranking\nS = Stock\n >> ').lower()
    if answer == 'r':
        answer = input('What coffee\'s ranking would you like to find?\ncold brew, black, latte\n\n >> ').lower()
        if ranking(answer) != 'invalid':
            print(f'The ranking of {answer} is {ranking(answer)}')
        else:
            print('That is a invalid coffe type')
    if answer == 's':
        answer = input('What coffee\'s stock would you like to find?\ncold brew, black, latte\n >> ').lower()
        if ranking(answer) != 'invalid':
            print(f'There are stock {stock(answer)} {answer}s available')
        else:
            print('That is a invalid coffe type')
