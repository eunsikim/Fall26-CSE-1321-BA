def main():
    # name,email,department,role,salary,start_date,office
    employee_info_string = "Marcus Chen,marcus.chen@example.com,Engineering,Senior Software Engineer,155000,2019-03-15,San Francisco"

    # `split()` is a STRING function
    # the `split()` function will split the string by a specified
    # separator string
    employee_info_list = employee_info_string.split(",")

    print(employee_info_list)

    print(employee_info_list[0])
    print(employee_info_list[4])

    # `join()` is a STRING function
    employee_info = "-".join(employee_info_list)
    print(employee_info)


if __name__ == "__main__":
    main()