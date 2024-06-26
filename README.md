![grafik](https://github.com/Moppi1/ECLIPSE_/assets/150188517/3fceb204-4549-4491-a63a-967b5538c0a6)

Anleitung zur Ausführung und die Vorführung des Programms als Video :
**https://youtu.be/qQhmenJg6J8**
-  

In den Projektdateien gibt es ein Textdokument mit dem Namen "Settings.txt", in welchem
die Sichtbarketi von Anzeigen und Objekten und andere Festlegungen
für die Kollisionserkennung und Auflösung festgelegt werden können.
Das bewegbare Polygon in der Demo kann mit "WASD" bewegt und mit "Q" und "E" skaliert werden.


Schritte zum Ausführen des Programms:
--
**1.Python installieren:**   
Da das Programm in Python geschrieben wurde, muss zuerst eine Pythonversion (am besten eine der neuesten) installiert werden.
Python kann entweder im Microsoft Store installiert https://apps.microsoft.com/detail/9pjpw5ldxlz5?hl=en-US&gl=US werden 
oder online über https://www.python.org/downloads/.  

**2. Anwendung  herunterladen:**  
Nachdem Python heruntergeladen und installiert wurde können die Dateien von Github heruntergeladen werden.
Dazu kann unter dem Button "Code" (oben rechts, siehe oberes Bild), die Option "download ZIP" gewählt werden (siehe unteres Bild).  
![grafik](https://github.com/Moppi1/3D_demo/assets/150188517/dbb51c8c-3c0c-44b5-ab87-4717f780275d)
![grafik](https://github.com/Moppi1/3D_demo/assets/150188517/e9dce9b8-7a07-4315-beb0-88caba47dade)  
Sobald die ZIP datei heruntergeladen wurde kann diese extrahiert werden.  

**3. Anwendung  Ausführen:**   
In dem Ordner, in dem die einzelnen Python-Skripte liegen, kann nun bei Windows in die Kopfzeile mit/anstatt
der Pfadangabe, `cmd` eingegeben werden (mit Enter bestätigen).
![grafik](https://github.com/Moppi1/3D_demo/assets/150188517/dc4073e6-fcc7-4af8-a361-460cc4716732)

Dadurch öffnet sich die Konsole direkt im richtigen Verzeichnis.
![grafik](https://github.com/Moppi1/3D_demo/assets/150188517/d346a169-f531-433c-b2dd-3a928667f265)

In dem neu geöffneten Konsolenfenster kann nun `python main.py` eingegeben, und bestätigt werden.
Dadurch sollte sich das Programm öffnen und ausgeführt werden können.

Mögliche Probleme:
------
Nach der Richtigen Ausführung der Schritte 1 bis 3 sollte das Programm eigentlich starten.
Sollte die Anwendung dennoch nicht startet kann das mehrere Gründe haben..  

**1. Falsches Verzeichnis**  
Der Befehl `python main.py` wurde nicht in dem richtigen Verzeichnis ausgeführt. Schließen sie dazu die Konsole,
gehen sie in den Projekt-Ordner, in dem sich die Datei `main.py` findet, und führen sie dort erneut Schritt 3 aus.  

**2. Fehlende Library**  
Eine der genutzten Library's ist nicht installiert.
Standardmäßig sollte bei einer Pythoninstallation Pygame installiert sein. Sollte dies aber nicht der Fall sein, kann in der 
Konsole der Befehl `pip install pygame` ausgeführt werden, um Pygame zu installieren.
Sollte diese Library bereits installiert sein, wird sie nur geupdatet wenn eine neue Version verfügbar ist,
oder nicht verändert. Es kann also, selbst wenn die Library bereits installiert ist nicht schaden die Library mit dem Befehl zu installieren/updaten.
