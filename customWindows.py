import pandas as pd
import tkinter as tk
from pandastable import Table, TableModel

#Used to display information straight from a pandas.DataFrame
def openExplorerWindow(_df, windowTitle="Dataframe"):
    window = tk.Toplevel()
    window.title(windowTitle)
    window.geometry("300x300")
    
    frame = tk.Frame(window)
    frame.pack()
    
    tbl = Table(frame, dataframe=_df, showtoolbar=True, showstatusbar=True)
    tbl.show()
    
    window.mainloop()

#displays a window with flight info (Departure, Arrival, Time, Date) and all passengers with a ticket for flight (openExplorerWindow)
def dispFlightPassInfo(flight, passengersDF):
    window = tk.Toplevel()
    window.title("Flight Information")
    window.geometry("500x300")

    window.title("Flight " + str(flight["index"]) + " Details")
    
    depPort = flight["Source"].values[0] 
    depDate = flight["Date_of_Journey"].values[0] 
    depTime = flight["Dep_Time"].values[0] 
    arrPort = flight["Destination"].values[0] 

    depPortLabel = tk.Label(window, text="Departure Port: " + str(depPort))
    depPortLabel.pack()
    depDateLabel = tk.Label(window, text="Date: " + str(depDate))
    depDateLabel.pack()
    depTimeLabel = tk.Label(window, text="Time: " + str(depTime))
    depTimeLabel.pack()
    arrPortLabel = tk.Label(window, text="Arrival Port: " + str(arrPort))
    arrPortLabel.pack()

    passLabel = tk.Label(window, text="Passengers:")
    passLabel.pack()

    frame = tk.Frame(window)
    frame.pack()
    
    passtbl = Table(frame, dataframe=passengersDF, showtoolbar=True, showstatusbar=True)
    passtbl.show()

    window.mainloop()

#Displays information when CheckPassenger finds a waitlist entry
def dispWaitlistInfo(waitlistrow):
    window = tk.Toplevel()
    window.geometry("300x300")
    window.title("Waitlist Passenger")

    passnameLabel = tk.Label(window, text="Passenger Name: " + str(waitlistrow['Name'].to_numpy()[0]))
    passnameLabel.pack()

    flightNumLabel = tk.Label(window, text="Flight Number: "  + str(waitlistrow['Flight_Number'].to_numpy()[0]))
    flightNumLabel.pack()

    ticketClassLabel = tk.Label(window, text="Ticket Class: " + str(waitlistrow['Class'].to_numpy()[0]))
    ticketClassLabel.pack()

    waitlistIndex = tk.Label(window, text="Waitlist Index: " + str(waitlistrow['index'].to_numpy()[0]))
    waitlistIndex.pack()

    window.mainloop()

#Displays information when CheckPassenger finds a ticket entry
def dispTicketInfo(ticketrow):
    window = tk.Toplevel()
    window.geometry("300x300")
    window.title("Passenger Ticket")

    passnameLabel = tk.Label(window, text="Passenger Name: " + str(ticketrow['Name'].to_numpy()[0]))
    passnameLabel.pack()

    flightNumLabel = tk.Label(window, text="Flight Number: "  + str(ticketrow['Flight_Number'].to_numpy()[0]))
    flightNumLabel.pack()

    seatNumberLabel = tk.Label(window, text="Seat Number: " + str(ticketrow['Seat_Number'].to_numpy()[0]))
    seatNumberLabel.pack()

    ticketClassLabel = tk.Label(window, text="Ticket Class: " + str(ticketrow['Class'].to_numpy()[0]))
    ticketClassLabel.pack()

    window.mainloop()
