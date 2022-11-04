import operations as op

def main():
    sum = op.sum(10, 30)
    print('Sum: ', sum)

    subs = op.subs(50, 36)
    print('Subs:', subs)

    multi = op.multi(40, 2)
    print('Multi: ', multi)

    div = op.div(54, 3)
    print('Div: ', div)


if __name__ == '__main__':
    main()