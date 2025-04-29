import pandas as pd
import tkinter as tk
import customWindows
#print departure airport
#departure date
#arrival airport
#list of all seats
#all names of passengers in seats



def findFlightPassengers(ticketsdf, flightnum):
    tickets = (ticketsdf.loc[ticketsdf['Flight_Number'] == flightnum])
    customWindows.openExplorerWindow(tickets, "Tickets for flight " + str(flightnum))

def getFlightDetails(flightsdf, flightnum):
    flight = (flightsdf.loc[flightsdf['Flight_Number'] == flightnum])
    customWindows.openExplorerWindow(flight, "Flight Information")

def OpenFlightInfoWin(flightsdf, ticketsdf):
    flightWindow = tk.Tk()
    
    flightNumLabel = tk.Label(flightWindow, text="Flight Number:")
    flightNumLabel.pack()

    flightNumEntry = tk.Entry(flightWindow)
    flightNumEntry.pack()

    getDetailsButton = tk.Button(flightWindow, text="Get Flight Details", command=lambda: getFlightDetails(flightsdf, flightNumEntry.get()))
    getDetailsButton.pack()

    getPassButton = tk.Button(flightWindow, text="Get Passengers", command=lambda: findFlightPassengers(ticketsdf, flightNumEntry.get()))
    getPassButton.pack()

