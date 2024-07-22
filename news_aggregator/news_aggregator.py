from datetime import datetime
import asyncio
import logging
import aiohttp
import feedparser
from news import NewsFeed, NewsItem

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class NewsAggregator:
    def __init__(self, feeds: list[NewsFeed]):
        self.feeds = feeds
        self.news_items: list[NewsItem] = []

    async def fetch_feed(
        self, session: aiohttp.ClientSession, feed: NewsFeed
    ) -> list[NewsItem]:
        try:
            async with session.get(feed.url) as response:
                content = await response.text()
                parsed_feed = feedparser.parse(content)

                return [
                    NewsItem(
                        title=entry.title,
                        link=entry.link,
                        source=feed.name,
                        published=datetime(*entry.published_parsed[:6])
                        if entry.get("published_parsed")
                        else datetime(1970, 1, 1),
                    )
                    for entry in parsed_feed.entries
                ]
        except Exception as e:
            logger.error("Error fetching feed %s: %s", feed.name, e)
            return []

    async def update_feeds(self):
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch_feed(session, feed) for feed in self.feeds]
            results = await asyncio.gather(*tasks)

            self.news_items = [item for sublist in results for item in sublist]
            self.news_items.sort(key=lambda x: x.published, reverse=True)
