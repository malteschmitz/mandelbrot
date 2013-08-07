Mandelbrot-Mengen
=================

[Mandelbrot-Mengen](http://de.wikipedia.org/wiki/Mandelbrot-Menge)
visualisieren mit [Python 3](http://www.python.org/) und
[Tk](http://www.tkdocs.com/).

Mathematik
----------

Die Mandelbrot-Menge ist definiert als die Menge aller Punkte c in
der komplexen Zahlenebene, für die die Folge

> z(0) = 0  
> z(n+1) = z(n)^2 + c

konvergiert. Für eine Koordinate (x,y) in der zweidimensionalen
Ebene wird c dabei berechnet als

> c = x + y*j

für die imaginäre Einheit i mit

> i^2 = -1

Diese zweidimensionale Ebene kann als Bild dargestellt werden.
Jeder Bildpunkt dieser Ebene wird dabei entsprechend seiner
Zugehörigkeit zur Mandelbrot-Menge eingefärbt. Die Konvergenz bzw.
Divergenz der dem aktuellen Punkt c entsprechenden Folge wird dabei
bestimmt, indem die ersten 255 Elemente der Folge berechnet werden.
Sobald ein Folgenelement größer als 2 wird, kann für die Folge
Divergenz angenommen werden, da die weiteren Folgenelemente nur
durch Quadrieren und Addition einer Konstanten berechnet
werden. Bleiben alle 255 Folgenelemente unter 2, so wird
für diese Folge Konvergenz angenommen. Im Falle der Divergenz
wird die Anzahl Folgenelemente bis zur eindeutigen Divergenz
als Indikator für die Geschwindigkeit der Divergenz verwendet.
Die Bildpunkte im Randbereich der Mandelbrot-Menge werden entsprechend
dieses Indikators eingefärbt.

Summer Camp 2013
----------------

Diese Software entstand im Rahmen des Informatik Summer Camps 2013 an der
Universität zu Lübeck. Die Klasse `Mandelbrot` war vorgegeben, die Funktion
`get_value` ist daraus ausgelagert und liefert den Farbwert für eine
Koordinate des Bildes. Der Code dieser Funktion zwischen den Kommentarzeilen
`Beginn/Ende der Lösung` wurde von den Teilnehmer selbst erarbeitet.

Bedienung
---------

Python ist auf vielen Systemen bereits installiert, sodass die Software über

    python3 mandelbrot.py

gestartet werden kann. Bei der Verwendung in interaktiven Systemen wie IDLE muss
die folgende Zeile am Ende der Datei `gameoflife.py` auskommentiert werden:
    
    app.run()

In diesem Fall übernehmen diese Systeme die Ausführung der Mainloop.

Die Bedienung erfolgt über das Menü oder die im Menü angegebenen Tastaturbefehle
und mit der Maus.

Mit der Maus kann ein rechteckiger Bereich durch Klicken und Ziehen in das
Bild aufgezogen werden. Dieser Bereich wird dann auf die volle Größe
vergrößert. Wie der Start des Programms kann auch diese Operation einige Zeit
in Anspruch nehmen, da alle Bildpunkte des Bildes neu berechnet werden.

### Zurücksetzen (R)

Verwirft den aktuellen Ausschnitt und wählt wieder den initialen Ausschnitt,
mit dem das Programm auch startet: Auf der X-Achse -2.5 bis 1.5 von links nach
rechts und auf der Y-Achse -1.5 bis 1.5 von unten nach oben. In diesem Ausschnitt
befindet sich die gesamte Mandelbrotmenge.

### Grafik speichern (S)

Speichert das aktuelle Bild im GIF-Format.

### Beenden (Q)

Beendet das Programm.

### Farbpalette

Die Funktion `get_value` gibt einen Wert zwischen 0 und 255 zurück. Dabei steht
0 für starke Divergenz und 255 für deutliche Konvergenz. Entsprechend wird
in der klassischen Darstellung die 0 weiß und die 255 schwarz dargestellt, sodass
alle Elemente, die zur Mandelbrot-Menge dazu gehören, in schwarz auf weißem
Hintergrund dargestellt werden. Statt Graustufen können auch andere Farben
für die Visualisierung dieses Indikators für die Geschwindigkeit der Divergenz
verwendet werden. Die entsprechende Farbplalette kann über dieses Menü
ausgewählt werden. Im Menü werden alle Farbpaletten angboten, die in der Datei
`palettes.py` enthalten sind. Eine Palette besteht dabei aus einer Liste von
256 Farbwerten im Format `#RRGGBB`, wobei `RR` den Rot-Anteil, `GG` den
Grün-Anteil und `BB` den Blau-Anteil der Farbe in hexadezimaler Darstellung
angeben.

License
-------

This software is released under the
[MIT License](http://www.opensource.org/licenses/MIT).