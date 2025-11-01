
import requests
from collections import defaultdict
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

# Define the base URL for E-utilities
BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
EMAIL = "your_email@example.com"  # Add your email for the NCBI API

def search_pubmed(keyword):
    # E-search to find articles based on the keyword
    params = {
        'db': 'pubmed',
        'term': keyword,
        'retmax': 1000,  # Maximum results
        'usehistory': 'y',  # Use history to retrieve more data if needed
        'retmode': 'xml'
    }
    response = requests.get(f"{BASE_URL}esearch.fcgi", params=params)
    return response.text

def fetch_pubmed_data(ids):
    # E-fetch to get article details (including publication dates)
    params = {
        'db': 'pubmed',
        'id': ','.join(ids),  # Join the list of PubMed IDs into a string
        'retmode': 'xml'
    }
    response = requests.get(f"{BASE_URL}efetch.fcgi", params=params)
    return response.text

def parse_pubmed_dates(xml_data):
    # Parse XML data to extract publication years
    root = ET.fromstring(xml_data)
    years = defaultdict(int)

    for pubmed_article in root.findall('.//PubmedArticle'):
        # Try to get the publication year
        pubdate = pubmed_article.find('.//PubDate')
        year = pubdate.find('Year').text if pubdate is not None else None
        if year:
            years[year] += 1

    return years

def plot_publications_per_year(year_data):
    # Sort years and prepare for plotting
    sorted_years = sorted(year_data.items())
    years, counts = zip(*sorted_years)

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.bar(years, counts, color='blue')
    plt.xlabel('Year')
    plt.ylabel('Number of Publications')
    plt.title('Number of Publications Per Year for the Given Keyword')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Step 1: Search for a keyword (Replace 'cancer' with your BSc thesis keyword)
keyword = "DNM2"
search_results = search_pubmed(keyword)

# Step 2: Parse the search results to extract PubMed IDs
root = ET.fromstring(search_results)
ids = [id_tag.text for id_tag in root.findall('.//Id')]

# Step 3: Fetch the publication details for the first 1000 results
if ids:
    pubmed_data = fetch_pubmed_data(ids)
    years = parse_pubmed_dates(pubmed_data)

    # Step 4: Plot the data
    plot_publications_per_year(years)
else:
    print("No results found.")

