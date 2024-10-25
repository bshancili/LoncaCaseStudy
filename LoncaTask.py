import xml.etree.ElementTree as ET
from pymongo import MongoClient, UpdateOne
from datetime import datetime
from datetime import datetime, timezone

# MongoDB setup
client = MongoClient('mongodb://localhost:27017/')
db = client['productDB']
collection = db['products']

# XML parsing function
def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    products = []
    
    for product in root.findall('Product'):
        # Extract product
        product_id = product.get('ProductId')
        name = product.get('Name', 'N/A').capitalize()
        images = [img.get('Path') for img in product.findall('.//Image')]
        details = {detail.get('Name'): detail.get('Value') for detail in product.findall('.//ProductDetail')}
        
        # Extract product details
        color = [details.get('Color', 'Unknown').capitalize()]
        price = float(details.get('Price', '0').replace(',', '.'))
        discounted_price = float(details.get('DiscountedPrice', '0').replace(',', '.'))
        is_discounted = details.get('IsDiscounted', False)
        quantity = int(details.get('Quantity', 0))
        product_type = details.get('ProductType', 'Unknown').capitalize()
        series = details.get('Series', 'N/A')
        season = details.get('Season', 'N/A')
        sample_size = details.get('SampleSize', 'N/A')
        status = details.get('Status', 'N/A')
        fabric = details.get('Fabric', 'N/A')
        product_measurements = details.get('ProductMeasurements', 'N/A')
        price_unit = details.get('PriceUnit', 'USD')
        
        # Extract descriptions and measurements
        description = product.find('Description').text if product.find('Description') is not None else ""
        model_measurements = "Model info missing"  # Set default if missing in description
        
        # Create product document
        product_doc = {
            'product_id': product_id,
            'name': name,
            'images': images,
            'color': color,
            'price': price,
            'discounted_price': discounted_price,
            'is_discounted': is_discounted,
            'quantity': quantity,
            'product_type': product_type,
            'series': series,
            'season': season,
            'description': description,
            'model_measurements': model_measurements,
            'price_unit': price_unit,
            'sample_size': sample_size,
            'status': status,
            'fabric': fabric,
            'product_measurements': product_measurements,

            'createdAt': datetime.now(timezone.utc),
            'updatedAt': datetime.now(timezone.utc)

        }

        # Append the product to products list
        products.append(product_doc)
    
    return products

# Function to upsert products to MongoDB
def upsert_products(products):
    operations = []
    
    for product in products:
        operations.append(UpdateOne(
            {'product_id': product['product_id']},  # Match by product_id
            {'$set': product},  # Set the new or updated data
            upsert=True  # If no match, insert as new product
        ))
    
    # Bulk upsert to MongoDB
    if operations:
        result = collection.bulk_write(operations)
        print(f"Upserted {result.upserted_count} products, updated {result.modified_count} products.")

# Main function to run the pipeline
def run_pipeline():
    xml_file_path = 'lonca-sample.xml'  # Update this to the actual file path
    products = parse_xml(xml_file_path)
    upsert_products(products)

# Schedule the pipeline to run periodically
if __name__ == '__main__':
    run_pipeline()
