import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium
import matplotlib.pyplot as plt
import datetime

st.set_page_config(layout="wide")
st.title("💧 Water Quality Contaminant Explorer")

# 🔁 Load station and results files directly
try:
    stations = pd.read_csv("station.csv")
    results = pd.read_csv("narrowresult.csv")
except FileNotFoundError:
    st.error("❌ Make sure 'station.csv' and 'narrowresult.csv' are in the same folder as this app.")
    st.stop()

# ✅ Convert columns to proper types
results['ActivityStartDate'] = pd.to_datetime(results['ActivityStartDate'], errors='coerce')

# ✅ Check required columns
if 'MonitoringLocationIdentifier' not in stations.columns or 'MonitoringLocationIdentifier' not in results.columns:
    st.error("⚠️ Required column 'MonitoringLocationIdentifier' is missing from one of the files.")
    st.write("Station columns:", stations.columns.tolist())
    st.write("Result columns:", results.columns.tolist())
    st.stop()

# 🧪 Contaminant selection
contaminants = sorted(results['CharacteristicName'].dropna().unique())
selected = st.selectbox("Select a Contaminant", contaminants)

# ✅ Filter results for selected contaminant
df = results[results['CharacteristicName'] == selected].copy()

# ✅ Convert measurement to numeric
df['ResultMeasureValue'] = pd.to_numeric(df['ResultMeasureValue'], errors='coerce')
df = df.dropna(subset=['ResultMeasureValue', 'ActivityStartDate'])

# 📅 Date and value range
date_min = df['ActivityStartDate'].min()
date_max = df['ActivityStartDate'].max()
value_min = float(df['ResultMeasureValue'].min())
value_max = float(df['ResultMeasureValue'].max())

# ✅ Convert dates to `datetime.date` for Streamlit sliders
date_min_date = date_min.date()
date_max_date = date_max.date()

col1, col2 = st.columns(2)
with col1:
    date_range = st.slider(
        "Date Range",
        min_value=date_min_date,
        max_value=date_max_date,
        value=(date_min_date, date_max_date)
    )
with col2:
    value_range = st.slider(
        "Measurement Range",
        value=(value_min, value_max)
    )

# ✅ Filter based on date and value range
df_filtered = df[
    (df['ActivityStartDate'].dt.date >= date_range[0]) &
    (df['ActivityStartDate'].dt.date <= date_range[1]) &
    (df['ResultMeasureValue'] >= value_range[0]) &
    (df['ResultMeasureValue'] <= value_range[1])
]

# ✅ Merge with station info
merged = pd.merge(df_filtered, stations, on='MonitoringLocationIdentifier', how='left')
merged = merged.dropna(subset=['LatitudeMeasure', 'LongitudeMeasure'])

# 🗺️ Display map
st.subheader("🗺️ Station Map with Selected Contaminant")
if not merged.empty:
    map_center = [merged['LatitudeMeasure'].mean(), merged['LongitudeMeasure'].mean()]
else:
    map_center = [0, 0]

map_ = folium.Map(location=map_center, zoom_start=6)
marker_cluster = MarkerCluster().add_to(map_)

for _, row in merged.iterrows():
    popup_text = f"""
    <b>{row.get('MonitoringLocationName', 'Site')}</b><br>
    Value: {row['ResultMeasureValue']}<br>
    Date: {row['ActivityStartDate'].date()}
    """
    folium.Marker(
        location=[row['LatitudeMeasure'], row['LongitudeMeasure']],
        popup=popup_text,
        icon=folium.Icon(color='blue')
    ).add_to(marker_cluster)

st_folium(map_, width=900, height=600)

# 📈 Plot time trend
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
