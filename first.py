import  streamlit as st
import numpy as np
import pandas as pd
import time
 


#chart_data=pd.DataFrame(
 #   np.random.randn(18,3),
#    columns=['a','b','c'])
#st.line_chart(chart_data)


 #map_data=pd.DataFrame(
  #   np.random.randn(1000,2)/[50,50]+[37.76,-122.4],
   #  columns=['lat','lon'])
 #st.map(map_data)



 if st.checkbox('show dataframe'):
     chart_data=pd.DataFrame(
       np.random.randn(20,3),
         columns=['a','b','c'])
 chart_data


# option=st.selectbox(
#     'which number do you like best?',
#     ['1','2','3']
#     )
# 'you selected:', option


# option=st.sidebar.selectbox(
#     'which number do you like best?',
#     [1,2,3])
# 'you selected',option



# left_column,right_column=st.columns(2)
# pressed=left_column.button('press me')
# if pressed:
#     right_column.write("woohoo!")
    
    
# expander=st.expander("FAQ")
# expander.write("here you could put in come really ,relly long explanation")



# 'starting a long computation.....'

# latest_iteration=st.empty()
# bar=st.progress(0)
# for i in range(100):
#     latest_iteration.text(f'iteration{i+1}')
#     bar.progress(i+1)
#     time.sleep(0.1)
    
# '...and now we\'re done!'   



# st.title('uber pickup in nyc')



# DATE_COLUMN = 'date/time'
# DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
#           'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# def load_data(nrows):
#     data = pd.read_csv(DATA_URL, nrows=nrows)
#     lowercase = lambda x: str(x).lower()
#     data.rename(lowercase, axis='columns', inplace=True)
#     data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
#     return data

# # Create a text element and let the reader know the data is loading.
# data_load_state = st.text('Loading data...')
# # Load 10,000 rows of data into the dataframe.
# data = load_data(10000)
# # Notify the reader that the data was successfully loaded.
# data_load_state.text('Loading data...done!')





  
