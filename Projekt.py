import requests
from bs4 import BeautifulSoup
from lxml import etree


def filter(column, from_value, to_value):
    x = 0
    for row in rows:
        if 0 < x < len(rows) - 1:
            text_from_table = row.findAll('td')[column].text
            list = [int(s) for s in text_from_table.split() if s.isdigit()]
            number = int(list[0])
            if from_value <= number <= to_value:
                print(club_names[x - 1])
        x = x + 1


def filterLastColumn(from_value, to_value):
    x = 0
    for row in rows:
        if 0 < x < len(rows) - 2:
            number = int(row.findAll('td')[15].text[:-2])
            if from_value <= number <= to_value:
                print(club_names[x - 1])
        x = x + 1


print('Witaj w wyszukiwarce klubów wszech czasów najwyższej polskiej ligi piłkarskiej! :)')
print('')

print('Ładowanie klubów...')

try:
    website_url = requests.get(
        'https://pl.wikipedia.org/wiki/Tabela_wszech_czas%C3%B3w_Ekstraklasy_w_pi%C5%82ce_no%C5%BCnej').text
    soup = BeautifulSoup(website_url, 'html.parser')
    main_table = soup.find('table', {'class': 'wikitable sortable'})
    rows = main_table.findAll('tr')

    i = 0
    club_names = []
    for row in rows:
        if i > 0:
            club_name = row.findAll('td')[1].text[:-1]
            club_names.append(club_name)
        i = i + 1

    print('')

    print('Wybierz interesujące Cię kryterium wpisując odpowiedni numer opcji:')
    print('1 - liczba sezonów rozegranych w Ekstraklasie')
    print('2 - liczba zdobytych tytułów')
    print('3 - ilość rozegranych meczy')
    print('4 - ilość zdobytych punktów')
    print('5 - ilość zwycięstw')
    print('6 - ilość remisów')
    print('7 - ilość porażek')
    print('8 - ilość strzelonych bramek')
    print('9 - ilość straconych bramek')
    print('10 - najwyższa pozycja w lidze')
    print('11 - rok założenia klubu')

    option = input()

    print('Podaj liczbowy zakres:')

    print('Od:')
    from_value = int(input())
    print('Do:')
    to_value = int(input())
    if to_value < from_value:
        print('Liczba DO nie może być mniejsza niż liczba OD!!!')
    else:
        print('')
        print('Przetwarzanie zapytania...')
        print('')
        if option == '1':
            column = 2
            filter(column, from_value, to_value)
        elif option == '2':
            column = 3
            filter(column, from_value, to_value)
        elif option == '3':
            column = 4
            filter(column, from_value, to_value)
        elif option == '4':
            column = 5
            filter(column, from_value, to_value)
        elif option == '5':
            column = 6
            filter(column, from_value, to_value)
        elif option == '6':
            column = 8
            filter(column, from_value, to_value)
        elif option == '7':
            column = 9
            filter(column, from_value, to_value)
        elif option == '8':
            column = 11
            filter(column, from_value, to_value)
        elif option == '9':
            column = 12
            filter(column, from_value, to_value)
        elif option == '10':
            filterLastColumn(from_value, to_value)
        elif option == '11':
            links = main_table.findAll('a')
            id = 0
            for link in links:
                try:
                    link2 = 'https://pl.wikipedia.org' + link.get('href')
                    if 'cite' not in str(link2):
                        number = 0
                        if '%C5%81TSG_%C5%81%C3%B3d%C5%BA' in link2:
                            number = 1908
                        elif 'Lechia_Gda%C5%84sk_(pi%C5%82ka_no%C5%BCna)' in link2:
                            number = 1995
                        else:
                            req = requests.get(link2)
                            store = etree.HTML(req.text)
                            output = store.xpath(
                                '//table[@class="infobox"]/tbody/tr[td[1]/text()="Data\xa0założenia\n"]/td[2]')
                            try:
                                year_text = output[0].text
                                if year_text is None:
                                    output = store.xpath(
                                        '//table[@class="infobox"]/tbody/tr[td[1]/text()="Data\xa0założenia\n"]/td[2]/a[last()]')
                                    year_text = output[0].text
                                    if len(year_text) == 11:
                                        year_text = year_text[-5:]
                                    list = [int(s) for s in year_text.split() if s.isdigit()]
                                    number = int(list[0])
                                else:
                                    if len(year_text) == 11:
                                        year_text = year_text[-5:]
                                    try:
                                        list = [int(s) for s in year_text.split() if s.isdigit()]
                                        number = int(list[-1])
                                    except Exception as err:
                                        output = store.xpath(
                                            '//table[@class="infobox"]/tbody/tr[td[1]/text()="Data\xa0założenia\n"]/td[2]/a')
                                        year_text = output[0].text
                                        list = [int(s) for s in year_text.split() if s.isdigit()]
                                        number = int(list[-1])
                            except Exception as err:
                                output = store.xpath(
                                    '//table[@class="infobox"]/tbody/tr[td[1]/text()="Data założenia\n"]/td[2]')
                                try:
                                    year_text = output[0].text
                                    list = [int(s) for s in year_text.split() if s.isdigit()]
                                    number = int(list[0])
                                except Exception as err:
                                    pass
                        if from_value <= number <= to_value:
                            print(club_names[id])
                        id = id + 1
                except Exception as err2:
                    continue
        else:
            print('Nie ma takiego kryterium!!!')
except Exception as err:
    print('Wystąpił nieoczekiwany błąd!!!', err)
print()
print('Koniec programu')
