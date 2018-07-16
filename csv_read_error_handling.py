file_name = "/files/data/sample.csv"

# Using 'with' to automatically close file
with open(file_name) as csv_file:
    
    try:
        dialect = csv.Sniffer().sniff(csv_file.read(1024))
    except csv.Error as err:
        # log that this file format could not be determined
        print(f"The file format of {file_name} could not be determined.")
    else:
        csv_file.seek(0)
    
        dta = csv.reader(csv_file, dialect=dialect)
    print(dialect)
    
    # dialect = <class 'csv.Sniffer.sniff.<locals>.dialect'>
    # print(dir(dialect)) = 
    #   ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', 
    #   '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
    #   '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
    #   '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
    #   '_name', '_valid', '_validate', 'delimiter', 'doublequote', 'escapechar', 'lineterminator',
    #   'quotechar', 'quoting', 'skipinitialspace']
