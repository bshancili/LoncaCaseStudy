# Scraper Pipeline - Product Entry

## Overview

The **Scraper Pipeline - Product Entry** is a Python script that parses an XML file containing product information and imports the data into a MongoDB database. 

## Installation

Clone the repository with following command in the directory which you want to set up the implementation:

   ```
   git clone https://github.com/bshancili/LoncaCaseStudy
   ```

## Usage

Make sure that MongoDB is downloaded in your computer. If not, you can download in [this link](https://www.mongodb.com/try/download/community). Afterwords, Launch the terminal or command prompt and start the MongoDB server:

   ```bash
   mongod
   ```

Afterwords, head to the directory in which you have downloaded the repository, and  run the implementation with following command:

   ```bash
   python LoncaTask.py
   ```

After a successful run, you should see an output like this:

   ```
   Upserted 0 products, updated 4 products.
   ```

## Results

Make sure that Mongo Shell is downloaded in your computer. If not, you can download in [this link](https://www.mongodb.com/try/download/shell). Afterwords, Launch the terminal or command prompt and start the MongoDB shell:

   ```bash
   mongosh
   ```

Switch to the productDB database:

   ```bash
   use productDB
   ```

Retrieve and display all products from the products collection:

   ```bash
   db.products.find().pretty()
   ```

An example of a product entry in the database will look like this:

   ```JSON
   {
  "_id": ObjectId("671ba1428d8837130c9a67c9"),
  "product_id": "62156-02",
  "color": ["Vizon"],
  "createdAt": ISODate("2024-10-25T13:46:42.260Z"),
  "description": "\n<ul><li><strong>Ürün Bilgisi: </strong>Polo yaka, düğmeli, göğüs ve sırt dekolteli, likralı, triko kumaş, likralı, crop boy, dar kalıp, dar kesim, bluz</li><li><strong>Kumaş Bilgisi:</strong> Triko</li><li><strong>Model Ölçüleri:</strong> Boy: 1.73, Kilo: 50, Göğüs: 87, Bel: 63, Kalça: 88</li><li>Modelin üzerindeki ürün <strong>STD</strong> bedendir.</li></ul>\n",
  "discounted_price": 1.24,
  "fabric": "N/A",
  "images": [
    "www.aday-butik-resim-sitesi/62156-vizon-1.jpeg",
    "www.aday-butik-resim-sitesi/62156-vizon-2.jpeg",
    "www.aday-butik-resim-sitesi/62156-vizon-3.jpeg"
  ],
  "is_discounted": false,
  "model_measurements": "Model info missing",
  "name": "Büzgü kollu t-shirt",
  "price": 3.24,
  "price_unit": "USD",
  "product_measurements": "N/A",
  "product_type": "T-shirt",
  "quantity": 0,
  "sample_size": "N/A",
  "season": "2023 Yaz",
  "series": "1M-1L-1XL",
  "status": "N/A",
  "updatedAt": ISODate("2024-10-25T13:46:42.260Z")
}
   ```
