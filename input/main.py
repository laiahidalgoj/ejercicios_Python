
def main():
    string = input('Add countries separate for comas: ')
    listCountries = string.split()
    print(" ".join(sorted(set(listCountries), reverse=False)))

if __name__ == '__main__':
    main()