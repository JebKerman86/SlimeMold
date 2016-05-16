# SlimeMold
Image processing and evaluation programs for physics lab on slime molds.

## Update
- Habe nen gaussfilter aus dem Paket scipy.ndimage ausprobiert filter funktioniert einfach und gut allerdings verschwimmt das bild dadurch mit dem kleinen rest der da oben am mikroplasmoid dranhängt und das wird im binärbild eine fläche. Mit kleinerem Sigma funktioniert es aber der Effekt ist auch klein. Stattdessen habe ich den MedianBlur filter verwendet, der sieht zumindest fürs binärbild besser aus. Für bestimmung analyse und vereinfachung der flächen habe ich uA scipy.label verwendet.
- Ich denke die scipy (ndimage)  pakete sind besser bzw. besser kommentiert und ausreichend für unsere zwecke als die extra bild bibliotheken. Geht auch für fouriertransform (fftpack muss extra importiert werden) habs aber vorerst mit numpy gemacht. Wenn möglich würde ich dann auf die Image bibliotheken ganz verzichten (openCV und PIL) da ich bisher alle funktionen ersetzen konnte und wir eig. auch keine image-objekte brauchen. Dann wären wir auf scipy numpy und plot, was standardt bibs von python sind, dann kann er auch den code ausführen ohne bibs zu installieren.
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

