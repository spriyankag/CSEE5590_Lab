
class Customer:#class creation
    __days_31 = [1,3,5,7,8,10,12]#private variable (encapsulation)
    days_30 = [4,6,9,11]
    days_28 = [2]
    dep_year = None
    dep_month = None
    dep_day = None

#created a constructor and passed values into it
    def __init__(self,year, month, day, name,num_of_rooms,occupants,date_duration):
        self.year = year
        self.month = month
        self.day = day
        self.name = name
        self.num_of_rooms = num_of_rooms
        self.date_duration = date_duration
        #arrival date
        self.arrival_date = str(self.year) + "-" + str(self.month) + "-" + str(self.day)
        self.occupants = occupants
        Customer.dep_day = self.day + self.date_duration
        Customer.dep_month = self.month
        Customer.dep_year = self.year

        #logic to find departure date
        if self.month == 2 and self.day == 29:
            Customer.dep_day = Customer.dep_day - 29
            Customer.dep_month = self.month + 1

        if self.month in Customer.__days_31:
            if Customer.dep_day > 31:
                Customer.dep_day = Customer.dep_day - 31
                Customer.dep_month = self.month + 1
                if Customer.dep_month > 12:
                    Customer.dep_month = 1
                    Customer.dep_year = self.year + 1
        elif self.month in Customer.days_30:
            if Customer.dep_day > 30:
                Customer.dep_day = Customer.dep_day - 30
                Customer.dep_month = self.month + 1
                if self.month == 13:
                    self.month = 1
                    Customer.dep_year = self.year + 1

        else:
            if Customer.dep_day > 28:
                Customer.dep_day = Customer.dep_day - 28
                Customer.dep_month = self.month + 1

        self.year = str(Customer.dep_year)
        self.month = str(Customer.dep_month)
        self.day = str(Customer.dep_day)

        #departure date
        self.departure_date = self.year + "-" + self.month + "-" + self.day

        print("Booking Details:")
        print("-----------------")
        print(" Name:", self.name, "\n",
              "Number of rooms:", self.num_of_rooms,  "\n",
              "Number of people:" ,self.occupants, "\n",
              "Number of days:", self.date_duration, "\n",
              "Arrival Date:", self.arrival_date,"\n",
              "Departure Date:", self.departure_date)


class Room_selection:#class creation
    def __init__(self,no_of_people,no_of_rooms):
        self.no_of_people = no_of_people
        self.no_of_rooms = no_of_rooms
        self.twin_bed_price = 1000
        self.tax = 14
        self.price = (self.twin_bed_price + ((self.twin_bed_price * self.tax) *100))

#display ordinary room price
    def get_bed_price(self):
        self.price = self.price * self.no_of_rooms
        if self.no_of_people > 2:
            self.price = self.price + self.no_of_people * 50
        print("ordinary room", self.price)

    def set_tax(self):
        self.tax = 14

    def get_no_of_people(self):
        return self.no_of_people

    def get_no_of_rooms(self):
        return self.no_of_rooms

    def get_tax(self):
        return self.tax

    def set_twin_bed_size(self):
        self.twin_bed_price = 1000

    def get_twin_bed_size(self):
        return self.twin_bed_price


class Deluxe_Room(Room_selection):#inheritance
    def __init__(self, no_of_people, no_of_rooms):
        super().__init__(no_of_people, no_of_rooms)#super class
        self.no_of_people = no_of_people
        self.no_of_rooms = no_of_rooms
        self.price = (Room_selection.get_twin_bed_size(self) + 250) + ((Room_selection.get_twin_bed_size(self) + 250) / Room_selection.get_tax(self)) * 100
        self.price = self.price * self.no_of_rooms
        if self.no_of_people > 2:
            self.price = self.price + self.no_of_people *50
#deluxe room price method
    def get_bed_price(self):#polymorphism
        print("Deluxe room price ;", self.price)


class Luxury_Room(Room_selection):#inheritance
    def __init__(self,no_of_people, no_of_rooms):
        super().__init__(no_of_people, no_of_rooms)#super class
        self.no_of_people = no_of_people
        self.no_of_rooms = no_of_rooms
        self.price = (Room_selection.get_twin_bed_size(self) + 300) + ((Room_selection.get_twin_bed_size(self) + 300) / Room_selection.get_tax(self)) * 100
        self.price = self.price * self.no_of_rooms
        if self.no_of_people > 2:
            self.price = self.price + self.no_of_people * 50
#luxury room price method
    def get_bed_price(self):#polymorphism
        print("Luxury room price", self.price)


class Booking_Information(Luxury_Room,Deluxe_Room,Customer):#multiple inheritance
    def __init__(self,no_of_people, no_of_rooms):
        self.no_of_people = no_of_people
        self.no_of_rooms = no_of_rooms
        super().__init__(no_of_people, no_of_rooms)#super class
        #calling deluxe_room class, Luxury room class and room selection class to print its price based on number of people and number of rooms
        Deluxe_Room.get_bed_price(self)
        Luxury_Room.get_bed_price(self)
        Room_selection.get_bed_price(self)

#creating objects for customer class and room class
customer_1 = Customer(2018,2,29,"Priyanka",2,4,4)
room_preference = Luxury_Room(3,4)
details = Booking_Information(2,3)
