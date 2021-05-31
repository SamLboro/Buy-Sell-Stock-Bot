# Buy-Sell-Stock-Bot

## Summary

This project is to create a bot that will scrape the Yahoo Finance SP500 list for analyst ratings of each company. Any company in the **Strong Buy** section will be sent to my email address with their stock tickers and their analyst rating. They will be sent through creating an email server, connecting to a less secure **gmail** account I set up, create a message, send the message, and close the server.

## Code Breakdown

### Scraping
First the bot must first access the Yahoo Finance page for the SPX500 page, collate each of the 500 stock tickers, then access those stock ticker pages for each consecutive stock and scrape the analyst ratings for each, collated into a range of numbers from 1-5. 1 is a Strong Buy and 5 is a Strong Sell.
