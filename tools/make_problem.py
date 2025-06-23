import os
import sys

TEMPLATE = """\
def main():
    n = int(input())
    print(n)

if __name__ == "__main__":
    main()
"""


def create_problem_folder(problem_name):
    base_path = os.path.expanduser(f"~/AtCoder/{problem_name}")
    os.makedirs(base_path, exist_ok=True)

    main_path = os.path.join(base_path, "main.py")
    if not os.path.exists(main_path):
        with open(main_path, "w") as f:
            f.write(TEMPLATE)

    os.makedirs(os.path.join(base_path, "test"), exist_ok=True)
    print(f"✅ {problem_name} フォルダを作成しました")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("❗ 使い方: python make_problem.py abc123/A")
    else:
        create_problem_folder(sys.argv[1])
