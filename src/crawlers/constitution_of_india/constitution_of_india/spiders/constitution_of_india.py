import scrapy
import yaml
from pathlib import Path

current_dir = Path(__file__).resolve()
config_path = current_dir.parents[3]/'config/config.yaml'

def get_config(file_path = config_path):
    try:
        with open(file_path, "r") as file:
            config = yaml.safe_load(file)
            return config
    except FileNotFoundError:
        print("Error: config.yaml not found.")
        return {}

config = get_config()
ingestion_config = config['ingestion']['web_sources']
coi_crawler_config = next((item for item in ingestion_config if item['name'] == "Constitution_of_India_web_crawl"), None)

class ConstitutionOfIndiaSpiderSpider(scrapy.Spider):
    name = "constitution_of_india_spider"
    allowed_domains = coi_crawler_config['allowed_domains']
    start_urls = coi_crawler_config['seed_url']

    def parse(self, response):
        pass