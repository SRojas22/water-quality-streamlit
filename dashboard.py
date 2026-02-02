import streamlit as st
import pandas as pd
import plotly.express as px
from api import apod_generator
import os
from dotenv import load_dotenv

load_dotenv()


st.set_page_config(page_title="Water Quality Dashboard", layout="wide")

st.title("Water Quality Dashboard")
st.header("Internship-Ready Software Development")
st.subheader("Susana Rojas")
st.divider()

st.markdown(
    """
**Overview:**  
This app explores Biscayne Bay water quality data using interactive visualizations.
Use the tabs below to examine the dataset, trends, and a live NASA API integration.
"""
)

# Load dataset
df = pd.read_csv("biscayneBay_waterquality.csv")

tab1, tab2, tab3, tab4 = st.tabs(
    ["Overview & Data", "2D Visualizations", "3D Visualization", "NASA APOD"]
)

# ---------------- TAB 1 ----------------
with tab1:
    st.subheader("Dataset Preview")
    st.write("Raw water quality measurements from Biscayne Bay.")
    st.dataframe(df, use_container_width=True)

    st.divider()
    st.subheader("Descriptive Statistics")
    st.write("Summary statistics for numeric variables.")
    st.dataframe(df.describe(), use_container_width=True)

# ---------------- TAB 2 ----------------
with tab2:
    st.subheader("2D Visualizations")
    st.write("Select a metric to view how it changes over time.")

    metric = st.selectbox(
        "Choose a metric to plot over time",
        ["Temperature (c)", "pH", "ODO mg/L"]
    )

    fig_time = px.line(
        df,
        x="Time",
        y=metric,
        title=f"{metric} Over Time",
        labels={"Time": "Time", metric: metric}
    )
    st.plotly_chart(fig_time, use_container_width=True)

    st.divider()
    st.write("Relationship between dissolved oxygen and temperature.")
    fig_scatter = px.scatter(
        df,
        x="ODO mg/L",
        y="Temperature (c)",
        color="pH",
        title="Dissolved Oxygen vs Temperature (Colored by pH)",
        labels={
            "ODO mg/L": "Dissolved Oxygen (mg/L)",
            "Temperature (c)": "Temperature (°C)",
            "pH": "pH"
        }
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

# ---------------- TAB 3 ----------------
with tab3:
    st.subheader("3D Visualization")
    st.write("Geographic distribution of water quality measurements.")

    fig3 = px.scatter_3d(
        df,
        x="Longitude",
        y="Latitude",
        z="Total Water Column (m)",
        color="pH",
        title="3D Water Quality View",
        labels={
            "Longitude": "Longitude",
            "Latitude": "Latitude",
            "Total Water Column (m)": "Water Column Depth (m)",
            "pH": "pH"
        }
    )
    fig3.update_scenes(zaxis_autorange="reversed")
    st.plotly_chart(fig3, use_container_width=True)

# ---------------- TAB 4 ----------------
with tab4:
    st.subheader("NASA Astronomy Picture of the Day")
    st.write("Live data fetched from NASA's public APOD API.")

    url = "https://api.nasa.gov/planetary/apod?api_key="
    nasa_key = os.getenv("NASA_API_KEY")
    try:
        nasa_key = st.secrets["NASA_API_KEY"]
    except Exception:
        pass

    if not nasa_key:
        st.warning("NASA API key not found. Add it in Streamlit Secrets.")
    else:
        try:
            response = apod_generator(url, nasa_key)

            if response.get("error"):
                st.error(response["error"].get("message", "API error"))
            else:
                st.markdown(f"### {response.get('title', 'NASA APOD')}")
                st.caption(response.get("date", ""))

                image_url = response.get("hdurl") or response.get("url")
                if image_url:
                    st.image(image_url, use_container_width=True)

                with st.expander("Explanation"):
                    st.write(response.get("explanation", ""))
        except Exception as e:
            st.error(f"API request failed: {e}")
