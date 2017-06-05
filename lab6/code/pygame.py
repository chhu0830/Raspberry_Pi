import os
import pygame
import time

import sys
import Adafruit_DHT

sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }
sensor = sensor_args['11']
pin = 4

class pyscope :
    
    def __init__(self):
        "Ininitializes a new pygame screen using the framebuffer"
        disp_no = os.getenv("DISPLAY")
        if disp_no:
            print "I'm running under X display = {0}".format(disp_no)
        
        # Check which frame buffer drivers are available
        drivers = ['directfb']
        found = False
        for driver in drivers:
            if not os.getenv('SDL_VIDEODRIVER'):
                os.putenv('SDL_VIDEODRIVER', driver)
            try:
                pygame.display.init()
            except pygame.error:
                print 'Driver: {0} failed.'.format(driver)
                continue
            found = True
            break
    
        if not found:
            raise Exception('No suitable video driver found!')

        size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        
        print "Framebuffer size: %d x %d" % (size[0], size[1])
        self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        # Clear the screen to start
        self.screen.fill((0, 0, 0))        
        # Initialize font support
        pygame.font.init()
        # Render the screen
        pygame.display.update()
        # Initialize mixer
		

    def __del__(self):
        "Destructor to make sure pygame shuts down, etc."

    def display(self):
        '''
        self.screen.fill((255,0,0))
        pygame.display.update()
        time.sleep(3)
        self.screen.fill((0,255,0))
        pygame.display.update()
        time.sleep(3)
        self.screen.fill((0, 0,255))
        pygame.display.update()
        time.sleep(3)
        '''
        BLUE = (0,0,255)
        WIDTH = pygame.display.Info().current_w
        HEIGHT = pygame.display.Info().current_h
        self.screen.fill((0, 0, 0))
        pygame.display.update()
        rect = (0,0,WIDTH,HEIGHT)
        pygame.draw.rect(self.screen,BLUE,rect,1)
        pygame.draw.line(self.screen,BLUE,(WIDTH/3,0),(WIDTH/3,HEIGHT),1)
        pygame.draw.line(self.screen,BLUE,(2*WIDTH/3,0),(2*WIDTH/3,HEIGHT),1)
        pygame.draw.line(self.screen,BLUE,(0,HEIGHT/3),(WIDTH,HEIGHT/3),1)
        pygame.draw.line(self.screen,BLUE,(0,2*HEIGHT/3),(WIDTH,2*HEIGHT/3),1)
        pygame.display.update()
        pygame.mixer.init()
        pygame.mixer.music.load("lab6.mp3")
        pygame.mixer.music.play(10)

        h1, t1 = Adafruit_DHT.read_retry(sensor, pin)
        for x in range(20):
            h2, t2 = Adafruit_DHT.read_retry(sensor, pin)
            pygame.draw.line(self.screen, (210, 210, 210), ((WIDTH/20.0)*x, HEIGHT - t1*10.0), ((WIDTH/20.0)*(x+1), HEIGHT - t2*10.0))
            t1 = t2
            pygame.mixer.music.set_volume(t2 / 100.0)
            pygame.display.update()
        time.sleep(1)
    
# Create an instance of the PyScope class
scope = pyscope()
scope.display()
