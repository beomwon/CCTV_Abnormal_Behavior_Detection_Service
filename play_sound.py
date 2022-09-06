import pygame
import os

def init():
    pygame.init()

def play(action_list):
    #step 1: 적당, 2: 중요, 3: 위급
    step_dic = {'assault': 3, 'fainting': 3, 'property_damage': 2, 'stairway_fall': 1, 'turnstile_trespassing': 1}
    step = 1
    for msg in action_list: # 위급순위가 높은 사운드로 출력시키기 위해
        cat, _ = msg.split()
        if step_dic[cat] > step:
            step = step_dic[cat]
    sound_name = os.path.join('sound','step_'+ str(step) + '.mp3')
    pygame.mixer.music.load(sound_name)
    pygame.mixer.music.play()

def is_singing():
    return pygame.mixer.music.get_busy()