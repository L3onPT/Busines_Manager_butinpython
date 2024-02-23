from random import randint
from time import sleep
starting_data_day = 22
starting_data_month = 2
starting_data_year = 2024

def main(starting_data_day, starting_data_month, starting_data_year):
    while True:
        sleep(1)
                    
        if starting_data_month >= 12:
            starting_data_month = 1
            starting_data_year = starting_data_year + 1
                
        if starting_data_day <= 29:
            starting_data_day = starting_data_day + 1

        elif starting_data_day >=30:
            starting_data_day = 1
            starting_data_month = starting_data_month + 1

        else:
            starting_data_day = starting_data_day + 1
        

        print(starting_data_day, "/", starting_data_month, "/", starting_data_year)

main(starting_data_day, starting_data_month, starting_data_year)