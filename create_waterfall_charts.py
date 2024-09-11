import pandas as pd
import plotly.graph_objects as go

#Load the streaming data from csv file
data = pd.read_csv('My Streaming Activity.csv')

#Group the data by song and count the number of times each song was streamed
song_stream_count = data.groupby('Song').size().sort_values(ascending=False)

#Get the top ten 10 and bottom 10 streamed songs
top_10_songs = song_stream_count.head(10)
bottom_10_songs = song_stream_count.tail(10)

#Create Waterfall chart for top 10 streamed songs
fig_top = go.Figure(go.Waterfall(
	name="Top Streamed Songs",
	orientation="v",
	measure=["relative"] * len(top_10_songs),
	x=top_10_songs.index,
	y=top_10_songs.values,
	decreasing={"marker": {"color": "lightgreen"}},
	increasing={"marker": {"color": "lightblue"}},
	totals={"marker": {"color": "darkblue"}}
))

#Custimize laytut for Top 10 Chart
fig_top.update_layout(
	title="Top 10 Streamed Songs - Waterfall Chart",
	xaxis_title="Song Name",
	yaxis_title="Stream Count",
	waterfallgap=0.3
)

#create Waterfall Chart for Bottom 10 Streamed Songs
fig_bottom = go.Figure(go.Waterfall(
	name="Bottom Streamed Songs",
	orientation="v",
	measure=["relative"] * len(bottom_10_songs),
	x=bottom_10_songs.index,
	y=bottom_10_songs.values,
	decreasing={"marker": {"color": "lightcoral"}},
	increasing={"marker": {"color": "lightpink"}},
	totals={"marker": {"color": "darkred"}}
))

#Custimize latout for Bottom 10 Chart
fig_bottom.update_layout(
	title="Bottom 10 Streamed Songs - Waterfall Chart",
	xaxis_title="Song Name",
	yaxis_title="Stream Count",
	waterfallgap=0.3
)

#Save the charts as html files
fig_top.write_html("Top_Streamed_Songs_Waterfall.html")
fig_bottom.write_html("Bottom_Streamed_Songs_Waterfall.html")

print("Waterfall charts have been created and saved as a html file.")

# Load the streaming data from CSV file
data = pd.read_csv('My Streaming Activity.csv')

# Group the data by song and count the number of times each song was streamed
song_stream_count = data.groupby('Song').size().sort_values(ascending=False)

# Get the top 10 and bottom 10 streamed songs
top_10_songs = song_stream_count.head(10)
bottom_10_songs = song_stream_count.tail(10)

# Create Waterfall chart for Top 10 Streamed Songs
fig_top = go.Figure(go.Waterfall(
        name="Top Streamed Songs",
        orientation="v",
        measure=["relative"] * len(top_10_songs),  # Corrected "realative" and "top_10songs"
        x=top_10_songs.index,
        y=top_10_songs.values,
        decreasing={"marker": {"color": "lightgreen"}},
        increasing={"marker": {"color": "lightblue"}},
        totals={"marker": {"color": "darkblue"}}
))

# Customize layout for Top 10 Chart
fig_top.update_layout(
        title="Top 10 Streamed Songs - Waterfall Chart",
        xaxis_title="Song Name",
        yaxis_title="Stream Count",
        waterfallgap=0.3
)

# Create Waterfall Chart for Bottom 10 Streamed Songs
fig_bottom = go.Figure(go.Waterfall(
        name="Bottom Streamed Songs",
        orientation="v",
        measure=["relative"] * len(bottom_10_songs),  # Corrected "realative"
        x=bottom_10_songs.index,
        y=bottom_10_songs.values,
        decreasing={"marker": {"color": "lightcoral"}},
        increasing={"marker": {"color": "lightpink"}},
        totals={"marker": {"color": "darkred"}}
))

# Customize layout for Bottom 10 Chart 
fig_bottom.update_layout(
        title="Bottom 10 Streamed Songs - Waterfall Chart",
        xaxis_title="Song Name",
        yaxis_title="Stream Count",
        waterfallgap=0.3
)

# Save the charts as HTML files
fig_top.write_html("Top_Streamed_Songs_Waterfall.html")  # Added closing quote
fig_bottom.write_html("Bottom_Streamed_Songs_Waterfall.html")  # Corrected "Botom" typo

print("Waterfall charts have been created and saved as HTML files.")
