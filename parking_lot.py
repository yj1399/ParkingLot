# parking_lot.py
import heapq
from collections import defaultdict, OrderedDict


class Car:

    def __init__(self, registration_number, driver_age):
        # Stores Registration Number for Each Car Object
        self.registration_number = registration_number
        # Stores Drivers Ages
        self.driver_age = driver_age

    def __str__(self):
        return "Car [registration_number=" + self.registration_number + ", driver=" + self.driver_age + "]"


class ParkingLot:

    def __init__(self):
        """
        init Method of Parking Lot Class to initialize Dictionaries
        """
        # Dictionary for registration_no and slot_no mapping
        self.registration_slot_mapping = dict()
        # Default Dictionary which will be initialised with empty list , store driver to registration_no mapping
        self.driver_age_registration_mapping = defaultdict(list)
        # Order Dictionary maintain the orders of cars while showing 'status'
        self.slot_car_mapping = OrderedDict()
        # initialize all slots as free
        self.available_parking_lots = []

    def create_parking_lot(self, total_slots):
        """
        This Method Create Parking_Lots of given size
        :param total_slots:
        :return Nothing:
        """
        # Using min heap as this will always give minimum slot number in O(1) time
        print("Created a parking lot with {} slots".format(total_slots))
        for i in range(1, total_slots + 1):
            heapq.heappush(self.available_parking_lots, i)
        return True

    def get_nearest_slot(self):
        """
        This Method Returns Nearest Slot_No Available
        :return slot_no:
        """
        return heapq.heappop(self.available_parking_lots
                             ) if self.available_parking_lots else None

    def leave(self, slot_to_be_freed):
        """
        This Method free the slot for given slot_no
        :param slot_to_be_freed:
        :return Boolean:
        """
        found = None
        for registration_no, slot in self.registration_slot_mapping.items():
            if slot == slot_to_be_freed:
                found = registration_no

        # Cleanup from all cache
        if found:
            heapq.heappush(self.available_parking_lots, slot_to_be_freed)
            del self.registration_slot_mapping[found]
            car_to_leave = self.slot_car_mapping[slot_to_be_freed]
            self.driver_age_registration_mapping[
                car_to_leave.driver_age].remove(found)
            del self.slot_car_mapping[slot_to_be_freed]
            print(
                f"Slot number {slot_to_be_freed} vacated, the car with vehicle registration number {car_to_leave.registration_number} left the space, the driver of the car was of age {car_to_leave.driver_age}"
            )
            return True

        else:
            print("slot is not in use")
            return False

    def park(self, car):
        """
        This Method Parks Car to Nearest Slot and return that slot_no
        :param car:
        :return slot_no:
        """
        slot_no = self.get_nearest_slot()
        if slot_no is None:
            print("Sorry, parking lot is full")
            return
        print(
            f"Car with vehicle registration number {car.registration_number} has been parked at slot number {slot_no}"
        )
        self.slot_car_mapping[slot_no] = car
        self.registration_slot_mapping[car.registration_number] = slot_no
        self.driver_age_registration_mapping[car.driver_age].append(
            car.registration_number)
        return slot_no

    def registration_numbers_for_cars_with_driver_age(self, driver_age):
        """
        This Methods returns Registrations Number of Cars for given Driver age
        :param driver_age:
        :return list:
        """
        registration_numbers = self.driver_age_registration_mapping[driver_age]
        print(", ".join(registration_numbers))
        return self.driver_age_registration_mapping[driver_age]

    # Slot numbers of all slots where a car of a particular colour is parked
    def slot_numbers_for_cars_with_driver_age(self, driver_age):
        """
        This Method returns the slot Numbers for given Driver Age
        :param driver_age:
        :return slot_no_list:
        """
        registration_numbers = self.driver_age_registration_mapping[driver_age]
        slots = [
            self.registration_slot_mapping[reg_no]
            for reg_no in registration_numbers
        ]
        print(", ".join(map(str, slots)))
        return slots

    def slot_number_for_registration_number(self, registration_number):
        """
        This Method returns the slot Number for given Registration Number
        :param registration_number:
        :return slot_number :
        """
        slot_number = None
        if registration_number in self.registration_slot_mapping:
            slot_number = self.registration_slot_mapping[registration_number]
            print(slot_number)
            return slot_number
        else:
            print("Not found")
            return slot_number
