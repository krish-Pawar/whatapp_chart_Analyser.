from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import  emoji


extract = URLExtract()


def fetch_stats(selected_user,df):


    if selected_user!='overall':
        df = df[df['user'] == selected_user]
        # fetching number of messages
    num_messages=df.shape[0]
    #      2.fetching no fo words
    words = []
    for message in df['message']:
        words.extend(message.split())
#   FETCHING NUMBER OF MEDIA MESSAGES
    num_media_message=df[df['message']=='<media omitted>\n'].shape[0]

    #  fetching the number of link shared
    links=[]
    for message in df['message']:
        links.extend(extract.find_urls(message))

    return num_messages, len(words),num_media_message,len(links)



def busy_user(df):
      x=df['user'].value_counts().head()
      df= round(df['user'].value_counts()/df.shape[0]*100,2).reset_index().rename(columns={'index':'name','user':'precent'})
      return x,df

def create_world_cloud(selected_user,df):



    f = open('stop_hinglish.txt', 'r')
    stopwords = f.read()

    if selected_user!='overall':
        df = df[df['user'] == selected_user]


    temp=df[df['user']!= 'group_notification']
    temp=temp[temp['message']!='<media omitted>\n']

    def  remove_stopwords(message):
        y=[]
        for word in message.lower().split():
            if  word not in stopwords:
                y.append(word)

        return ' '.join(y)

    wc=WordCloud(width=800, height=400,min_font_size=10,max_font_size=80,background_color='white')
    temp['message']=temp['message'].apply(remove_stopwords)
    df_wc=wc.generate(temp['message'].str.cat(sep=" "))
    return df_wc



def most_common_words(selected_user,df):
    f = open('stop_hinglish.txt', 'r')
    stopwords = f.read()

    if selected_user != 'overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<media omitted>\n']


    words=[]

    for message in temp['message']:
        for word in message.lower().split(' '):
            if word not in  stopwords:
                words.append(word)


    most_common_df = pd.DataFrame(Counter(words).most_common(20))
    return most_common_df


def emoji_helper(selected_user,df):


    if selected_user != 'overall':
        df = df[df['user'] == selected_user]

    emojis=[]
    for message in df['message']:
        emojis.extend([c for c in message if c in emoji.EMOJI_DATA])

    emoji_df=pd.DataFrame(
        Counter(emojis).most_common(len(Counter(emojis))),
        columns=['emoji','count'])

    return emoji_df


def monthly_timeline(selected_user, df):

    if selected_user != 'overall':
        df = df[df['user'] == selected_user]

    timeline = (
        df.groupby(['year', 'month'])['message']
        .count()
        .reset_index()
    )

    timeline['time'] = (
        timeline['month'] + '-' + timeline['year'].astype(str)
    )

    return timeline

def daily_timeline(selected_user, df):
    if selected_user != 'overall':
        df = df[df['user'] == selected_user]

    daily_timelines = (
        df.groupby('only_time')['message'].count().reset_index()
    )

    return daily_timelines


def week_activity_map(selected_user, df):
    if selected_user != 'overall':
        df = df[df['user'] == selected_user]
    return df['day_name'].value_counts()

def montly_activity_map(selected_user, df):
    if selected_user != 'overall':
        df = df[df['user'] == selected_user]
    return df['month'].value_counts()