import pandas as pd
import tkinter as tk
from tkinter import messagebox
#Choose a passenger
#Choose a flight
#If there are passengers on the waitlist, 
#print the name of the next passenger and give the option 
# to schedule that passenger for the available seat

def openCancelWindow():
    window = tk.Toplevel()
    window.geometry("300x300")
    window.title("Cancel Ticket")

    flightNumberLabel = tk.Label(window, text="Flight Number: ")
    flightNumberLabel.pack()

    flightNumberEntry = tk.Entry(window)
    flightNumberEntry.pack()

    passNameLabel = tk.Label(window, text="Passenger Name: ")
    passNameLabel.pack()

    passNameEntry = tk.Entry(window)
    passNameEntry.pack()

    cancelTicketButton = tk.Button(window, text="Cancel Ticket", command=lambda:CancelTicket(flightNum=int(flightNumberEntry.get()), passName=passNameEntry.get()))
    cancelTicketButton.pack()

def CancelTicket(flightNum, passName):
    ticketsdf = pd.read_csv("tickets.csv")

    correctFlight = ticketsdf.loc[(ticketsdf["Flight_Number"] == flightNum)]

    correctName = correctFlight.loc[(correctFlight["Name"] == str(passName))]

    numFound = correctName.shape[0]

    if (numFound == 0):
        #none found
        messagebox.showerror(title="Error", message=f"Unable to find {passName} on flight {flightNum}")
    else:
        #confirm
        askBox = messagebox.askokcancel(title="Confirm", message=f"Confirm cancellation of {passName} for flight {flightNum}")
        if (askBox == True):
            #actualltyCancelTicket

            ticketsdf.drop(index=correctName['index'], axis=0, inplace=True)
            ticketsdf.to_csv("tickets.csv",index=False)
            
        return