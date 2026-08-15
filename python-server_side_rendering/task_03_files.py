from flask import Flask, render_template, request
import csv
import json

app = Flask(__name__)


def read_json():
    with open('products.json', 'r') as file:
        return json.load(file)


def read_csv():
    with open('products.csv', 'r') as file:
        return list(csv.DictReader(file))


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ('json', 'csv'):
        return render_template(
            'product_display.html',
            products=[],
            error='Wrong source'
        )

    try:
        if source == 'json':
            data = read_json()
        else:
            data = read_csv()
    except (FileNotFoundError, json.JSONDecodeError, csv.Error):
        return render_template(
            'product_display.html',
            products=[],
            error='Error reading data file'
        )

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template(
                'product_display.html',
                products=[],
                error='Product not found'
            )

        data = [
            product for product in data
            if int(product['id']) == product_id
        ]

        if not data:
            return render_template(
                'product_display.html',
                products=[],
                error='Product not found'
            )

    return render_template(
        'product_display.html',
        products=data,
        error=None
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
