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
### To run the spider and output the data to a CSV file, use the following command:
```bash
scrapy crawl animes -o anime.csv
```
### To output the data to a JSON file, use the following command:

```bash
scrapy crawl animes -o anime.json
```
The spider will start crawling AniDB and extract the specified information, saving it to the specified file in either CSV or JSON format.

## Spider
The main spider (AnimesSpider) is located in animedb/spiders/animes.py. It crawls AniDB to extract anime information.

## Settings
The project settings are configured in animedb/settings.py. Some important settings include:

- USER_AGENT: The user agent string used for the requests.
- ROBOTSTXT_OBEY: Whether to obey the robots.txt rules of the target website.
- DOWNLOAD_DELAY: The delay (in seconds) between consecutive requests.
- AUTOTHROTTLE_ENABLED: Whether to enable the AutoThrottle extension.
