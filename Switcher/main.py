def case_one():
    return "Case One Executed!"

def case_two():
    return "Case Two Executed!"

def case_three():
    return "Case Three Executed!"

def default_case():
    return "Default Case Executed!"

def switcher_example(case):
    switcher = {
        1: case_one,
        2: case_two,
        3: case_three
    }
    # Get the function from the dictionary, default to `default_case`
    func = switcher.get(case, default_case)
    return func()  # Call the function

# Example usage
print(switcher_example(1))  # Output: Case One Executed!
print(switcher_example(4))  # Output: Default Case Executed!
