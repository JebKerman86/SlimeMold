# SlimeMold
Image processing and evaluation programs for physics lab on slime molds.

## Update
Habe nen gaussfilter aus dem Paket scipy.ndimage ausprobiert filter funktioniert einfach und gut allerdings verschwimmt das bild dadurch mit dem kleinen rest der da oben am mikroplasmoid dranhängt und das wird im binärbild eine fläche. Daher versuche ich nochmal das exakte bild auszuwerten und ne gescheite funktion zu basteln die das in den griff kriegt.
Mögliche python alternative scipy.label zu matlab bwconncomp
scipy.ndimage enthält jedemenge image funktionen die ich intuitiver finde als opencv und PIL alles was ich gesehen hab lässte sich ersetzen
auf image objects können wir ganz verzichten denke ich oder? anzeigen geht gut mit matplotlib siehe output in main und einlesen kann man direkt als array siehe erste zeile main
dann sparen wir uns die nicht standard bibs. FFT hab ich jetz mit numpy gemacht steckt aber auch in scipy man muss scipy.fftpack allerdings seperat importieren da es nicht mit scipy mit importiert wird (zusatzbib)

- hab dein kymographen die variablen klein geschrieben und paar kommentare gemacht kannste vlt. auch noch richtig auskommentieren, ich schreib in die info oben immer was fürn datentyp man reintut und was rauskommt, damit man zB gleich sieht, dass da nen array(array,pixelweite) rauskommt kein wunder dass ich den so nicht plotten konnte ;).

- binarization hab ich fertig funzt echt nice auch flächen berechnung und schwerpunkt hab ich schon guck mal rein in die änderungen bevor es soviel wird, dass du die übersicht verlierst...



## TODO
- write main script for single image first.tif
- beutify code and add comments
- größte fläche füllen andere löschen
- finish krymograph
- finish other functions
- evaluation for first.tif
- evaluation for all images
- plot importants beatiful

## NOTES
recording 0.2 frames per second (each 5sec)


## GIT
### Commandline
git clone https://github.com/JebKerman86/SlimeMold

git pull (get changes from others)

git add newcreatedfile.py

git commit modifiedfile.py

git commit -a  (adds all changed files does not add new ones)

enter comment into vim promt after using commit
 or use -m or -am to enter 'message' in parameter
git push

