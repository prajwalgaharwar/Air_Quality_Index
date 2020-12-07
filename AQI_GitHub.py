#!/usr/bin/env python
# coding: utf-8

# In[377]:


import pandas as pd
import folium
from bs4 import BeautifulSoup as bs

from geopy.geocoders import ArcGIS
nom=ArcGIS()

update=False

coordinates={}
PM25={}
PM10={}
NO2={}
NH3={}
SO2={}
CO={}
OZONE={}
level={}
html = """<h4>Air Quality Information:</h4>
<b>Station:</b> %s<br />
<b>Last Updated:</b> %s<br /><br />

<b>PM2.5:</b><br />Min: %s -- Avg: %s -- Max: %s<br /><br />
<b>PM10:</b><br />Min: %s -- Avg: %s -- Max: %s<br /><br />
<b>NO2:</b><br />Min: %s -- Avg: %s -- Max: %s<br /><br />
<b>NH3:</b><br />Min: %s -- Avg: %s -- Max: %s<br /><br />
<b>SO2:</b><br />Min: %s -- Avg: %s -- Max: %s<br /><br />
<b>CO:</b><br />Min: %s -- Avg: %s -- Max: %s<br /><br />
<b>OZONE:</b><br />Min: %s -- Avg: %s -- Max: %s<br /><br />
"""


# Getting data from data.gov.in server

# In[378]:


api_key=""# Enter your data.gov.in api key here
url="https://api.data.gov.in/resource/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69?api-key="+api_key+"&format=csv&offset=0&limit=1600"
df=pd.read_csv(url)


# Initializing pollutant dictionary

# In[379]:


for a in range(len(df2["station"])):
    PM25[df2.at[a,'station']]={}
    PM10[df2.at[a,'station']]={}
    NO2[df2.at[a,'station']]={}
    NH3[df2.at[a,'station']]={}
    SO2[df2.at[a,'station']]={}
    CO[df2.at[a,'station']]={}
    OZONE[df2.at[a,'station']]={}

for Name in df["station"]:
        PM25[Name]['min']='NA'
        PM25[Name]['max']="NA"
        PM25[Name]['avg']="NA"
        PM10[Name]['min']="NA"
        PM10[Name]['max']="NA"
        PM10[Name]['avg']="NA"
        NO2[Name]['min']="NA"
        NO2[Name]['max']="NA"
        NO2[Name]['avg']="NA"
        NH3[Name]['min']="NA"
        NH3[Name]['max']="NA"
        NH3[Name]['avg']="NA"
        SO2[Name]['min']="NA"
        SO2[Name]['max']="NA"
        SO2[Name]['avg']="NA"
        CO[Name]['min']="NA"
        CO[Name]['max']="NA"
        CO[Name]['avg']="NA"
        OZONE[Name]['min']="NA"
        OZONE[Name]['max']="NA"
        OZONE[Name]['avg']="NA"
        
        


# Check for pre-strored coordinates of stations

# In[380]:


try:
    add=pd.read_csv('coordinates.csv')
    update=False
except:
    update=True


# Creating duplicate data frame
# 

# In[381]:


df['pollutant_min'] = df['pollutant_min'].fillna(0) 
df['pollutant_max'] = df['pollutant_max'].fillna(0) 
df['pollutant_avg'] = df['pollutant_avg'].fillna(0) 

df=df
df2=df
df["Complete_Address"]=df["station"]+", "+df["city"]+", "+df["state"]
df["Coordinates"]=None
df["latitude"]=None
df["longitude"]=None

df2=df2.drop(['id','country','state','city','last_update','Complete_Address','latitude','longitude','pollutant_unit'],axis=1)


# Adding pollutants to dictionary

# In[382]:


new=0
for a in range(len(df2["station"])):
    if df.at[a,'pollutant_id']=='PM2.5':
        PM25[df2.at[a,'station']]['min']=df2.at[a,'pollutant_min']
        PM25[df2.at[a,'station']]['max']=df2.at[a,'pollutant_max']
        PM25[df2.at[a,'station']]['avg']=df2.at[a,'pollutant_avg']
    
    elif df.at[a,'pollutant_id']=='PM10':
        PM10[df2.at[a,'station']]['min']=df2.at[a,'pollutant_min']
        PM10[df2.at[a,'station']]['max']=df2.at[a,'pollutant_max']
        PM10[df2.at[a,'station']]['avg']=df2.at[a,'pollutant_avg']
    
    elif df.at[a,'pollutant_id']=='NO2':
        NO2[df2.at[a,'station']]['min']=df2.at[a,'pollutant_min']
        NO2[df2.at[a,'station']]['max']=df2.at[a,'pollutant_max']
        NO2[df2.at[a,'station']]['avg']=df2.at[a,'pollutant_avg']
        
    elif df.at[a,'pollutant_id']=='NH3':
        NH3[df2.at[a,'station']]['min']=df2.at[a,'pollutant_min']
        NH3[df2.at[a,'station']]['max']=df2.at[a,'pollutant_max']
        NH3[df2.at[a,'station']]['avg']=df2.at[a,'pollutant_avg']
    
    elif df.at[a,'pollutant_id']=='SO2':
        SO2[df2.at[a,'station']]['min']=df2.at[a,'pollutant_min']
        SO2[df2.at[a,'station']]['max']=df2.at[a,'pollutant_max']
        SO2[df2.at[a,'station']]['avg']=df2.at[a,'pollutant_avg']
    
    elif df.at[a,'pollutant_id']=='CO':
        CO[df2.at[a,'station']]['min']=df2.at[a,'pollutant_min']
        CO[df2.at[a,'station']]['max']=df2.at[a,'pollutant_max']
        CO[df2.at[a,'station']]['avg']=df2.at[a,'pollutant_avg']
        
    elif df.at[a,'pollutant_id']=='OZONE':
        OZONE[df2.at[a,'station']]['min']=df2.at[a,'pollutant_min']
        OZONE[df2.at[a,'station']]['max']=df2.at[a,'pollutant_max']
        OZONE[df2.at[a,'station']]['avg']=df2.at[a,'pollutant_avg']
        
#print(len(PM25.keys()),len(PM10.keys()),len(NO2.keys()),len(NH3.keys()),len(SO2.keys()),len(CO.keys()),len(OZONE.keys()))    


# Checking if Update of coordinates is required

# In[383]:


#update flag from file import and cross referencing of data of station
if update is False:
    for a in range(len(df["Complete_Address"])):
        address=df.at[a,'Complete_Address']
    for b in range(len(add["Complete_Address"])):
        if df.at[a,'Complete_Address']== add.at[b,'Complete_Address']:
            pass
        else:
            if df.at[a,'Complete_Address']=="Ward-32 Bapupara, Siliguri - WBPCB, Siliguri, West_Bengal":
                pass
            else:
                update=True
                print(df.at[a,'Complete_Address'])
            


# Updating coordinate data if required

# In[384]:


if update is True:
    
    for a in range(len(df["id"])):
        add=df.at[a,'Complete_Address']
        
        if add in coordinates:
            pass
        else:
            try:
                #lst.append(df.at[a,'Complete_Address']+','+nom.geocode(add))
                data=nom.geocode(add)
                coordinates[add]=data
                #df2.at[a,'Coordinates']=nom.geocode(add)
            except:
                print("not for {} trying city ".format(df.at[a,'Complete_Address'] ))
                
                try:
                    add1=df.at[a,'city']
                    data=nom.geocode(add1)
                    coordinates[add]=data
                    print("updated for CITY {} the data is {}".format(add1,data))
                except:
                    print("failed for {} too".format(df.at[a,'city'] ))
                    pass
    
    
    
    for a in range(len(df["Complete_Address"])):
        df.at[a,'Coordinates']=coordinates.get(df.at[a,'Complete_Address'])
    df["latitude"]=df["Coordinates"].apply(lambda x: x.latitude if x!= None else None)
    df["longitude"]=df["Coordinates"].apply(lambda x: x.longitude if x!= None else None)
    
    selected_columns = df[["Complete_Address","latitude","longitude"]]
    new_df = selected_columns.copy()
    new_df=new_df.drop_duplicates()
    new_df.to_csv('coordinates.csv', header=True, index=False, encoding='utf-8')
    add=pd.read_csv('coordinates.csv')


# Inserting pre-stored coordinates in known locations
# 

# In[385]:


for a in range(len(df["Complete_Address"])):
    address=df.at[a,'Complete_Address']
    for b in range(len(add["Complete_Address"])):
        if df.at[a,'Complete_Address']== add.at[b,'Complete_Address']:
            df.at[a,'latitude']=add.at[b,'latitude']
            df.at[a,'longitude']=add.at[b,'longitude']
        else:
            pass


# Initializing data form Map

# In[386]:


ln=list(df["longitude"])
lt=list(df["latitude"])
Name=list(df["station"])
City =list(df["city"])
Last_up=list(df["last_update"])


# Function for threat colour

# In[387]:


def get_colour(name):
    if PM25[name]['avg']=='NA' or PM10[name]['avg']=='NA' or NO2[name]['avg']=='NA' or NH3[name]['avg']=='NA' or SO2[name]['avg']=='NA' or CO[name]['avg']=='NA' or OZONE[name]['avg']=='NA':
        return 'green'
#300+ Maroon
    elif int(PM25[name]['avg'])>=300 or int(PM10[name]['avg'])>=300 or int(NO2[name]['avg'])>=300 or int(NH3[name]['avg'])>=300 or int(SO2[name]['avg'])>=300 or int(CO[name]['avg'])>=300 or int(OZONE[name]['avg'])>=300:
        return "maroon"
#200+ int(Purple
    elif int(PM25[name]['avg'])>=200 or int(PM10[name]['avg'])>=200 or int(NO2[name]['avg'])>=200 or int(NH3[name]['avg'])>=200 or int(SO2[name]['avg'])>=200 or int(CO[name]['avg'])>=200 or int(OZONE[name]['avg'])>=200:
        return "purple"
#150+ Red
    elif int(PM25[name]['avg'])>=150 or int(PM10[name]['avg'])>=150 or int(NO2[name]['avg'])>=150 or int(NH3[name]['avg'])>=150 or int(SO2[name]['avg'])>=150 or int(CO[name]['avg'])>=150 or int(OZONE[name]['avg'])>=150:
        return "red"
#100+ Orange
    elif int(PM25[name]['avg'])>=100 or int(PM10[name]['avg'])>=100 or int(NO2[name]['avg'])>=100 or int(NH3[name]['avg'])>=100 or int(SO2[name]['avg'])>=100 or int(CO[name]['avg'])>=100 or int(OZONE[name]['avg'])>=100:
        return "orange"
#50+ Yellow
    elif int(PM25[name]['avg'])>=50 or int(PM10[name]['avg'])>=50 or int(NO2[name]['avg'])>=50 or int(NH3[name]['avg'])>=50 or int(SO2[name]['avg'])>=50 or int(CO[name]['avg'])>=50 or int(OZONE[name]['avg'])>=50:
        return "yellow"
#0 Green
    else:
        return "green"


# Adding map

# In[388]:




map=folium.Map(location=[23.208, 77.437],zoom_start=5,min_zoom=2)


# Adding features

# In[389]:


fg1=folium.FeatureGroup(name="Stations",overlay=True, control=False)

for lat,lon,name,city,time in zip(lt,ln,Name,City,Last_up):

        iframe = folium.IFrame(html=html % (name,time,
                           str(PM25[name]['min']),str(PM25[name]['avg']),str(PM25[name]['max']),
                           str(PM10[name]['min']),str(PM10[name]['avg']),str(PM25[name]['max']),
                           str(NO2[name]['min']),str(NO2[name]['avg']),str(PM25[name]['max']),
                           str(NH3[name]['min']),str(NH3[name]['avg']),str(PM25[name]['max']),
                           str(SO2[name]['min']),str(SO2[name]['avg']),str(PM25[name]['max']),
                           str(CO[name]['min']),str(CO[name]['avg']),str(PM25[name]['max']),
                           str(OZONE[name]['min']),str(OZONE[name]['avg']),str(PM25[name]['max'])),
                           width=350, height=200)
            
            
            
        fg1.add_child(folium.CircleMarker(location=[lat,lon],radius=5,
                               popup=folium.Popup(iframe),
                               fill_color=
                                          get_colour(name),
                                          color=get_colour(name),
                                     fill_opacity=0.7))


    
        
       
        
map.add_child(fg1)


# In[390]:


map.save("Map1.html")


# In[391]:


map.save("Map1.html")

