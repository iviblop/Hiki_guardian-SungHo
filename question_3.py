def Devide(a, b):
    print(b / a)


def main():
    while True:
        try:
            a, b = map(int, input().strip().split(", "))
            Devide(a, b)
            break
        except ValueError:
            print("프로토콜에 어긋난 입력입니다.")
        except ZeroDivisionError:
            print("0으로는 나눌 수 없습니다")


if __name__ == '__main__':
    main()

