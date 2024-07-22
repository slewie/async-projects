import asyncio
from aiohttp import web
from news_aggregator import NewsAggregator
from news import NewsFeed


class NewsServer:
    def __init__(self, aggregator: NewsAggregator):
        self.aggregator = aggregator
        self.app = web.Application()
        self.app.router.add_get("/", self.handle_home)

    async def handle_home(self, request):
        await self.aggregator.update_feeds()

        html = "<h1>Latest News</h1>"
        for item in self.aggregator.news_items[:10]:  # Display top 10 news
            html += f"<p><strong>{item.source}</strong>: <a href='{item.link}'>{item.title}</a> ({item.published})</p>"

        return web.Response(text=html, content_type="text/html")

    async def start(self):
        runner = web.AppRunner(self.app)
        await runner.setup()
        site = web.TCPSite(runner, "localhost", 8080)
        await site.start()
        print("Server started at http://localhost:8080")


async def main():
    feeds = [
        NewsFeed("BBC", "http://feeds.bbci.co.uk/news/rss.xml"),
        NewsFeed("CNN", "http://rss.cnn.com/rss/edition.rss"),
    ]

    aggregator = NewsAggregator(feeds)
    server = NewsServer(aggregator)
    await server.start()

    while True:
        await asyncio.sleep(3600)


if __name__ == "__main__":
    asyncio.run(main())
