# Asynchronous Web Scraper

## Description:
This project aims to create a powerful and efficient web scraper that can handle multiple websites concurrently. The goal is to demonstrate the benefits of asynchronous programming in I/O-bound tasks like web scraping.

## Practical benefits:
* Significantly faster data collection compared to synchronous scrapers
* Ability to gather large amounts of data from multiple sources quickly
* Useful for market research, price monitoring, or content aggregation
* Teaches how to respect websites' resources through rate limiting

## Requirements:
* Handle at least 50 concurrent requests
* Implement rate limiting to avoid overwhelming target websites
* Parse HTML content and extract specific data (e.g., article titles, prices)
* Save results to a CSV file

## Allowed libraries: 
- aiohttp
- beautifulsoup4
- asyncio
- csv