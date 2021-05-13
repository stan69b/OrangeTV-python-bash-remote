This project is based on code provided by @blipn : https://github.com/blipn/LiveBoxTV-PC-Remote
I needed a scriptable version to be able to controle the Orange TV Box using homeBridge : https://github.com/homebridge/homebridge 
@blipn has a java/GUI version if you need, this one is scripted in python3.
a set of shell scripts are provided as well, they act as Interfaces to execute python3 orangeTVRemote.py 192.168.x.x [remote button to trigger]

key list :

     116 : ON/OFF
     512 : 0
     513 : 1
     514 : 2
     515 : 3
     516 : 4
     517 : 5
     518 : 6
     519 : 7
     520 : 8
     521 : 9
     402 : CH+
     403 : CH-
     115 : VOL+
     114 : VOL-
     113 : MUTE
     103 : UP
     108 : DOWN
     105 : LEFT
     106 : RIGHT
     352 : OK
     158 : BACK
     139 : MENU
     164 : PLAY/PAUSE
     168 : FBWD
     159 : FFWD
     167 : REC
     393 : VOD
