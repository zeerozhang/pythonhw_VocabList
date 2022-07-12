## README

### 项目说明
本项目用于根据用户提供的生词本（如 `./example.txt` ）生成复习所用的单词本。

### 使用方法
* 用户需首先安装pygtrans拓展包。安装指令为：**pip3 install pygtrans**
* 用户需能访问**谷歌翻译**网站

```Python
1. 用户可先输入形如“words.txt“的待复习单词表
2. -n 表示用户希望从自己所选择范围内具体想要抽取的行数（由于有空行，该数值并不代表抽中的单词数量）
3. --r 表示用户希望随机选择单词（不输入 --r 则表示不希望随机选择）
4. -s 表示用户希望从第几个单词开始
5. -l 表示用户希望复习的单词范围大小，也即从 start 开始，长度为 length
```

  例如：`python3 selector.py example.txt -n 100 --r -s 20 -l 200` 表示希望从生词本的第 20 个单词开始到第 220 个单词结束的范围内随机抽取 100 个生词生成生词本。

生词本存放于 `./vocabulary` 路径下，含有带谷歌翻译（with_tran.txt）和不带翻译（no_trans.txt）两种。旧的生词本不会被新生成的生词本覆盖。

### 功能演示
* **输入**：python3 solve.py TOFEL_listening.txt --r -n 50
   **输出**：no_trans.txt，with_trans.txt，二者单词顺序对应，为在全部单词中随机抽选50行。
* **输入**：python3 solve.py TOFEL_listening.txt -n 40 --r -s 10 -l 100
   **输出**：no_trans_0.txt，with_trans_0.txt，二者单词顺序对应，为在10至110行单词中随机抽选40行。
