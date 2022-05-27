#!/usr/bin/env python
import fileinput
import sys

from main import ParkingLot, Car

parking_lot = ParkingLot()


def process(command_params):
    command_with_params = command_params.strip().split(' ')
    command = command_with_params[0]

    if command == 'Create_parking_lot':
        assert len(command_with_params) == 2, "create_parking_lot needs no of slots as well"
        assert command_with_params[1].isdigit() is True, "param should be 'integer type'"
        parking_lot.create_parking_lot(int(command_with_params[1]))

    elif command == 'Park':
        assert len(command_with_params) == 4, "park needs registration number and color as well"
        car = Car(command_with_params[1], command_with_params[3])
        parking_lot.park(car)

    elif command == 'Leave':
        assert len(command_with_params) == 2, "leave needs slot number as well"
        assert command_with_params[1].isdigit() is True, "slot number should be 'integer type'"

        parking_lot.leave(int(command_with_params[1]))

    elif command == 'Vehicle_registration_number_for_driver_of_age':
        assert len(command_with_params) == 2, "registration_numbers_for_cars_with_colour needs color as well"
        parking_lot.registration_numbers_for_cars_with_driver_age(command_with_params[1])

    elif command == 'Slot_numbers_for_driver_of_age':
        assert len(command_with_params) == 2, "slot_numbers_for_cars_with_colour needs color as well"
        parking_lot.slot_numbers_for_cars_with_driver_age(command_with_params[1])

    elif command == 'Slot_number_for_car_with_number':
        assert len(command_with_params) == 2, "slot_number_for_registration_number needs registration_number as well"
        parking_lot.slot_number_for_registration_number(command_with_params[1])

    elif command == 'exit':
        exit(0)
    else:
        raise Exception("Wrong command")


if len(sys.argv) == 1:
    while True:
        line = input()
        process(line)
else:
    for line in fileinput.input():
        process(line)