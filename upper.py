import sys

def convert_to_uppercase(name):
    return name.upper()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python upper_name.py <name>")
        sys.exit(1)

    name = sys.argv[1]
    uppercased_name = convert_to_uppercase(name)
    print(uppercased_name)
