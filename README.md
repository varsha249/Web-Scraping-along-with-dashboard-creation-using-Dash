# Web Scraping and Dashboard Creation using Dash

This project demonstrates the process of **web scraping** data from an e-commerce website (Jumia), cleaning and organizing the scraped data, and building an **interactive dashboard** using **Dash** and **Plotly** to visualize the results. The project focuses on smartphones, showcasing product prices, ratings, and links for further exploration. .

---

## **Features**
### **Web Scraping**
- Scrapes product data such as:
  - Product Name
  - Price
  - Rating
  - Product Link
- Handles dynamic pagination to scrape multiple pages.
- Mimics real user behavior with randomized delays and rotating User-Agent headers.
- Logs errors into a `scraper.log` file for debugging.

### **Dashboard**
- Interactive dashboard with:
  - **Price Range Slider**: Filter smartphones based on price.
  - **Minimum Rating Dropdown**: Filter smartphones by rating (e.g., 4.0 and above).
  - **Price Distribution Graph**: A histogram showing the distribution of smartphone prices.
  - **Price vs. Rating Scatter Plot**: Displays the relationship between price and ratings.
  - **Top Products Table**: A ranked table of the top 10 smartphones based on ratings.
- Built with **Dash** for interactivity and **Plotly** for visualizations.

---

## **Technologies Used**
### **Web Scraping**
- `requests`: To send HTTP requests and fetch webpage content.
- `BeautifulSoup`: To parse and extract data from HTML.
- `random` and `time`: To mimic human-like behavior with randomized delays.
- `logging`: To track errors and debug issues during scraping.

### **Data Handling**
- `pandas`: For data cleaning, processing, and exporting to CSV.

### **Dashboard**
- `Dash`: For creating the interactive dashboard.
- `Plotly`: For generating visualizations like histograms and scatter plots.

---

## **Setup Instructions**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/Web-Scraping-along-with-dashboard-creation-using-Dash.git
   cd Web-Scraping-along-with-dashboard-creation-using-Dash
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.7+ installed. Then install the required libraries:
   ```bash
   pip install pandas BeautifulSoup requests random logging 
   ```

3. **Run the Web Scraper**:
   Execute the scraper to collect data from Jumia:
   ```bash
   python webscraping.ipynb
   ```
   The scraped data will be saved as `jumia_enhanced_with_ratings.csv`.

4. **Run the Dashboard**:
   Launch the Dash dashboard:
   ```bash
   python dash_dashboard.py
   ```
   Open the link provided in the terminal in your browser.



## **Key Functions**
### **Web Scraper (`webscraping.ipynb`)**
- **`get_total_pages(url, headers)`**:
  - Fetches the total number of pages in the search results.
- **`scrape_jumia(num_pages)`**:
  - Extracts product data (name, price, rating, link) from multiple pages.
  - Saves the data into a CSV file (`jumia_enhanced_with_ratings.csv`).

### **Dashboard (`dash_dashboard.py`)**
- **Price Range Slider**:
  - Adjusts the price range for filtering smartphones.
- **Minimum Rating Dropdown**:
  - Filters smartphones by customer ratings.
- **Graphs and Table**:
  - Visualizes price distribution and price-rating relationships.
  - Displays the top-rated products in a table format.

---

## **Future Enhancements**
- Add more product categories (e.g., laptops, tablets) to the scraper.
- Including additional visualizations (e.g., average price by brand).
- Integrating advanced anti-scraping techniques like proxy rotation.
- Deploying the dashboard to a cloud platform (e.g., Heroku, AWS).. 

---

## **Acknowledgments**
- **Dash and Plotly**: For enabling the creation of interactive dashboards.
- **BeautifulSoup**: For simplifying HTML parsing and data extraction.
- **Jumia**: For providing the data used in this project (for educational purposes).
