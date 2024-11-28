import csv
import os
import django

# Set up Django environment if running this script outside of Django context
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'geolocation.settings')  # Replace with your project name
django.setup('C:\\Users\\Admin\\Desktop\\Django\\geolocation\\DATA\\parks.csv')

from Twendesafari.models import Park  # Replace 'your_app' with your app name

def load_parks_from_csv(csv_file_path):
    parks_to_create = []

    # Open CSV file and read its data
    with open('C:\\Users\\Admin\\Desktop\\Django\\geolocation\\DATA\\parks.csv', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile)
        
        # Loop through each row in the CSV file
        for row in csvreader:
            park = Park(
                name=row['name'],
                description=row['description'],
                latitude = float((row['latitude'] or 0.0)),
                longitude=float((row['longitude'] or 0.0)),
            )
            parks_to_create.append(park)
        
        # Insert all park objects at once using bulk_create()
        Park.objects.bulk_create(parks_to_create)
        print(f"Successfully added {len(parks_to_create)} parks.")

# Example usage:
load_parks_from_csv('C:\\Users\\Admin\\Desktop\\Django\\geolocation\\DATA\\parks.csv')  # Replace with the path to your CSV file
