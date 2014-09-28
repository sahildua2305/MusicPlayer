import simplegui

def play():
    sound.play()
    
def pause():
    sound.pause()

def rewind():
    sound.rewind()
    
def laugh():
    laugh.play()

def vol_down():
    global vol
    if vol>0:
        vol = vol-1
    sound.set_volume(vol/10.0)
    volume_button.set_text("Volume = "+str(vol))
    
def vol_up():
    global vol
    if vol<10:
        vol = vol+1
    sound.set_volume(vol/10.0)
    volume_button.set_text("Volume = "+str(vol))


frame = simplegui.create_frame("Player", 250, 250, 100);
frame.add_button("Play", play, 100 )
frame.add_button("Pause", pause, 100)
frame.add_button("Rewind", rewind, 100)
frame.add_button("Laugh", laugh, 100)
frame.add_button("Volume up", vol_up, 100)
frame.add_button("Volume down", vol_down, 100)

vol=7
volume_button = frame.add_label("Volume = "+str(vol))

sound = simplegui.load_sound('http://commondatastorage.googleapis.com/codeskulptor-assets/Epoq-Lepidoptera.ogg')
laugh = simplegui.load_sound('http://commondatastorage.googleapis.com/codeskulptor-assets/Evillaugh.ogg') 

frame.start()

