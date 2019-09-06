Mission to Mars - Web Scraping using BeautifulSoup

Summary: Build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page


Summary:
Build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

Prerequisites:

Pandas
Flask
MongoDB
BeautifulSoup
Requests/Splinter
chromedriver

Methodology

Two Python scripts were created - mission_to_mars.py which contains the scrape function and app.py to run the Flask app.

The scrape function utilizes BeautifulSoup and Requests/Splinter to scrape the data. All the scraped data is saved in variables which are later passed into one dictionary.

In app.py, Flask routes are created to build the home page and to call the scrape function. The dictionary built at the end of the scrape function is saved in MongoDB as a python dictionary.To populate the HTML page, the database is queried.
