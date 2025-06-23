import sys

def main():
    input = sys.stdin.readline  # 1行ずつ高速に読み込む
    N = int(input())
    A = list(map(int, input().split()))
    print(sum(A))

if __name__ == "__main__":
    main()