import pandas as pd
import tkinter as tk
from pandastable import Table, TableModel

def openExplorerWindow(_df, windowTitle="Dataframe"):
    window = tk.Tk()
    window.title(windowTitle)
    
    frame = tk.Frame(window)
    frame.pack()
    
    tbl = Table(frame, dataframe=_df, showtoolbar=True, showstatusbar=True)
    tbl.show()
    
    window.mainloop()

def dispWaitlistInfo(waitlistrow):
    window = tk.Tk()
    window.title("Waitlist Operation")

    passnameLabel = tk.Label(window, text="Passenger Name: " + str(waitlistrow['Name'].to_numpy()[0]))
    passnameLabel.pack()

    flightNumLabel = tk.Label(window, text="Flight Number: "  + str(waitlistrow['Flight_Number'].to_numpy()[0]))
    flightNumLabel.pack()

    ticketClassLabel = tk.Label(window, text="Ticket Class: " + str(waitlistrow['Class'].to_numpy()[0]))
    ticketClassLabel.pack()

    waitlistIndex = tk.Label(window, text="Waitlist Index: " + str(waitlistrow['index'].to_numpy()[0]))
    waitlistIndex.pack()

    window.mainloop()

def dispTicketInfo(ticketrow):
    window = tk.Tk()
    window.title("Waitlist Operation")

    passnameLabel = tk.Label(window, text="Passenger Name: " + str(ticketrow['Name'].to_numpy()[0]))
    passnameLabel.pack()

    flightNumLabel = tk.Label(window, text="Flight Number: "  + str(ticketrow['Flight_Number'].to_numpy()[0]))
    flightNumLabel.pack()

    seatNumberLabel = tk.Label(window, text="Seat Number: " + str(ticketrow['Seat_Number'].to_numpy()[0]))
    seatNumberLabel.pack()

    ticketClassLabel = tk.Label(window, text="Ticket Class: " + str(ticketrow['Class'].to_numpy()[0]))
    ticketClassLabel.pack()

    window.mainloop()
