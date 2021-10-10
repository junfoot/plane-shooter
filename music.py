import pygame,globalvar
pygame.mixer.init()
scene = globalvar.get_value('scene')
if scene == 1:
    from scene_banana import *
elif scene == 2:
    from scene_chicken import *
elif scene == 3:
    from scene_oldeight import *

