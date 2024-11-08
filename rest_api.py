import requests
import pandas as pd
import json
from bs4 import BeautifulSoup
import requests
import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def make_graph(stock_data, revenue_data, stock):
    # Get historical data and reset index to access 'Date' column
    stock_data_specific = stock_data.history(period="max").reset_index()
    # Filter data by date
    stock_data_specific = stock_data_specific[stock_data_specific['Date'] <= '2021-06-14']
    # Create the plot
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
                        subplot_titles=("Historical Share Price", "Historical Revenue"),
                        vertical_spacing=0.3)
# Your plotting code goes here
    fig.show()

tesla_stock = yf.Ticker('TSLA')
print(tesla_stock)
tesla_data = tesla_stock.history(period="max")
tesla_data.reset_index(inplace=True)
tesla_data.head(5)


html_data = requests.get("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm").text
soup = BeautifulSoup(html_data, "html.parser")
dates = []
revenues = []
#for row in soup.find_all('tr'):
 #   cols = row.find_all('td')
  #  if len(cols) >= 2:  # Ensure there are at least two columns
   #     dates.append(cols[0].text.strip())
    #    revenues.append(cols[1].text.strip())

tesla_revenue = pd.DataFrame({'Date': dates, 'Revenue': revenues})
#print(tesla_revenue)
#print(tesla_revenue.tail(5))

gme_stock = yf.Ticker('GME')
gme_stock.history(period="max")
print(gme_stock)


html_data2 = requests.get("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html").text
soup2 = BeautifulSoup(html_data2, "html5lib")
dates1 = []
revenues1 = []
for row in soup2.find_all('tr'):
    cols = row.find_all('td')
    if(len(cols)) >=2:
        dates1.append(cols[0].text.strip())
        revenues1.append(cols[1].text.strip())
gme_revenue = pd.DataFrame({'Dates':dates1, 'Revenues':revenues1})
print(gme_revenue.tail(5))
make_graph(gme_stock,gme_revenue,'GameStop')













