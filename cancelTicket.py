import pandas as pd
import tkinter as tk
from tkinter import messagebox

import bookTicket
import waitlist
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
    #gets the flight's details
    correctFlight = ticketsdf.loc[(ticketsdf["Flight_Number"] == flightNum)]
    #checks that passenger with name {passName} is on flight {flightNum}
    correctName = correctFlight.loc[(correctFlight["Name"] == str(passName))]
    numFound = correctName.shape[0]

    if (numFound == 0):
        #passenger is not on flight
        messagebox.showerror(title="Error", message=f"Unable to find {passName} on flight {flightNum}")
    else:
        #Confirm operation
        askBox = messagebox.askokcancel(title="Confirm", message=f"Confirm cancellation of {passName} for flight {flightNum}")
        if (askBox == True):
            #Cancel the Ticket
            ticketsdf.drop(index=correctName['index'], axis=0, inplace=True)
            ticketsdf.to_csv("tickets.csv",index=False)

            waitlistdf = pd.read_csv("waitlist.csv")
            #Gets passengers on waitlist for flight with same ticket class
            waitlistPass = waitlistdf.loc[(waitlistdf['Flight_Number'] == flightNum)]
            waitlistPass = waitlistPass[(waitlistPass['Class'] == correctName['Class'])]
            print(waitlistPass)


            if (waitlistPass.shape[0] > 0):
                #if passenger has a ticket
                passInfo = waitlistPass.iloc[0]
                addWaitlistPassAskBox = messagebox.askyesno(title="Add From Waitlist?", message="Add Passenger " + passInfo["Name"] + " in waitlist to flight " + str(flightNum))

                if addWaitlistPassAskBox == True:
                    #Add the passenger
                    #Remove the entry from the waitlist
                    bookTicket.BookPassenger(flightnumber=flightNum, ticketclass=passInfo["Class"], name=passInfo["Name"])

                    waitlist.RemoveFromWaitlist(flinum=flightNum, name=passInfo["Name"])

        return