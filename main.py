from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
import csv
import requests
import grab
import clean
import update


NYT_dict = {}

month_dict = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12
}

if __name__ == '__main__':

    # Grab the json data
    soup1 = grab.grab_data()

    # Extract data from soup
    date, ranks, names, times = grab.create_data(soup1)

    # Clean the incoming data
    rev_rank, rev_name, rev_time = clean.clean_data(date, ranks, names, times)

    # Creation of the date - this gets manual
    date_comps = date[0].split(",")
    date_day = date_comps[0]

    date_month_day = date_comps[1][1:]
    date_month_day_comps = date_month_day.split(" ")
    date_month = date_month_day_comps[0]
    date_date = date_month_day_comps[1]

    date_year = date_comps[2][1:]

    dt_month = month_dict[date_month]

    # month / day / year
    final_date = str(dt_month) + "/" + date_date + "/" + date_year

    date_list = update.update_dict(rev_rank, rev_name, rev_time)

    # Create dict
    NYT_dict['date'] = final_date

    i = 0
    for rank in rev_rank:
        NYT_dict[rank] = date_list[i]
        i+=1

    # Check
    print(NYT_dict)

    # Write to csv
    w = csv.writer(open("Times.csv", "a+"))
    for key, val in NYT_dict.items():
        w.writerow([key, val])






