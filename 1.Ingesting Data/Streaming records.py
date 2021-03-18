# Retrieve the products of the shop called Tesco.
# Use the convenience function to query the API
tesco_items = retrieve_products("Tesco")

singer.write_schema(stream_name="products", schema=schema,
                    key_properties=[])
                    
                    
# Based on the output of the previous step, use the function write_record() to write one of these products to the products stream, 
# which is where you also wrote the schema to. Make sure to add to the product a key-value pair that is mentioned in the schema, 
# but is missing from the product, so that the record you write complies with the schema.
# Use the convenience function to query the API
tesco_items = retrieve_products("Tesco")

singer.write_schema(stream_name="products", schema=schema,
                    key_properties=[])

# Write a single record to the stream, that adheres to the schema
singer.write_record(stream_name="products", 
            record={**tesco_items[0], 'store_name': "Tesco"})


# Now use the more appropriate function write_records() to write all items for all shops exposed by the API. 
# As you don’t know a priori how big the dataset will be, you will be using a generator expression in which you enrich the items with the store_name one at a time.
# Use the convenience function to query the API
tesco_items = retrieve_products("Tesco")

singer.write_schema(stream_name="products", schema=schema,
                    key_properties=[])

# Write a single record to the stream, that adheres to the schema
singer.write_record(stream_name="products", 
                    record={**tesco_items[0], "store_name": "Tesco"})

for shop in requests.get(SHOPS_URL).json()["shops"]:
    # Write all of the records that you retrieve from the API
    singer.write_records(
      stream_name="products", # Use the same stream name that you used in the schema
      records=({**item, "store_name": shop}
               for item in retrieve_products(shop))
    )

