from google.cloud import bigquery;
import pgsql
import sql

if __name__ == '__main__':
    client = bigquery.Client()
    #pgsql.query(sql.create_schema)
    #pgsql.query(sql.create_table)

    query = client.query(
        """
        SELECT geo_id, sub_region_1, country_region, sales_vector 
        FROM( 
            SELECT geo_id, sub_region_1, country_region, AVG(retail_and_recreation_percent_change_from_baseline) as sales_vector
            FROM bigquery-public-data.census_bureau_acs.county_2017_1yr
            JOIN bigquery-public-data.covid19_google_mobility.mobility_report
            ON geo_id || '.0' = census_fips_code
            WHERE median_rent <= 2000 AND median_age <= 30
            GROUP BY geo_id, sub_region_1, country_region
        )
        WHERE sales_vector  > -15"""
    )
    for row in query.result():
        pgsql.query(sql.insert_table, row)
