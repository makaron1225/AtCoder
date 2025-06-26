import sys


def main():
    input = sys.stdin.readline  # 1行ずつ高速に読み込む
    N = int(input())
    A = list(map(int, input().split()))
    K = int(input())

    count = 0
    for a in A:
        if K <= a:
            count += 1
    print(count)


if __name__ == "__main__":
    main()