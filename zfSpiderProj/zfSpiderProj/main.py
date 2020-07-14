#用于在ide调试
from scrapy.cmdline import execute
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy','crawl','arxiv'])
