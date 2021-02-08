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


def data_writer(core_no, apt_nos, floors):
    global led_count
    floor_no = 1
    for floor in range(floors[0],floors[1]):
        for apt in apt_nos:
            data.append({"name": "B2." + str(floor) + "." + str(apt),
                         "value": value,
                         "num": led_count
                         })
            led_count += 1
            print(data[-1])
            if led_count == 64:
                print("New channel from controller. Core - " + str(core_no) + ". Building - B2. " + "Floor - " + str(floor) + ". Apartment - " + str(apt))


# Function call with arguments
data_writer(1, [1,2,3], [1,13])
data_writer(2, [4, 5, 6], [1, 7])
data_writer(2, [4, 5, 6, 7], [7, 13])
data_writer(3, [7, 10, 11], [1, 7])
data_writer(4, [8, 9], [1, 7])

''' previous effort
# Number of floors in model
floors = range(1, 12)

# List of cores in model
cores = [1, 2]

# Loop through cores in variable list
for core in cores:
    # Branch for core number 1
    if core == 1:
        # Counter to keep track of led's in chain
        led_count = 0
        # Counter for floors processed
        floor_no = 1
        # Loop through each floor
        for floor in floors:
            # Branch for condition applicable to floors 1 to 6
            if floor_no in range(1, 6):
                # Loop through floors 1 to 6
                for i in range(1, 7):
                    # Loop through apartments 1 to 6
                    for apartment in range(1, 7):
                        # Add new entry to output
                        data.append({"name": "B2." + str(floor_no) + "." + str(apartment),
                                     "value": 255,
                                     "num": led_count
                                    })
                        # previous num constructor
                        # float(str(core) + "." + str(led_count)

                        # Add count to led counter
                        led_count += 1
                    # Add count floor counter
                    floor_no += 1
            elif floor_no in range(7, 13):
                # Loop through floors 7 to 12
                for n in range(7, 13):
                    # Loop through apartments 1 to 6
                    for apartment in range(1, 8):
                        # Add new entry to output
                        data.append({"name": "B2." + str(floor_no) + "." + str(apartment),
                                     "value": 255,
                                     "num": led_count
                                    })
                        # previous num constructor
                        # float(str(core) + "." + str(led_count)

                        # Add count to led counter
                        led_count += 1
                    # Add count floor counter
                    floor_no += 1
            else:
                pass
        else:
            pass
    else:
        pass

print(data)

'''
json.dumps(data, indent=4)

with open('data.json', 'w') as outfile:
    # Convert the object to a string
    json.dump(data, outfile)

