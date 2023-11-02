# Import requests and BeautifulSoup libraries
import requests
from bs4 import BeautifulSoup

# Define a function that takes no arguments and returns a list of news headlines and links from https://vnexpress.net/
def get_news():
    # Initialize an empty list to store the news
    news = []

    # Define the URL of the website
    url = "https://vnexpress.net/"

    # Send a GET request to the website and store the response
    response = requests.get(url)

    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # Parse the response content as HTML using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all the elements with class name "title-news" that contain the news headlines
        headlines = soup.find_all(class_="title-news")

        # Loop through each headline element
        for headline in headlines:
            # Get the text of the headline
            text = headline.get_text().strip()

            # Get the link of the headline
            link = headline.find("a")["href"]

            # Append a tuple of text and link to the news list
            news.append((text, link))
    
    # Return the news list
    return news


def get_sports_news():
    # Initialize an empty list to store the news
    news = []

    # Define the URL of the sports section of the website
    url = "https://vnexpress.net/the-thao"

    # Send a GET request to the website and store the response
    response = requests.get(url)

    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # Parse the response content as HTML using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all the elements with class name "title-news" that contain the news headlines
        headlines = soup.find_all(class_="title-news")

        # Loop through each headline element
        for headline in headlines:
            # Get the text of the headline
            text = headline.get_text().strip()

            # Get the link of the headline
            link = headline.find("a")["href"]

            # Append a tuple of text and link to the news list
            news.append((text, link))
    
    # Return the news list
    return news


# Call the function and store the result
# result = get_news()
result = get_sports_news()
print(result)
print(len(result))
print(type(result))

# Loop through each item in the result and print it
# for item in result:
#     print(item[0], item[1])
