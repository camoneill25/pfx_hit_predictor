import urllib2.request
from bs4 import BeautifulSoup
import pandas as pd

web_address = "http://www.brooksbaseball.net/pfxVB/tabdel_expanded.php?pitchSel=664641&game=gid_2017_04_06_seamlb_houmlb_1/&s_type=&h_size=700&v_size=500"
pitcher_table = urllib2.urlopen(web_address)
soup_table = BeautifulSoup(pitcher_table)
read_html_str = str(soup_table)
pitcher_df = pd.read_html(read_html_str, header=0)
