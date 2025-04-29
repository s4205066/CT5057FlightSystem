import pandas as pd
import tkinter as tk
from tkinter import messagebox
#Choose a passenger
#Choose a flight
#If there are passengers on the waitlist, 
#print the name of the next passenger and give the option 
# to schedule that passenger for the available seat

def openCancelWindow():
    window = tk.Tk()

    flightNumberLabel = tk.Label(window, text="Flight Number: ")
    flightNumberLabel.pack()

    flightNumberEntry = tk.Entry(window)
    flightNumberEntry.pack()

    passNameLabel = tk.Label(window, text="Passenger Name: ")
    passNameLabel.pack()

    passNameEntry = tk.Entry(window)
    passNameEntry.pack()

    cancelTicketButton = tk.Button(window, text="Cancel Ticket")
    cancelTicketButton.pack()

def CancelTicket(flightNum, passName):
    ticketsdf = pd.read_csv("flights.csv")

    correctFlight = ticketsdf.loc[(ticketsdf["Flight_Number"] == str(flightNum))]

    correctName = correctFlight.loc[(correctFlight["Name"] == str(passName))]

    numFound = correctName.shape[0]

    if (numFound == 0):
        #none found
        messagebox.showerror(title="Error", message=f"Unable to find {passName} on flight {flightNum}")
    else:
        #confirm
        askBox = messagebox.askokcancel(title="Confirm", message=f"Confirm cancellation of {passName} for flight {flightNum}")
        if (askBox == messagebox.OK):
            #actualltyCancelTicket
            ticketsdf.drop(correctName, inplace=True)
            ticketsdf.to_csv("tickets.csv",index=False)