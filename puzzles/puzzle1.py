import pandas as pd

alphabet = {"a":2, "b":2,"c":2,
            "d":3, "e":3,"f":3,
            "g":4, "h":4,"i":4,
            "j":5, "k":5,"l":5,
            "m":6, "n":6,"o":6,
            "p":7, "q":7,"r":7, "s":7,
            "t":8, "u":8,"v":8,
            "w":9, "x":9,"y":9, "z":9}

def createDF():
    file = "../noahs-csv/noahs-customers.csv"
    df = pd.read_csv(file)
    return df 

def processName(name):
    ans = ""
    for n in name:
        ans += str(alphabet[n.lower()])
    return ans

def main(df):
    names = list(df["name"])
    numbers = list(df["phone"])

    cleaned_names = list()
    cleaned_numbers = list()

    for name in names:
        last = name.split()[1]

        if len(last) == 10:
            cleaned_names.append(name)

    for number in numbers:
        num = number.replace("-", "")
        cleaned_numbers.append(num)

    for name in cleaned_names:
        name_number = processName(name.split()[1])
        if name_number in cleaned_numbers:
            print(f"{name}: {name_number}")

if __name__ == '__main__':
    df = createDF()
    print(df.head())
    main(df)
