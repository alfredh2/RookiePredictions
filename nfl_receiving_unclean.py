import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# Function to scrape data for a given year
def scrape_year(year):
    url = f'https://www.pro-football-reference.com/years/{year}/receiving.htm'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table with player stats
    table = soup.find('table', {'id': 'receiving'})

    # Extract the correct table headers
    if year == 2010:  # Extract headers only once
        header_row = table.find('thead').find('tr')
        headers = [th.get_text() for th in header_row.find_all('th')]
        headers.remove(headers[0])
        scrape_year.headers = headers  # Store headers as a function attribute

    # Extract the table rows
    rows = table.find('tbody').find_all('tr')
    
    # Extract the table data
    data = []
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        if cols:  # Only add rows that contain data
            # Remove asterisk from player names (assuming the name is in the first column)
            cols[0] = re.sub(r'[\*\+]', '', cols[0])
            cols.append(year)  # Add the year as the last column
            data.append(cols)

    return data

# List of years to scrape
years = list(range(2010, 2024))

# Scrape data for all years and combine into a single DataFrame
all_data = []
for year in years:
    year_data = scrape_year(year)
    all_data.extend(year_data)

# Create a DataFrame
headers = scrape_year.headers + ['Year']  # Add 'Year' to the headers
df = pd.DataFrame(all_data, columns=headers)

# Save the DataFrame to a CSV file
df.to_csv('nfl_receiving_unclean.csv', index=False)