import sys
import os

# configuration
title = "Code Templates"
author = "Your Name"

# 各级文件夹对应的目录等级
level_map = {1: "section",
             2: "subsection",
             3: "subsubsection"}
source_dir = "./sources"

stdout0 = sys.stdout  # 备份stdout


def open_file_and_redirect_stdout():
    global stdout0
    stdout0 = sys.stdout
    if not os.path.isdir("./.temp"):
        os.mkdir("./.temp")
    sys.stdout = open("./.temp/code.tex", "w", encoding='utf-8')


def close_file_and_recover_stdout():
    global stdout0
    sys.stdout.close()
    sys.stdout = stdout0


def add_preset():
    print(r"% 声明文章类型")
    print(r"\documentclass[UTF8]{article}")
    print()

    print(r"% 声明使用包")
    print(r"\usepackage{ctex}")  # 中文支持
    print(r"\usepackage{listings}")  # 代码环境支持
    print(r"\usepackage{xcolor}")  # 修改颜色使用
    print()

    print(r"% 声明颜色")
    print(r"\definecolor{dkgreen}{rgb}{0,0.6,0}")
    print(r"\definecolor{gray}{rgb}{0.5,0.5,0.5}")
    print(r"\definecolor{mauve}{rgb}{0.58,0,0.82}")
    print()

    print(r"% 设置代码高亮颜色", end="")
    print(r"""
\lstset{
    frame=leftline, 
    aboveskip=3mm,
    belowskip=3mm,
    showstringspaces=false,
    columns=flexible,
    framerule=1pt,
    rulecolor=\color{gray!35},
    backgroundcolor=\color{white},
    basicstyle={\small\ttfamily},
    numbers=left,
    numberstyle=\tiny\color{gray}\tt,
    keywordstyle=\color{blue},
    commentstyle=\color{dkgreen},
    stringstyle=\color{mauve},
    breaklines=true,
    breakatwhitespace=true,
    tabsize=4,
}
    """)

    print(r"% 论文信息")
    print(r"\title{" + title + "}")
    print(r"\author{" + author + "}")
    print()


def add_beginning():
    print(r"\pagestyle{empty}")
    print(r"% 生成首页")
    print(r"\maketitle")
    print(r"\thispagestyle{empty}")
    print(r"\newpage")
    print(r"% 生成目录")
    print(r"\tableofcontents")
    print(r"\newpage")
    print("")
    print(r"%正文开始")
    print(r"%\pagestyle{plain}")
    print(r"\setcounter{page}{1}")


def code2latex(path):
    file_ext = os.path.splitext(os.path.basename(path))[1]
    if file_ext == ".cpp":
        lang = "c++"
    elif file_ext == ".c":
        lang = "c"
    elif file_ext == ".py":
        lang = "python"
    elif file_ext == ".m":
        lang = "matlab"
    else:
        raise Exception("no fucking language.")
    print(r"\begin{lstlisting}[language=" + lang + "]")
    with open(path, "r", encoding="utf-8") as file:
        tot = file.readlines()
        for i in tot:
            print(i, end="")
    print(r"\end{lstlisting}")


def add_main_body(root=source_dir, level=1):
    dirs = []
    files = []
    for path in os.listdir(root):
        path = os.path.join(root, path)
        if os.path.isdir(path):
            dirs.append(path)
        elif os.path.isfile(path):
            files.append(path)
    dirs = sorted(dirs)
    files = sorted(files)
    for path in dirs:
        dir_name = os.path.basename(path)
        print("\\" + level_map[level] + "{" + dir_name + "}")
        add_main_body(path, level + 1)
    for path in files:
        file_name = os.path.splitext(os.path.basename(path))[0]
        print("\\" + level_map[level] + "{" + file_name + "}")
        code2latex(path)


if __name__ == '__main__':
    open_file_and_redirect_stdout()

    add_preset()

    print(r"\begin{document}")

    add_beginning()
    add_main_body()

    print(r"\end{document}")
    close_file_and_recover_stdout()
