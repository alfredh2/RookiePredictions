import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape data for a given year
def scrape_year(year):
    url = f'https://www.sports-reference.com/cfb/years/{year}-receiving.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table with player stats
    table = soup.find('table', {'id': 'receiving'})

    # Extract the correct table headers
    if year == 2007:  # Extract headers only once
        header_row = table.find('thead').find_all('tr')[1]  # Skip the first header row
        headers = [th.get_text() for th in header_row.find_all('th')]
        headers[-4:] = [header + '_S' for header in headers[-4:]]
        headers[-8:-4] = [header + '_R' for header in headers[-8:-4]]
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
            cols[0] = cols[0].rstrip('*')
            cols.append(year)  # Add the year as the last column
            data.append(cols)

    return data

# List of years to scrape
years = list(range(2007, 2023))

# Scrape data for all years and combine into a single DataFrame
all_data = []
for year in years:
    year_data = scrape_year(year)
    all_data.extend(year_data)

# Create a DataFrame
headers = scrape_year.headers + ['Year']  # Add 'Year' to the headers
df = pd.DataFrame(all_data, columns=headers)

# Save the DataFrame to a CSV file
df.to_csv('college_receiving_unclean.csv', index=False)