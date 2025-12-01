import sqlite3
import random
import matplotlib.pyplot as plt

def create_database(db_name="population_LP.db"):
    """
    Create (or open) the database and the population table.
    Also insert base data for the year 2023.
    """
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS population (
            city TEXT NOT NULL,
            year INTEGER NOT NULL,
            population INTEGER NOT NULL
        )
    """)

    cities_2023 = {
        "Miami": 456000,
        "Orlando": 312000,
        "393389": 410000,
        "Jacksonville": 962000,
        "Tallahassee": 202000,
        "St. Petersburg": 261000,
        "Fort Lauderdale": 183000,
        "Gainesville": 355000,
        "Sarasota": 56000,
        "Pensacola": 54000
    }

    cur.execute("DELETE FROM population WHERE year = 2023")

    for city, pop in cities_2023.items():
        cur.execute(
            "INSERT INTO population (city, year, population) VALUES (?, ?, ?)",
            (city, 2023, pop)
        )

    conn.commit()
    print("Database created and 2023 data inserted.")
    return conn 

def simulate_population_growth(conn, start_year=2024, years=20):
    """
    Simulate population growth/decline for all cities in the table,
    starting from start_year, for 'years' years, and insert results.
    Each year and city gets its own random growth rate.
    """
    cur = conn.cursor()


    cur.execute("SELECT city, population FROM population WHERE year = 2023")
    base_data = cur.fetchall()

    if not base_data:
        print("No base data found for 2023. Make sure to run create_database() first.")
        return


    random.seed(42)


    cur.execute("DELETE FROM population WHERE year >= ?", (start_year,))

    for city, pop_2023 in base_data:
        current_population = pop_2023

        for year in range(start_year, start_year + years):

            growth_rate = random.uniform(-0.02, 0.03)
            current_population = int(current_population * (1 + growth_rate))

            cur.execute(
                "INSERT INTO population (city, year, population) VALUES (?, ?, ?)",
                (city, year, current_population)
            )

    conn.commit()
    print(f"Simulated population from {start_year} to {start_year + years - 1}.")

def show_city_population_growth(conn):
    """
    Show the population growth graph for a city chosen by the user.
    """
    cur = conn.cursor()

    cur.execute("SELECT DISTINCT city FROM population ORDER BY city")
    cities = [row[0] for row in cur.fetchall()]

    if not cities:
        print("No city data found. Make sure to create the database and simulate growth first.")
        return

    print("Available cities:")
    for idx, city in enumerate(cities, start=1):
        print(f"{idx}. {city}")

    choice = input("Enter the number of the city you want to see: ")
    try:
        choice_index = int(choice) - 1
        if choice_index < 0 or choice_index >= len(cities):
            print("Invalid choice.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    selected_city = cities[choice_index]
    print(f"You selected: {selected_city}")

    cur.execute(
        "SELECT year, population FROM population WHERE city = ? ORDER BY year",
        (selected_city,)
    )
    rows = cur.fetchall()

    if not rows:
        print("No population data found for that city.")
        return

    years = [row[0] for row in rows]
    pops = [row[1] for row in rows]

    plt.figure()
    plt.plot(years, pops, marker="o")
    plt.title(f"Population Growth: {selected_city}")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():

    conn = create_database("population_LP.db")

    simulate_population_growth(conn, start_year=2024, years=20)

    show_city_population_growth(conn)

    conn.close()


if __name__ == "__main__":
    main()
