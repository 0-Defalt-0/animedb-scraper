# AnimeDB Scrapy Project
This Scrapy project (animedb) is designed to crawl AniDB and extract information about anime titles.

## Installation
Clone the repository:
```bash
git clone https://github.com/your-username/animedb.git
```
## Install the required packages:

```bash
cd animedb
pip install -r requirements.txt
```
## Usage
To run the spider, navigate to the project directory containing the scrapy.cfg file and run:
```bash
scrapy crawl animes
```
The spider will start crawling AniDB and extract the specified information.

## Spider
The main spider (AnimesSpider) is located in animedb/spiders/animes.py. It crawls AniDB to extract anime information.

## Settings
The project settings are configured in animedb/settings.py. Some important settings include:

- USER_AGENT: The user agent string used for the requests.
- ROBOTSTXT_OBEY: Whether to obey the robots.txt rules of the target website.
- DOWNLOAD_DELAY: The delay (in seconds) between consecutive requests.
- AUTOTHROTTLE_ENABLED: Whether to enable the AutoThrottle extension.
