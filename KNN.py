#K Nearest Neighbour
import math
import csv


# C:\Users\Myles\Downloads\CFIR-dataset-2020.csv
def main():
    unchecked = []
    checked = []
    k = 3
    #change
    print("Please supply the CSV file you wish to have KNN'd:\n")
    file = input()
    print("Opening: ", file)
    with open(file, 'r') as csvfile:
        csvfile.seek(0)
        reader = csv.DictReader(csvfile)
        data = list(reader)
        k = k_calc(len(data))
        for record in data:
            if record.get('State') == '':
                unchecked.append(record)
            else:
                checked.append(record)

    results = status_calculator(unchecked, checked, k)

    keys = results[0].keys()
    with open('/results.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(results)



def status_calculator(unchecked, checked, k):

    for uncheckedValue in unchecked:
        euc_vals = []
        for checkedValue in checked:
#            print(uncheckedValue.get('x'))
            euc_dist = euclidean_distance(uncheckedValue.get('x'), uncheckedValue.get('y'), checkedValue.get('x'), checkedValue.get('y'))
            if (len(euc_vals) <= k):
                euc_vals.append({'Host': checkedValue.get('Host'), 'State': checkedValue.get('State'), 'Distance': euc_dist})
            else:
                euc_vals = sorted(euc_vals, key=lambda i: i['Distance'])
                if euc_vals[-1].get('Distance') > euc_dist:
                    euc_vals[-1] = {'Host': checkedValue.get('Host'), 'State': checkedValue.get('State'), 'Distance': euc_dist}
        uncheckedValue['State'] = count_states(euc_vals, k)
    return checked + unchecked

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((float(x1) - float(x2))**2 + (float(y1) - float(y2))**2)


def count_states(euc_vals, k):
    normal = 0
    for neighbour in euc_vals:
        if neighbour.get('State') == 'Normal':
            normal += 1
    if normal > (k / 2):
        return 'Normal'
    else:
        return 'Infected'


def k_calc(count):
    return round(math.sqrt(count))


if __name__ == "__main__":
    main()