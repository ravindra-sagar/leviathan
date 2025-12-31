import scrapy

class Preamble(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    scraped = scrapy.Field()
    main_text = scrapy.Field()
    versions = scrapy.Field()
    historical_context = scrapy.Field()
    last_modified_date = scrapy.Field() # Use - response.xpath('//meta[@property="article:modified_time"]/@content').get()
    scraped_at = scrapy.Field()

class Part(scrapy.Item):
    part_number = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    scraped = scrapy.Field()
    main_text = scrapy.Field()
    chapters = scrapy.Field()
    historical_context = scrapy.Field()
    last_modified_date = scrapy.Field()
    scraped_at = scrapy.Field()

class Article(scrapy.Item):
    article_number = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    scraped = scrapy.Field()
    main_text = scrapy.Field()
    versions = scrapy.Field()
    historical_context = scrapy.Field()
    last_modified_date = scrapy.Field()
    scraped_at = scrapy.Field()

class Schedule(scrapy.Item):
    schedule_number = scrapy.Field()
    title = scrapy.Field()
    scraped = scrapy.Field()
    provisions = scrapy.Field()
    related_articles = scrapy.Field()
    last_modified_date = scrapy.Field()
    scraped_at = scrapy.Field()