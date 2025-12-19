def generate_row(row_num: int, size: int) -> list:
    """
    Generate a row of a multiplication table.

    Parameters
    ----------
    row_num : int
        The row number of the multiplication table.
    size : int
        The size of the multiplication table.

    Returns
    -------
    list
        A list representing the row of the multiplication table.
    """

    return [row_num * i for i in range(1, size+1)]


def generate_table(size: int) -> list:
    """
    Generate a multiplication table of a specified size.

    Parameters
    ----------
    size : int
        The size of the multiplication table.

    Returns
    -------
    list
        A list of lists, where each inner list represents a row of the multiplication table.
    """
    return [generate_row(i, size) for i in range(1, size+1)]

if __name__ == "__main__":
    
    HEADER = """
                          MULTIPLICATION TABLE
                       ==========================
            How to use this program:
            \t1. Set the desired size of the multiplication table by entering a positive integer.
            \t2. The program will generate and display the multiplication table of the specified size.
            \t3. To exit the program, enter 'exit'.
                """
    print(HEADER)
    print("\n\n")

    print("\tEnter the size of the multiplication table (positive integer) or 'exit' to quit:")
    choice = input("\t>>>>>>>>    ")
    print("\n")

    while choice.lower() != "exit":
        try:
            size =int(choice)
            if size <= 0:
                raise ValueError("Size must be a positive integer.\n")
            table = generate_table(size)
            for row in table:
                print("\t".join(f"| {num:4}" for num in row))
            choice = input("\n\tEnter another size or 'exit' to quit:\n\t>>>>>>>>    ")
            print("\n")
        except ValueError as ve:
            print(f"\tError: {ve}")