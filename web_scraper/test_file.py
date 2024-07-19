import asyncio
from web_scraper import AsyncWebScraper

async def test_scraper():
    urls = ["http://example1.com", "http://example2.com", "http://example3.com"]
    scraper = AsyncWebScraper(urls)
    results = await scraper.run()
    
    assert len(results) == len(urls)
    assert all(isinstance(result, dict) for result in results)
    assert all("title" in result for result in results)

asyncio.run(test_scraper())