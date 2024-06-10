Ein einfacher HTTP-Client
=====

## Aufgabe A
Schreiben Sie einen HTTP-Client, der den Server `www.michael-eichberg.de` kontaktiert, die Datei `/index.html` anfordert und die Antwort des Servers auf dem Bildschirm ausgibt.

Verwenden Sie HTTP/1.1 und eine Struktur ähnlich der in der Vorlesung vorgestellten Echo-Client.

Senden Sie das GET-Kommando, die Host-Zeile sowie eine Leerzeile als Strings an den Server.


## Aufgabe B
Erweitern Sie Ihren Client um die Fähigkeit URLs auf der Kommandozeile anzugeben.

Verwenden Sie existierende Funktionalität, um die angegebene URL zu zerlegen (`urlparse` von `urllib.parse`).


## Aufgabe C
Speichern Sie die Antwort des Servers in einer lokalen Datei. Prüfen Sie, dass die Datei in einem Browser korrekt angezeigt wird.

Kann Ihr Programm auch Bilddateien (z. B. "http://www.michael-eichberg.de/acm.svg") korrekt speichern? Falls nicht, prüfen Sie ob Sie Antwort des Servers richtig verarbeiten; analysieren Sie ggf. den Header und passen Sie Ihr Programm entsprechend an.