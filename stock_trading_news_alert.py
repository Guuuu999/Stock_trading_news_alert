import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

twilio_sid = "ACefb8ff21992d2206910ec4e272392f4f"
twilio_autho_token = "430a030da14d1611181ebf940365f53e"

stock_api = "WNDUWBDO0Q7O09O0"
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": stock_api,
}
response = requests.get(STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in stock_data.items()]
print(data_list)
yesterday_data = data_list[0]
closing_price1 = float(yesterday_data["4. close"])
print(closing_price1)

day_before_data = data_list[1]
closing_price2 = float(day_before_data["4. close"])
print(closing_price2)

pos_difference = round(abs(closing_price1 - closing_price2), 2)
print(pos_difference)

percent_diff = (pos_difference/closing_price1) * 100

if percent_diff > 5:
    print("Get news")

news_api = "d4471affdf894574b08f0d8d8432ec60"
param_news = {
    "q": COMPANY_NAME,
    "apikey": news_api,
}
response = requests.get(NEWS_ENDPOINT, params=param_news)
response.raise_for_status()
news_data = response.json()

articles = news_data["articles"]
three_articles = articles[:3]
print(three_articles)

head_des_list = [f"Headline: {article['title']}\nBrief: {article['description']}" for article in three_articles]
print(head_des_list)

client = Client(twilio_sid, twilio_autho_token)
for article in head_des_list:
    message = client.messages.create(
        body="sms_event_notifications",
        from_="+17372583478",
        to="+16462885909",
    )

    print(message.body)


