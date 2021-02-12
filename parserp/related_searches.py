from bs4 import BeautifulSoup
import pandas as pd
import re, os, time, shutil
from datetime import datetime
from datetime import timedelta
import __main__
from parserp import soup_from_file

output_files = 'output_data'
file_related_searches = 'related_searches.csv'


def get_related_searches(soup):
    div_obj = {}
    div_obj['Keyword'] = []
    div_obj['Query'] = []
    div_obj['Link'] = []

    #soup = soup_from_file(f'{html_file}/{file}'.format(file=file,html_file=html_file))
    html_related_searches = soup.find("div", {"class": "card-section"})
    #print(html_relate)
    related_queries = html_related_searches.find_all('a')
    #print(related_queries)
    for related_query in related_queries:
        keyword = soup.find('title').text.strip().split('-')[0]
        #print(keyword)
        div_obj['Keyword'].append(keyword)
        query = re.sub(' +',' ',related_query.text.strip().replace('\n',''))
        #print(query)
        div_obj['Query'].append(query)
        link = related_query.attrs['href']
        #print(link)
        div_obj['Link'].append(link)
    #print(div_obj)
    div_obj_df = pd.DataFrame(div_obj, index=None)
    #print(div_obj_df)
    now = datetime.now()
    dt_string = now.strftime("%Y%m%d-%H")
    div_obj_df.to_csv(f'{output_files}/{dt_string}-{file_related_searches}', mode='a', header=False, index=False, encoding='UTF-8', sep=';')
    print('---- related_searches')