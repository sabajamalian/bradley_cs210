from faker import Faker
import csv
import random

def generate_more_shuffled_contacts(num_contacts=50):
    fake = Faker()
    contacts = []

    for _ in range(num_contacts):
        contact = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'phone_number': fake.phone_number()
        }
        contacts.append(contact)

    # Sort by first name
    contacts.sort(key=lambda x: x['last_name'])

    # But shuffle 20% of the contacts with nearby elements
    num_swaps = int(len(contacts) * 0.2)
    for _ in range(num_swaps):
        i = random.randint(0, len(contacts) - 2)
        j = random.randint(0, len(contacts) - 2)
        contacts[i], contacts[j] = contacts[j], contacts[i]

    return contacts

def save_contacts_to_csv(contacts, filename='contacts.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['first_name', 'last_name', 'phone_number'])
        writer.writeheader()
        writer.writerows(contacts)

if __name__ == "__main__":
    contacts = generate_more_shuffled_contacts(100000)
    save_contacts_to_csv(contacts)
