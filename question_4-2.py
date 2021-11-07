def main():
    while True:
        try:
            foo, bar = map(int, input().strip().split(" "))
            print("*  ", end='')
            for baz in range(1, 10):
                print("%3d" % baz, end='')
            print("\n──────────────────────────────", end='')
            for baz in range(foo, bar + 1):
                print("\n%-3d" % baz, end='')
                for qux in range(1, 10):
                    print("%3d" % (baz * qux), end='')
            break
        except ValueError:
            print("프로토콜에 어긋난 입력입니다.")


if __name__ == '__main__':
    main()

