import scrapy
import yaml
from pathlib import Path
from items import Preamble
from datetime import datetime

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
        preamble_link = response.css("a[href*='/articles/preamble/']::attr(href)").get()
        if preamble_link:
            yield response.follow(preamble_link, callback=self.parse_preamble, priority=10,)

        # Extracing parts
        part_links = response.css("a[href*='/parts/part-'']::attr(href)").getall()
        part_links = list(set(part_links)) 
        for part_link in part_links:
            yield response.follow(part_link, callback=self.parse_part, priority=5,)

        # Extracting schedules
        schedule_provision_links = response.css("a[href*='/schedules/']::attr(href)").getall()
        schedule_provision_links = list(set(schedule_provision_links)) 
        for schedule_provision_link in schedule_provision_links:
            yield response.follow(schedule_provision_link, callback=self.parse_schedule_provision, priority=3,)

    def parse_premable(self, response: Response):
        item = Preamble()
        item['title'] = response.css("h1::text").get(default='').strip()
        item['url'] = response.url
        item['main_text'] = '\n'.join(response.css("div.article-detail__intro-content p::text").getall()).strip()
        item['versions'] = []
        for additional_content in response.css("div.article-detail__content__main-block"):
            title = additional_content.css("h3::text").get()
            if 'Version' in title:
                item['versions'].append({
                    'title': title,
                    'content': '\n'.join(additional_content.css("div.article-detail__content__sub-block p::text").getall()).strip()
                })
            if 'Summary' in title:
                item['historical_context'] = '\n'.join(additional_content.css("div.article-detail__content__sub-block p::text").getall()).strip()
        item['last_modified_at'] = datetime.fromisoformat(response.css("meta[property='article:modified_time']::attr(content)").get())
        item['scraped_at'] = datetime.now(timezone.utc)

    def parse_part(self, response: Response):
        item = Part()
        item['part_number'] = response.css("div.page-parts-listing__intro span:contains('Part')::text").get()
        item['title'] = response.css("div.page-parts-listing__intro h1::text").get()
        item['url'] = response.url
        item['main_text'] = response.css("div.page-parts-listing__intro div.text-lg::text").get()
        item['chapters'] = []
        for chapter in response.css("div.page-parts-listing__articles div.space-y-16"):
            item['chapters'].append({
                'title' : chapter.css("p::text").get(),
                'articles' : chapter.css("a[href*='/articles']::attr(href)").getall()
            })
        item['scraped_at'] = datetime.now(timezone.utc)
        for article_link in item['chapters']['articles']:
            yield response.follow(article_link, callback=self.parse_article, priority=2,)

    def parse_article(self, response: Response):
        item = Article()
        item['article_number'] = response.css("div.article-detail__article-no span.number-field::text").get()
        item['title'] = response.css("h1::text").get(default='').strip()
        item['url'] = response.url
        item['main_text'] = '\n'.join(response.css("div.article-detail__intro-content p::text").getall()).strip()
        item['versions'] = []
        for additional_content in response.css("div.article-detail__content__main-block"):
            title = additional_content.css("h3::text").get()
            if 'Version' in title:
                item['versions'].append({
                    'title': title,
                    'content': '\n'.join(additional_content.css("div.article-detail__content__sub-block p::text").getall()).strip()
                })
            if 'Summary' in title:
                item['historical_context'] = '\n'.join(additional_content.css("div.article-detail__content__sub-block p::text").getall()).strip()
        item['last_modified_at'] = datetime.fromisoformat(response.css("meta[property='article:modified_time']::attr(content)").get())
        item['scraped_at'] = datetime.now(timezone.utc)

    def schedule_provision_link(self, response: Response):
        schedule_number = response.css("div.schedule-detail__main-content h2::text").get()
        related_articles = response.css("div.schedule-detail__main-content p.inline-block::text").get()
        provision_title = response.css("div.schedule-detail__main-content h1::text").get()
        
        item = response.meta.get('item', Schedule(schedule_number=schedule_number))
        item = Schedule()
