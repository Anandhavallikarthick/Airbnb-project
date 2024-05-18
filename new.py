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





class feature():     

  

    def feature_analysis():
        import mysql.connector
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        )

        print(mydb)
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("use Airbnb")
        
        
        mycursor.execute(f"""select distinct country,street,property_type,room_type,host_location,price,review_scores from airbnb order by price""")
        mydb.commit()
        s = mycursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        data = pd.DataFrame(s, columns=['Country','street','property_type','room_type','host_location','price','review_scores'], index=i)
        data = data.rename_axis('S.No')
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))

        # Vertical bar chart for property type vs count
        mycursor.execute("SELECT property_type, COUNT(property_type) AS Total_propertycount FROM airbnb GROUP BY property_type ORDER BY COUNT(property_type) DESC LIMIT 10")

# Fetch results and create DataFrame
        df = pd.DataFrame(mycursor.fetchall(), columns=['property_type', 'Total_propertycount'])

# Create a bar chart with color based on property_type
        fig = px.bar(df, 
             x='property_type', 
             y='Total_propertycount', 
             title='Property Type vs Count',
             color='property_type',  # Specify the column to use for color
             color_discrete_sequence=px.colors.qualitative.Pastel)  # Set color palette

# Display the chart in Streamlit
        st.plotly_chart(fig, use_container_width=True)
        
        # Line & pie charts
        col1, col2 = st.columns(2)
        with col1:
           mycursor.execute("SELECT bed_type, COUNT(bed_type) AS Total_bedcount FROM airbnb GROUP BY bed_type ORDER BY COUNT(bed_type) DESC LIMIT 10")

            # Fetch results and create DataFrame
           df = pd.DataFrame(mycursor.fetchall(), columns=['bed_type', 'Total_bedcount'])

            # Create a donut (pie) chart
           fig = px.pie(df, 
                        values='Total_bedcount', 
                        names='bed_type', 
                        title='Bed Type Distribution',
                        hole=0.5)  # Adjust the 'hole' parameter to change the size of the center hole (0 for no hole)
           
           fig.update_layout(
                title={
                    'text': 'Bed Type Distribution',
                    'y':0.95,  # Title y position
                    'x':0.40,  # Title x position (center)
                    'xanchor': 'center',  # Horizontal anchor
                    'yanchor': 'top'  # Vertical anchor
                },
                width=800,  # Specify the width
                height=600  # Specify the height
            )
           st.plotly_chart(fig, use_container_width=True)
# Display the chart in Streamlit
        with col2:
            mycursor.execute("SELECT room_type, COUNT(room_type) AS Total_roomcount FROM airbnb GROUP BY room_type ORDER BY COUNT(room_type) DESC LIMIT 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['room_type', 'Total_roomcount'])
            fig = px.pie(df, title='Room Type Distribution', names='room_type', values='Total_roomcount')
            fig.update_layout(
                title={
                    'text': 'Room Type Distribution',
                    'y':0.95,  # Title y position
                    'x':0.40,  # Title x position (center)
                    'xanchor': 'center',  # Horizontal anchor
                    'yanchor': 'top'  # Vertical anchor
                },
                width=800,  # Specify the width
                height=600  # Specify the height
            )
            
            st.plotly_chart(fig, use_container_width=True)

        # Tabs for minimum and maximum nights vs average price
        tab1, tab2 = st.tabs(['Minimum Nights', 'Maximum Nights'])
        with tab1:
            mycursor.execute("SELECT minimum_nights, AVG(price) AS Avg_price FROM airbnb GROUP BY minimum_nights ORDER BY minimum_nights DESC LIMIT 10")

            # Fetch results and create DataFrame
            df = pd.DataFrame(mycursor.fetchall(), columns=['minimum_nights', 'Avg_price'])

            # Create a line chart
            fig = px.line(df, 
                        title='Minimum Nights Stay vs Average Price', 
                        x='minimum_nights', 
                        y='Avg_price',
                        labels={'minimum_nights': 'Minimum Nights', 'Avg_price': 'Average Price'})

            # Customize layout if needed
            fig.update_layout(xaxis_title='Minimum Nights', yaxis_title='Average Price')

            # Display the chart in Streamlit
            st.plotly_chart(fig, use_container_width=True)
        with tab2:
           
            mycursor.execute("SELECT maximum_nights, price FROM airbnb WHERE maximum_nights <= 50000 ORDER BY maximum_nights desc limit 100")
            # Fetch results and create DataFrame
            df = pd.DataFrame(mycursor.fetchall(), columns=['maximum_nights', 'Avg_price'])

            # Create a line chart
            fig = px.line(df, 
                        title='maximum nights Stay vs Average Price', 
                        x='maximum_nights', 
                        y='Avg_price',
                        labels={'maximum_nights': 'maximum_nights', 'Avg_price': 'Average Price'})

            # Customize layout if needed
            fig.update_layout(xaxis_title='maximum nights', yaxis_title='Average Price')

            # Display the chart in Streamlit
            st.plotly_chart(fig, use_container_width=True)
        # Line chart for cancellation policy vs count by property type  
        mycursor.execute("SELECT cancellation_policy,  COUNT(*) AS policy_count FROM airbnb GROUP BY cancellation_policy ORDER BY policy_count DESC LIMIT 10")
        df = pd.DataFrame(mycursor.fetchall(), columns=['cancellation_policy',  'policy_count'])
        fig = px.line(df, title='Cancellation Policy vs Count', x='cancellation_policy', y='policy_count')
        st.plotly_chart(fig, use_container_width=True)

        # Vertical bar chart for accommodates vs average price by property type
        mycursor.execute("""
            SELECT accommodates, AVG(price) AS Avg_price 
            FROM airbnb 
            GROUP BY accommodates 
            ORDER BY Avg_price 
            LIMIT 10
        """)

        # Fetch the results and create a DataFrame
        df = pd.DataFrame(mycursor.fetchall(), columns=['Accommodates', 'Avg_price'])



        # Create a horizontal bar chart using Plotly Express
        fig = px.bar(
            df,
            x='Avg_price',
            y='Accommodates',
            orientation='h', 
            title='Average Price by Accommodation Capacity',
            labels={'Accommodates': 'Accommodates', 'Avg_price': 'Average Price'}
        )

        # Update the layout for better visualization
        fig.update_layout(
            titlefont=dict(size=20),
            xaxis=dict(title="Average Price", titlefont=dict(size=20)),
            yaxis=dict(title="Accommodates", titlefont=dict(size=20))
        )

        # Display the horizontal bar chart in Streamlit
        st.plotly_chart(fig, use_container_width=True)
        # Tabs for beds, bedrooms, bathrooms vs average price by property type
        tab1, tab2, tab3 = st.tabs(['Beds', 'Bedrooms', 'Bathrooms'])
        with tab1:
           mycursor.execute("""
            SELECT country,bed_type, AVG(price) AS Avg_price, property_type 
            FROM airbnb 
            GROUP BY bed_type, property_type,country
            
        """)

        # Fetch the results and create a DataFrame
           df = pd.DataFrame(mycursor.fetchall(), columns=['country','bed_type', 'Avg_price', 'property_type'])

        
        # Create a sunburst chart using Plotly Express
           fig_sunburst = px.sunburst(
            df,
            path=['country','property_type', 'bed_type'],
            values='Avg_price',
            title='Average Price by Property Type and Bed_type'
        )

# Update the layout for the sunburst chart to make it bigger
           fig_sunburst.update_layout(
            width=600,
            height=600,
            title_font=dict(size=24)
        )
# Display the sunburst chart in Streamlit
           st.plotly_chart(fig_sunburst, use_container_width=True)
        
        with tab2:
            mycursor.execute("""
            SELECT country,bedrooms, AVG(price) AS Avg_price, property_type 
            FROM airbnb 
            GROUP BY bedrooms, property_type,country
            
        """)

        # Fetch the results and create a DataFrame
            df = pd.DataFrame(mycursor.fetchall(), columns=['country','bedrooms', 'Avg_price', 'property_type'])

        
        # Create a sunburst chart using Plotly Express
            fig_sunburst = px.sunburst(
            df,
            path=['country','property_type', 'bedrooms'],
            values='Avg_price',
            title='Average Price by Property Type and bedrooms'
        )

# Update the layout for the sunburst chart to make it bigger
            fig_sunburst.update_layout(
            width=600,
            height=600,
            title_font=dict(size=24)
        )
# Display the sunburst chart in Streamlit
            st.plotly_chart(fig_sunburst, use_container_width=True)
            
            
           
        
        with tab3:
            
            mycursor.execute("""
            SELECT country,bathrooms, AVG(price) AS Avg_price, property_type 
            FROM airbnb 
            GROUP BY bedrooms, property_type,country
            
        """)

        # Fetch the results and create a DataFrame
            df = pd.DataFrame(mycursor.fetchall(), columns=['country','bathrooms', 'Avg_price', 'property_type'])

        
        # Create a sunburst chart using Plotly Express
            fig_sunburst = px.sunburst(
            df,
            path=['country','property_type', 'bathrooms'],
            values='Avg_price',
            title='Average Price by Property Type and bathrooms'
        )

# Update the layout for the sunburst chart to make it bigger
            fig_sunburst.update_layout(
            width=600,
            height=600,
            title_font=dict(size=24)
        )
# Display the sunburst chart in Streamlit
            st.plotly_chart(fig_sunburst, use_container_width=True)

            
                        
        mycursor.execute("""
            SELECT room_type,AVG(price) AS Avg_price, property_type, country 
            FROM airbnb 
            GROUP BY  property_type, country 
            ORDER BY Avg_price 
        """)

        # Fetch the results and create a DataFrame
        df = pd.DataFrame(mycursor.fetchall(), columns=['room_type','Avg_price', 'Property_Type', 'Country'])

        

        # Create a sunburst chart using Plotly Express
        fig = px.sunburst(
            df,
            path=['Country', 'Property_Type', 'room_type'],
            values='Avg_price',
            title='Average Price  Property Type, and Country and room_type '
        )

        fig.update_layout(
            width=700,
            height=700,
            title_font=dict(size=24)
        )

        # Display the sunburst chart in Streamlit
        st.plotly_chart(fig, use_container_width=True)

                # Tabs for price, cleaning fee, extra people, guests included by property type
        tab1, tab2, tab3, tab4 = st.tabs(['Price', 'Cleaning Fee', 'Extra People', 'Guests Included'])
        with tab1:
                mycursor.execute("SELECT property_type, AVG(price) AS Avg_price FROM airbnb GROUP BY property_type order by Avg_price desc limit 10")
                df = pd.DataFrame(mycursor.fetchall(), columns=['property_type', 'Avg_price'])
                fig = px.bar(df, x='property_type', y='Avg_price', title='Average Price by Property Type',color='property_type')
                st.plotly_chart(fig, use_container_width=True)
            
        with tab2:
            mycursor.execute("SELECT property_type, AVG(cleaning_fee) AS Avg_cleaning_fee FROM airbnb WHERE cleaning_fee IS NOT NULL GROUP BY property_type order by Avg_cleaning_fee desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['property_type', 'Avg_cleaning_fee'])
            fig = px.bar(df, x='property_type', y='Avg_cleaning_fee', title='Average Cleaning Fee by Property Type',color='property_type')
            st.plotly_chart(fig, use_container_width=True)
        
        with tab3:
            mycursor.execute("""
            SELECT extra_people, COUNT(extra_people) AS count_extra_people, AVG(price) as Average_price 
            FROM airbnb 
            GROUP BY extra_people 
            ORDER BY count_extra_people 
            LIMIT 10
        """)

        # Fetch the results and create a DataFrame
            df = pd.DataFrame(mycursor.fetchall(), columns=['extra_people', 'count_extra_people', 'Average_price'])

        # Create a pie chart using Plotly Express
            fig = px.pie(
                df,
                values='Average_price',
                names='extra_people',
                title='Average price of Extra People',
                hole=0.3,  # Optional: to create a donut chart
            )

        # Update the layout to make the chart bigger
            fig.update_layout(
                width=600,  # Specify the width
                height=600,  # Specify the height
                titlefont=dict(size=20)
            )

       # Display the pie chart in Streamlit
            st.plotly_chart(fig, use_container_width=True)

        with tab4:
            mycursor.execute("""
            SELECT guests_included, COUNT(guests_included) AS cguests_included, AVG(price) as Average_price 
            FROM airbnb 
            GROUP BY guests_included 
            ORDER BY cguests_included 
            LIMIT 10
        """)

        # Fetch the results and create a DataFrame
            df = pd.DataFrame(mycursor.fetchall(), columns=['guests_included', 'cguests_included', 'Average_price'])

        # Create a pie chart using Plotly Express
            fig = px.pie(
                df,
                values='Average_price',
                names='guests_included',
                title='Average price of guests included',
                
            )

        # Update the layout to make the chart bigger
            fig.update_layout(
                width=600,  # Specify the width
                height=600,  # Specify the height
                titlefont=dict(size=20)
            )

       # Display the pie chart in Streamlit
            st.plotly_chart(fig, use_container_width=True)
        # Line chart for host response time vs count
        mycursor.execute("SELECT host_response_time, COUNT(*) AS listing_count FROM airbnb WHERE host_response_time IS NOT NULL GROUP BY host_response_time ORDER BY FIELD(host_response_time, 'within an hour', 'within a few hours', 'within a day', 'a few days or more')")
        df = pd.DataFrame(mycursor.fetchall(), columns=['host_response_time', 'listing_count'])
        fig = px.line(df, x='host_response_time', y='listing_count', title='Count of Listings by Host Response Time')
        st.plotly_chart(fig, use_container_width=True)


        mycursor.execute("""
            SELECT Accommodates,AVG(price) AS Avg_price, property_type, country 
            FROM airbnb 
            GROUP BY  property_type, country 
            ORDER BY Avg_price 
        """)

            # Fetch the results and create a DataFrame
        df = pd.DataFrame(mycursor.fetchall(), columns=['Accommodates','Avg_price', 'Property_Type', 'Country'])

        

        # Create a sunburst chart using Plotly Express
        fig = px.sunburst(
            df,
            path=['Country', 'Property_Type', 'Accommodates'],
            values='Avg_price',
            title='Average Price by Property Type,Country and Accommodates'
        )
        # Update the layout to make the chart bigger
        fig.update_layout(
            width=700,
            height=700,
            title_font=dict(size=24)
        )

    

        # Display the sunburst chart in Streamlit
        st.plotly_chart(fig, use_container_width=True)

        
        

                # Tabs for host response rate and host listings count
        tab1, tab2 = st.tabs(['Host Response Rate', 'Host Listings Count'])
        with tab1:
            mycursor.execute(f"""select host_name, host_response_rate
                            from airbnb WHERE host_response_rate IS NOT NULL
                            group by host_name
                            limit 10""")
            df = pd.DataFrame(mycursor.fetchall(), columns=['host_name', 'host_response_rate'])
            fig = px.bar(df, x='host_name', y='host_response_rate', title='Host Name by Host Response Rate')
            st.plotly_chart(fig, use_container_width=True)

        with tab2:
            mycursor.execute("""
                SELECT host_listings_count, host_name
                FROM airbnb
                WHERE host_listings_count IS NOT NULL
                GROUP BY host_name
                limit 10
            """)
            
            # Fetch the results and create a DataFrame
            df = pd.DataFrame(mycursor.fetchall(), columns=['host_listings_count', 'host_name'])
            
            # Create a bar chart using Plotly
            fig = px.bar(df,
                        x='host_name',
                        y='host_listings_count',
                        title='Host Name by Host Listings Count',
                        labels={'host_listings_count': 'Host Listings Count', 'host_name': 'host_name'})
            
            # Customize layout if needed
            fig.update_layout(xaxis_title='host_name', yaxis_title='Host Listings Count')
            
            # Display the chart in Streamlit
            st.plotly_chart(fig, use_container_width=True)




        # SQL Query to fetch the distinct records
        mycursor.execute("""
            SELECT DISTINCT Country, Host_Neighbourhood, property_type,count(Host_Neighbourhood) as counts
            FROM airbnb group by Host_Neighbourhood
        """)

        # Fetch the results and create a DataFrame
        df = pd.DataFrame(mycursor.fetchall(), columns=['Country', 'Host_Neighbourhood', 'Property_Type','counts'])

        # Create a scatter plot using Plotly Express
        fig = px.scatter(
            df,
            x="Country",
            y="Host_Neighbourhood",
            color="Property_Type",
            size = 'counts',
            title="Property Type in country the Neighbourhood and Neighbourhood Group-wise Data",
            labels={"Country": "Neighbourhood Group", "Host_Neighbourhood": "Neighbourhood", 'Property_Type': 'Property Type'}
        )

        # Update the layout
        fig.update_layout(
            titlefont=dict(size=20),
            xaxis=dict(title="Neighbourhood Group", titlefont=dict(size=20)),
            yaxis=dict(title="Neighbourhood", titlefont=dict(size=20))
        )

      

        # Display the scatter plot in Streamlit
        st.plotly_chart(fig, use_container_width=True)

        tab1, tab2, tab3,tab4 = st.tabs(
            ['Host is Superhost', 'Host has Profile Picture', 'Host Identity Verified','Is_Location_exact'])
        with tab1:
            mycursor.execute("""
                SELECT host_is_superhost, COUNT(host_is_superhost) as count
                FROM airbnb
                GROUP BY host_is_superhost
            """)

            # Fetch the results and create a DataFrame
            df1 = pd.DataFrame(mycursor.fetchall(), columns=['host_is_superhost', 'count'])

            # Create a pie chart using Plotly Express
            fig = px.pie(
                df1,
                names='host_is_superhost',
                values='count',
                title='Host is Superhost'
            )

            # Update the layout to center the title
            fig.update_layout(
                title={
                    'text': 'Host is Superhost',
                    'y':0.95,  # Title y position
                    'x':0.44,  # Title x position (center)
                    'xanchor': 'center',  # Horizontal anchor
                    'yanchor': 'top'  # Vertical anchor
                },
                width=800,  # Specify the width
                height=600  # Specify the height
            )
           
            # Display the pie chart in Streamlit
            st.plotly_chart(fig, use_container_width=True)


        with tab2:
            mycursor.execute(f"""select  host_has_profile_pic, count(host_has_profile_pic) as count
                           from airbnb
                           group by host_has_profile_pic
                      """)
            df1 = pd.DataFrame(mycursor.fetchall(), columns=['host_has_profile_pic','count'])

            fig = px.pie(df1, names = 'host_has_profile_pic',
                             values = 'count', title='host has profile picture')
            # Update the layout to center the title
            fig.update_layout(
                title={
                    'text': 'Host has Profile Picture',
                    'y':0.95,  # Title y position
                    'x':0.44,  # Title x position (center)
                    'xanchor': 'center',  # Horizontal anchor
                    'yanchor': 'top'  # Vertical anchor
                },
                width=800,  # Specify the width
                height=600  # Specify the height
            )

           
            # Display the pie chart in Streamlit
            st.plotly_chart(fig, use_container_width=True)

        with tab3:
            mycursor.execute(f"""select  host_identity_verified, count(host_identity_verified) as count
                           from airbnb
                           group by host_identity_verified
                      """)
            df1 = pd.DataFrame(mycursor.fetchall(), columns=['host_identity_verified','count'])

            fig = px.pie(df1, names = 'host_identity_verified',
                             values = 'count', title='host identity verified')
            # Update the layout to center the title
            fig.update_layout(
                title={
                    'text': 'Host Identity Verified',
                    'y':0.95,  # Title y position
                    'x':0.44,  # Title x position (center)
                    'xanchor': 'center',  # Horizontal anchor
                    'yanchor': 'top'  # Vertical anchor
                },
                width=800,  # Specify the width
                height=600  # Specify the height
            )

           
            # Display the pie chart in Streamlit
            st.plotly_chart(fig, use_container_width=True)

        with tab4:
            mycursor.execute(f"""select  is_location_exact, count(is_location_exact) as count
                           from airbnb
                           group by is_location_exact
                      """)
            df1 = pd.DataFrame(mycursor.fetchall(), columns=['is_location_exact','count'])

            fig = px.pie(df1, names = 'is_location_exact',
                             values = 'count', title='Is Location Exact')
            # Update the layout to center the title
            fig.update_layout(
            title={
                'text': 'Is Location Exact',
                'y':0.95,  # Title y position
                'x':0.44,  # Title x position (center)
                'xanchor': 'center',  # Horizontal anchor
                'yanchor': 'top'  # Vertical anchor
            },
            width=800,  # Specify the width
            height=600  # Specify the height
        )

           
            # Display the pie chart in Streamlit
            st.plotly_chart(fig, use_container_width=True)

        tab1, tab2, tab3, tab4 = st.tabs(['Availability 30', 'Availability 60',
                                          'Availability 90', 'Availability 365'])
        with tab1:
            mycursor.execute("""
                SELECT availability_30, COUNT(availability_30) as count
                FROM airbnb
                GROUP BY availability_30
                LIMIT 10
            """)

            # Fetch the results and create a DataFrame
            df = pd.DataFrame(mycursor.fetchall(), columns=['availability_30', 'count'])

            # Create a bar chart using Plotly Express
            fig = px.bar(
                df,
                x='availability_30',
                y='count',
                title='Availability in the Next 30 Days'
            )

            # Update the layout to center the title and set chart size
            fig.update_layout(
                title={
                    'text': 'Availability in the Next 30 Days',
                    'y': 0.95,  # Title y position
                    'x': 0.5,  # Title x position (center)
                    'xanchor': 'center',  # Horizontal anchor
                    'yanchor': 'top'  # Vertical anchor
                },
                width=800,  # Specify the width
                height=600,  # Specify the height
                xaxis=dict(
                    title='Availability in the Next 30 Days',
                    titlefont=dict(size=20)
                ),
                yaxis=dict(
                    title='Count',
                    titlefont=dict(size=20)
                )
            )

            # Display the bar chart in Streamlit
            st.plotly_chart(fig, use_container_width=True)

                
        
        with tab2:
            mycursor.execute("""
                SELECT availability_60, COUNT(availability_60) as count
                FROM airbnb
                GROUP BY availability_60
                LIMIT 10
            """)

            # Fetch the results and create a DataFrame
            df = pd.DataFrame(mycursor.fetchall(), columns=['availability_60', 'count'])

            # Create a bar chart using Plotly Express
            fig = px.bar(
                df,
                x='availability_60',
                y='count',
                title='Availability in the Next 60 Days'
            )

            # Update the layout to center the title and set chart size
            fig.update_layout(
                title={
                    'text': 'Availability in the Next 60 Days',
                    'y': 0.95,  # Title y position
                    'x': 0.5,  # Title x position (center)
                    'xanchor': 'center',  # Horizontal anchor
                    'yanchor': 'top'  # Vertical anchor
                },
                width=800,  # Specify the width
                height=600,  # Specify the height
                xaxis=dict(
                    title='Availability in the Next 60 Days',
                    titlefont=dict(size=20)
                ),
                yaxis=dict(
                    title='Count',
                    titlefont=dict(size=20)
                )
            )

            # Display the bar chart in Streamlit
            st.plotly_chart(fig, use_container_width=True)
        with tab3:
            mycursor.execute("""
                SELECT availability_90, COUNT(availability_90) as count
                FROM airbnb
                GROUP BY availability_90
                LIMIT 10
            """)

            # Fetch the results and create a DataFrame
            df = pd.DataFrame(mycursor.fetchall(), columns=['availability_90', 'count'])

            # Create a bar chart using Plotly Express
            fig = px.bar(
                df,
                x='availability_90',
                y='count',
                title='Availability in the Next 90 Days'
            )

            # Update the layout to center the title and set chart size
            fig.update_layout(
                title={
                    'text': 'Availability in the Next 90 Days',
                    'y': 0.95,  # Title y position
                    'x': 0.5,  # Title x position (center)
                    'xanchor': 'center',  # Horizontal anchor
                    'yanchor': 'top'  # Vertical anchor
                },
                width=800,  # Specify the width
                height=600,  # Specify the height
                xaxis=dict(
                    title='Availability in the Next 30 Days',
                    titlefont=dict(size=20)
                ),
                yaxis=dict(
                    title='Count',
                    titlefont=dict(size=20)
                )
            )

            # Display the bar chart in Streamlit
            st.plotly_chart(fig, use_container_width=True)
        with tab4:
            mycursor.execute("""
                SELECT availability_365, COUNT(availability_365) as count
                FROM airbnb
                GROUP BY availability_365
                LIMIT 10
            """)

            # Fetch the results and create a DataFrame
            df = pd.DataFrame(mycursor.fetchall(), columns=['availability_365', 'count'])

            # Create a bar chart using Plotly Express
            fig = px.bar(
                df,
                x='availability_365',
                y='count',
                title='Availability in the Next 365 Days'
            )

            # Update the layout to center the title and set chart size
            fig.update_layout(
                title={
                    'text': 'Availability in the Next 365 Days',
                    'y': 0.95,  # Title y position
                    'x': 0.5,  # Title x position (center)
                    'xanchor': 'center',  # Horizontal anchor
                    'yanchor': 'top'  # Vertical anchor
                },
                width=800,  # Specify the width
                height=600,  # Specify the height
                xaxis=dict(
                    title='Availability in the Next 365 Days',
                    titlefont=dict(size=20)
                ),
                yaxis=dict(
                    title='Count',
                    titlefont=dict(size=20)
                )
            )

            # Display the bar chart in Streamlit
            st.plotly_chart(fig, use_container_width=True)
        # vertical_bar,pie,map chart
        tab1, tab2, tab3 = st.tabs(['Number of Reviews', 'Maximum Number of Reviews', 'Review Scores'])
        with tab1:
            mycursor.execute("""
                SELECT name, COUNT(Number_of_Reviews) as Number_of_Reviews
                FROM airbnb
                WHERE name IS NOT NULL
                GROUP BY Number_of_Reviews
                LIMIT 10
            """)

            # Fetch the results and create a DataFrame
            df = pd.DataFrame(mycursor.fetchall(), columns=['name', 'Number of Reviews'])

            # Create a pie chart using Plotly Express
            fig = px.pie(
                df,
                names='name',
                values='Number of Reviews',
                title='Name by Number of Reviews'
            )

            # Update the layout to center the title and set chart size
            fig.update_layout(
                title={
                    'text': 'Name by Number of Reviews',
                    'y': 0.95,  # Title y position
                    'x': 0.40,  # Title x position (center)
                    'xanchor': 'center',  # Horizontal anchor
                    'yanchor': 'top'  # Vertical anchor
                },
                width=800,  # Specify the width
                height=600  # Specify the height
            )

           

            # Display the pie chart in Streamlit
            st.plotly_chart(fig, use_container_width=True)

        with tab2:
            mycursor.execute("""
                SELECT Number_of_Reviews, name
                FROM airbnb
                WHERE Number_of_Reviews IS NOT NULL
                GROUP BY name
                ORDER BY Number_of_Reviews desc
                limit 10
            """)
            
            # Fetch the results and create a DataFrame
            df = pd.DataFrame(mycursor.fetchall(), columns=['Number of Reviews', 'name'])
            
            # Create a bar chart using Plotly
            fig = px.bar(df,
                        x='name',
                        y='Number of Reviews',
                        color='Number of Reviews',
                        title='Name by Number of Reviews',
                        color_continuous_scale='oranges',
                        labels={'Number of Reviews': 'Number of Reviews', 'name': 'name'})
            
            # Customize layout if needed
            fig.update_layout(
                title={
                    'text': 'Name by Number of Reviews',
                    'y': 0.95,  # Title y position
                    'x': 0.44,  # Title x position (center)
                    'xanchor': 'center',  # Horizontal anchor
                    'yanchor': 'top'  # Vertical anchor
                },
                width=800,  # Specify the width
                height=600,  # Specify the height
                xaxis=dict(
                    title='Name',
                    titlefont=dict(size=20)
                ),
                yaxis=dict(
                    title='Number of Reviews',
                    titlefont=dict(size=20)
                )
            )
            
            # Display the chart in Streamlit
            st.plotly_chart(fig, use_container_width=True)
        with tab3:
            mycursor.execute("""
                SELECT Review_scores, name
                FROM airbnb
                WHERE Review_scores IS NOT NULL
                GROUP BY name
                limit 10
            """)
            
            # Fetch the results and create a DataFrame
            df = pd.DataFrame(mycursor.fetchall(), columns=['Review_scores', 'name'])
            
            # Create a bar chart using Plotly
            fig = px.bar(df,
                        x='name',
                        y='Review_scores',
                        color='Review_scores',
                        title='Name by Review_scores',
                        color_continuous_scale='greens',
                        labels={'Review_scores': 'Review_scores', 'name': 'name'})
            
            # Customize layout if needed
            fig.update_layout(
                title={
                    'text': 'Name by Review_scores',
                    'y': 0.95,  # Title y position
                    'x': 0.44,  # Title x position (center)
                    'xanchor': 'center',  # Horizontal anchor
                    'yanchor': 'top'  # Vertical anchor
                },
                width=800,  # Specify the width
                height=600,  # Specify the height
                xaxis=dict(
                    title='Name',
                    titlefont=dict(size=20)
                ),
                yaxis=dict(
                    title='Review scores',
                    titlefont=dict(size=20)
                )
            )
            
            # Display the chart in Streamlit
            st.plotly_chart(fig, use_container_width=True)




# streamlit title, background color and tab configuration
streamlit_config()
st.write('')


with st.sidebar:
    image_url = 'airbnb_banner.jpeg'
    st.image(image_url, use_column_width=True)

    option = option_menu(menu_title='', options=['Migrating to SQL','Features Analysis','Explore Data','Exit'],
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
        col2.subheader("BATCH : MDTM20")
      
    st.success('Thank you for your time. Exiting the application')
    st.balloons()
