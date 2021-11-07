def Sum(foo):
    global SUM
    print(foo)
    SUM += foo


def main():
    while True:
        foo = input().strip().replace(" ", "")
        try:
            if '의배수' in foo:
                for bar in range(int(foo[0]), 101, int(foo[0])):
                    Sum(bar)
                break
            elif '수' in foo:
                if '짝' in foo:
                    for bar in range(2, 101, 2):
                        Sum(bar)
                    break
                elif '홀' in foo:
                    for bar in range(1, 101, 2):
                        Sum(bar)
                    break
            print("프로토콜에 어긋난 입력입니다.")
        except ValueError:
            print("프로토콜에 어긋난 입력입니다.")

    print(SUM)


if __name__ == '__main__':
    SUM = 0
    main()

