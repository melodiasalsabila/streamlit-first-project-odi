import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


# load cleaned data
all_df = pd.read_csv("datalengkap_050324.csv")
all_df["datetime"] = pd.to_datetime(all_df["datetime"])

df_wd = pd.read_csv("data_wd.csv")

# Filter data
min_date = all_df["datetime"].min()
max_date = all_df["datetime"].max()

with st.sidebar:
    st.image("https://github.com/melodiasalsabila/streamlit-first-project-odi/blob/main/logo_heheweather.jpg?raw=true")

    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Select desired date range!',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

    # unique items of select boxes
    stationList = all_df["station"].drop_duplicates()
    FilterStation = st.selectbox("Select desired station!", stationList)

filtered_df = all_df.loc[(all_df["station"] == FilterStation)]
                     
main_df = filtered_df[(all_df["datetime"] >= str(start_date)) & 
                (all_df["datetime"] <= str(end_date))]

filtered_wd_df = df_wd.loc[(df_wd["station"] == FilterStation)]
                     
main_wd_df = filtered_wd_df[(df_wd["datetime"] >= str(start_date)) & 
                (df_wd["datetime"] <= str(end_date))]


st.image("https://images.pexels.com/photos/2846034/pexels-photo-2846034.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1")

st.title(':warning: Beijing Pollution Dashboard :warning:')
st.header('Data from {} station during {} until {}'.format(FilterStation, start_date, end_date))

tab1, tab2, tab3 = st.tabs(["Pollutant Chart", "Other Conditions", "Raw Data"])
with tab1:
    st.subheader('Concentration of PM2.5 over time')
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
    main_df["datetime"],
    main_df["PM2.5"],
    marker='o', 
    linewidth=2,
    color="#90CAF9"
    )
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    
    st.pyplot(fig)

    st.subheader('Concentration of PM10 over time')
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
    main_df["datetime"],
    main_df["PM10"],
    marker='o', 
    linewidth=2,
    color="#90CAF9"
    )
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    
    st.pyplot(fig)

    st.subheader('Concentration of SO2 over time')
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
    main_df["datetime"],
    main_df["SO2"],
    marker='o', 
    linewidth=2,
    color="#90CAF9"
    )
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    
    st.pyplot(fig)

    st.subheader('Concentration of NO2 over time')
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
    main_df["datetime"],
    main_df["NO2"],
    marker='o', 
    linewidth=2,
    color="#90CAF9"
    )
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    
    st.pyplot(fig)

    st.subheader('Concentration of CO over time')
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
    main_df["datetime"],
    main_df["CO"],
    marker='o', 
    linewidth=2,
    color="#90CAF9"
    )
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    
    st.pyplot(fig)

    st.subheader('Concentration of O3 over time')
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
    main_df["datetime"],
    main_df["O3"],
    marker='o', 
    linewidth=2,
    color="#90CAF9"
    )
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    
    st.pyplot(fig)


with tab2:
    st.subheader('Average conditions during selected date range')
    col1, col2, col3 = st.columns(3)

    with col1:
        datacol1 = main_df["TEMP"].mean()
        st.metric("Average Temperature", value="{:.1f}°C".format(datacol1))

    with col2:
        datacol2 = main_df["WSPM"].mean()
        st.metric("Average Wind Speed", value="{:.1f}m/s".format(datacol2))

    with col3:
        datacol3 = main_df["RAIN"].mean()
        st.metric("Average Precipitation", value="{:.1f}mm".format(datacol3))

    st.subheader('Wind Direction Tendencies')
    df_piechart = main_wd_df["wd"].value_counts().reset_index()
    fig, ax = plt.subplots(figsize=(11, 9))
    plt.pie(df_piechart["count"], labels=df_piechart["wd"], autopct='%1.0f%%')

    st.pyplot(fig)

    with st.expander("What does these labels mean?"):
        st.write(
            """
            These labels are indicating the direction of the wind according to a 16-wind compass rose. 
            here are north (N), east (E), south (S), west (W),
            northeast (NE), southeast (SE), southwest (SW), northwest (NW), 
            north-northeast (NNE), east-northeast (ENE), east-southeast (ESE), 
            south-southeast (SSE), south-southwest (SSW), west-southwest (WSW),
            west-northwest (WNW), and north-northwest (NNW).
            """
        )



with tab3:
    df_dataset = main_df.reset_index().drop(columns='Unnamed: 0')
    st.dataframe(data=df_dataset, width=1200, height=500)


