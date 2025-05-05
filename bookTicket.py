import tkinter as tk
from tkinter import messagebox
import pandas as pd

import waitlist
# choose flight
# choose seat class
# if seats are full, offer to put onto waitlist
## waitlist is individual for each class

#Each flight has 10 first class, 40 business class, and 120 economy class seats.

def OpenBookingWindow():
    fliNumWindow = tk.Toplevel()
    fliNumWindow.title("Booking")
    fliNumWindow.geometry("300x300")

    fliNumLabel = tk.Label(fliNumWindow, text="Flight Number: ")
    fliNumLabel.pack()
    fliNumEntry = tk.Entry(fliNumWindow)
    fliNumEntry.pack()

    getFlightButton = tk.Button(fliNumWindow, text="Check for flight", command=lambda: SearchFlight(flightNumber=fliNumEntry.get()))
    getFlightButton.pack()

    fliNumWindow.mainloop()


def SearchFlight(flightNumber):
    #Gets flight information, given the flightNumber
    flightdf = pd.read_csv("flights.csv")
    if ((flightdf.loc[flightdf['index']] == flightNumber).shape[0] > 0):
        #Flight with that number has been found
        customerWindow = tk.Toplevel()
        customerWindow.geometry("300x300")
        customerWindow.title("Book Ticket")

        fliNumLabel = tk.Label(customerWindow, text="Flight Number: " + str(flightNumber))
        fliNumLabel.pack()

        nameLabel = tk.Label(customerWindow, text="Customer Name:")
        nameLabel.pack()
        nameEntry = tk.Entry(customerWindow)
        nameEntry.pack()

        classLabel = tk.Label(customerWindow, text="Ticket class:")
        classLabel.pack()

        ticketClass = tk.StringVar()

        #Updates when a first/business/economy class button is pressed
        def update(value):
            selection = "Ticket Class: " + value
            classLabel.config(text = selection)
            ticketClass.set(value=value)
        
        firstRButton = tk.Radiobutton(customerWindow, text="First Class", value='First', variable=ticketClass, command=lambda: update('First'))
        firstRButton.pack()
        businessRButton = tk.Radiobutton(customerWindow, text="Business Class", value='Business', variable=ticketClass, command=lambda: update('Business'))
        businessRButton.pack()
        economyRButton = tk.Radiobutton(customerWindow, text="Economy Class", value='Economy', variable=ticketClass, command=lambda: update('Economy'))
        economyRButton.pack()

        bookTicketButton = tk.Button(customerWindow, text="Book Ticket", command=lambda: BookPassenger(flightnumber=flightNumber, ticketclass=ticketClass.get(), name=nameEntry.get()))
        bookTicketButton.pack()

        customerWindow.mainloop()

    else:
        #Shows when flightnumber is invalid
        messagebox.showerror(title="Booking Error", message=f"Unable to find flight: {flightNumber}")
    
def BookPassenger(flightnumber, ticketclass, name):
    ticketdf = pd.read_csv('tickets.csv')
    nextIndex = ticketdf.shape[0]

    seatNumber = getNextValidSeat(ticketdf, flightnumber, ticketclass)

    if (seatNumber == -1):
        #Couldn't find a seat for class on flight
        #offer to place the passenger on waitlist
        waitlistBox = messagebox.askquestion("No Seat Found", f"No {ticketclass} class seat found for flight {flightnumber}. Add to waitlist?")

        if (waitlistBox == messagebox.YES):
            waitlist.AddToWaitlist(flightnumber, ticketclass, name)
            return
        elif (waitlistBox == messagebox.NO):
            return
    
    newTicket = pd.DataFrame([{'index': nextIndex, 'Flight_Number': flightnumber, 'Seat_Number': seatNumber, 'Class': ticketclass, 'Name': str(name)}], columns=['index','Flight_Number','Seat_Number','Class','Name'])
    ticketdf = pd.concat([ticketdf, newTicket], ignore_index=True)

    try:
        ticketdf.to_csv('tickets.csv', index=False)
        successmsg = f"Passenger {name} is booked for a(n) {ticketclass} ticket for flight {flightnumber}"
        messagebox.showinfo(title="Waitlist Operation", message=successmsg)
    except:
        #Error catching
        messagebox.showerror(title="Waitlist Error", message="Error!")

    return

def getNextValidSeat(ticketsdf, flightnum, ticketclass):
    flightTickets = (ticketsdf.loc[(ticketsdf['Flight_Number'] == int(flightnum))])
    print("ticketclass = " + ticketclass)
    classSeatsBooked = (flightTickets.loc[(flightTickets['Class'] == str(ticketclass))])

    #print("classSeatsBooked = ")
    #print(classSeatsBooked)

    startseat = 0
    endseat = 0
    match str(ticketclass):
        case "First":
            startseat = 1
            endseat = 10
        case "Business":
            startseat = 11
            endseat = 50
        case "Economy":
            startseat = 51
            endseat = 170

    for i in range((endseat-startseat) + 1):
        foundTicket = classSeatsBooked.loc[classSeatsBooked['Seat_Number'] == i+startseat]
        if (foundTicket.shape[0] == 0):
            #seat isnt booked
            print("Seat " + str(i+startseat) + " is available")
            return i+startseat
        
        #print(foundTicket)
        #print(foundTicket.shape)

    return -1

if __name__ == "__main__":
    OpenBookingWindow()