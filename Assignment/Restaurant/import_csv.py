import csv
from Restaurant.models import Restaurant

def import_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            Restaurant.objects.create(
                restaurant_id = row['restaurant_id'],
                restaurant_name = row['restaurant_name'], 
                country_code = row['country_code'],
                address = row['address'],
                cuisines = row['cuisines'],
                has_table_booking = row['has_table_booking'],
                has_online_delivery = row['has_online_delivery']

            )

if __name__ == '__main__':
    csv_file_path = 'path/to/restaurant.csv'
    import_csv(csv_file_path)