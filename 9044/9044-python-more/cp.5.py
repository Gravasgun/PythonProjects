import sys
import subprocess  # 导入 subprocess 模块，用于调用外部命令

# 检查命令行参数个数是否为 3（程序名 + 输入文件名 + 输出文件名）
if len(sys.argv) != 3:
    print(f"Usage:{sys.argv[0]}  <infile> <outfile>")  # 提示正确用法
    sys.exit(1)  # 异常退出，状态码 1 表示错误

# 使用 subprocess.run() 执行 cp 命令，参数必须以列表形式传入
p = subprocess.run(["cp", sys.argv[1], sys.argv[2]])

# 以 cp 命令的返回码作为当前程序的退出码
sys.exit(p.returncode)
