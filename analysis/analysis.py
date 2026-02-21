import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


DB_PATH = Path("data/rentals.db")


def analyze():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM rentals", conn)
    conn.close()

    print("\n----- ANALYSIS -----")
    print("Total Listings:", len(df))
    print("Average Rent:", df["price"].mean())
    print("Median Rent:", df["price"].median())
    print("Maximum Rent:", df["price"].max())
    print("Minimum Rent:", df["price"].min())
    print(df.groupby("bhk")["price"].mean())

    # Remove extreme outliers for visualization
    df = df[(df["price"] > 8000) & (df["price"] < 200000)]
   

    df["price"].hist(bins=20)
    plt.title("Chennai Rent Distribution")
    plt.xlabel("Rent")
    plt.ylabel("Frequency")
    plt.show()