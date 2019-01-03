import scrapy
from scrapy_splash import SplashRequest
# import logging
from datetime import timedelta, date
 
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)
 
 
def build_start_urls(date_range):
    urls = []
    for single_date in date_range:
        urls.append('http://www.espn.com/nba/scoreboard/_/date/{}'.format(single_date.strftime("%Y%m%d")))
    
    return urls

def lower_join_city(city_name):
    return '_'.join(city_name.lower().split(' '))  
 
class NBAScoresSpider(scrapy.Spider):
    # identity
    name = 'nba_scores'
 
    start_date = date(2018, 10, 16)
    end_date = date(2018, 12, 28)
 
    date_range = daterange(start_date, end_date)
 
    start_urls = build_start_urls(date_range)
 
    def start_requests(self):
        for site in self.start_urls:
            yield SplashRequest(url = site, callback = self.parse, endpoint = 'render.html', args = {'wait': 5}, meta = {'date': site.split('/')[-1]})
 
    def parse(self, response):
        for a in response.xpath("//a[@class='mobileScoreboardLink']"):
            score_page = 'http://www.espn.com' + a.xpath(".//@href").extract_first()
            yield scrapy.Request(url = score_page, callback = self.parse_score,  meta = {'date': response.meta.get('date')})
 
    def parse_score(self, response):
        score_board = response.xpath("//div[contains(@class,'competitors')]")
        team_away_city = score_board.xpath(".//div[@class='team away']//span[@class='long-name']/text()").extract_first()
        team_away_name = score_board.xpath(".//div[@class='team away']//span[@class='short-name']/text()").extract_first().lower()
        team_home_city = score_board.xpath(".//div[@class='team home']//span[@class='long-name']/text()").extract_first()
        team_home_name = score_board.xpath(".//div[@class='team home']//span[@class='short-name']/text()").extract_first().lower()

        team_away_city = lower_join_city(team_away_city)
        team_home_city = lower_join_city(team_home_city)

        yield {
            'date': response.meta.get('date'),
            'team_away_city': team_away_city,
            'team_away_name': team_away_name,
            'team_away_score': response.xpath("//div[@class='score icon-font-after']/text()").extract_first(),
            'team_home_city': team_home_city,
            'team_home_name': team_home_name,
            'team_home_score': response.xpath("//div[@class='score icon-font-before']/text()").extract_first()
        }