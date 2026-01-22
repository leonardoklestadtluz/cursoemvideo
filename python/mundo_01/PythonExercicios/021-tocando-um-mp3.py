"""
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
"""

""" FUNCIONOU inserindo a função input( ) """
import pygame
pygame.init()
pygame.mixer.music.load('mediaEx021/ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
pygame.quit()


""" ESta bilbioteca funcionou também
from playsound import playsound
playsound('/home/leonardo/Documentos/cursoemvideo/python/01_modulo/PythonExercicios/mediaEx021/ex021.mp3')
"""


