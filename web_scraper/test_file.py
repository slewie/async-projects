"""
Module doc
"""
import asyncio
from web_scraper import AsyncWebScraper

async def test_scraper():
    """
    Function doc
    """
    urls = [
        'https://www.crummy.com/software/BeautifulSoup/bs4/doc/'
        'https://docs.aiohttp.org/en/stable/index.html',
        'https://superfastpython.com/python-asyncio/#Coroutines_in_Python',
        'https://www.python.org/dev/peps/pep-0492/',
        'https://docs.python.org/3/library/asyncio-dev.html',
        'https://www.python.org/dev/peps/pep-0530/',
        'https://www.python.org/dev/peps/pep-0534/',
        'https://www.python.org/dev/peps/pep-0537/',
        'https://www.evidentlyai.com/ml-system-design',
        'https://huyenchip.com/ml-interviews-book/contents/chapter-1.-ml-jobs.html'
    ]
    scraper = AsyncWebScraper(urls)
    results = await scraper.run()
    
    assert len(results) == len(urls)
    assert all(isinstance(result, dict) for result in results)
    assert all("title" in result for result in results)

asyncio.run(test_scraper())
