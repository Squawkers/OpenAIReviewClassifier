import pandas as pd
import numpy as np
from app_store_scraper import AppStore

data = AppStore(country='us', app_name='LinkedIn: Job Search & News', app_id = '288429040')

data.review(how_many=100)

data1 = pd.DataFrame(np.array(data.reviews),columns=['review'])
data2 = data1.join(pd.DataFrame(data1.pop('review').tolist()))

data2 = data2.sort_values('date', ascending=False)
data2.head()

linkedIn = data2[['date','userName','review','rating']]

#linkedIn.to_csv('LinkedIn100Reviews.csv', index=False)
linkedIn.to_excel('LinkedIn100Reviews.xlsx', index=False)
