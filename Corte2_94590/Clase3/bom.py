
def boom(x):
    if x > 0:
        print(x)
        boom(x-1)
    else:
        print("booooom")
    print(f"finalizo{x}")


def main():
    boom(5)



if __name__ == "__main__":
    main()