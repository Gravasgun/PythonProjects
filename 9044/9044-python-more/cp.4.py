import sys
from shutil import copyfile

# 检查命令行参数个数是否为 3（程序名 + 输入文件名 + 输出文件名）
if len(sys.argv) != 3:
    print(f"Usage:{sys.argv[0]}  <infile> <outfile>")  # 提示正确用法
    sys.exit(1)  # 异常退出，状态码 1 表示错误

try:
    copyfile(sys.argv[1], sys.argv[2])
except OSError as e:
    print(f"{sys.argv[0]},error: {e}", file=sys.stderr)
    sys.exit(1) 