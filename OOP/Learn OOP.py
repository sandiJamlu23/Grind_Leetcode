'''
View available tables

Book a table for a specific time

Cancel a booking

Show current bookings

'''
class Table(object):
    def __init__(self, table_id, seats):
        self.table_id = table_id
        self.seats = seats
        self.booked = False
        self.booking_info = None

    def book(self, name, time):
        # this is for the name and time for ordered table
        if self.booked:
            return print(f"Table {self.table_id} has been booked")
        
        self.booked = True
        self.booking_info = {"name": name, "time":time}
        return f"Table {self.table_id} booked for {name} at {time}"
           
    def cancel_booking(self):
        if not self.booked:
            return f"Table {self.table_id} is not booked yet"
        
        self.booked = False
        self.booking_info = None
        return f"Booking for Table {self.table_id} has been canceled."

    def __str__(self):
        status = "Booked" if self.booked else "Available"
        return f"Table {self.table_id} ({self.seats} seats) - {status}"

class BookingSystem:
    def __init__(self):
       self.tables = []
    def add_table(self, table):
       self.tables.append(table)

    def show_tables(self):
        for table in self.tables:
            print(table)

    def book_table(self, table_id, name, time):
        for table in self.tables:
            if table.table_id == table_id:
                return table.book(name, time)
        return f"Table {table_id} not found"

    def cancel_table(self, table_id):
        for table in self.tables:
            if table.table_id == table_id:
                return table.cancel_booking()
        return f"Table {table_id} not found."


if __name__ == "__main__":
    system = BookingSystem()
    
    # Create 3 tables
    system.add_table(Table(1, 2))
    system.add_table(Table(2, 4))
    system.add_table(Table(3, 6))

    print("\n--- All Tables ---")
    system.show_tables()

    print("\n--- Booking Table 2 ---")
    print(system.book_table(2, "Sandi", "7 PM"))

    print("\n--- Booking Table 2 Again ---")
    print(system.book_table(2, "Alex", "8 PM"))

    print("\n--- Cancel Table 2 ---")
    print(system.cancel_table(2))

    print("\n--- All Tables After Updates ---")
    system.show_tables()

