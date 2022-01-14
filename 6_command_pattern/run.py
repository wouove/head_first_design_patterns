from remote_control import SimpleRemoteControl
from light import Light
from command import LightOnCommand

remote = SimpleRemoteControl()
light = Light()
light_on = LightOnCommand(light)

remote.set_command(light_on)
remote.button_was_pressed()