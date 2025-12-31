import logging
import scrapy
import yaml
from pathlib import Path

current_dir = Path(__file__).resolve()
config_path = current_dir.parents[5]/'config/ingestion_config.yaml'

def get_config(file_path = config_path):
    try:
        with open(file_path, "r") as file:
            config = yaml.safe_load(file)
            return config
    except FileNotFoundError:
        print("Error: config.yaml not found.")
        return {}

config = get_config()
ingestion_config = config['web_sources']
coi_crawler_config = next((item for item in ingestion_config if item['name'] == "constitution_of_india_crawler"), None)


class ConstitutionOfIndiaSpiderSpider(scrapy.Spider):
    name = "constitution_of_india_spider"
    
    allowed_domains = coi_crawler_config['allowed_domains']
    start_urls = coi_crawler_config['seed_url']
    

    def parse(self, response):
        # Extracing preamble
        preamble_link = response.css('a[href*="/articles/preamble/"]::attr(href)').get()
        if preamble_link:
            yield response.follow(preamble_link, callback=self.parse_preamble, priority=10,)

        # Extracing parts
        part_links = response.css('a[href*="/parts/part-"]::attr(href)').getall()
        part_links = list(set(part_links)) 
        for part_link in part_links:
            yield response.follow(part_link, callback=self.parse_part, priority=5,)

        # Extracting schedules
        schedule_links = response.css('a[href*="/schedules/"]::attr(href)').getall()
        schedule_links = list(set(schedule_links)) 
        for schedule_link in schedule_links:
            yield response.follow(schedule_link, callback=self.parse_schedule, priority=3,)




        





