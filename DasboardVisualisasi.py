import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide")
st.title("Dashboard Kecanduan Media Sosial Mahasiswa")

# Upload file
uploaded_file = st.file_uploader("Unggah file Excel", type=["xlsx"])
if uploaded_file:
    xls = pd.ExcelFile(uploaded_file)
    df = xls.parse('dataset')

    tab1, tab2, tab3 = st.tabs(["Rata-rata Penggunaan", "Korelasi", "Platform Adiktif"])

    with tab1:
    st.header("Rata-rata Jam Penggunaan Media Sosial Harian")
    fig = px.bar(
        df,
        x="Academic_Level",
        y="Avg_Daily_Usage_Hours",
        color="Gender",
        barmode="group",
        hover_data=["Avg_Daily_Usage_Hours", "Gender", "Academic_Level"]
    )
    fig.update_layout(
        title="Penggunaan Harian berdasarkan Gender & Pendidikan",
        yaxis_title="Jam / Hari",
        xaxis_title="Academic_Level"
    )
    st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.header("Korelasi Media Sosial, Tidur, dan Kesehatan Mental")
        corr_data = df[["Avg_Daily_Usage_Hours", "Sleep_Hours_Per_Night", "Mental_Health_Score"]].corr()
        fig, ax = plt.subplots()
        sns.heatmap(corr_data, annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

    with tab3:
        st.header("Platform Media Sosial Paling Menyita Waktu")
        platform_avg = df.groupby("Most_Used_Platform")["Avg_Daily_Usage_Hours"].mean().sort_values(ascending=False)
        fig, ax = plt.subplots()
        sns.barplot(x=platform_avg.index, y=platform_avg.values, ax=ax)
        ax.set_ylabel("Rata-rata Jam / Hari")
        ax.set_title("Platform Paling Menyita Waktu")
        plt.xticks(rotation=25)
        st.pyplot(fig)
