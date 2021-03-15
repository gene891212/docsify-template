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
    Get _sidebar.md and home.md's TOC automatic,
    please input the directory you want to ignore in 'IGNORE_DIRS'
    """

    def write(self, f, content):
        f.write(content + "\n")

    def main(self):
        with open('HOME.md') as f:
            pattern = r'[\s\S]*Table Of Contents'
            search = re.search(pattern, f.read())
            toc = search.group() if search else ""
        # self.write(sidebar, "* [Headline](HOME.md)")

        sidebar = open("_sidebar.md", "w")
        home = open("HOME.md", "w")
        self.write(home, toc)
        tree = os.walk("./", topdown=True)
        for root, dirs, files in tree:
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
            if root == "./":
                continue
            title = root.split("./")[-1].capitalize()
            self.write(home, TOC_TITLE.format(title))
            self.write(sidebar, TITLE.format(title))
            for file in sorted(files):
                subtitle = file[:-3].replace("_", " ").capitalize()
                path = f"{title}/{file}"
                self.write(home, TOC_LIST.format(subtitle, path))
                self.write(sidebar, SUBTITLE.format(subtitle, path))
        sidebar.close()
        home.close()


if __name__ == '__main__':
    hi = Generate()
    hi.main()
