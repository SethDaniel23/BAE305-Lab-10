
import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("💧 Water Quality Contaminant Explorer")

# File Uploads
station_file = st.file_uploader("Upload station.csv", type="csv")
results_file = st.file_uploader("Upload narrowresults.csv", type="csv")

if station_file and results_file:
    # Load data
    stations = pd.read_csv(station_file)
    results = pd.read_csv(results_file)
    results['ActivityStartDate'] = pd.to_datetime(results['ActivityStartDate'])

    # Ensure expected columns exist
    if 'site_id' not in stations.columns:
        st.error("station.csv must contain a 'site_id' column.")
    elif 'MonitoringLocationIdentifier' not in results.columns:
        st.error("narrowresults.csv must contain a 'MonitoringLocationIdentifier' column.")
    else:
        # Contaminant selection
        contaminants = sorted(results['CharacteristicName'].dropna().unique())
        selected = st.selectbox("Select a Contaminant", contaminants)

        # Filter by contaminant
        df = results[results['CharacteristicName'] == selected]

        # Filter sliders
        date_min = df['ActivityStartDate'].min()
        date_max = df['ActivityStartDate'].max()
        value_min = float(df['ResultMeasureValue'].min())
        value_max = float(df['ResultMeasureValue'].max())

        col1, col2 = st.columns(2)
        with col1:
            date_range = st.slider("Date Range", min_value=date_min, max_value=date_max, value=(date_min, date_max))
        with col2:
            value_range = st.slider("Measurement Range", value=(value_min, value_max))

        # Apply filters
        df_filtered = df[
            (df['ActivityStartDate'] >= date_range[0]) &
            (df['ActivityStartDate'] <= date_range[1]) &
            (df['ResultMeasureValue'] >= value_range[0]) &
            (df['ResultMeasureValue'] <= value_range[1])
        ]

        # Merge with station info
        merged = pd.merge(df_filtered, stations, left_on='MonitoringLocationIdentifier', right_on='site_id', how='left')
        merged = merged.dropna(subset=['latitude', 'longitude'])

        # Map
        st.subheader("🗺️ Station Map with Selected Contaminant")
        map_center = [merged['latitude'].mean(), merged['longitude'].mean()] if not merged.empty else [0, 0]
        map_ = folium.Map(location=map_center, zoom_start=6)
        marker_cluster = MarkerCluster().add_to(map_)

        for _, row in merged.iterrows():
            popup_text = f"""
            <b>{row.get('site_name', 'Site')}</b><br>
            Value: {row['ResultMeasureValue']}<br>
            Date: {row['ActivityStartDate'].date()}
            """
            folium.Marker(
                location=[row['latitude'], row['longitude']],
                popup=popup_text,
                icon=folium.Icon(color='blue')
            ).add_to(marker_cluster)

        st_folium(map_, width=900, height=600)

        # Trend Plot
        st.subheader("📈 Contaminant Trend Over Time (Filtered Sites)")
        fig, ax = plt.subplots(figsize=(10, 5))
        for site, group in merged.groupby('MonitoringLocationIdentifier'):
            ax.plot(group['ActivityStartDate'], group['ResultMeasureValue'], label=site)

        ax.set_title(f"{selected} Levels Over Time")
        ax.set_xlabel("Date")
        ax.set_ylabel("Measurement")
        ax.legend(title="Site", bbox_to_anchor=(1.05, 1), loc='upper left')
        ax.grid(True)
        st.pyplot(fig)
