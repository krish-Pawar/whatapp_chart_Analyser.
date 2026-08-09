# 📊 WhatsApp Chat Analyser

> Turn your WhatsApp conversations into simple and meaningful insights.

**WhatsApp Chat Analyser** is a Python-based data analysis project that takes an exported WhatsApp chat and converts it into useful statistics and visualisations.

Instead of manually scrolling through thousands of messages, this tool helps you quickly understand **who is most active, when the chat is most active, which words and emojis are used most, and how the conversation changes over time.**

---

## 🎯 Problem It Solves

A WhatsApp conversation contains a lot of data, but it is difficult to understand the patterns just by reading messages.

This project converts raw chat messages into visual insights.

For example, you can find:

* 👤 Who sent the most messages?
* 💬 How many messages and words were sent?
* 📅 Which days are the busiest?
* 📈 How does chat activity change over time?
* 🔤 Which words are used most often?
* 😀 Which emojis are used the most?
* 🔗 How many links were shared?
* 📱 How many media messages were shared?

---

## ✨ Features

### 📊 Chat Statistics

* Total messages
* Total words
* Media messages
* Shared links

### 👥 User Analysis

* Analyse the complete conversation
* Analyse an individual user
* Find the most active users
* Compare user activity

### 📈 Activity Analysis

* Monthly chat timeline
* Daily chat timeline
* Most active days of the week
* Most active months

### ☁️ Text Analysis

* Word cloud
* Most common words
* Stop-word filtering for cleaner results

### 😀 Emoji Analysis

* Count emojis used in the chat
* Find the most frequently used emojis
* Visualise emoji usage

---

## 🛠️ Technologies Used

| Technology     | Purpose                                  |
| -------------- | ---------------------------------------- |
| **Python**     | Core programming and data processing     |
| **Streamlit**  | Building the interactive web application |
| **Pandas**     | Data cleaning and analysis               |
| **Matplotlib** | Creating charts and visualisations       |
| **WordCloud**  | Generating word cloud                    |
| **Emoji**      | Detecting and analysing emojis           |
| **URLExtract** | Extracting links from messages           |
| **Regex**      | Parsing WhatsApp chat messages           |

---

## 🔄 How It Works

```text
WhatsApp Chat Export
        ↓
    Upload .txt file
        ↓
   Parse Chat Data
        ↓
  Pandas DataFrame
        ↓
   Data Analysis
        ↓
 Charts & Visualisations
        ↓
     Insights
```

The application first reads the exported WhatsApp chat, extracts the **date, time, user and message**, and converts the data into a structured Pandas DataFrame.

After that, different analysis functions calculate statistics and generate visualisations.

---

## 🚀 Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/krish-Pawar/whatapp_chart_Analyser..git
```

### 2. Open the project

```bash
cd whatapp_chart_Analyser.
```

### 3. Install the required libraries

```bash
pip install streamlit pandas matplotlib wordcloud emoji urlextract
```

### 4. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📱 How to Use

1. Export a WhatsApp conversation as a **`.txt` file**.
2. Open the WhatsApp Chat Analyser.
3. Upload the exported chat file.
4. Select **Overall** or a specific user.
5. Click **Analyse**.
6. Explore the statistics and visualisations.

> **Note:** The current parser supports the WhatsApp export date/time format implemented in `preprocessor.py`. Other export formats may require changes to the parser.

---

## 📂 Project Structure

```text
whatsapp_chat_Analyser/
│
├── app.py                 # Streamlit application
├── helper.py              # Data analysis functions
├── preprocessor.py        # Chat parsing and preprocessing
├── stop_hinglish.txt      # Stop words for text analysis
└── README.md              # Project documentation
```

---

## 🧠 What I Learned

Building this project helped me improve my understanding of:

* Python programming
* Pandas and DataFrames
* Data preprocessing
* Regular expressions
* Data visualisation
* Streamlit
* Text analysis
* Working with real-world data
* Turning raw data into meaningful insights



## 🔮 Future Improvements

I plan to improve the project with:

* [ ] Sentiment analysis
* [ ] Reply-time analysis
* [ ] Chat activity heatmap
* [ ] Better support for different WhatsApp export formats
* [ ] Downloadable analysis reports
* [ ] More advanced conversation insights
* [ ] Deployment as a public web application

---




## ⭐ Project Idea

The idea behind this project is simple:

**Turn conversations into data.
Turn data into insights.**
