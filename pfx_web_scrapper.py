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
        pitcher_df.to_csv('csv_pitcher_table.csv', sep='\t', encoding='utf-8')
        with open ('test.csv', 'r') as f:
            reader = csv.reader(f)
            columns = next(reader)
            query = "INSERT INTO PitchByPitch({0}) values ({1})"
            query = query.format(','.join(columns), ','.join('?' * len(columns)))
            cursor = connection.cursor()
            for data in reader:
                cursor.execute(query, data)
            cursor.commit()
