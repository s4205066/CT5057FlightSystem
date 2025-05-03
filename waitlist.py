import tkinter as tk
from tkinter import messagebox
import pandas as pd
import customWindows

def openWaitlistWindow():
    waitlistWindow = tk.Toplevel()
    
    entryLabel = tk.Label(waitlistWindow, text="Flight Number: ")
    entryLabel.pack()

    entryBar = tk.Entry(waitlistWindow)
    entryBar.pack()

    removeFlightsButton = tk.Button(waitlistWindow, text="Remove Departed Flight", command=lambda: RemoveDepartedFlights(waitlistdf=pd.read_csv("waitlist.csv"), flightnum=entryBar.get()))
    removeFlightsButton.pack()

    checkWaitlistButton = tk.Button(waitlistWindow, text="Check Waitlist", command=lambda: CheckWaitlist(pd.read_csv("waitlist.csv"), entryBar.get()))
    checkWaitlistButton.pack()

def AddToWaitlist(flinum, ticclass, name):
    waitlistdf = pd.read_csv('waitlist.csv')
    #newwaitlistID = waitlistdf.iloc[dfrows]['index']
    newRow = pd.DataFrame({"index": [len(waitlistdf)], "Flight_Number": [flinum], "Class": [ticclass], "Name": [name]})
    waitlistdf = pd.concat([waitlistdf, newRow], ignore_index=False)

    try:
        waitlistdf.to_csv('waitlist.csv', index=False)
        successmsg = f"Passenger {name} is on the waitlist for a {ticclass} ticket for flight {flinum}"#\n WaitlistID: {newwaitlistID}"
        messagebox.showinfo(title="Waitlist Operation", message=successmsg)
    except:
        messagebox.showerror(title="Waitlist Error", message="Error!")
    return



def RemoveFromWaitlist(flinum, name):
    waitlistdf = pd.read_csv('waitlist.csv')
    correctrows = waitlistdf.loc[(waitlistdf['Flight_Number'] == flinum) & (waitlistdf['Name'] == name)]

    #if only 1 ticket under name on flight
    #remove immediately
    if (correctrows.shape[0] == 1):
        waitlistindex = correctrows['index']
        waitlistdf.drop(waitlistindex, axis=0, inplace=True)

        try:
            waitlistdf.to_csv("waitlist.csv", index=False)
            messagebox.showinfo(title="Waitlist Operation", message=f"Removed {name} from waitlist for flight {flinum}")
        except:
            messagebox.showerror(title="Waitlist Error", message="Failed to save waitlist operation.")
    # if more than one passsenger shares a name
    # WaitlistID is required
    else:
        messagebox.showwarning(title="Operation Interruption", message=f"More than 1 ticket for {name} for flight {flinum}\n Confirm WaitlistID")
        selectWindow = tk.Toplevel()

        waitIDLabel = tk.Label(selectWindow, text="WaitlistID:")
        waitIDLabel.pack()
        waitIDEntry = tk.Entry(selectWindow)
        waitIDEntry.pack()

        confirmButton = tk.Button(selectWindow, text="Confirm", command=lambda: RemoveFromWaitlist(waitlistdf=waitlistdf, correctrows=correctrows, waitlistID=waitIDEntry.get()))
        confirmButton.pack()

        

def RemoveFromWaitlist(waitlistdf, correctrows, waitlistID):
    row = (correctrows.loc['index'] == waitlistID)
    waitlistdf.drop(row, axis=0, inplace=True) 

    try:
        waitlistdf.to_csv("waitlist.csv", index=False)
        messagebox.showinfo(title="Waitlist Operation", message=f"Removed {waitlistID} from waitlist:\n Passenger: {row["Name"]}, Class: {row["Class"]}, Flight: {row["Flight_Number"]}")
    except:
        messagebox.showerror(title="Waitlist Error", message="Failed to complete waitlist operation.")



def RemoveDepartedFlights(waitlistdf, flightnum):
    rows = (waitlistdf.loc[waitlistdf['Flight_Number'] == flightnum])
    print(rows)
    waitlistdf = waitlistdf.drop(rows['index'], axis=0)

    recordsLen = len(rows)

    #print(waitlistdf.columns[0])

    try:
        #waitlistdf.drop(waitlistdf.columns[0], axis=0, inplace=True)
        waitlistdf.to_csv("waitlist.csv", index=False)
        messagebox.showinfo(title="Waitlist Operation", message=f"Removed {recordsLen} waitlist records for flight {flightnum} from waitlist")
    except:
        messagebox.showerror(title="Waitlist Error", message="Failed to complete waitlist operation.")



def CheckWaitlist(waitlistdf, flightnum=None):
    rows = []
    
    if (flightnum != None):
        rows = (waitlistdf.loc[waitlistdf['Flight_Number'] == flightnum])
    else:
        rows = waitlistdf
    
    customWindows.openExplorerWindow(rows, "Waitlist")

#if __name__ == "__main__":
#    CheckWaitlist(pd.read_csv("waitlist.csv"))