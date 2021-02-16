import json

# var to contain output data
data = []

# patterns to generate output.  [core number, [apartment numbers(as list)], [floors(as list)]]
# patterns = [

# pattern = [1, [1,2,3], [1,12]]

'''
    [1, [1,2,3], [1,12]]
    [2, [4,5,6], [1,6]],
    [2, [4,5,6,7], [7,12]],
    [3, [7,10,11], [1, 6]],
    [4, [8,9], [1,6]],
]
'''

# var for "value" in output, this sets the default brightness of the LEDs
value = 255

led_count = 0


def apartment_data_writer(core_no, apt_nos, floors):
    global led_count
    for floor in range(floors[0],floors[1]):
        for apt in apt_nos:
            data.append({"name": "B2." + str(floor) + "." + str(apt),
                         "value": value,
                         "num": led_count
                         })
            led_count += 1
            print(data[-1])
            # make a function to check led count
            if led_count == 64:
                print("New channel from controller. Core - " + str(core_no) + ". Building - B2. " + "Floor - " + str(floor) + ". Apartment - " + str(apt))
            if led_count == 128:
                print("New channel from controller. Core - " + str(core_no) + ". Building - B2. " + "Floor - " + str(floor) + ". Apartment - " + str(apt))


def nonapartment_data_writer(no_of_leds, name):
    global led_count
    for led in range(0, no_of_leds):
        data.append({"name": name,
                        "value": value,
                        "num": led_count
                        })
        led_count += 1
        print(data[-1])
        if led_count == 64:
            print("New channel from controller. " + name + " at LED number " + led)
        if led_count == 128:
            print("New channel from controller. " + name + " at LED number " + led)


# Function call with arguments - (core, apartment numbers, floors)
# This call basically maps the LEDs to their apartments and floors.
# Core is not used for the JSON config file, it is used to identify the physical location of LEDs
apartment_data_writer(1, [1,2,3], [1,13])
apartment_data_writer(2, [4, 5, 6], [1, 7])
apartment_data_writer(2, [4, 5, 6, 7], [7, 13])
apartment_data_writer(3, [7, 10, 11], [1, 7])
apartment_data_writer(4, [8, 9], [1, 7])

nonapartment_data_writer(6, "stairwell")
nonapartment_data_writer(3, "ground_floor")


json.dumps(data, indent=4)

with open('data.json', 'w') as outfile:
    # Convert the object to a string
    json.dump(data, outfile)

