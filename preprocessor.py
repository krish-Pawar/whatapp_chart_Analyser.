import re
import pandas as pd



def preprocess(chats):
    data = []
    # pattern = r"(/\d{1,2}\/\d{1,2}\/\d{1,2}\,\s\d{1,2}\:\d{1,2})\s-\s([^:]+):\s(.*)"
    pattern=r"^(\d{1,2}\/\d{1,2}\/\d{2},\s\d{1,2}:\d{2}\s?[AP]M)\s-\s([^:]+):\s(.+)$"

    for line in chats.split("\n"):
        line = line.strip()
        match = re.match(pattern, line)

        if match:
            datetime = match.group(1)

            user = match.group(2)
            message = match.group(3)

            data.append([datetime, user, message])


    # create dataframe
    df = pd.DataFrame(data, columns=["datetime","user", "message"])


    # converting   datetime in the  datetime object


    df['date'] = pd.to_datetime(df['datetime'], format="%m/%d/%y, %I:%M %p")


    # making  more columns with dates
    df['only_time'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['months_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day']=df['date'].dt.day
    df['day_name']=df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute
    df.drop('date', axis=1, inplace=True)


    return df