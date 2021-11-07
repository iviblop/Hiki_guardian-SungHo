class Student:
    def __init__(self, gr, cl, nu):
        self.gr = gr
        self.cl = cl
        self.nu = nu

    def info(self):
        print(self.gr, "학년이군요.\n", self.cl, "반의 학급 분위기는 어떤가요?\n번호가 ", self.nu, "번이라 좋은 점이 있나요?", sep='')


def main():
    foo = input().replace(" ", "")
    while True:
        try:
            Student(int(foo[0]), int(foo[1:3]), int(foo[3:5])).info()
            break
        except ValueError:
            print("{학년}{반}{번호} 형식으로 입력해주세요.")


if __name__ == '__main__':
    main()

