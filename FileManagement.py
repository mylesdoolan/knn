import csv

def openCSVFile(file):
    with open(file, 'r') as csvfile:
        print('reaches here')
        dialect = csv.Sniffer().sniff(csvfile.read(1024))

        csvfile.seek(0)
        reader = csv.DictReader(csvfile)

        for data in reader:

            data.update("EuclideanValue", ev)


