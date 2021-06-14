import pandas as pd
import time

df = pd.read_csv("countriesArea.csv", sep=";", usecols=['Ranking', 'Country', 'Area'])

def check_empty(comparison):
    return df[df["Country"] == comparison].empty

comparisonCountry = input("Enter your country: ")
while check_empty(comparisonCountry):
    print("TYPE A VALID COUNTRY")
    comparisonCountry = input("Enter your country: ")

countriesList = []
print("TO FINISH EXECUTION JUST PRESS ENTER WITHOUT TYPING")
while True:
    country = str(input(f"Enter country {len(countriesList) + 1}: "))
    if not check_empty(country):
        countriesList.append(country)
    if country == "":
        if len(countriesList) > 0:
            print("CALCULATING VALUES...")
            time.sleep(1)
            break
        print("No countries to compare finishing execution")
        exit()

def get_value_from_df(comparison,column="Area"):
    return df[df["Country"] == comparison][column].to_numpy()[0]

countries_area = [ get_value_from_df(i) for i in countriesList ]
chosen_country = get_value_from_df(comparisonCountry)
ranking_countries = { i: get_value_from_df(i,column="Ranking") for i in countriesList }

print("The area of the chosen countries", countriesList, "represent approximately:",
      round(float(sum(countries_area) / chosen_country * 100),2),"% of", comparisonCountry)
print("Chosen Country ranking: \n",
      comparisonCountry, ":", get_value_from_df(comparisonCountry,column="Ranking"))
print("Countries to compare ranking: \n", ranking_countries)