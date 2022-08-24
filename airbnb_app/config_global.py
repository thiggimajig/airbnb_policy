#!/usr/bin/env python3
import pandas as pd
from .models import AirbnbListings
# from . import policy_functions as pf
from datetime import date, time, datetime
import tracemalloc
# tracemalloc.start()
# from .models import AirbnbListings
#i think here we want to load all the data base maps and then import whenever i need them i
#in views.py ... 
#https://stackoverflow.com/questions/51198019/setting-database-variables-as-global-variables-python 
#trying for database optimization to create a function that calls all pf functions at beginning
#or will this not help because am i calling it when I import it above as pf? 
def get_time():
    today = date.today()
    current_time = time(datetime.now().hour, datetime.now().minute, datetime.now().second)
    date_today = datetime.combine(today, current_time)
    new_date_time = str(date_today).replace(" ", "_").replace("-", "_").replace(":", "_")
    return(new_date_time)


#so this made it a lot faster but still taking 30 seconds... 
new_date_time = get_time()
print("i'm running{}".format(new_date_time))
# getmapstuple = pf.getbubmaps()
# map_orig = getmapstuple[0]
# map_1 = getmapstuple[1]
# map_2 = getmapstuple[2]
# map_3 = getmapstuple[3]
# # print("i'm running census spot{}".format(new_date_time))
# census_map = getmapstuple[4]
#TODO why not just try mkaing the database a global
#yes that is the answer ^^^^ 
# df = pd.DataFrame(list(AirbnbListings.objects.all().values('id', 'has_liscense', 'days_rented_ltm', 'rounded_revenue_ltm', 'price', 'name', 'host_id', 'bedrooms', 'many_listings', 'availability_365', 'is_hotel', 'host_name', 'commercial', 'is_entire', 'latitude', 'longitude')))
# print(df.head())

#for more optimization
#i think i need to use iterator here to help memory issues... 
# star_set = Star.objects.all()
# # The `iterator()` method ensures only a few rows are fetched from
# # the database at a time, saving memory.
# for star in star_set.iterator():
#     print(star.name)
#try using @cached_property
df = pd.DataFrame(list(AirbnbListings.objects.all().values('effected_by_policy_3','effected_by_policy_2','effected_by_policy_1','host_since','host_total_listings_count','host_florence','reviews_per_month','accommodates','room_type','dist_duomo','id', 'has_liscense', 'neighbourhood_cleansed', 'license','listing_url','days_rented_ltm', 'rounded_revenue_ltm', 'price', 'name', 'host_id', 'bedrooms', 'many_listings', 'availability_365', 'is_hotel', 'host_name', 'commercial', 'is_entire', 'latitude', 'longitude')))
print("load data base is running from config")

#original
# def load_database_data():
#     # airbnb_data = AirbnbListings.objects.all().values('id', 'has_liscense', 'days_rented_ltm', 'rounded_revenue_ltm', 'price', 'name', 'host_id', 'bedrooms', 'many_listings', 'availability_365', 'is_hotel', 'host_name', 'commercial', 'is_entire', 'latitude', 'longitude')
#     # for listing in airbnb_data.iterator():
#     #     df = pd.DataFrame(list(listing))
#     #.iterator() tried to see if faster... 
#     df = pd.DataFrame(list(AirbnbListings.objects.all().values('effected_by_policy_3','effected_by_policy_2','effected_by_policy_1','host_since','host_total_listings_count','host_florence','reviews_per_month','accommodates','room_type','dist_duomo','id', 'has_liscense', 'neighbourhood_cleansed', 'license','listing_url','days_rented_ltm', 'rounded_revenue_ltm', 'price', 'name', 'host_id', 'bedrooms', 'many_listings', 'availability_365', 'is_hotel', 'host_name', 'commercial', 'is_entire', 'latitude', 'longitude')))
#     print("load data base is running")
#     return df

# snapshot = tracemalloc.take_snapshot()
# top_stats = snapshot.statistics('lineno')

# print("[ Top 10 ]")
# for stat in top_stats[:10]:
#     print(stat)