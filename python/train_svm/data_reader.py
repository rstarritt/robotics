# reads and parses data files

# Expected data format
#  Int     int   float float float
# Frame   Joint    x     y     z
def get_data(filename):
    data = []
    try:
        with open(filename) as f:
            while True:
                line = f.readline()
                if line == "":
                    break
                line = line.split()
                line[0] = int(line[0])
                line[1] = int(line[1])
                line[2] = float(line[2])
                line[3] = float(line[3])
                line[4] = float(line[4])
                data.append(line)
        return data
    except FileNotFoundError:
        print("Data File DNE")
        exit()