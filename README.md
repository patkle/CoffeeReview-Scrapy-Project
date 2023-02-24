# CoffeeReview

This project is configured to be hosted on [Scrapy Cloud](https://www.zyte.com/scrapy-cloud/).  

It uses [Zyte Smart Proxy Manager](https://scrapinghub.com/?rfsn=4170080.0597ad) as proxy service.  

This project uses Spidermon for monitoring purposes. 
It is also set up to send messages via a telegram bot.
The dataset can be found [here](https://www.kaggle.com/datasets/patkle/coffeereviewcom-over-7000-ratings-and-reviews).  
A Jupyter Notebook with some EDA on that data can be found [here](https://www.kaggle.com/patkle/coffeereview-eda).

## Reviews

The spider can be ran with
```zsh
python3 -m scrapy crawl reviews -a pages=5 -O reviews.csv
```

### Arguments

With `-a` you can specify arguments for the spider.  

|argument   |type  |description   | 
|---|---|---|
|pages   |int   |number of pages to scrape   |


## Setting up locally
  
When setting up this project locally you must create a **.env** file with the following data:  

|setting   |description   |  
|---|---|
|ZYTE_SMARTPROXY_APIKEY   |your smart proxy manager api key   |
|[SPIDERMON_TELEGRAM_SENDER_TOKEN](https://spidermon.readthedocs.io/en/latest/howto/configuring-telegram-for-spidermon.html)   |authorization token for your telegram bot   |  
|[SPIDERMON_TELEGRAM_RECIPIENTS](https://spidermon.readthedocs.io/en/latest/howto/configuring-telegram-for-spidermon.html)   |@channelname, chat it or group id   |
  

## Deploy to Scrapy Cloud
There's a shortcut in the Makefile, just running `make deploy` will deploy the project to Scrapy Cloud (given that you provided the project ID in `scrapinghub.yml`).Don't forget to add the following settings in your cloud project's settings:
|setting   |description   | 
|---|---|
|ZYTE_SMARTPROXY_APIKEY   |your smart proxy manager api key   |
|[SPIDERMON_TELEGRAM_SENDER_TOKEN](https://spidermon.readthedocs.io/en/latest/howto/configuring-telegram-for-spidermon.html)   |authorization token for your telegram bot   |  
|[SPIDERMON_TELEGRAM_RECIPIENTS](https://spidermon.readthedocs.io/en/latest/howto/configuring-telegram-for-spidermon.html)   |@channelname, chat it or group id   |
  
## Also, 
you could [buy me a coffe](https://www.buymeacoffee.com/kleinp) if you wanted to. I'd really appreciate that.  
