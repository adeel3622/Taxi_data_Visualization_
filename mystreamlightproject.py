import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
# Load the data
df = pd.read_csv("taxis.csv")

# Categorize the charts
chart_categories = {
    "All Charts": ["Visualization of Taxi's Data of USA of one Month"],
    "Pie Chart": ["Pie Chart of Passenger Counts", "Pie Chart of Average Total Bill and Tip","Pie chart of Total Average Bill and Their Tip","Pie chart of Payment Method Used by customer"],
    "Bar Chart": ["Passenger Comparison Graph", "Payment Method of Customers"],
    "Histogram": ["Histogram chart for Passengers comparison according to their taxi's", "Histogram of Distance Traveled by Taxis","Total Amount Paid by Year", "Total Amount Paid by Month","Total Amount Paid by Day","Histogram Of Distance Traveled By Taxi's","Histogram Chart That shows tha frequency of Taxi Separately","Histogram Chart in which we Compare Both Red and White Taxi By substituting Their Frequency"],
    "Box Plot": ["Box Plot of Fare by Taxi Color"]
}

# Sidebar - Chart selection
st.sidebar.title("Chart Selection")
# st.image("mytaxi.jpg",width=300)



chart_type = st.sidebar.selectbox("Select Chart Type", list(chart_categories.keys()))
def visualization():
    st.image("mytaxi.jpg",width=300)
    st.subheader("Histogram Charts of number of Taxi's")
    df=pd.read_csv("taxis.csv")
    df.sort_values(by="passengers",ascending=False)
    df.sort_values(by="passengers",ascending=False)
    show=df.passengers.value_counts()
    labels=show.index
    grpy=df.groupby("passengers")["color"].sum().value_counts()
    fig=go.Figure(data=[go.Histogram(x=df.color,marker_color=["yellow","green"])])
    fig.update_layout(title_text="<b>Taxi's Color</b>",
    title_x=0.5,title_font=dict(size=20, color="Black", family="Arial")
    ,xaxis_title="Taxi's Color", yaxis_title="Number of Taxi",bargap=0.5)
    st.plotly_chart(fig)


    st.header("Pie Chart")
    st.subheader("Pie Chart of Passenger Counts")
    count = df["passengers"].value_counts()
    labels = count.index
    values = count.values
    fig_pie_passenger = go.Figure(data=[go.Pie(labels=labels, values=values)])
    st.plotly_chart(fig_pie_passenger)

    st.header("Bar Chart")
    st.subheader("Passenger Comparison Graph")
    passenger_count = df["passengers"].value_counts()
    fig_bar_passenger = px.bar(passenger_count, x=passenger_count.index, y=passenger_count.values, labels={'x': 'Number of Passengers', 'y': 'Passengers Travel'}, title='Passenger Comparison Graph')
    st.plotly_chart(fig_bar_passenger)

    st.subheader("Payment Method of Customers")
    payment_counts = df["payment"].value_counts()
    fig_bar_payment = go.Figure(data=[go.Bar(x=payment_counts.index, y=payment_counts.values)])
    fig_bar_payment.update_layout(title_text="Payment Method of Customers")
    st.plotly_chart(fig_bar_payment)

    
    st.header("Histogram")
    st.subheader("Histogram chart for Total amount paid by Year Day and Month")


# Read the data from the CSV file
    df = pd.read_csv("taxis.csv")

# Convert the 'pickup' column to datetime format
    df['pickup'] = pd.to_datetime(df['pickup'])

# Extract year, month, and day from the 'pickup' column
    df['year'] = df['pickup'].dt.year
    df['month'] = df['pickup'].dt.month
    df['day'] = df['pickup'].dt.day

# Group the data by year, month, and day and calculate the total amount paid
    total_by_year = df.groupby('year')['total'].sum()
    total_by_month = df.groupby(['year', 'month'])['total'].sum()
    total_by_day = df.groupby(['year', 'month', 'day'])['total'].sum()
# Create Plotly figures for total amount paid by year, month, and day
    fig_year = px.bar(total_by_year, x=total_by_year.index, y=total_by_year.values, labels={'x': 'Year', 'y': 'Total Amount Paid'}, title='Total Amount Paid by Year')
    fig_month = px.bar(total_by_month, x=total_by_month.index.get_level_values('month'), y=total_by_month.values, labels={'x': 'Month', 'y': 'Total Amount Paid'}, title='Total Amount Paid by Month')
    fig_day = px.bar(total_by_day, x=total_by_day.index.get_level_values('day'), y=total_by_day.values, labels={'x': 'Day', 'y': 'Total Amount Paid'}, title='Total Amount Paid by Day')
    fig_year.update_layout(title_x=0.5)
    fig_month.update_layout(title_x=0.5)
    fig_day.update_layout(title_x=0.5)
    fig_year.update_traces(marker_color='red')
    fig_month.update_traces(marker_color='green')
    fig_day.update_traces(marker_color='blue')
    st.plotly_chart(fig_year)
    st.plotly_chart(fig_month)
    st.plotly_chart(fig_day)
    st.subheader("Histogram of Distance Traveled by Taxis")
    fig_hist_distance = px.histogram(df, x="distance", title="Histogram of Distance Traveled by Taxis")
    st.plotly_chart(fig_hist_distance)

    st.subheader("Histogram Chart that shows the frequency of taxi used by customer separately")
    df = pd.read_csv("taxis.csv")

# Group the data by color and passengers, then count occurrences
    passenger_by_taxi = df.groupby("color")["passengers"].value_counts().reset_index(name="passenger_count")

# Convert the grouped data into a DataFrame
    df1 = pd.DataFrame(passenger_by_taxi)
    plt.figure(figsize=(12, 6))  # Set the overall figure size

# Subplot 1: Histogram of 'passengers' for 'green' taxis
    plt.subplot(1, 2, 1)  # 1 row, 2 columns, subplot index 1
    plt.hist(df[df['color'] == 'green']['passengers'], color='green', bins=5)
    plt.title('Green Taxis')
    plt.xlabel('Passengers')
    plt.ylabel('Frequency')

# Subplot 2: Histogram of 'passengers' for 'yellow' taxis
    plt.subplot(1, 2, 2)  # 1 row, 2 columns, subplot index 2
    plt.hist(df[df['color'] == 'yellow']['passengers'], color='yellow', bins=5)
    plt.title('Yellow Taxis')
    plt.xlabel('Passengers')
    plt.ylabel('Frequency')

    plt.tight_layout()  # Adjust layout to prevent overlap
    plt.suptitle("Histogram chart for Passengers comparison according to their taxi's")
    plt.subplots_adjust(top=0.9)
    st.pyplot(plt)

    st.subheader("Histogram Chart In Which we Compare Both red and white taxi by substituting")
# Read the data from the CSV file
    df = pd.read_csv("taxis.csv")

# Group the data by color and passengers, then count occurrences
    passenger_by_taxi = df.groupby("color")["passengers"].value_counts().reset_index(name="passenger_count")

# Create a figure
    fig = go.Figure()

# Add trace for 'green' taxis
    fig.add_trace(go.Histogram(x=df[df['color'] == 'green']['passengers'], 
                                name='Green Taxis',
                                marker=dict(color='green'),
                                opacity=0.75))

# Add trace for 'yellow' taxis
    fig.add_trace(go.Histogram(x=df[df['color'] == 'yellow']['passengers'], 
                                name='Yellow Taxis',
                                marker=dict(color='yellow'),
                                opacity=0.70))

# Update layout
    fig.update_layout(
        title='Passengers According to their taxi and we subtitute both taxi',
        xaxis=dict(title='Passengers'),
        yaxis=dict(title='Frequency'),
        barmode='overlay',  # Overlay the histograms
        bargap=0.1,  # Set gap between bars
        bargroupgap=0.05,  # Set gap between groups of bars
        showlegend=True,  # Show legend
        title_x=0.1,
        title_y=0.9
    )

# Show the plot
    st.plotly_chart(fig)

    st.subheader("Pie chart of Average Total Bill and their tip")
    df=pd.read_csv("taxis.csv")
    average_tip=np.array(df.tip.mean())
    average_total=np.array(df.total.mean())
    average_tip_str = str(average_tip)
    average_total_str = str(average_total)
    label= ["Average Tip Price: $" + average_tip_str, "Average Total Price: $" + average_total_str]
    values=[average_tip,average_total]
    color=["green","blue"]
    fig=go.Figure(data=[go.Pie(labels=label, values=values,marker_colors=color)])
    fig.update_layout(
        title="Pie Chart of Average Total Bill and their Tip",
        title_x=0.5,

    )
    fig.update_traces(hoverinfo='label+value',textinfo="percent",textfont_size=30,marker=dict(colors=["green","yellow"],line=dict(color="black",width=3)))
    st.plotly_chart(fig)

    st.header("Box Plot")
    st.subheader("Box Plot of Fare by Taxi Color")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x=df["color"], y=df["fare"], data=df)
    st.pyplot(fig)

    payment_counts = df["payment"].value_counts()

# Create a Pie chart
    fig = go.Figure(data=[go.Pie(labels=payment_counts.index, values=payment_counts)])
    fig.update_layout(
        title   =  {
            'text': "Payment Method of Custmor",
            'x': 0.3,  # Set x-coordinate to center
            'y': 0.9   # Set y-coordinate to center
        }
    )
    colors=["red","blue"]
    fig.update_traces(hoverinfo='label+value',textinfo="percent",textfont_size=30,marker=dict(colors=colors,line=dict(color="black",width=3)))
    st.plotly_chart(fig)


    
    
st.title("Taxi Data Visualization")

# Main content
if chart_type == "All Charts":
    st.write("**For This project We Collect a One Month Taxi Data OF USA and Then I make project By comparing Taxi color their Fare and Distance Traveled.**")
    visualization()

elif chart_type == "Pie Chart":
    st.header("Pie Chart")
    st.subheader("Pie Chart of Passenger Counts")
    st.markdown("In this Chart we shows that How many customer use taxi at a time i mean the customers that Book a taxi at a time are shown in Following below Chart")
    count = df["passengers"].value_counts()
    labels = count.index
    values = count.values
    fig_pie_passenger = go.Figure(data=[go.Pie(labels=labels, values=values)])
    st.plotly_chart(fig_pie_passenger)

    st.subheader("Pie Charts of number of Taxi's")
    df = pd.read_csv("taxis.csv")

    # Sort DataFrame by "passengers" column in descending order
    df = df.sort_values(by="passengers", ascending=False)

    # Value counts of passengers
    show = df["passengers"].value_counts()
    labels = show.index
    colors=["yellow","green"]
    # Creating the pie chart
    fig = go.Figure(data=[go.Pie(labels=["yellow Taxi", "Green Taxi"], values=show,marker=dict(colors=colors))])

    # Updating layout
    fig.update_layout(
        title_text="<b>Taxi's Color</b>",
        title_x=0.5,
        title_font=dict(size=20, color="Black", family="Arial"),
        xaxis_title="Taxi's Color",
        yaxis_title="Number of Taxi",
        bargap=0.5
    )

    # Displaying the pie chart
    st.plotly_chart(fig)


    st.subheader("Pie chart of Average Total Bill and their tip")
    st.markdown("This chart shows the total average bill and their tip of customers")
    df=pd.read_csv("taxis.csv")
    average_tip=np.array(df.tip.mean())
    average_total=np.array(df.total.mean())
    average_tip_str = str(average_tip)
    average_total_str = str(average_total)
    label= ["Average Tip Price: $" + average_tip_str, "Average Total Price: $" + average_total_str]
    values=[average_tip,average_total]
    color=["green","blue"]
    fig=go.Figure(data=[go.Pie(labels=label, values=values,marker_colors=color)])
    fig.update_layout(
        title="Pie Chart of Average Total Bill and their Tip",
        title_x=0.5,

    )
    fig.update_traces(hoverinfo='label+value',textinfo="percent",textfont_size=30,marker=dict(colors=["green","yellow"],line=dict(color="black",width=3)))
    st.plotly_chart(fig)

    st.subheader("Pie chart of Payment Method of Customer")
# Read the data from the CSV file
    df = pd.read_csv("taxis.csv")
    
# Perform value counts on the 'payment' column
    st.write("This pie charts which method is most used by the customer for payment Red color show the credit card and blue color shows the Cash")
    payment_counts = df["payment"].value_counts()

# Create a Pie chart
    fig = go.Figure(data=[go.Pie(labels=payment_counts.index, values=payment_counts)])
    fig.update_layout(
        title   =  {
            'text': "Payment Method of Custmor",
            'x': 0.3,  # Set x-coordinate to center
            'y': 0.9   # Set y-coordinate to center
        }
    )
    colors=["red","blue"]
    fig.update_traces(hoverinfo='label+value',textinfo="percent",textfont_size=30,marker=dict(colors=colors,line=dict(color="black",width=3)))
    st.plotly_chart(fig)


elif chart_type == "Bar Chart":
    st.header("Bar Chart")
    st.subheader("Passenger Comparison Graph")
    st.markdown("This chart shows the frequency of customers at a time.It shows that how many numbers of customers travel at same time.")
    passenger_count = df["passengers"].value_counts()
    fig_bar_passenger = px.bar(passenger_count, x=passenger_count.index, y=passenger_count.values, labels={'x': 'Number of Passengers', 'y': 'Passengers Travel'}, title='Passenger Comparison Graph')
    st.plotly_chart(fig_bar_passenger)

    st.subheader("Payment Method of Customers")
    st.markdown("This chart shows the Method of payment that customer mostly used. Red color Shows Credit Card and Blue Color shows Cash")
    payment_counts = df["payment"].value_counts()
    fig_bar_payment = go.Figure(data=[go.Bar(x=payment_counts.index, y=payment_counts.values)])
    fig_bar_payment.update_traces(marker_color=['Blue','Green'])
    fig_bar_payment.update_layout(title_text="Payment Method of Customers")
    st.plotly_chart(fig_bar_payment)

    


elif chart_type == "Histogram":
    st.header("Histogram")
    st.subheader("Histogram chart for Passengers comparison according to their taxi's")
    st.markdown("This Chart shows that How much Money Company Gets from Taxi in Year in a Month and in a Day")


# Read the data from the CSV file
    df = pd.read_csv("taxis.csv")

# Convert the 'pickup' column to datetime format
    df['pickup'] = pd.to_datetime(df['pickup'])

# Extract year, month, and day from the 'pickup' column
    df['year'] = df['pickup'].dt.year
    df['month'] = df['pickup'].dt.month
    df['day'] = df['pickup'].dt.day

# Group the data by year, month, and day and calculate the total amount paid
    total_by_year = df.groupby('year')['total'].sum()
    total_by_month = df.groupby(['year', 'month'])['total'].sum()
    total_by_day = df.groupby(['year', 'month', 'day'])['total'].sum()
# Create Plotly figures for total amount paid by year, month, and day
    fig_year = px.bar(total_by_year, x=total_by_year.index, y=total_by_year.values, labels={'x': 'Year', 'y': 'Total Amount Paid'}, title='Total Amount Paid by Year')
    fig_month = px.bar(total_by_month, x=total_by_month.index.get_level_values('month'), y=total_by_month.values, labels={'x': 'Month', 'y': 'Total Amount Paid'}, title='Total Amount Paid by Month')
    fig_day = px.bar(total_by_day, x=total_by_day.index.get_level_values('day'), y=total_by_day.values, labels={'x': 'Day', 'y': 'Total Amount Paid'}, title='Total Amount Paid by Day')
    fig_year.update_layout(title_x=0.5)
    fig_month.update_layout(title_x=0.5)
    fig_day.update_layout(title_x=0.5)
    fig_year.update_traces(marker_color='red')
    fig_month.update_traces(marker_color='green')
    fig_day.update_traces(marker_color='blue')
    st.plotly_chart(fig_year)
    st.plotly_chart(fig_month)
    st.plotly_chart(fig_day)
    st.subheader("Histogram of Distance Traveled by Taxis")
    fig_hist_distance = px.histogram(df, x="distance", title="Histogram of Distance Traveled by Taxis")
    st.plotly_chart(fig_hist_distance)
    

# Read the data from the CSV file
    st.subheader("Histogram Chart that shows the frequency of taxi used by customer separately")
    st.markdown("This chart explain the frequency of Customers That Travel at a same time")
    df = pd.read_csv("taxis.csv")

# Group the data by color and passengers, then count occurrences
    passenger_by_taxi = df.groupby("color")["passengers"].value_counts().reset_index(name="passenger_count")

# Convert the grouped data into a DataFrame
    df1 = pd.DataFrame(passenger_by_taxi)
    plt.figure(figsize=(12, 6))  # Set the overall figure size

# Subplot 1: Histogram of 'passengers' for 'green' taxis
    plt.subplot(1, 2, 1)  # 1 row, 2 columns, subplot index 1
    plt.hist(df[df['color'] == 'green']['passengers'], color='green', bins=5)
    plt.title('Green Taxis')
    plt.xlabel('Passengers')
    plt.ylabel('Frequency')

# Subplot 2: Histogram of 'passengers' for 'yellow' taxis
    plt.subplot(1, 2, 2)  # 1 row, 2 columns, subplot index 2
    plt.hist(df[df['color'] == 'yellow']['passengers'], color='yellow', bins=5)
    plt.title('Yellow Taxis')
    plt.xlabel('Passengers')
    plt.ylabel('Frequency')

    plt.tight_layout()  # Adjust layout to prevent overlap
    plt.suptitle("Histogram chart for Passengers comparison according to their taxi's")
    plt.subplots_adjust(top=0.9)
    st.pyplot(plt)
  
    st.subheader("Histogram Chart In Which we Compare Both red and white taxi by substituting")
    st.markdown("This chart define the differnces Between Yellow and Green Taxi By Substituting Both Tax's")
# Read the data from the CSV file
    df = pd.read_csv("taxis.csv")

# Group the data by color and passengers, then count occurrences
    passenger_by_taxi = df.groupby("color")["passengers"].value_counts().reset_index(name="passenger_count")

# Create a figure
    fig = go.Figure()

# Add trace for 'green' taxis
    fig.add_trace(go.Histogram(x=df[df['color'] == 'green']['passengers'], 
                                name='Green Taxis',
                                marker=dict(color='green'),
                                opacity=0.75))

# Add trace for 'yellow' taxis
    fig.add_trace(go.Histogram(x=df[df['color'] == 'yellow']['passengers'], 
                                name='Yellow Taxis',
                                marker=dict(color='yellow'),
                                opacity=0.70))

# Update layout
    fig.update_layout(
        title='Passengers According to their taxi and we subtitute both taxi',
        xaxis=dict(title='Passengers'),
        yaxis=dict(title='Frequency'),
        barmode='overlay',  # Overlay the histograms
        bargap=0.1,  # Set gap between bars
        bargroupgap=0.05,  # Set gap between groups of bars
        showlegend=True,  # Show legend
        title_x=0.1,
        title_y=0.9
    )

# Show the plot
    st.plotly_chart(fig)


# Create subplots of histograms




    

elif chart_type == "Box Plot":
    st.header("Box Plot")
    st.subheader("Box Plot of Fare by Taxi Color")
    st.markdown("This chart shows that how many average fare that yellow and green taxi gets")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x=df["color"], y=df["fare"], data=df)
    st.pyplot(fig)
    pass


# Footer
st.sidebar.title("Chart Categories")
for category, charts in chart_categories.items():
    st.sidebar.subheader(category)
    for chart in charts:
        st.sidebar.write("- " + chart)

