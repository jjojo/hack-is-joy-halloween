import time
import os
import playsound
import footTap
import footTapAndHeadBup
import faceMimeing
import wreckingball
import hammerSkeletonSinging
import lyrics

playsound.playsound('Miley_Cyrus_Wrecking_Ball.mp3', False)
startTime = time.time()
previous = lyrics.frames[str(0.0)]


def printLyricLine(time):
    global previous

    try:
        previous = lyrics.frames[str(time)+'.0']
        print(lyrics.frames[str(time)+'.0'])
    except:
        print(previous)
    

def animate(frames, duration, cycles):
    """Iterate through the frames, printing then clearing each one to create an animation."""
    count = 0
    
    while count < cycles:
        for frame in frames:
            print(frame)
            printLyricLine(round(time.time() - startTime))
            time.sleep(duration)
            print(os.system('clear'))
        count = count + 1


# time.sleep(8.5)
animate(faceMimeing.frames, 0.3, 19)
animate(wreckingball.frames, 0.15, 5)
animate([wreckingball.frames[22]], 0.3, 7)
animate(hammerSkeletonSinging.frames, 0.5, 30 )
animate(wreckingball.frames, 0.15, 10)
animate(hammerSkeletonSinging.frames, 0.5, 30 )
animate(faceMimeing.frames, 0.3, 4)
animate(wreckingball.frames, 0.15, 13)
animate([wreckingball.frames[22]], 0.3, 100)






#animate(footTap.frames, 0.3, 4)
#animate(footTapAndHeadBup.frames, 0.3, 4)
