# Przetwarzanie danych z Wikipedii z użyciem web scrappingu

Wyszukiwarka klubów wszech-czasów polskiej Ekstraklasy piłkarskiej

Jak obsługiwać program:
* Po załadowaniu programu i bazy klubów Ekstraklasy, należy podać numer kryterium, po którym będziemy filtrować kluby. W Tym celu należy wpisać jedną z liczb od 1 do 11.
* Następnie podajemy liczbowy zakres zadanego kryterium z poprzedniego kroku. Program zapyta najpierw o liczbę „Od:” (początek zakresu), następnie po naciśnięciu ENTER, program zapyta o liczbę „Do:” (koniec zakresu).
* Na końcu program wypisuje nazwy pasujących klubów piłkarskich do zadanych kryteriów.

Zasada działania programu:
* Program na początku pobiera listę nazw wszystkich klubów z tabeli na stronie: https://pl.wikipedia.org/wiki/Tabela_wszech_czas%C3%B3w_Ekstraklasy_w_pi%C5%82ce_no%C5%BCnej
* Kryteria od 1-10 pobierają dane bezpośrednio z tabeli z powyższego linka. Program wypisuje nazwy klubów, które odpowiadają zadanym kryteriom.
* Kryterium 11 jest bardziej rozbudowane. Program wchodzi na linki do wszystkich klubów Ekstraklasy znajdujących się w tabeli wszech-czasów Ekstraklasy, pobiera rok założenia klubu z infoboxa i wypisuje nazwę klubu, jeżeli rok zawiera się w zadanym zakresie.

W przypadku ostatniego kryterium 11, wyzwaniem okazało się obsłużenie 4 przypadków pobrania roku z daty założenia klubu (brak jednolitych standardów na polskiej Wikipedii). Zostały użyte 4 następujące ścieżki xpath:
* //table[@class="infobox"]/tbody/tr[td[1]/text()="Data\xa0założenia\n"]/td[2]
* //table[@class="infobox"]/tbody/tr[td[1]/text()="Data\xa0założenia\n"]/td[2]/a[last()]
* //table[@class="infobox"]/tbody/tr[td[1]/text()="Data\xa0założenia\n"]/td[2]/a
* //table[@class="infobox"]/tbody/tr[td[1]/text()="Data założenia\n"]/td[2]
