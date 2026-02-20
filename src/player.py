import pygame

class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()
        
    def player(self, path_file):
        pygame.mixer.music.load(path_file)
        pygame.mixer.music.play()
        
    def get_time(self):
        return pygame.mixer.music.get_pos()/1000.0
    
    def stop(self):
        pygame.mixer.music.stop()
    
    def pause(self):
        pygame.mixer.music.pause()
    
    def is_playing(self):
        return pygame.mixer.music.get_busy()
    
    def get_duration(self, path):
        sound = pygame.mixer.Sound(path)
        return sound.get_length()