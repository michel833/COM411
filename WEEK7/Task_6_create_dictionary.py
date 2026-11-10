def short_pattern () :
    pattern = {"sequence":101 ,"occurrences":5 }
    return pattern


def medium_pattern () :
    pattern = {"sequence":111000 ,"occurrences": 25 }
    return pattern


def long_pattern () :
    pattern = {"sequence":1100110011001100 ,"occurrences":50 }
    return pattern


def run_task3 () :
    print ("Analysing patterns...")
    pattern={ "short_sequence":short_pattern(),
    "medium_sequence":medium_pattern(),
    "long_sequence":long_pattern(),}
    for keys, values in pattern.items ():
        print (f"{keys}: {values}")

run_task3()

