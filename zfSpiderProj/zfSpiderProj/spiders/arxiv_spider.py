import scrapy

class ArxivSpider(scrapy.Spider):
    name = "arxiv"
    allowed_domains=['https://arxiv.org']
    start_urls = [
        'https://arxiv.org/search/?query=nlp&searchtype=all&source=header&start=0'
    ]
    # def start_requests(self):
    #     #pass
    #     urls = [
    #             'https://arxiv.org/search/?query=nlp&searchtype=all&source=header&start=0'
    #          ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        selectors = response.xpath('//*[@id=\'main-container\']/div[2]/ol/li')#'//li')
        # '//*[@id=\'main-container\']/div[2]/ol/li'

        for sel in selectors:#extract_first() 相当于下面的 get()
            title = sel.xpath('./p[1]/text()').get() #sel.xpath返回类型为<class 'scrapy.selector.unified.SelectorList'>
            author = sel.xpath('./p[2]/a[1]/text()').get()
            down_url=sel.xpath('./div/p/span/a[1]/@href').get()
            print(title,author,down_url)
            print('-------------------')
        #pass
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)