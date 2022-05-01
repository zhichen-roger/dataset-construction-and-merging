import  csv
if __name__ == '__main__':
    with open("D:\\ddf\\china.csv","r",encoding="utf-8")  as f:
        csv1=[]
        reader = csv.reader(f)
        i=0
        k=0
        print(type(reader))
        for row in reader:
            if "sentence" in  row[0]:
                k=k+1
                row[0]="Sentence: "+str(k)

            i=i+1
            csv1.append(row)

        with open("D:\\ddf\\ner_data2.csv", "w", encoding="utf-8",newline="")  as f1:
            csv_writer = csv.writer(f1)
            print("1234",len(csv1))
            for row in csv1:
                csv_writer.writerow(row)
