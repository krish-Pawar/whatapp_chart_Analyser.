import matplotlib.pyplot as plt
import streamlit as st

import helper
import preprocessor

st.title("Chat Analyser")
st.sidebar.title("Whatapp Chat Analyser")
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:

    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    chats=bytes_data.decode('utf-8')
    # st.write(chats)

    df=preprocessor.preprocess(chats)



#    fetching the no fo users
    user_list=df['user'].unique().tolist()
    user_list.sort()
    user_list.insert(0,'overall')

    selected_user=st.sidebar.selectbox("User List",user_list)
    if st.sidebar.button("Analyse"):

        num_messages,words,num_media_messages,num_links=helper.fetch_stats(selected_user,df)

        st.title('Top Statistics')

        col1, col2,  col3, col4=st.columns(4)

        with col1:
            st.header('Total Messages')
            st.title(num_messages)
        with col2:
            st.header('Total Words')
            st.title(words)
        with col3:
            st.header('media shared')
            st.title(num_media_messages)
        with col4:
            st.header('Links   ')
            st.title(num_links)

#        monthly Timeline
        st.title("Monthly Timeline")
        timeline=helper.monthly_timeline(selected_user,df)
        fig,ax=plt.subplots()
        ax.plot(timeline['time'],timeline['message'],color='green')
        plt.xticks(rotation=90)
        st.pyplot(fig)

#         daily timeline
        st.title("Daily  Timeline")
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_time'], daily_timeline['message'], color='red')
        plt.xticks(rotation=90)
        st.pyplot(fig)


        # activity map
        st.title('activity map')
        col1, col2, =st.columns(2)

        with col1:
            st.header('Most busy day')
            busyday=helper.week_activity_map(selected_user, df)
            fig,ax=plt.subplots()
            ax.bar(busyday.index,busyday.values,color='green')
            plt.xticks(rotation=90)
            st.pyplot(fig)

        with col2:
            st.header('Most busy month')
            busymonth = helper.montly_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busymonth.index, busymonth.values, color='navy')
            plt.xticks(rotation=90)
            st.pyplot(fig)








#         finding the busiest user in the group(group level)
        if selected_user=='overall':

            st.title('most busy users')
            x,new_df=helper.busy_user(df)
            fig,ax=plt.subplots()

            col1,col2=st.columns(2)


            with col1:
               ax.bar(x.index,x.values)
               plt.xticks(rotation=90)
               st.pyplot(fig)

            with col2:
                st.dataframe(new_df)
#       wordcloud
        df_wc=helper.create_world_cloud(selected_user, df)
        fig,ax=plt.subplots()
        ax.imshow(df_wc)
        st.title('Word cloud visualization')
        st.pyplot(fig)

#       MOST COMMON WORDS
        most_common_df=helper.most_common_words(selected_user, df)

        fig,ax=plt.subplots()
        ax.barh(most_common_df[0],most_common_df[1])
        plt.xticks(rotation=90)
        st.title('most common words')
        st.pyplot(fig)



#      emoji analysis
        emoji_df=helper.emoji_helper(selected_user, df)

        st.title('Emoji Analysis')

        col1,col2=st.columns(2)

        with col1:
            st.dataframe(emoji_df)
        with col2:
            fig,ax=plt.subplots()
            ax.pie(emoji_df['count'].head(),labels=emoji_df['emoji'].head(),autopct='%1.0f%%')
            st.pyplot(fig)