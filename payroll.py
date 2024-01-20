"""
Author(s): Bessie Li and Dika KC
Consulted: Maggie Yan
Date: 12/12/23
"""

import csv

def columnAverage(file, string):
    ''' reads a file and averages the given nums in the specified column by adding them up and divinding by the # of values'''
    try:
        count = 0
        total = 0
        with open(file, "r") as f:
            dctReader = csv.DictReader(f)
            for dict in dctReader:
                try:
                    count += 1
                    total += float(dict[string])
                except (ValueError, KeyError):
                    pass 
            if count == 0:
                return None
            return (total/count)
    except FileNotFoundError:
        return None
    

def mergeReports(file1, file2, outputFile):
    '''merges two files together and writes them into an output file'''
    with open(file1, "r") as f1:
        reader1 = csv.DictReader(f1)
        rows1 = [row for row in reader1]
        
    with open(file2, "r") as f2:
        reader2 = csv.DictReader(f2)
        rows2 = [row for row in reader2]
        
    with open(outputFile, "w", newline = "") as out:
        col = rows1[0].keys()
        writer1 = csv.DictWriter(out, fieldnames= col)
        writer1.writeheader()

        for row in rows1:
            writer1.writerow(row)
        for row in rows2:
            writer1.writerow(row)
    
def updateReport(original, update, result):
    ''''writes an updated report based on combining the origninal and updated into a new file'''
    with open(original, "r") as f1:
        orig = csv.DictReader(f1)
        rows1 = [row for row in orig]
    with open(update, "r") as f2:
        upd = csv.DictReader(f2)
        rows2 = [row for row in upd]
        Id = [row["Id"] for row in rows2]
        
        filter = [row for row in rows1 if row["Id"] not in Id]
        new = filter + rows2
        
    with open(result, "w", newline="") as f3:
        res = csv.DictWriter(f3, fieldnames=rows1[0].keys())
        res.writeheader()
        res.writerows(new)
            
def salariesReport(report, output):
    '''creates a report on all salaried employees'''
    with open(report, "r", newline = "") as f:
        dctReader = csv.DictReader(f)
        
        with open(output, "w", newline = "") as f1:
            fieldnames = ["Name", "Id", "Pay", "Hours"]
            dctWriter = csv.DictWriter(f1, fieldnames = fieldnames)
            dctWriter.writeheader()
            
            for row in dctReader:
                if row["Wage"] == "salaried":
                    new = {key: row[key] for key in fieldnames}
                    dctWriter.writerow(new)
            
            
            
    

