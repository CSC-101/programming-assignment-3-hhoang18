import data
import county_demographics
from data import CountyDemographics
import hw3_tests

# Part 1
def population_total(list1: list[CountyDemographics])->int:
    total_pop = 0
    for county in list1: #go through every county in the list
        if "2014 Population" in county.population:
            total_pop += county.population["2014 Population"]
    return total_pop
#the function's purpose is to return the total 2014 population for the counties in the list
#the input is the list of county demographics
#the output is an integer (the total 2014 population)
#the parameter is type list
#an integer is returned

# Part 2
def filter_by_state(counties: list[CountyDemographics], abbrev: str)->list[CountyDemographics]:
    filtered = []
    for county in counties:
        if county.state == abbrev:
            filtered.append(county)
    return filtered
#the function's purpose is to return a list of counties that are from a specific state (the abbreviation is specified)
#the input is a list of county demographics and a two letter state abbreviation
#the output is a list of counties that are within the specified state
#the parameters are type list and type string
#a list is returned

# Part 3
def population_by_education(counties: list[CountyDemographics], educ_key: str) -> float:
    total_pop=0.0
    for county in counties:
        if educ_key in county.education:
            total_pop += county.population["2014 Population"] * (county.education[educ_key]/100)
    return total_pop
#the function's purpose is to find the 2014 subpopulation in the set of counties for a specified education key
#the input is an education key of interest and a list of county demographics
#the output is the 2014 subpopulation
#the parameters are type list and string
#a float is returned
def population_by_ethnicity(counties: list[CountyDemographics], ethnicity_key: str) -> float:
    total_pop=0.0
    for county in counties:
        if ethnicity_key in county.ethnicities:
            total_pop += county.population["2014 Population"] * (county.ethnicities[ethnicity_key]/100)
    return total_pop
#the function's purpose is to return the 2014 subpopulation across a set of counties for the specified ethnicity key
#the input is an ethnicity key of interest and a list of county demographics
#the output is the 2014 subpopulation
#the parameters are type list and string
#a float is returned
def population_below_poverty_level(counties: list[CountyDemographics]) -> float:
    total_pop=0.0
    for county in counties:
        if "Persons Below Poverty Level" in county.income:
            total_pop += county.population["2014 Population"] * (county.income["Persons Below Poverty Level"] / 100)
    return total_pop
#the function's purpose is to return the 2014 subpopulation across a set of counties for income key
#"Persons Below Poverty Level"
#the inputs are the income key "Persons Below Poverty Level" and a list of county demographics
#the output is the 2014 subpopulation
#the parameter is type list
#a float is returned

# Part 4
def percent_by_education(counties: list[CountyDemographics], educ_key: str) -> float:
    total_pop = population_total(counties) #part 1
    education_pop = population_by_education(counties, educ_key)
    if total_pop>0:
        percentage = (education_pop/total_pop)*100
    else:
        percentage = 0.0
    return percentage
#the function's purpose is to find the 2014 subpopulation for the specified education key
#as a percentage of the total 2014 population of the counties
#the inputs are a list of county demographics and an education key of interest
#the output is the 2014 subpopulation as a percentage of the total 2014 population
#the parameters are type list and type string
#a float is returned
def percent_by_ethnicity(counties: list[CountyDemographics], ethnicity: str) -> float:
    total_pop = population_total(counties) #part 1
    ethnicity_pop = population_by_ethnicity(counties, ethnicity)
    if total_pop>0:
        percentage = (ethnicity_pop/total_pop)*100
    else:
        percentage = 0.0
    return percentage
#the function's purpose is to find the 2014 subpopulation for the specified ethnicity key
#as a percentage of the total 2014 population of the counties
#the inputs are a list of county demographics and an ethnicity key of interest
#the output is the 2014 subpopulation as a percentage of the total 2014 population
#the parameters are type list and type string
#a float is returned
def percent_below_poverty_level(counties: list[CountyDemographics]) -> float:
    total_pop = population_total(counties)  # part 1
    pov_pop = population_below_poverty_level(counties)
    if total_pop > 0:
        percentage = (pov_pop / total_pop) * 100
    else:
        percentage = 0.0
    return percentage
#the function's purpose is to find the 2014 subpopulation for the income key "Persons Below Poverty Level"
#as a percentage of the total 2014 population of the counties
#the input is a list of county demographics (and income key "Persons Below Poverty Level")
#the output is the 2014 subpopulation as a percentage of the total 2014 population
#the parameter is type list
#a float is returned

# Part 5
def education_greater_than(counties: list[CountyDemographics], educ: str, limit: float) -> list[CountyDemographics]:
    result = []
    for county in counties:
        if educ in county.education:
            if county.education[educ]>limit:
                result.append(county)
    return result
#the function's purpose is to return a list of county demographics objects where the value for the education key
#is greater than a specified threshold
#the inputs are a list of county demographics, the education key of interest, and a threshold value
#the output is a list of country demographic objects
#the parameters are type list, string, and float
#a list is returned
def education_less_than(counties: list[CountyDemographics], educ: str, limit: float) -> list[CountyDemographics]:
    result = []
    for county in counties:
        if educ in county.education:
            if county.education[educ]<limit:
                result.append(county)
    return result
#the function's purpose is to return a list of county demographics objects where the value for the education key
#is less than a specified threshold
#the inputs are a list of county demographics, the education key of interest, and a threshold value
#the output is a list of country demographic objects
#the parameters are type list, string, and float
#a list is returned
def ethnicity_greater_than(counties: list[CountyDemographics], ethnicity: str, limit: float) -> list[CountyDemographics]:
    result = []
    for county in counties:
        if ethnicity in county.ethnicities:
            if county.ethnicities[ethnicity]>limit:
                result.append(county)
    return result
#the function's purpose is to return a list of county demographics objects where the value for the ethnicity key
#is greater than a specified threshold
#the inputs are a list of county demographics, the ethnicity key of interest, and a threshold value
#the output is a list of country demographic objects
#the parameters are type list, string, and float
#a list is returned
def ethnicity_less_than(counties: list[CountyDemographics], ethnicity: str, limit: float) -> list[CountyDemographics]:
    result = []
    for county in counties:
        if ethnicity in county.ethnicities:
            if county.ethnicities[ethnicity]<limit:
                result.append(county)
    return result
#the function's purpose is to return a list of county demographics objects where the value for the ethnicity key
#is less than a specified threshold
#the inputs are a list of county demographics, the ethnicity key of interest, and a threshold value
#the output is a list of country demographic objects
#the parameters are type list, string, and float
#a list is returned
def below_poverty_level_greater_than(counties: list[CountyDemographics], limit: float) -> list[CountyDemographics]:
    result = []
    for county in counties:
        if "Persons Below Poverty Level" in county.income:
            if county.income["Persons Below Poverty Level"] > limit:
                result.append(county)
    return result
#the function's purpose is to return a list of county demographic objects where the value for the key
#"Persons Below Poverty Level" is greater than the specified threshold
#the inputs are the list of county demographics and a threshold value (and the key "Persons Below Poverty Level" is known
#the output is a list of county demographics objects
#the parameters are type list and float
#a list is returned
def below_poverty_level_less_than(counties: list[CountyDemographics], limit: float) -> list[CountyDemographics]:
    result = []
    for county in counties:
        if "Persons Below Poverty Level" in county.income:
            if county.income["Persons Below Poverty Level"] < limit:
                result.append(county)
    return result
#the function's purpose is to return a list of county demographic objects where the value for the key
#"Persons Below Poverty Level" is less than the specified threshold
#the inputs are the list of county demographics and a threshold value (and the key "Persons Below Poverty Level" is known
#the output is a list of county demographics objects
#the parameters are type list and float
#a list is returned









