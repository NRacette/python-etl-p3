create_schema = ('''
    create schema IF NOT EXISTS petl3;
''')

create_table = ('''
    CREATE TABLE petl3.viable_countys(
    geo_id INT PRIMARY KEY NOT NULL,
    state TEXT NOT NULL,
    county TEXT NOT NULL,
    sales_vector INT NOT NULL
    );
''')

insert_table = ('''
    INSERT INTO petl3.viable_countys
    VALUES(%s,%s,%s,%s);
''')
