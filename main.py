import os
import argparse

def main():
    parser = argparse.ArgumentParser(description="CLI for directory generation prompt .")
    parser.add_argument('-d', '--dirName', type=str, required=True, help='directory for story generation.')
    args = parser.parse_args()
    if not args.dirName:
        parser.error('The --dirName argument is required.')
    dir_name=args.dirName
    print(dir_name)

    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


if __name__ == "__main__":
    main()