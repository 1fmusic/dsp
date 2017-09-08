import csv

def write_to_csv(list_of_emails):
    with open("emails.csv","w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(('emails',))
        for row in list_of_emails:
            writer.writerow((row,))
