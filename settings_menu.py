from ursina import *
import json

settings = {}

def load_settings():
    global settings
    try:
        with open('settings.json') as f:
            settings = json.load(f)
    except:
        settings = {"volume": 0.5, "shadows": True, "bloom": True}

load_settings()

class SettingsMenu(Entity):
    def __init__(self, sun_entity, camera_entity):
        super().__init__(enabled=False)
        self.sun = sun_entity
        self.cam = camera_entity

        self.bg = Entity(parent=self, model='quad',
                         color=color.black66, scale=(0.6,0.7), z=1)

        Text(parent=self, text="Settings", y=0.28, x=-0.12, scale=2)

        self.volume_slider = Slider(parent=self, min=0, max=1,
                                    default=settings['volume'], y=0.15,
                                    text="Volume")
        self.volume_slider.on_value_changed = self.apply_settings

        self.shadows_button = Button(text='Shadows: ON' if settings['shadows'] else 'Shadows: OFF',
                                     parent=self, y=0.05, color=color.azure,
                                     scale=(0.4,0.07))
        self.shadows_button.on_click = self.toggle_shadows

        self.bloom_button = Button(text='Bloom: ON' if settings['bloom'] else 'Bloom: OFF',
                                   parent=self, y=-0.05, color=color.orange,
                                   scale=(0.4,0.07))
        self.bloom_button.on_click = self.toggle_bloom

        self.save_button = Button(text='Save & Close', parent=self,
                                  y=-0.2, color=color.lime)
        self.save_button.on_click = self.save_and_close

        self.apply_settings()

    def toggle_shadows(self):
        settings['shadows'] = not settings['shadows']
        self.shadows_button.text = f"Shadows: {'ON' if settings['shadows'] else 'OFF'}"
        self.apply_settings()

    def toggle_bloom(self):
        settings['bloom'] = not settings['bloom']
        self.bloom_button.text = f"Bloom: {'ON' if settings['bloom'] else 'OFF'}"
        self.apply_settings()

    def apply_settings(self):
        Audio.volume = self.volume_slider.value
        self.cam.bloom_strength = 0.4 if settings['bloom'] else 0
        self.sun.enabled = settings['shadows']

    def save_and_close(self):
        settings['volume'] = self.volume_slider.value
        with open('settings.json', 'w') as f:
            json.dump(settings, f)
        self.enabled = False
