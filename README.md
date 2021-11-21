# code2pdf

将代码打印到一个pdf文件里，同时包含封面和目录。毕竟直接copy到word里再打印看起来太折磨了。

# Usage

将本仓库clone到你的电脑上，然后把代码放到仓库根目录下的sourses文件夹里，你可以通过修改代码文件的名称来修改输出文件中各段代码的标题。

# Dependencies

- python3.8+
- XeLatex
- 其他Tex支持，例如中文需要使用的CJK支持

如果你使用Ubuntu系统，你可以直接运行以下命令配置编译环境
`sudo apt install python3.8 texlive-full`

