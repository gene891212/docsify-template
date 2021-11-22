import os
import re

TITLE = "* {}"
SUBTITLE = "    * [{}]({})"
TOC_TITLE = "\n### {}\n"
TOC_LIST = "* [{}]({})"
IGNORE_DIRS = [
    ".git",
    "static",
]


class Generate():
    """
    Get _sidebar.md and home.md's TOC automatic.
    Input the directory you want to ignore in 'IGNORE_DIRS'
    """

    def write(self, f, content):
        f.write(content + "\n")

    def main(self):
        sidebar = open("_sidebar.md", "w")
        tree = os.walk("./", topdown=True)
        for root, dirs, files in tree:
            dirs[:] = sorted([d for d in dirs if d not in IGNORE_DIRS])
            print(dirs)
            if root == "./":
                continue
            title = root.split("./")[-1]
            self.write(sidebar, TITLE.format(title.capitalize()))
            for file in sorted(files):
                subtitle = file[:-3].replace("_", " ").capitalize()
                path = f"{title}/{file}"
                self.write(sidebar, SUBTITLE.format(subtitle, path))
        sidebar.close()


if __name__ == '__main__':
    hi = Generate()
    hi.main()
