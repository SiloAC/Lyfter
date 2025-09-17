# Base class 1: Wi-Fi capability
class WiFiDevice:
    def connect_wifi(self):
        print("Connecting to Wi-Fi...")

# Base class 2: Voice control capability
class VoiceControlDevice:
    def activate_voice(self):
        print("Voice control activated!")

# Derived class with multiple inheritance
class SmartSpeaker(WiFiDevice, VoiceControlDevice):
    def play_music(self):
        print("Playing music...")

speaker = SmartSpeaker()
speaker.connect_wifi()       # From WiFiDevice
speaker.activate_voice()     # From VoiceControlDevice
speaker.play_music()         # Own method