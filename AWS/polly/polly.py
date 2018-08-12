import boto3
import pygame
import time

pygame.mixer.init()

polly = boto3.client('polly')
response = polly.synthesize_speech(OutputFormat='mp3',
                                    Text="Hello my name is Leonard",
                                    VoiceId='Justin')
### save MP3 FILE #####

with open('output1.mp3', 'wb') as stream:
    stream.write(response['AudioStream'].read()) # read the audiostream and write to file in same line
    stream.close()
pygame.mixer.music.load('output1.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy() == True:  # test if music is playing
    print ('loop')
    pass
print ('FINISHED')


#pygame.mixer.music.load(response['AudioStream'])
#pygame.mixer.music.play()
#time.sleep(2)

