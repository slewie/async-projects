"""
This module contains the classes and methods for scraping data from a website.
"""
from typing import List, Dict, Optional
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import logging


class AsyncWebScraper:
    """
    This class is used to scrape web pages asynchronously.
    """

    def __init__(self, urls: List[str]) -> None:
        self.urls: List[str] = urls
        
        # TODO: add semaphores
        # TODO: create a session once and reuse it for all requests.
        
        """
        Possible solution:
        
        self.session = None  # Initialize session to None

        async def __aenter__(self):
            self.session = await aiohttp.ClientSession().__aenter__()
            return self

        async def __aexit__(self, exc_type, exc_val, exc_tb):
            await self.session.__aexit__(exc_type, exc_val, exc_tb)
            
        async with AsyncWebScraper(urls) as scraper:
            results = await scraper.run()
        """

    async def run(self) -> List[Dict[str, str]]:
        """
        This method is used to run the scraper. It runs the scraper for the all websites in the list.
        """
        tasks = [self._get_and_scrap(url) for url in self.urls]
        return await asyncio.gather(*tasks)
        
    async def _get_and_scrap(self, url: str) -> List[Dict[str, str]]:
        """
        This method is used to scrape the web page. It takes a url as input and returns a list of dictionaries.
        """
        html = await self._get_html(url)
        return await self._scrap(html)
        
    async def _scrap(
        self, html: str, scrapped_tags: Optional[List[str]] = None
    ) -> Dict[str, str]:
        """
        This method is used to scrape the html using beautiful soup.
        """
        if scrapped_tags is None:
            scrapped_tags = ["title", "h1", "h2", "h3", "p"]
        soup = BeautifulSoup(html, features="html.parser")

        return {tag.name: tag.text for tag in soup.find_all(scrapped_tags)}
        
    async def _get_html(self, url: str) -> str:
        """
        This method is used to get the html from a website.
        """
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    return await response.text()
        except aiohttp.ClientError as e:
            logging.error(f"Request to the {url} failed: {e}")
            return ""
