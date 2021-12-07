import os

MAX_X = 1000
MAX_Y = 900
FRAME_RATE = 30

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

IMAGE_COVID = os.path.join(os.getcwd(), "./final_project/assets/covid.png")
IMAGE_SANITIZER = os.path.join(os.getcwd(), "./final_project/assets/sanitizer.png")
IMAGE_ATTACK = os.path.join(os.getcwd(), "./final_project/assets/attack.png")
IMAGE_MASK = os.path.join(os.getcwd(), "./final_project/assets/mask.png")
IMAGE_TITLE = os.path.join(os.getcwd(), "./final_project/assets/title.png")
IMAGE_CSE210 = os.path.join(os.getcwd(), "./final_project/assets/cse210.png")
SOUND_START = os.path.join(os.getcwd(), "./final_project/assets/halo.wav")

SOUND_BOUNCE = os.path.join(os.getcwd(), "./final_project/assets/water.wav")
SOUND_OVER = os.path.join(os.getcwd(), "./final_project/assets/over.wav")

ATTACK_X = MAX_X / 2
ATTACK_Y = MAX_Y - 125

ATTACK_DX = 8
ATTACK_DY = ATTACK_DX * -1

SANITIZER_X = MAX_X / 2
SANITIZER_Y = MAX_Y - 25

COVID_WIDTH = 48
COVID_HEIGHT = 24

MASK_WIDTH = 100
MASK_HEIGHT = 30

TITLE_WIDTH = 40
TITLE_HEIGHT = 30

COVID_SPACE = 5

SANITIZER_SPEED = 15

SANITIZER_WIDTH = 96
SANITIZER_HEIGHT = 24

ATTACK_WIDTH = 24
ATTACK_HEIGHT = 24


CSE210_WIDTH = 40
CSE210_HEIGHT = 30
