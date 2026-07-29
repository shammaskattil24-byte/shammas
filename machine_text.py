bookings = {}

def book_room(bookings):
    room_no = input("Enter the room number ")
    if room_no in bookings:
        print("thr room is already booked")
        return
    guest_name = input("Enter the guest name")
    room_type = input("Enter the room type you want to book")
    days = int(input("Enter the number of days you want to book"))
    while days <= 0:
        days = int(input("Enter the number of days"))
    total_price = float(input("Enter the tatal price"))
    while total_price <= 0:
        total_price = float(input("Enter the total price"))
    bookings[room_no] = {
        "guest name": guest_name,"room type": room_type,"number of days": days,"total price": total_price
    }
    print("the room booked successfully")




def view_bookings(bookings):
    if not bookings:
        print("there id no booking records found")
        return
    for room_no, details in bookings.items():
        print("room number", room_no)
        print("guest name", details["guest name"])
        print("room type", details["room type"])
        print("number of days", details["number of days"])
        print("total price", details["total price"])




def search_booking(bookings):
    room_no = input("Enter the room number you want to search")
    if room_no in bookings:
        details = bookings[room_no]

        print("room number", room_no)
        print("guest name", details["guest name"])
        print("room type", details["room type"])
        print("number of days", details["number of days"])
        print("total price", details["total price"])
    else:
        print("booking is not found")




def update_booking(bookings):
    room_no = input("Enter the room number you wqnt to update")
    if room_no in bookings:
        days = int(input("Enter the number of days you want to update"))
        while days <= 0:
            days = int(input("Enter the number of days you want to update"))
        bookings[room_no]["number of days"] = days
        print("number of days are updated successfully")
    else:
        print("booking is not found")


def cancel_booking(bookings):
    room_no = input("Enter the room number rou want to cancel")
    if room_no in bookings:
        del bookings[room_no]
        print("booking cancelled successfully")
    else:
        print("booking is not found")


while True:
    print("1,book a room")
    print("2,view bookings")
    print("3,search bookings")
    print("4,update bookings")
    print("5,cancel bookings")
    print("6,exit")

    choice = int(input("Enter your choice"))
    if choice == 1:
        book_room(bookings)
    elif choice == 2:
        view_bookings(bookings)
    elif choice == 3:
        search_booking(bookings)
    elif choice == 4:
        update_booking(bookings)
    elif choice == 5:
        cancel_booking(bookings)
    elif choice == 6:
        print("exiting the program")
        break
    else:
        print("invalid choice please try again")