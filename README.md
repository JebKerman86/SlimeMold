# SlimeMold
Image processing and evaluation programs for physics lab on slime molds.

## Update
Habe nen gaussfilter aus dem Paket scipy.ndimage ausprobiert filter funktioniert einfach und gut allerdings verschwimmt das bild dadurch mit dem kleinen rest der da oben am mikroplasmoid dranhängt und das wird im binärbild eine fläche. Daher versuche ich nochmal das exakte bild auszuwerten und ne gescheite funktion zu basteln die das in den griff kriegt.
Matlab befehl umd zusammenhängende flächen als matrizen mit koords der pixel auszugeben: bwconncomp
Mögliche python alternative scipy.label
opencv installiert 
import cv2 bietet mediablurr vlt. besser als gauss ausprobieren
PIL bietet auch die Filter evt. cv2 nicht nötig, werde ich dann wieder rausnehmen brauchst erstmal nicht installieren codec



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

