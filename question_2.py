def main():
    SUM = 0
    while True:
        foo = input().replace(" ", "")
        try:
            if '의배수' in foo:
                for bar in range(int(foo[0]), 101, int(foo[0])):
                    print(foo)
                    SUM += foo
                break
            elif '수' in foo:
                if '짝' in foo:
                    for bar in range(2, 101, 2):
                        print(foo)
                        SUM += foo
                    break
                elif '홀' in foo:
                    for bar in range(1, 101, 2):
                        print(foo)
                        SUM += foo
                    break
            print("프로토콜에 어긋난 입력입니다.")
        except ValueError:
            print("프로토콜에 어긋난 입력입니다.")

    print(SUM)


if __name__ == '__main__':
    main()

