# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    figuras = [
        {'nome': 'aaa', 'caracteristicas': [1, 2, 3]},
        {'nome': 'vvv', 'caracteristicas': [3, 2]},
        {'nome': 'bbb', 'caracteristicas': [5, 2, 1]},
        {'nome': 'ttt', 'caracteristicas': [6, 1, 6, 7, 8]},
    ]

    print(figuras[0]['caracteristicas'][0])

    '''  for figura in figuras:
        # figurinha é um dicionario
        print(figura['nome'])
        for caracteristica in figura['caracteristicas']:
            print(caracteristica)
    '''

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
