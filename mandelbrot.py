# Mandelbrotmengen in Python zeichnen

# Dimensionen des Bildes in Pixeln
width = 640
height = 480

# An dieser Funktion müssen Änderungen vorgenommen werden
def get_value(x, y):
    """Berechnet den Wert an der Position (x,y). Zurückgegeben
       wird ein Wert zwischen 0 für eindeutige Konvergenz und
       255 für eindeutige Divergenz. Werte zwischen 0 und 255
       geben den Grad der Divergenz an und bilden damit einen
       Divergenzkoeffizienten."""
    # Beginn der Lösung
    c = x + y*1j
    z = 0
    for i in range(256):
        z = z*z + c
        if abs(z) > 2:
            return i
    return 255
    # Ende der Lösung

#############################################################

# Die folgende Klasse organisiert die GUI und muss nicht mehr angepasst werden.

# Laden der Komponenten für die GUI
from tkinter import *
# Laden des Speichern-Dialoges
from tkinter.filedialog import asksaveasfilename
# Laden der Farb-Paletten
from palettes import palettes

class Mandelbrot():
    def compute(self):
        # Werte berechnen
        self.data = [[0 for x in range(width)] for y in range(height)]
        for x in range(width):
            for y in range(height):
                val = get_value(self.x0 + x / width * self.width,
                    self.y0 + y / height * self.height)
                val = 255 - val % 256
                self.data[y][x] = val

    def draw(self):
        # Bild mit den Werten erzeugen
        self.photo = PhotoImage(width = width, height = height)
        self.photo.put(" ".join(map(
            lambda line: "{" + " ".join(map(
                lambda val: self.palette[val], line)) + "}", self.data)))

        # Bild auf die Leinwand zeichnen
        if self.image:
            self.canvas.delete(self.image)
        self.image = self.canvas.create_image(0, 0, anchor = NW, image = self.photo)

    def resetCoords(self):
        self.x0 = -2.5
        self.y0 = -1.5
        self.width = 4
        self.height = self.width * height / width

    def __init__(self):
        self.root = Tk()
        
        # Verhindern, dass die Fenstergröße angepasst werden kann
        self.root.resizable(0, 0)

        # Menüleiste erzeugen
        menubar = Menu(self.root)

        # Dateimenü erzeugen
        filemenu = Menu(menubar, tearoff = 0)
        filemenu.add_command(label = "Zurücksetzen", command = self.handleReset, accelerator = "R")
        filemenu.add_command(label = "Grafik speichern unter...", command = self.handleSave, accelerator = "S")
        filemenu.add_separator()
        filemenu.add_command(label = "Beenden", command = self.handleQuit, accelerator = "Q")
        
        # Farbmenü erzeugen
        palettesmenu = Menu(menubar, tearoff = 0)
        palette_keys = sorted(list(palettes.keys()))
        self.palette_var = StringVar()
        for key in palette_keys:
            palettesmenu.add_radiobutton(label = key, variable = self.palette_var, value = key,
                command = self.handlePalette)
        self.palette_var.set(palette_keys[0])
        self.palette = palettes[self.palette_var.get()]

        # Menüleiste zusammensetzen und verwenden
        menubar.add_cascade(label = "Datei", menu = filemenu)
        menubar.add_cascade(label = "Farbpalette", menu = palettesmenu)
        self.root.config(menu = menubar)

        # Koordinaten initialisieren
        self.resetCoords()
        
        # Leinwand erzeugen
        self.canvas = Canvas(self.root, width = width, height = height,
            bd = 0, highlightthickness = 0, relief = 'ridge')

        # Bild zeichnen
        self.image = None
        self.compute()
        self.draw()

        # Größe der Canvas auf ihren Inhalt anpassen
        self.canvas.pack()

        # Ereginisse an die Leinwadn binden
        self.canvas.bind("<Button-1>", self.handleClick)
        self.canvas.bind("<B1-Motion>", self.handleClick)
        self.canvas.bind("<ButtonRelease-1>", self.handleRelease)

        # Titel des Fensters setzen
        self.root.title("Mandelbrot")

        # Die Zeichenfläche soll Tastaturereignisse erhalten
        self.canvas.focus_set()

        # Shortcuts registrieren
        self.canvas.bind("<q>", self.handleQuit)
        self.canvas.bind("<r>", self.handleReset)
        self.canvas.bind("<s>", self.handleSave)

        # Eigenschaften für das Focus-Rechteck initialisieren
        self.start = None
        self.rect = None

    def handlePalette(self, event = None):
        self.palette = palettes[self.palette_var.get()]
        self.draw()

    def handleSave(self, event = None):
        self.save()

    def handleQuit(self, event = None):
        self.root.quit()

    def handleReset(self, event = None):
        self.resetCoords()
        self.compute()
        self.draw()

    def save(self):
        filename = asksaveasfilename(title = "Grafik speichern unter...",
            defaultextension = ".gif",
            filetypes = [("GIF-Dateien (*.gif)", "*.gif")])
        self.photo.write(filename, 'gif')

    def handleClick(self, event):
        if self.start:
            if self.rect:
                self.canvas.delete(self.rect)
            w = abs(event.x - self.start[0]) + 1
            h = w * height / width
            y = self.start[1] + h
            self.rect = self.canvas.create_rectangle(self.start[0], self.start[1],
                event.x, y, outline = "red", width = 2, dash = (2,4))
        else:
            self.start = [event.x, event.y]

    def handleRelease(self, event):
        if self.rect:
            self.canvas.delete(self.rect)
        if self.start:
            w = abs(event.x - self.start[0]) + 1
            if w > 5:
                self.x0 = self.x0 + self.start[0] / width * self.width
                self.y0 = self.y0 + self.start[1] / height * self.height
                self.width = w / width * self.width
                self.height = self.width * height / width
                self.compute()
                self.draw()
        self.start = None
        self.rect = None

    def run(self):
        self.root.mainloop()

    def donothing(self):
        print("Does nothing.")

if __name__ == '__main__':
    app = Mandelbrot()
    # Bei der Verwendung in interaktiven Systemen wie IDLE muss die folgende
    # Zeile auskommentiert werden. In diesem Fall übernehmen diese Systeme
    # die Ausführung der Mainloop.
    app.run()
