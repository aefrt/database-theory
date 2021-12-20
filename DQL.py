dql_file = open('DQL.sql', mode='w')
dql_file.writelines('')
dql_file.close()

dql_file = open('DQL.sql', mode='a')

y = []
for x in list(second_third_level_categories_and_subcategories.values()):
    y += x

z = []

for x in list(first_second_level_categories_and_subcategories.values()):
    z += x

categories_names = list(first_second_level_categories_and_subcategories.keys()) + z + y
numbers = list(range(len(categories_names)))
categories_mapping = dict(zip(categories_names, numbers))

for key in categories_mapping:
    query = "INSERT INTO Categories VALUES ({}, '{}');\n".format(categories_mapping[key], key)
    dql_file.writelines(query)

dql_file.writelines("\n\nINSERT INTO Sites VALUES (0, 'vons.com', 'vons.com', 'vons.com', 'vons.com');\n\n")

vons_id = 0
for key in first_second_level_categories_and_subcategories:
    values = first_second_level_categories_and_subcategories[key]
    for value in values:
        query = "INSERT INTO Supplier_categories VALUES ({}, {}, {}, {});\n".format(categories_mapping[value], 
                                                                                categories_mapping[key], categories_mapping[value], vons_id)
        dql_file.writelines(query)

dql_file.close()