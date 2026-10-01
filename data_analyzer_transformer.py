# ============================================================
# DATA ANALYZER AND TRANSFORMER
# ============================================================

data = []
summary = {}


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():
    """Run the Data Analyzer and Transformer program."""

    print("Welcome to the Data Analyzer and Transformer Program")

    while True:

        print("\nMain Menu:")
        print("1. Input Data")
        print("2. Display Data Summary ")
        print("3. Calculate Factorial ")
        print("4. Filter Data by Threshold ")
        print("5. Sort Data")
        print("6. Exit Program")

        choice = input("Please enter your choice: ")

        if choice == "1":
            input_data()

        elif choice == "2":
            display_data_summary()

        elif choice == "3":
            calculate_factorial()

        elif choice == "4":
            filter_data()

        elif choice == "5":
            sort_data()

        elif choice == "6":
            print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye!")
            break

        else:
            print("\nInvalid choice! Please select 1 to 7.")


# ============================================================
# STEP 1 - INPUT DATA
# ============================================================

def input_data():
    """Accept 1D or 2D list data from the user."""

    global data
    global summary

    print("\nInput Data:")
    print("1. Enter 1D Data")
    print("2. Enter 2D Data")
    print("3. Use Sample Data")

    choice = input("Enter your choice: ")

    if choice == "1":

        values = input(
            "Enter numbers separated by commas: "
        )

        data = [int(x.strip()) for x in values.split(",")]

        print("Data entered successfully.")
        print("Data:", data)

        # Update global summary
        summary = create_summary(
            total_elements=len(data),
            minimum=min(data),
            maximum=max(data),
            total=sum(data),
            average=sum(data) / len(data)
        )

    elif choice == "2":

        data = [
            [12, 21, 34],
            [43, 56, 78],
            [90, 25, 30]
        ]

        print("\n2D Data:")

        for row in data:
            print(row)

        numbers = flatten(data)

        summary = create_summary(
            total_elements=len(numbers),
            minimum=min(numbers),
            maximum=max(numbers),
            total=sum(numbers),
            average=sum(numbers) / len(numbers)
        )

    elif choice == "3":

        data = [12, 21, 34, 43, 56, 78, 90]

        print("Sample Data:", data)

        summary = create_summary(
            total_elements=len(data),
            minimum=min(data),
            maximum=max(data),
            total=sum(data),
            average=sum(data) / len(data)
        )

    else:
        print("Invalid choice!")


# ============================================================
# STEP 2 - BUILT-IN FUNCTIONS
# ============================================================

def display_data_summary():
    """Display basic dataset statistics using built-in functions."""

    if not data:
        print("\nPlease enter data first.")
        return

    numbers = flatten(data)

    # *args demonstration
    values = accept_values(*numbers)

    # **kwargs demonstration
    summary_data = create_summary(
        total_elements=len(values),
        minimum=min(values),
        maximum=max(values),
        total=sum(values),
        average=sum(values) / len(values)
    )

    print("\nData Summary:")
    print("- Total elements:", len(values))
    print("- Minimum value:", min(values))
    print("- Maximum value:", max(values))
    print("- Sum of all values:", sum(values))
    print("- Average value:", round(summary_data["average"], 2))


# ============================================================
# USER DEFINED FUNCTIONS
# ============================================================

def accept_values(*args):
    """Accept multiple values using *args."""

    return list(args)


def create_summary(**kwargs):
    """Create a dataset summary using **kwargs."""

    return kwargs


# ============================================================
# STEP 3 - RECURSION
# ============================================================

def factorial(number):
    """Calculate factorial using recursion."""

    if number == 0:
        return 1

    return number * factorial(number - 1)


def calculate_factorial():
    """Take a number and display its factorial."""

    number = int(
        input("\nEnter a number to calculate its factorial: ")
    )

    result = factorial(number)

    print("\nFactorial of", number, "is:", result)


# ============================================================
# STEP 4 - LAMBDA FUNCTION
# ============================================================

def filter_data():
    """Filter data using lambda and filter functions."""

    if not data:
        print("\nPlease enter data first.")
        return

    numbers = flatten(data)

    threshold = int(
        input(
            "\nEnter a threshold value to filter out data above this value: "
        )
    )

    # Lambda function
    result = list(
        filter(lambda x: x >= threshold, numbers)
    )

    print("\nFiltered Data (values >= {}):".format(threshold))

    if result:
        print(", ".join(map(str, result)))
    else:
        print("No values found.")


# ============================================================
# STEP 5 - SORT DATA
# ============================================================

def sort_data():
    """Sort 1D or 2D data using sort and sorted."""

    if not data:
        print("\nPlease enter data first.")
        return

    print("\nChoose sorting option:")
    print("1. Ascending")
    print("2. Descending")

    choice = input("\nEnter your choice: ")

    numbers = flatten(data)

    if choice == "1":

        # sort() method
        sorted_data = numbers.copy()
        sorted_data.sort()

        print("\nSorted Data in Ascending Order:")
        print(", ".join(map(str, sorted_data)))

    elif choice == "2":

        # sorted() function
        sorted_data = sorted(numbers, reverse=True)

        print("\nSorted Data in Descending Order:")
        print(", ".join(map(str, sorted_data)))

    else:
        print("Invalid choice!")

# ============================================================
# 1D AND 2D LIST
# ============================================================

def flatten(dataset):
    """Convert a 2D list into a 1D list."""

    if not dataset:
        return []

    if isinstance(dataset[0], list):

        result = []

        for row in dataset:
            result.extend(row)

        return result

    return dataset


# ============================================================
# START PROGRAM
# ============================================================

if __name__ == "__main__":
    main()
