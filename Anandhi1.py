import pandas as pd
import pymongo
import mysql.connector
import plotly.express as px
import streamlit as st
from streamlit_option_menu import option_menu
pd.set_option('display.max_columns', None)
from PIL import Image
import certifi
ca = certifi.where()

def streamlit_config():

    # page configuration
    page_icon_url = '/Users/karthickkumar/Desktop/Airbnb/airbnb_logo.png'
    st.set_page_config(page_title='Airbnb',
                       page_icon=page_icon_url, layout="wide")

    # page header transparent color
    page_background_color = """
    <style>

    [data-testid="stHeader"] 
    {
    background: rgba(0,0,0,0);
    }

    </style>
    """
    st.markdown(page_background_color, unsafe_allow_html=True)

    # title and position
    st.markdown(f'<h1 style="text-align: center;">Airbnb Analysis</h1>',
                unsafe_allow_html=True)



df1=pd.read_csv("Airbnb.csv")

            


class sql:
    def create_table():
        import mysql.connector
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        )

        print(mydb)
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("use Airbnb")
        mycursor.execute(f"""create table if not exists airbnb(
                                _id			    varchar(255) primary key,
                                listing_url		text,
                                name			varchar(255),
                                property_type	varchar(255),
                                room_type		varchar(255),
                                bed_type		varchar(255),
                                minimum_nights		int,
                                maximum_nights		int,
                                cancellation_policy	varchar(255),
                                accommodates		int,
                                bedrooms		    int,
                                beds			    int,
                                number_of_reviews	int,
                                bathrooms		    float,
                                price			    int,
                                extra_people		int,
                                guests_included		int,
                                images			    text,
                                review_scores		int,
                                cleaning_fee        int,
                                host_id			varchar(255),
                                host_url		text,
                                host_name		varchar(255),
                                host_location		varchar(255),
                                host_response_time  varchar(255),
                                host_thumbnail_url	text,
                                host_picture_url	text,
                                host_neighbourhood	varchar(255),
                                host_is_superhost	varchar(25),
                                host_has_profile_pic	varchar(25),
                                host_identity_verified	varchar(25),
                                host_listings_count	        int,
                                host_total_listings_count	int,
                                host_verifications		text,
                                host_response_rate      varchar(50),
                                street				varchar(255),
                                suburb				varchar(255),
                                government_area		varchar(255),
                                market				varchar(255),
                                country				varchar(255),
                                country_code		varchar(255),
                                location_type		varchar(255),
                                longitude			float,
                                latitude			float,
                                is_location_exact	        varchar(25),
                                availability_30		        int,
                                availability_60		        int,
                                availability_90		        int,
                                availability_365	        int,
                                amenities			text);""")
        mydb.commit()
        mydb.close()
    
    def data_migration():
        import mysql.connector
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        )

        print(mydb)
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("use Airbnb")



        for index, row in df1.iterrows():
            insert_query = '''INSERT INTO airbnb(_id, listing_url, name, property_type, room_type, bed_type, minimum_nights, maximum_nights, cancellation_policy, accommodates, bedrooms, beds, number_of_reviews, bathrooms, price, extra_people, guests_included, images, review_scores, cleaning_fee, host_id, host_url, host_name, host_location,host_response_time, host_thumbnail_url, host_picture_url, host_neighbourhood, host_is_superhost, host_has_profile_pic, host_identity_verified, host_listings_count, host_total_listings_count, host_verifications, host_response_rate, street, suburb, government_area, market, country, country_code, location_type, longitude, latitude, is_location_exact, availability_30, availability_60, availability_90, availability_365, amenities) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''

            values = (
                row['_id'], row['listing_url'], row['name'], row['property_type'], row['room_type'], row['bed_type'], 
                row['minimum_nights'], row['maximum_nights'], row['cancellation_policy'], row['accommodates'], 
                row['bedrooms'], row['beds'], row['number_of_reviews'],row['bathrooms'], row['price'], row['extra_people'], 
                row['guests_included'], row['images'], row['review_scores'], row['cleaning_fee'], row['host_id'], 
                row['host_url'], row['host_name'], row['host_location'],row['host_response_time'], row['host_thumbnail_url'], row['host_picture_url'], 
                row['host_neighbourhood'], row['host_is_superhost'], row['host_has_profile_pic'], row['host_identity_verified'], 
                row['host_listings_count'], row['host_total_listings_count'], row['host_verifications'],row['host_response_rate'], row['street'], 
                row['suburb'], row['government_area'], row['market'], row['country'], row['country_code'], row['location_type'], 
                row['longitude'], row['latitude'], row['is_location_exact'], row['availability_30'], row['availability_60'], 
                row['availability_90'], row['availability_365'], row['amenities']
            )

            mycursor.execute(insert_query, values)

        mydb.commit()
        mydb.close()


    def delete_table():
        import mysql.connector
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        )

        print(mydb)
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("use Airbnb")
        mycursor.execute(f"""delete from airbnb;""")
        mydb.commit()
        mydb.close()





class plotly:

    def pie_chart(df1, x, y, title, title_x=0.20):

        fig = px.pie(df1, names=x, values=y, hole=0.5, title=title)

        fig.update_layout(title_x=title_x, title_font_size=22)

        fig.update_traces(text=df1[y], textinfo='percent+value',
                          textposition='outside',
                          textfont=dict(color='white'))

        st.plotly_chart(fig, use_container_width=True)

    def horizontal_bar_chart(df1, x, y, text, color, title, title_x=0.25):

        fig = px.bar(df1, x=x, y=y, labels={x: '', y: ''}, title=title)

        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)

        fig.update_layout(title_x=title_x, title_font_size=22)

        text_position = ['inside' if val >= max(
            df1[x]) * 0.75 else 'outside' for val in df1[x]]

        fig.update_traces(marker_color=color,
                          text=df1[text],
                          textposition=text_position,
                          texttemplate='%{x}<br>%{text}',
                          textfont=dict(size=14),
                          insidetextfont=dict(color='white'),
                          textangle=0,
                          hovertemplate='%{x}<br>%{y}')

        st.plotly_chart(fig, use_container_width=True)

    def vertical_bar_chart(df1, x, y, text, color, title, title_x=0.25):

        fig = px.bar(df1, x=x, y=y, labels={x: '', y: ''}, title=title)

        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)

        fig.update_layout(title_x=title_x, title_font_size=22)

        text_position = ['inside' if val >= max(
            df1[y]) * 0.90 else 'outside' for val in df1[y]]

        fig.update_traces(marker_color=color,
                          text=df1[text],
                          textposition=text_position,
                          texttemplate='%{y}<br>%{text}',
                          textfont=dict(size=14),
                          insidetextfont=dict(color='white'),
                          textangle=0,
                          hovertemplate='%{x}<br>%{y}')

        st.plotly_chart(fig, use_container_width=True, height=100)

    def line_chart(df1, x, y, text, textposition, color, title, title_x=0.25):

        fig = px.line(df1, x=x, y=y, labels={
                      x: '', y: ''}, title=title, text=df1[text])

        fig.update_layout(title_x=title_x, title_font_size=22)

        fig.update_traces(line=dict(color=color, width=3.5),
                          marker=dict(symbol='diamond', size=10),
                          texttemplate='%{x}<br>%{text}',
                          textfont=dict(size=13.5),
                          textposition=textposition,
                          hovertemplate='%{x}<br>%{y}')

        st.plotly_chart(fig, use_container_width=True, height=100)


class feature:

    def feature(column_name, order='count desc', limit=10):
        import mysql.connector
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        )

        print(mydb)
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("use Airbnb")
        mycursor.execute(f"""select distinct {column_name}, count({column_name}) as count
                           from airbnb
                           group by {column_name}
                           order by {order}
                           limit {limit};""")
        mydb.commit()
        s = mycursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        data = pd.DataFrame(s, columns=[column_name, 'count'], index=i)
        data = data.rename_axis('S.No')
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        data['percentage'] = data['count'].apply(
            lambda x: str('{:.2f}'.format(x/55.55)) + '%')
        data['y'] = data[column_name].apply(lambda x: str(x)+'`')
        return data

     

    def cleaning_fee():
        import mysql.connector
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        )

        print(mydb)
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("use Airbnb")
        mycursor.execute(f"""select distinct cleaning_fee, count(cleaning_fee) as count
                           from airbnb
                           where cleaning_fee != 'Not Specified'
                           group by cleaning_fee
                           order by count desc
                           limit 10""")
        mydb.commit()
        s = mycursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        data = pd.DataFrame(s, columns=['cleaning_fee', 'count'], index=i)
        data = data.rename_axis('S.No')
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        data['percentage'] = data['count'].apply(
            lambda x: str('{:.2f}'.format(x/55.55)) + '%')
        data['y'] = data['cleaning_fee'].apply(lambda x: str(x)+'`')
        return data

    def location():
        import mysql.connector
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        )

        print(mydb)
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("use Airbnb")
        mycursor.execute(f"""select host_id, country, longitude, latitude
                           from airbnb
                           group by host_id, country, longitude, latitude""")
        mydb.commit()
        s = mycursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        data = pd.DataFrame(
            s, columns=['Host ID', 'Country', 'Longitude', 'Latitude'], index=i)
        data = data.rename_axis('S.No')
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def feature_analysis():

        # vertical_bar chart
        property_type = feature.feature('property_type')
        plotly.vertical_bar_chart(df1=property_type, x='property_type', y='count',
                                  text='percentage', color='#5D9A96', title='Property Type', title_x=0.43)

        # line & pie chart
        col1, col2 = st.columns(2)
        with col1:
            bed_type = feature.feature('bed_type')
            plotly.line_chart(df1=bed_type, y='bed_type', x='count', text='percentage', color='#5cb85c',
                              textposition=[
                                  'top center', 'bottom center', 'middle right', 'middle right', 'middle right'],
                              title='Bed Type', title_x=0.50)
        with col2:
            room_type = feature.feature('room_type')
            plotly.pie_chart(df1=room_type, x='room_type',
                             y='count', title='Room Type', title_x=0.30)

        # vertical_bar chart
        tab1, tab2 = st.tabs(['Minimum Nights', 'Maximum Nights'])
        with tab1:
            minimum_nights = feature.feature('minimum_nights')
            plotly.vertical_bar_chart(df1=minimum_nights, x='y', y='count', text='percentage',
                                      color='#5cb85c', title='Minimum Nights', title_x=0.43)
        with tab2:
            maximum_nights = feature.feature('maximum_nights')
            plotly.vertical_bar_chart(df1=maximum_nights, x='y', y='count', text='percentage',
                                      color='#5cb85c', title='Maximum Nights', title_x=0.43)
        

        # line chart
        cancellation_policy = feature.feature('cancellation_policy')
        plotly.line_chart(df1=cancellation_policy, y='cancellation_policy', x='count', text='percentage', color='#5D9A96',
                          textposition=['top center', 'top right',
                                        'top center', 'bottom center', 'middle right'],
                          title='Cancellation Policy', title_x=0.43)

        # vertical_bar chart
        accommodates = feature.feature('accommodates')
        plotly.vertical_bar_chart(df1=accommodates, x='y', y='count', text='percentage',
                                  color='#5D9A96', title='Accommodates', title_x=0.43)

        # vertical_bar chart
        tab1, tab2, tab3 = st.tabs(['Bedrooms', 'Beds', 'Bathrooms'])
        with tab1:
            bedrooms = feature.feature('bedrooms')
            plotly.vertical_bar_chart(df1=bedrooms, x='y', y='count', text='percentage',
                                      color='#5cb85c', title='Bedrooms', title_x=0.43)
        with tab2:
            beds = feature.feature('beds')
            plotly.vertical_bar_chart(df1=beds, x='y', y='count', text='percentage',
                                      color='#5cb85c', title='Beds', title_x=0.43)
        with tab3:
            bathrooms = feature.feature('bathrooms')
            plotly.vertical_bar_chart(df1=bathrooms, x='y', y='count', text='percentage',
                                      color='#5cb85c', title='Bathrooms', title_x=0.43)

        # vertical_bar chart
        tab1, tab2, tab3, tab4 = st.tabs(
            ['Price', 'Cleaning Fee', 'Extra People', 'Guests Included'])
        with tab1:
            price = feature.feature('price')
            plotly.vertical_bar_chart(df1=price, x='y', y='count', text='percentage',
                                      color='#5D9A96', title='Price', title_x=0.43)
        with tab2:
            cleaning_fee = feature.cleaning_fee()
            plotly.vertical_bar_chart(df1=cleaning_fee, x='y', y='count', text='percentage',
                                      color='#5D9A96', title='Cleaning Fee', title_x=0.43)
        with tab3:
            extra_people = feature.feature('extra_people')
            plotly.vertical_bar_chart(df1=extra_people, x='y', y='count', text='percentage',
                                      color='#5D9A96', title='Extra People', title_x=0.43)
        with tab4:
            guests_included = feature.feature('guests_included')
            plotly.vertical_bar_chart(df1=guests_included, x='y', y='count', text='percentage',
                                      color='#5D9A96', title='Guests Included', title_x=0.43)

        # line chart
        host_response_time = feature.feature('host_response_time')
        plotly.line_chart(df1=host_response_time, y='host_response_time', x='count', text='percentage', color='#5cb85c',
                          textposition=['top center', 'top right',
                                        'top right', 'bottom left', 'bottom left'],
                          title='Host Response Time', title_x=0.43)

        # vertical_bar chart
        tab1, tab2 = st.tabs(['Host Response Rate', 'Host Listings Count'])
        with tab1:
            host_response_rate = feature.feature('host_response_rate')
            plotly.vertical_bar_chart(df1=host_response_rate, x='y', y='count', text='percentage',
                                      color='#5cb85c', title='Host Response Rate', title_x=0.43)
        with tab2:
            host_listings_count = feature.feature('host_listings_count')
            plotly.vertical_bar_chart(df1=host_listings_count, x='y', y='count', text='percentage',
                                      color='#5cb85c', title='Host Listings Count', title_x=0.43)

        # pie chart
        tab1, tab2, tab3 = st.tabs(
            ['Host is Superhost', 'Host has Profile Picture', 'Host Identity Verified'])
        with tab1:
            host_is_superhost = feature.feature('host_is_superhost')
            plotly.pie_chart(df1=host_is_superhost, x='host_is_superhost',
                             y='count', title='Host is Superhost', title_x=0.39)
        with tab2:
            host_has_profile_pic = feature.feature('host_has_profile_pic')
            plotly.pie_chart(df1=host_has_profile_pic, x='host_has_profile_pic',
                             y='count', title='Host has Profile Picture', title_x=0.37)
        with tab3:
            host_identity_verified = feature.feature('host_identity_verified')
            plotly.pie_chart(df1=host_identity_verified, x='host_identity_verified',
                             y='count', title='Host Identity Verified', title_x=0.37)

        # vertical_bar,pie,map chart
        tab1, tab2, tab3 = st.tabs(['Market', 'Country', 'Location Exact'])
        with tab1:
            market = feature.feature('market', limit=12)
            plotly.vertical_bar_chart(df1=market, x='market', y='count', text='percentage',
                                      color='#5D9A96', title='Market', title_x=0.43)
        with tab2:
            country = feature.feature('country')
            plotly.vertical_bar_chart(df1=country, x='country', y='count', text='percentage',
                                      color='#5D9A96', title='Country', title_x=0.43)
        with tab3:
            is_location_exact = feature.feature('is_location_exact')
            plotly.pie_chart(df1=is_location_exact, x='is_location_exact', y='count',
                             title='Location Exact', title_x=0.37)

        # vertical_bar,pie,map chart
        tab1, tab2, tab3, tab4 = st.tabs(['Availability 30', 'Availability 60',
                                          'Availability 90', 'Availability 365'])
        with tab1:
            availability_30 = feature.feature('availability_30')
            plotly.vertical_bar_chart(df1=availability_30, x='y', y='count', text='percentage',
                                      color='#5cb85c', title='Availability 30', title_x=0.45)
        with tab2:
            availability_60 = feature.feature('availability_60')
            plotly.vertical_bar_chart(df1=availability_60, x='y', y='count', text='percentage',
                                      color='#5cb85c', title='Availability 60', title_x=0.45)
        with tab3:
            availability_90 = feature.feature('availability_90')
            plotly.vertical_bar_chart(df1=availability_90, x='y', y='count', text='percentage',
                                      color='#5cb85c', title='Availability 90', title_x=0.45)
        with tab4:
            availability_365 = feature.feature('availability_365')
            plotly.vertical_bar_chart(df1=availability_365, x='y', y='count', text='percentage',
                                      color='#5cb85c', title='Availability 365', title_x=0.45)

        # vertical_bar,pie,map chart
        tab1, tab2, tab3 = st.tabs(['Number of Reviews', 'Maximum Number of Reviews', 'Review Scores'])
        with tab1:
            number_of_reviews = feature.feature('number_of_reviews')
            plotly.vertical_bar_chart(df1=number_of_reviews, x='y', y='count', text='percentage',
                                      color='#5D9A96', title='Number of Reviews', title_x=0.43)
        with tab2:
            max_number_of_reviews = feature.feature(
                'number_of_reviews', order='number_of_reviews desc')
            plotly.vertical_bar_chart(df1=max_number_of_reviews, x='y', y='count', text='percentage',
                                      color='#5D9A96', title='Maximum Number of Reviews', title_x=0.35)
        with tab3:
            review_scores = feature.feature('review_scores')
            plotly.vertical_bar_chart(df1=review_scores, x='y', y='count', text='percentage',
                                      color='#5D9A96', title='Review Scores', title_x=0.43)

class host:

    def countries_list():
        import mysql.connector
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        )

        print(mydb)
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("use Airbnb")
        mycursor.execute(f"""select distinct country from airbnb order by country asc""")
        mydb.commit()
        s = mycursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        data = pd.DataFrame(s, columns=['Country'], index=i)
        data = data.rename_axis('S.No')
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def column_value(country, column_name, limit=10):
        import mysql.connector
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        )

        print(mydb)
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("use Airbnb")
        mycursor.execute(f"""select {column_name}, count({column_name}) as count
                           from airbnb
                           where country='{country}'
                           group by {column_name}
                           order by count desc
                           limit {limit}""")
        mydb.commit()
        s = mycursor.fetchall()
        data = pd.DataFrame(s, columns=[column_name, 'count'])
        return data[column_name].values.tolist()

    def column_value_names(country, column_name, order='desc', limit=10):
       import mysql.connector
       mydb = mysql.connector.connect(
       host="localhost",
       user="root",
       password="",
       )

       print(mydb)
       mycursor = mydb.cursor(buffered=True)
       mycursor.execute("use Airbnb")
       mycursor.execute(f"""select {column_name}, count({column_name}) as count
                           from airbnb
                           where country='{country}'
                           group by {column_name}
                           order by {column_name} {order}
                           limit {limit}""")
       mydb.commit()
       s = mycursor.fetchall()
       data = pd.DataFrame(s, columns=[column_name, 'count'])
       return data[column_name].values.tolist()

    def column_value_count_not_specified(country, column_name, limit=10):
        import mysql.connector
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        )

        print(mydb)
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("use Airbnb")
        mycursor.execute(f"""select {column_name}, count({column_name}) as count
                           from airbnb
                           where country='{country}' and {column_name}!='Not Specified'
                           group by {column_name}
                           order by count desc
                           limit {limit}""")
        mydb.commit()
        s = mycursor.fetchall()
        data = pd.DataFrame(s, columns=[column_name, 'count'])
        return data[column_name].values.tolist()

    def host(country, column_name, column_value, limit=10):
        import mysql.connector
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        )

        print(mydb)
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("use Airbnb")

        mycursor.execute(f"""select distinct host_id, count(host_id) as count
                           from airbnb
                           where country='{country}' and {column_name}='{column_value}'
                           group by host_id
                           order by count desc
                           limit {limit}""")
        mydb.commit()
        s = mycursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        data = pd.DataFrame(s, columns=['host_id', 'count'], index=i)
        data = data.rename_axis('S.No')
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        data['percentage'] = data['count'].apply(
            lambda x: str('{:.2f}'.format(x/55.55)) + '%')
        data['y'] = data['host_id'].apply(lambda x: str(x)+'`')
        return data

    def main(values, label):
        col1, col2, col3 = st.columns(3)
        with col1:
            a = str(values) + '_column_value_list'
            b = str(values) + '_column_value'

            a = host.column_value(country=country, column_name=values)
            b = st.selectbox(label=label, options=a)

            values = host.host(country=country, column_name=values,
                               column_value=b)
            return values

    def main_min(values, label):
        col1, col2, col3 = st.columns(3)
        with col1:
            a = str(values) + '_column_value_list'
            b = str(values) + '_column_value'

            a = host.column_value_names(
                country=country, column_name=values, order='asc')
            b = st.selectbox(label=label, options=a)

            values = host.host(country=country, column_name=values,
                               column_value=b)
            return values

    def main_max(values, label):
        col1, col2, col3 = st.columns(3)
        with col1:
            a = str(values) + '_column_value_list'
            b = str(values) + '_column_value'

            a = host.column_value_names(
                country=country, column_name=values, order='desc')
            b = st.selectbox(label=label, options=a)

            values = host.host(country=country, column_name=values,
                               column_value=b)
            return values

    def not_specified(values, label):
        col1, col2, col3 = st.columns(3)
        with col1:
            a = str(values) + '_column_value_list'
            b = str(values) + '_column_value'

            a = host.column_value_count_not_specified(
                country=country, column_name=values)
            b = st.selectbox(label=label, options=a)

            values = host.host(country=country, column_name=values,
                               column_value=b)
            return values

    def host_analysis():

        # vertical_bar chart
        property_type = host.main(values='property_type', label='Property Type')
        plotly.vertical_bar_chart(df1=property_type, x='y', y='count', text='percentage',
                                  color='#5D9A96', title='Property Type', title_x=0.45)

        # vertical_bar chart
        tab1, tab2 = st.tabs(['Room Type', 'Bed Type'])
        with tab1:
            room_type = host.main(values='room_type', label='')
            plotly.vertical_bar_chart(df1=room_type, x='y', y='count', text='percentage',
                                      color='#5cb85c', title='Room Type', title_x=0.45)
        with tab2:
            bed_type = host.main(values='bed_type', label='')
            plotly.vertical_bar_chart(df1=bed_type, x='y', y='count', text='percentage',
                                      color='#5cb85c', title='Bed Type', title_x=0.45)

        # vertical_bar chart
        tab1, tab2 = st.tabs(['Minimum Nights', 'Maximum Nights'])
        with tab1:
            minimum_nights = host.main(values='minimum_nights', label='')
            plotly.vertical_bar_chart(df1=minimum_nights, x='y', y='count', text='percentage',
                                      color='#5D9A96', title='Minimum Nights', title_x=0.45)
        with tab2:
            maximum_nights = host.main(values='maximum_nights', label='')
            plotly.vertical_bar_chart(df1=maximum_nights, x='y', y='count', text='percentage',
                                      color='#5D9A96', title='Maximum Nights', title_x=0.45)

        # vertical_bar chart
        cancellation_policy = host.main(
            values='cancellation_policy', label='Cancellation Policy')
        plotly.vertical_bar_chart(df1=cancellation_policy, x='y', y='count', text='percentage',
                                  color='#5cb85c', title='Cancellation Policy', title_x=0.45)

        # vertical_bar chart
        tab1, tab2 = st.tabs(
            ['Minimum Accommodates', 'Maximum Accommodates'])
        with tab1:
            minimum_accommodates = host.main_min(
                values='accommodates', label='')
            plotly.vertical_bar_chart(df1=minimum_accommodates, x='y', y='count', text='percentage',
                                      color='#5D9A96', title='Minimum Accommodates', title_x=0.45)
        with tab2:
            maximum_accommodates = host.main_max(
                values='accommodates', label='')
            plotly.vertical_bar_chart(df1=maximum_accommodates, x='y', y='count', text='percentage',
                                      color='#5D9A96', title='Maximum Accommodates', title_x=0.45)

        # vertical_bar chart
        tab1, tab2, tab3, tab4 = st.tabs(
            ['Bedrooms', 'Minimum Beds', 'Maximum Beds', 'Bathrooms'])
        with tab1:
            bedrooms = host.main(values='bedrooms', label='')
            plotly.vertical_bar_chart(df1=bedrooms, x='y', y='count', text='percentage',
                                      color='#5cb85c', title='Bedrooms', title_x=0.45)
        with tab2:
            minimum_beds = host.main_min(values='beds', label='')
            plotly.vertical_bar_chart(df1=minimum_beds, x='y', y='count', text='percentage',
                                      color='#5cb85c', title='Minimum Beds', title_x=0.45)
        with tab3:
            maximum_beds = host.main_max(values='beds', label='')
            plotly.vertical_bar_chart(df1=maximum_beds, x='y', y='count', text='percentage',
                                      color='#5cb85c', title='Maximum Beds', title_x=0.45)
        with tab4:
            bathrooms = host.main(values='bathrooms', label='')
            plotly.vertical_bar_chart(df1=bathrooms, x='y', y='count', text='percentage',
                                      color='#5cb85c', title='Bathrooms', title_x=0.45)

        # vertical_bar chart
        tab1, tab2, tab3, tab4 = st.tabs(
            ['Price', 'Minimum Price', 'Maximum Price', 'Cleaning Fee'])
        with tab1:
            price = host.main(values='price', label='')
            plotly.vertical_bar_chart(df1=price, x='y', y='count', text='percentage',
                                      color='#5D9A96', title='Price', title_x=0.45)
        with tab2:
            minimum_price = host.main_min(values='price', label='')
            plotly.vertical_bar_chart(df1=minimum_price, x='y', y='count', text='percentage',
                                      color='#5D9A96', title='Minimum Price', title_x=0.45)
        with tab3:
            maximum_price = host.main_max(values='price', label='')
            plotly.vertical_bar_chart(df1=maximum_price, x='y', y='count', text='percentage',
                                      color='#5D9A96', title='Maximum price', title_x=0.45)
        with tab4:
            cleaning_fee = host.not_specified(values='cleaning_fee', label='')
            plotly.vertical_bar_chart(df1=cleaning_fee, x='y', y='count', text='percentage',
                                      color='#5D9A96', title='Cleaning Fee', title_x=0.45)

        # vertical_bar chart
        tab1, tab2, tab3, tab4 = st.tabs(
            ['Guests Included', 'Cost at Extra People',
                                          'Minimum Cost at Extra People', 'Maximum Cost at Extra People'])
        with tab1:
            guests_included = host.main(values='guests_included', label='')
            plotly.vertical_bar_chart(df1=guests_included, x='y', y='count', text='percentage',
                                      color='#5cb85c', title='Guests Included', title_x=0.45)
        with tab2:
            extra_people = host.main(values='extra_people', label='')
            plotly.vertical_bar_chart(df1=extra_people, x='y', y='count', text='percentage',
                                      color='#5cb85c', title='Cost at Extra People', title_x=0.45)
        with tab3:
            extra_people_min_cost = host.main_min(
                values='extra_people', label='')
            plotly.vertical_bar_chart(df1=extra_people_min_cost, x='y', y='count', text='percentage',
                                      color='#5cb85c', title='Minimum Cost at Extra People', title_x=0.45)
        with tab4:
            extra_people_max_cost = host.main_max(
                values='extra_people', label='')
            plotly.vertical_bar_chart(df1=extra_people_max_cost, x='y', y='count', text='percentage',
                                      color='#5cb85c', title='Maximum Cost at Extra People', title_x=0.45)

        # vertical_bar chart
        tab1, tab2 = st.tabs(['Response Time', 'Response Rate'])
        with tab1:
            host_response_time = host.main(
                values='host_response_time', label='')
            plotly.vertical_bar_chart(df1=host_response_time, x='y', y='count', text='percentage',
                                      color='#5D9A96', title='Response Time', title_x=0.45)
        with tab2:
            host_response_rate = host.not_specified(
                values='host_response_rate', label='')
            plotly.vertical_bar_chart(df1=host_response_rate, x='y', y='count', text='percentage',
                                      color='#5D9A96', title='Response Rate', title_x=0.45)

        # vertical_bar chart
        tab1, tab2, tab3, tab4 = st.tabs(
            ['Availability 30', 'Availability 60', 'Availability 90', 'Availability 365'])
        with tab1:
            availability_30 = host.main_max(
                values='availability_30', label='')
            plotly.vertical_bar_chart(df1=availability_30, x='y', y='count', text='percentage',
                                      color='#5cb85c', title='Availability of Next 30 Days', title_x=0.45)
        with tab2:
            availability_60 = host.main_max(
                values='availability_60', label='')
            plotly.vertical_bar_chart(df1=availability_60, x='y', y='count', text='percentage',
                                      color='#5cb85c', title='Availability of Next 60 Days', title_x=0.45)
        with tab3:
            availability_90 = host.main_max(
                values='availability_90', label='')
            plotly.vertical_bar_chart(df1=availability_90, x='y', y='count', text='percentage',
                                      color='#5cb85c', title='Availability of Next 90 Days', title_x=0.45)
        with tab4:
            availability_365 = host.main_max(
                values='availability_365', label='')
            plotly.vertical_bar_chart(df1=availability_365, x='y', y='count', text='percentage',
                                      color='#5cb85c', title='Availability of Next 365 Days', title_x=0.45)

        # vertical_bar chart
        tab1, tab2 = st.tabs(['Number of Reviews', 'Review Scores'])
        with tab1:
            number_of_reviews = host.main_max(
                values='number_of_reviews', label='')
            plotly.vertical_bar_chart(df1=number_of_reviews, x='y', y='count', text='percentage',
                                      color='#5D9A96', title='Number of Reviews', title_x=0.45)
        with tab2:
            review_scores = host.main_max(values='review_scores', label='')
            plotly.vertical_bar_chart(df1=review_scores, x='y', y='count', text='percentage',
                                      color='#5D9A96', title='Review Scores', title_x=0.45)


# streamlit title, background color and tab configuration
streamlit_config()
st.write('')


with st.sidebar:
    image_url = 'airbnb_banner.jpeg'
    st.image(image_url, use_column_width=True)

    option = option_menu(menu_title='', options=['Migrating to SQL','Features Analysis', 'Host Analysis','Explore Data','Exit'],
                         icons=['database-fill', 'list-task', 'person-circle', 'sign-turn-right-fill',])
    col1, col2, col3 = st.columns([0.26, 0.48, 0.26])
    with col2:
        button = st.button(label='Submit')
if button and option == 'Migrating to SQL':
    st.write('')
    sql.create_table()
    sql.delete_table()
    sql.data_migration()
    st.header('Airbnb Analysis')
    st.subheader("Airbnb is an American San Francisco-based company operating an online marketplace for short- and long-term homestays and experiences. The company acts as a broker and charges a commission from each booking. The company is credited with revolutionizing the tourism industry, while also having been the subject of intense criticism by residents of tourism hotspot cities like Barcelona and Venice for enabling an unaffordable increase in home rents, and for a lack of regulation.")
    st.subheader("Airbnb is an online marketplace that connects people who want to rent out their property with people who are looking for accommodations, typically for short stays. Airbnb offers hosts a relatively easy way to earn some income from their property. Guests often find that Airbnb rentals are cheaper and homier than hotels.")
    st.subheader('Skills take away From This Project:')
    st.subheader('Python Scripting, Data Preprocessing, Visualization, Plotly, Streamlit, MongoDb, Mysql database')
    st.subheader('Domain:')
    st.subheader('Travel Industry, Property management and Tourism')
    st.success('Successfully Data Migrated to SQL Database')


    st.balloons()


elif option == 'Features Analysis':
    try:
        st.write('')
        feature.feature_analysis()

    except:
        col1, col2 = st.columns(2)
        with col1:
            st.info('SQL Database is Currently Empty')


elif option == 'Host Analysis' :
    try:
        st.write('')
        col1, col2, col3 = st.columns(3)
        with col1:
            countries_list = host.countries_list()
            country = st.selectbox(label='Country', options=countries_list)
        if country:
            host.host_analysis()

    except: 
       st.info(f'SQL Database is Currently Empty')

elif option== 'Explore Data':
    room_type_df =df1.groupby(by=["room_type"], as_index=False)["price"].sum()
    cl1, cl2 = st.columns((2))
    with cl1:
        with st.expander("room_type wise price"):

            st.write(room_type_df.style.background_gradient(cmap="Blues"))
            csv = room_type_df.to_csv(index=False).encode('utf-8')
            st.download_button("Download Data", data=csv, file_name="room_type.csv", mime="text/csv",
                            help='Click here to download the data as a CSV file')

    with cl2:
        with st.expander("neighbourhood_group wise price"):
            neighbourhood_group = df1.groupby(by="host_neighbourhood", as_index=False)["price"].sum()
            st.write(neighbourhood_group.style.background_gradient(cmap="Oranges"))
            csv = neighbourhood_group.to_csv(index=False).encode('utf-8')
            st.download_button("Download Data", data=csv, file_name="neighbourhood_group.csv", mime="text/csv",
                            help='Click here to download the data as a CSV file')

    # Create a scatter plot
    data1 = px.scatter(df1, x="host_neighbourhood", y="host_location", color="room_type")
    data1['layout'].update(title="Room_type in the Neighbourhood and Neighbourhood_Group wise data using Scatter Plot.",
                            titlefont=dict(size=20), xaxis=dict(title="Neighbourhood_Group", titlefont=dict(size=20)),
                            yaxis=dict(title="Neighbourhood", titlefont=dict(size=20)))
    st.plotly_chart(data1, use_container_width=True)

    with st.expander("Detailed Room Availability and Price View Data in the Neighbourhood"):
        st.write(df1.iloc[:500, 1:20:2].style.background_gradient(cmap="Oranges"))
        
    # Download orginal DataSet
    csv = df1.to_csv(index=False).encode('utf-8')
    st.download_button('Download Data', data=csv, file_name="Data.csv", mime="text/csv")

    import plotly.figure_factory as ff

    st.subheader(":point_right: Neighbourhood_group wise Room_type and Minimum stay nights")
    with st.expander("Summary_Table"):
        df_sample = df1[0:5][["host_listings_count", "host_neighbourhood", "number_of_reviews", "room_type", "price", "minimum_nights", "host_name"]]
        fig = ff.create_table(df_sample, colorscale="Cividis")
        st.plotly_chart(fig, use_container_width=True)

    # map function for room_type

    # If your DataFrame has columns 'Latitude' and 'Longitude':
    st.subheader("Airbnb Analysis in Map view")
    df = df1.rename(columns={"Latitude": "lat", "Longitude": "lon"})

    st.map(df)


elif option == 'Exit':
    st.write('')
    import mysql.connector
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    )

    print(mydb)
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute("use Airbnb")
    mydb.close()
    col1, col2 = st.columns(2)

 # Load and display the image
    with col1:
            image1 = Image.open("/Users/karthickkumar/Desktop/Airbnb/airbnb_logo.png")
            st.image(image1, width=300)
            
    with col2:
        col2.subheader("NAME : Anandhavalli")
        col2.subheader("EMAIL: anandhavallikarthick@gmail.com")
        col2.subheader("BATCH : DT18DT19")
      
    st.success('Thank you for your time. Exiting the application')
    st.balloons()
