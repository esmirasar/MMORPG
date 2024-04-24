import random

BASE = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm123456789'

RANDOM_STRING = ''.join([random.choice(BASE) for _ in range(30)])