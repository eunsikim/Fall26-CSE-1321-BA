"""
Create a function that takes in a list, each index in this
list should represent each of these values:
    name,email,department,role,salary,start_date,office
The function should return the NetID of this person.

NetID Format:
first character of the firstname, first four characters of 
lastname, and start_date day
"""
def main():
    # firstname, lastname,email,department,role,salary,start_date,office
    employee_info_string = "Marcus,Chen,marcus.chen@example.com,Engineering,Senior Software Engineer,155000,2019-03-15,San Francisco"

if __name__ == "__main__":
    main()