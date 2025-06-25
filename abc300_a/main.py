def main():
    n, a, b = map(int, input().split())
    c = list(map(int, input().split()))
    target = a + b
    for i in range(n):
        if c[i] == target:
            print(i + 1)
            return


if __name__ == "__main__":
    main()
