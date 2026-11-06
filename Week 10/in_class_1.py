"""
Create a function that takes in a list, each index in this
list should represent each of these values:
    first name,last name,email,department,role,salary,start_date,office
The function should return the NetID of this person.

NetID Format:
first character of the firstname, first four characters of 
lastname, and start_date day
"""

def main():
    # firstname, lastname,email,department,role,salary,start_date,office
    employee_info_string = "Marcus,Chen,marcus.chen@example.com,Engineering,Senior Software Engineer,155000,2019-03-15,San Francisco"

    employee_info_list = employee_info_string.split(",")

    print(employee_info_list)

    netID = ""

    netID += employee_info_list[0][0]

    for x in range(4):
        netID += employee_info_list[1][x]

    netID += employee_info_list[6][8]
    netID += employee_info_list[6][9]

    print(netID)

if __name__ == "__main__":
    main()