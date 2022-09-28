def calc_square_root(n):

    from my_math_calculator import sqrt

    answer = sqrt(n)
    return answer


def main():
    try:
        print(calc_square_root(-4))  # If it catches an error,
    # it will go to the exceptions
    except TypeError:
        print("You sent a string instead of an integer")
    except ValueError:
        print("Don't use negatives")
    else:
        x = 5
    finally:
        print("Code is done")
    print("Reached the end")


if __name__ == "__main__":
    main()
