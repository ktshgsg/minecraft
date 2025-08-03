from ursina import *
from settings_menu import SettingsMenu, load_settings, settings

app = Ursina()

sun = DirectionalLight()
camera.bloom_strength = 0.4 if settings['bloom'] else 0
Audio.volume = settings['volume']
sun.enabled = settings['shadows']

settings_menu = SettingsMenu(sun, camera)

def input(key):
    if key == 'escape':
        settings_menu.enabled = not settings_menu.enabled

app.run()
