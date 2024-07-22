from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class NewsFeed:
    name: str
    url: str


@dataclass
class NewsItem:
    title: str
    link: str
    source: Optional[str]
    published: Optional[datetime] = datetime(1970, 1, 1)
    