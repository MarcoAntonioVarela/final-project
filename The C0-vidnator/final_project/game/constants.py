import os



MAX_X = 1000
MAX_Y = 900
FRAME_RATE = 30

DEFAULT_SQUARE_SIZE = 290
DEFAULT_FONT_SIZE = 120
DEFAULT_TEXT_OFFSET = 9

IMAGE_COVID = os.path.join(os.getcwd(), "./final_project/assets/covid.png")
IMAGE_SANITIZER = os.path.join(os.getcwd(), "./final_project/assets/sanitizer.png")
IMAGE_ATTACK = os.path.join(os.getcwd(), "./final_project/assets/attack.png")
IMAGE_COVID_ATTACK = os.path.join(os.getcwd(), "./final_project/assets/covid_attack.png")
IMAGE_MASK = os.path.join(os.getcwd(), "./final_project/assets/mask.png")
IMAGE_TITLE = os.path.join(os.getcwd(), "./final_project/assets/title.png")
IMAGE_CSE210 = os.path.join(os.getcwd(), "./final_project/assets/cse210.png")
IMAGE_GAME_OVER = os.path.join(os.getcwd(), "./final_project/assets/game_over.png")
IMAGE_VICTORY = os.path.join(os.getcwd(), "./final_project/assets/victory.png")


SOUND_START = os.path.join(os.getcwd(), "./final_project/assets/halo.wav")
SOUND_VICTORY = os.path.join(os.getcwd(), "./final_project/assets/victory.wav")
SOUND_VICTORY_BACKGROUND = os.path.join(os.getcwd(), "./final_project/assets/victory_background.wav")
SOUND_BOUNCE = os.path.join(os.getcwd(), "./final_project/assets/water.wav")
SOUND_DEATH = os.path.join(os.getcwd(), "./final_project/assets/covid_dying.wav")
SOUND_OVER = os.path.join(os.getcwd(), "./final_project/assets/over.wav")
SOUND_FINISH_HIM = os.path.join(os.getcwd(), "./final_project/assets/finish_him.wav")

ATTACK_X = MAX_X / 2
ATTACK_Y = MAX_Y - 125

ATTACK_DX = 8
ATTACK_DY = ATTACK_DX * -1

SANITIZER_X = MAX_X / 2
SANITIZER_Y = MAX_Y - 25

COVID_WIDTH = 67
COVID_HEIGHT = 70

MASK_WIDTH = 205
MASK_HEIGHT = 154

TITLE_WIDTH = 40
TITLE_HEIGHT = 30


GAME_OVER_WIDTH = 400
GAME_OVER_HEIGHT = 300


VICTORY_WIDTH = 400
VICTORY_HEIGHT = 300

COVID_SPACE = 5

SANITIZER_SPEED = 15

SANITIZER_WIDTH = 96
SANITIZER_HEIGHT = 24

ATTACK_WIDTH = 30
ATTACK_HEIGHT = 30


CSE210_WIDTH = 40
CSE210_HEIGHT = 30

COVID_SPEED = 15

COVID_ATTACK_X = MAX_X / 2
COVID_ATTACK_Y = MAX_Y - 125

COVID_ATTACK_DX = 8
COVID_ATTACK_DY = ATTACK_DX * -1

COVID_ATTACK_WIDTH = 30
COVID_ATTACK_HEIGHT = 30