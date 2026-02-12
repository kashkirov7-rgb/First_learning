my_vehicle = {}

vehicle = input("Enter your vehicle car or bike: ")
model_vehicle = input("Enter your model: ")

# my_vehicle[vehicle] = model_vehicle
my_vehicle.update({vehicle: model_vehicle})

your_gaming_console = input("You use console(xbox/ps) or PC?: ")
Color_gaming_device = input("How color your device: ")

my_vehicle.update({your_gaming_console: Color_gaming_device})

voice_device = input("You use microphone of webcam: ")
color_voice_device = input("How color your device: ")

my_vehicle.update({voice_device: color_voice_device})
# можно .update написать один раз и добавить всё сразу пример: kode.update({a: b, c: d})

print(my_vehicle)


my_vehicle.update({'my_keyboard': 'DEXP'})
my_vehicle.update({'color_my_tshort': 'purple'})

print(my_vehicle)
del my_vehicle['my_keyboard']

print(my_vehicle)
