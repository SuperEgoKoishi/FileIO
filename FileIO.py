import os

if __name__ == '__main__':
    # 将文本写入文件
    text = "\nTexture to be written to the file"
    target_file = open("{}\\target_file.txt".format(os.path.dirname(__file__)), "a")
    target_file.write(text)
    target_file.close()

    # 读取文件内容并展示
    target_file = open("{}\\target_file.txt".format(os.path.dirname(__file__)), "r")
    content = target_file.read()
    print(content)
    target_file.close()
