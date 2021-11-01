import pygame
from tkinter import messagebox, Tk

from pygame import draw
from pygame.constants import MOUSEBUTTONDOWN
from config import *
from xocore import checkWin,move,moves,play_array,who,player1,player2

Tk().wm_withdraw()
size = (w_widht, w_height)
window = pygame.display.set_mode(size)
cell_size = ((w_widht*w_height)/9)**0.5
border_size = int(cell_size/10)
window.fill(colors['background'])
winner = None
pygame.display.set_caption('Крестики-нолики')
pygame.init()

def draw_field():
    for i in 0,1,2:
        for j in 0,1,2:
            pygame.draw.rect(window,colors['grid'],(cell_size*j,cell_size*i,cell_size,cell_size),border_size)
    for i in range(9):
        if play_array[i] != ' ':
            draw_move(play_array[i],i)

def draw_move(char, cell):
    x, y = border_size+cell%3*cell_size, border_size+cell//3*cell_size
    if char == 'X':
        pygame.draw.line(window,colors['x'],(x,y),(x+cell_size-2*border_size,y+cell_size-2*border_size), border_size//2)
        pygame.draw.line(window,colors['x'],(x+cell_size-2*border_size,y),(x,y+cell_size-2*border_size), border_size//2)
    elif char == 'O':
        radius = cell_size/2
        pygame.draw.circle(window,colors['o'],(x+radius-border_size,y+radius-border_size),radius-border_size,border_size//2)

def game():
    global who
    global winner
    x_mouse, y_mouse = pygame.mouse.get_pos()
    cell = int(x_mouse//cell_size+y_mouse//cell_size*3)
    if moves<9:
        if move(who,cell):
            if checkWin(who):
                render()
                winner = who
                messagebox.showinfo('Поздравляем!',f'Игрок {winner} выиграл!')
                return        
            if who==player1:
                who=player2
            else:
                who=player1
            
def render():
    draw_field()
    pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and winner == None:
            game()
    render()