import sys


def main():
    input = sys.stdin.readline  # 1行ずつ高速に読み込む
    P = input().strip()
    L = int(input())

    if len(P) >= L:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
