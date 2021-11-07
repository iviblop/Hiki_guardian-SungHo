def main():
    while True:
        try:
            foo = int(input().replace(" ", ""))
            for bar in range(1, 10):
                print(f"{foo} * {bar} = {foo * bar}")
            break
        except ValueError:
            print("프로토콜에 어긋난 입력입니다.")


if __name__ == '__main__':
    main()

