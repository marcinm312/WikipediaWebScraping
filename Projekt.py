import requests
from bs4 import BeautifulSoup
from lxml import etree


def filtruj(kolumna, od, do):
    x = 0
    for row in rows:
        if 0 < x < len(rows) - 1:
            tekst = row.findAll('td')[kolumna].text
            list = [int(s) for s in tekst.split() if s.isdigit()]
            number = int(list[0])
            if od <= number <= do:
                print(nazwy_klubow[x - 1])
        x = x + 1


def filtrujOstatniaKolumne(od, do):
    x = 0
    for row in rows:
        if 0 < x < len(rows) - 2:
            number = int(row.findAll('td')[15].text[:-2])
            if od <= number <= do:
                print(nazwy_klubow[x - 1])
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
    nazwy_klubow = []
    for row in rows:
        if i > 0:
            nazwa_klubu = row.findAll('td')[1].text[:-1]
            nazwy_klubow.append(nazwa_klubu)
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

    kryterium = input()

    print('Podaj liczbowy zakres:')

    print('Od:')
    od = int(input())
    print('Do:')
    do = int(input())
    if do < od:
        print('Liczba DO nie może być mniejsza niż liczba OD!!!')
    else:
        print('')
        print('Przetwarzanie zapytania...')
        print('')
        if kryterium == '1':
            kolumna = 2
            filtruj(kolumna, od, do)
        elif kryterium == '2':
            kolumna = 3
            filtruj(kolumna, od, do)
        elif kryterium == '3':
            kolumna = 4
            filtruj(kolumna, od, do)
        elif kryterium == '4':
            kolumna = 5
            filtruj(kolumna, od, do)
        elif kryterium == '5':
            kolumna = 6
            filtruj(kolumna, od, do)
        elif kryterium == '6':
            kolumna = 8
            filtruj(kolumna, od, do)
        elif kryterium == '7':
            kolumna = 9
            filtruj(kolumna, od, do)
        elif kryterium == '8':
            kolumna = 11
            filtruj(kolumna, od, do)
        elif kryterium == '9':
            kolumna = 12
            filtruj(kolumna, od, do)
        elif kryterium == '10':
            filtrujOstatniaKolumne(od, do)
        elif kryterium == '11':
            links = main_table.findAll('a')
            id = 0
            for link in links:
                try:
                    link2 = 'https://pl.wikipedia.org' + link.get('href')
                    if 'cite' not in str(link2):
                        number = 0
                        if '%C5%81TSG_%C5%81%C3%B3d%C5%BA' in link2:
                            number = 1908
                        elif 'Lechia/Olimpia_Gda%C5%84sk' in link2:
                            number = 1995
                        else:
                            req = requests.get(link2)
                            store = etree.fromstring(req.text)
                            output = store.xpath(
                                '//table[@class="infobox"]/tbody/tr[td[1]/text()="Data\xa0założenia\n"]/td[2]')
                            try:
                                rok_surowy = output[0].text
                                if rok_surowy is None:
                                    output = store.xpath(
                                        '//table[@class="infobox"]/tbody/tr[td[1]/text()="Data\xa0założenia\n"]/td[2]/a[last()]')
                                    rok_surowy = output[0].text
                                    if len(rok_surowy) == 11:
                                        rok_surowy = rok_surowy[-5:]
                                    list = [int(s) for s in rok_surowy.split() if s.isdigit()]
                                    number = int(list[0])
                                else:
                                    if len(rok_surowy) == 11:
                                        rok_surowy = rok_surowy[-5:]
                                    try:
                                        list = [int(s) for s in rok_surowy.split() if s.isdigit()]
                                        number = int(list[-1])
                                    except Exception as err:
                                        output = store.xpath(
                                            '//table[@class="infobox"]/tbody/tr[td[1]/text()="Data\xa0założenia\n"]/td[2]/a')
                                        rok_surowy = output[0].text
                                        list = [int(s) for s in rok_surowy.split() if s.isdigit()]
                                        number = int(list[-1])
                            except Exception as err:
                                output = store.xpath(
                                    '//table[@class="infobox"]/tbody/tr[td[1]/text()="Data założenia\n"]/td[2]')
                                try:
                                    rok_surowy = output[0].text
                                    list = [int(s) for s in rok_surowy.split() if s.isdigit()]
                                    number = int(list[0])
                                except Exception as err:
                                    pass
                        if od <= number <= do:
                            print(nazwy_klubow[id])
                        id = id + 1
                except Exception as err2:
                    continue
        else:
            print('Nie ma takiego kryterium!!!')
except Exception as err:
    print('Wystąpił nieoczekiwany błąd!!!', err)
print()
print('Koniec programu')
