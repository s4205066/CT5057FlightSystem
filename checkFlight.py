import pandas as pd
import tkinter as tk
import customWindows
#print departure airport
#departure date
#arrival airport
#list of all seats
#all names of passengers in seats



def findFlightPassengers(flightnum):
    #Gets and returns all passengers for flight number {flightnum}
    ticketsdf = pd.read_csv("tickets.csv")
    print("FliNum = " + str(flightnum))
    print(str(ticketsdf['Flight_Number']))
    tickets = (ticketsdf.loc[ticketsdf['Flight_Number'] == flightnum])
    print("Tickets:" + str(tickets))
    return tickets

def getFlightDetails(flightsdf, flightnum):
    flight = (flightsdf.loc[flightsdf['index'] == flightnum])
    tickets = findFlightPassengers(flightnum=flightnum)
    customWindows.dispFlightPassInfo(flight=flight, passengersDF=tickets)

def OpenFlightInfoWin():
    flightsdf = pd.read_csv("flights.csv")
    flightWindow = tk.Toplevel()
    flightWindow.title("Flight Search")
    flightWindow.geometry("300x300")
    
    flightNumLabel = tk.Label(flightWindow, text="Flight Number:")
    flightNumLabel.pack()

    flightNumEntry = tk.Entry(flightWindow)
    flightNumEntry.pack()

    getDetailsButton = tk.Button(flightWindow, text="Get Flight Details", command=lambda: getFlightDetails(flightsdf, int(flightNumEntry.get())))
    getDetailsButton.pack()

