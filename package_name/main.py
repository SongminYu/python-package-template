from package_name.sub_module.my_sub_module import sum_two_numbers


def main() -> None:
    n1: int = 10
    n2: int = 20

    result: int = sum_two_numbers(n1, n2)

    print(f"{n1} + {n2} = {result}")


if __name__ == "__main__":
    main()
