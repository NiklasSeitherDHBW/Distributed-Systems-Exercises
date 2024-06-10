# Protokollaggregation

Schreiben Sie einen Python basierten Server, mit dem sich Protokoll-Meldungen auf einem Server zentral anzeigen lassen. Das Programm soll mehrere Clients unterstützen und UDP verwenden. Jeder Client liest von der Tastatur eine Eingabezeile in Form eines Strings ein, validiert die Eingabe und sendet diese dann ggf. sofort zum Server. Der Server wartet auf Port 5678 und empfängt die Meldungen beliebiger Clients, die er dann unmittelbar ausgibt.

Stellen Sie sicher, dass Fehler adäquat behandelt werden.