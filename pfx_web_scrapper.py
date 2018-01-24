import urllib2.request
from bs4 import BeautifulSoup
import pandas as pd
from pfx_data_collection import http_request_urls

for url in http_request_urls:
    pitcher_table = urllib2.urlopen(url)
    soup_table = BeautifulSoup(pitcher_table)
    read_html_str = str(soup_table)
    if 'result not valid' in read_html_str:
        continue
    else:
        pitcher_df = pd.read_html(read_html_str, header=0)
