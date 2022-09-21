import requests


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
api_key = "XXXXXXXX"
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": api_key

}

STOCK_ENDPOINT = "https://www.alphavantage.co/query"

stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
print(stock_data)

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "XXXXXXXXX"
news_parameters = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
    "language": "en",
    "sortBy": "publishedAt",
    "searchIn": "description"

}

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

data_list = [value for (key, value) in stock_data.items()]
print(data_list)
yesterday_data = data_list[0]
before_yesterday_data = data_list[1]
yesterday_closing_price = float(yesterday_data["4. close"])
print(yesterday_closing_price)

#Get the day before yesterday's closing stock price

before_yesterday_data = data_list[1]
before_yester_closing_price = float(before_yesterday_data["4. close"])
print(before_yester_closing_price)

#Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

stock_price_diff = abs(yesterday_closing_price - before_yester_closing_price)
print(stock_price_diff)

#Work out the percentage difference in price between closing price yesterday and closing price the day
#  before yesterday.

percentage_difference_in_price = round((stock_price_diff / (float(before_yester_closing_price)) * 100))
print(percentage_difference_in_price)

# If percentage is greater than 5 then print("Get News").

up_down = None
if percentage_difference_in_price > 0.01:
    up_down = "🔺"
else:
    up_down = "🔻"


news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
news_response.raise_for_status()
articles = news_response.json()["articles"]
print(articles)




# Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
three_articles = articles[:3]
print(three_articles)


#Create a new list of the first 3 article's headline and description using list comprehension.

formatted_articles_list = [f"{STOCK_NAME}: {up_down}{percentage_difference_in_price}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
print(formatted_articles_list)








