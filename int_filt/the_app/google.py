import int_filt.the_app.amazon as amazon
amazon_list = amazon.search_amazon(amazon._query_to_url('laptop'))

for i in amazon_list:
    print(i.name)