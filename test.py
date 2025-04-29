import pandas as pd

def main():
    df = pd.read_csv("flights.csv")
    print(df.columns)

    df2 = pd.read_csv("tickets.csv")
    print(df2.columns)

if __name__ == "__main__":
    main()