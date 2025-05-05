import tkinter as tk
import pandas as pd
import bookTicket, checkPassenger, checkFlight, waitlist, cancelTicket


def main():
    mainWindow = tk.Tk()
    mainWindow.title("Main Menu")
    mainWindow.geometry("300x300")

    bookPassButton = tk.Button(mainWindow, text="Book Passenger", command=lambda: bookTicket.OpenBookingWindow())
    bookPassButton.pack()

    checkPassButton = tk.Button(mainWindow, text="Check Passenger", command=lambda: checkPassenger.OpenPassInfoWin())
    checkPassButton.pack()

    checkFlightButton = tk.Button(mainWindow, text="Check Flight", command=lambda: checkFlight.OpenFlightInfoWin())
    checkFlightButton.pack()

    waitlistButton = tk.Button(mainWindow, text="Waitlist Functions", command=lambda: waitlist.openWaitlistWindow())
    waitlistButton.pack()

    cancelTicketButton = tk.Button(mainWindow, text="Cancel Ticket", command=lambda:cancelTicket.openCancelWindow())
    cancelTicketButton.pack()

    mainWindow.mainloop()



if __name__ == "__main__":
    main()