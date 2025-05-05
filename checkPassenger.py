import tkinter as tk
import pandas as pd
import customWindows
#choose a passenger
#if the passenger is scheduled for a flight, print flight information
#if passenger is on waitlist, print flight info and passengers position on waitlist



def OpenPassInfoWin():
    window = tk.Toplevel()
    window.geometry("300x300")
    window.title("Check Passenger")

    passNameLabel = tk.Label(window, text="Passenger Name:")
    passNameLabel.pack()
    passNameEntry = tk.Entry(window)
    passNameEntry.pack()

    checkInfoButton = tk.Button(window, text="Check Info", command=lambda: CheckPassInfo(passname=passNameEntry.get()))
    checkInfoButton.pack()

    window.mainloop()

def CheckPassInfo(passname):
    ticketdf = pd.read_csv("tickets.csv")
    waitlistdf = pd.read_csv("waitlist.csv")

    
    #Get all tickets with name {passname}
    foundTickets = ticketdf.loc[(ticketdf['Name'] == str(passname))]
    print("FoundTickets =")
    print(foundTickets)

    if (foundTickets.shape[0] == 1):
        #1 passenger with name {passname} has a ticket
        customWindows.dispTicketInfo(foundTickets)
        return
    elif(foundTickets.shape[0] > 1):
        #Multiple passengers with name {passname} has a ticket
        #Opens window with all passengers found with passName
        print("Duplicate passengers found in tickets")
        customWindows.openExplorerWindow(foundTickets, windowTitle="Tickets")
        return
    

    #If code runs to here, passenger with {passName} is NOT in ticketsdf
    #Look for passenger in the waitlist
    waitlistPass = waitlistdf.loc[(waitlistdf['Name'] == str(passname))]
    print("waitlistPass =")
    print(waitlistPass)

    if (waitlistPass.shape[0] > 0):
        #pasenger found in ticketsdf
        customWindows.dispWaitlistInfo(waitlistPass)
        return
    elif(waitlistPass.shape[0] > 1):
        print("Duplicate passengers found in waitlist")
        customWindows.openExplorerWindow(waitlistPass, windowTitle="Waitlist")
        return


if __name__ == "__main__":
    OpenPassInfoWin(pd.read_csv("tickets.csv"), pd.read_csv("waitlist.csv"))