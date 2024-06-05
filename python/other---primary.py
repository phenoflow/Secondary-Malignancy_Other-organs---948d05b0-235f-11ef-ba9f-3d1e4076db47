# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"48828.0","system":"readv2"},{"code":"9505.0","system":"readv2"},{"code":"13569.0","system":"readv2"},{"code":"55096.0","system":"readv2"},{"code":"53528.0","system":"readv2"},{"code":"60335.0","system":"readv2"},{"code":"22146.0","system":"readv2"},{"code":"6170.0","system":"readv2"},{"code":"44615.0","system":"readv2"},{"code":"35999.0","system":"readv2"},{"code":"97832.0","system":"readv2"},{"code":"100296.0","system":"readv2"},{"code":"65490.0","system":"readv2"},{"code":"21590.0","system":"readv2"},{"code":"104480.0","system":"readv2"},{"code":"16760.0","system":"readv2"},{"code":"45824.0","system":"readv2"},{"code":"55090.0","system":"readv2"},{"code":"19945.0","system":"readv2"},{"code":"63896.0","system":"readv2"},{"code":"73213.0","system":"readv2"},{"code":"43930.0","system":"readv2"},{"code":"41144.0","system":"readv2"},{"code":"73616.0","system":"readv2"},{"code":"62828.0","system":"readv2"},{"code":"51551.0","system":"readv2"},{"code":"34145.0","system":"readv2"},{"code":"97091.0","system":"readv2"},{"code":"1952.0","system":"readv2"},{"code":"70736.0","system":"readv2"},{"code":"60134.0","system":"readv2"},{"code":"49145.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('secondary-malignancy_other-organs-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["other---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["other---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["other---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
