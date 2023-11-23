from app import app
from flask import render_template, request
from scraper.scraper import fetch_page, extract_data, save_to_csv

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        selector = request.form['selector']
        html = fetch_page(url)
        if html:
            data = extract_data(html, selector)
            save_to_csv(data, 'output.csv')
            return render_template('result.html', data=data)
        else:
            return "Failed to fetch the page. Please check the URL."
    return render_template('index.html')
