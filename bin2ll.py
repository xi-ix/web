import struct
import sys

def bin_to_cpp_longlong(bin_file_path, cpp_file_path):
    """
    读取二进制文件，并将其内容转换为 C++ long long 格式的输出。

    Args:
        bin_file_path (str): 二进制文件的路径。
        cpp_file_path (str): C++ 输出文件的路径。
    """

    try:
        with open(bin_file_path, 'rb') as bin_file, open(cpp_file_path, 'w') as cpp_file:
            cpp_file.write("#include <iostream>\n")
            cpp_file.write("#include <vector>\n\n")
            cpp_file.write("int main() {\n")
            cpp_file.write("    std::vector<long long> data = {\n")

            first_element = True
            while True:
                # 尝试读取 8 个字节 (long long 的大小)
                chunk = bin_file.read(8)
                if not chunk:
                    break  # 文件结束

                # 解包为 long long (q 代表 signed long long,  可以使用 Q 代表 unsigned long long)
                value = struct.unpack('q', chunk)[0]

                if not first_element:
                    cpp_file.write(",\n")
                else:
                    first_element = False

                cpp_file.write(f"        {value}")

            cpp_file.write("\n    };\n")
            cpp_file.write("    for (long long val : data) {\n")
            cpp_file.write("        std::cout << val << std::endl;\n")
            cpp_file.write("    }\n")
            cpp_file.write("    return 0;\n")
            cpp_file.write("}\n")

        print(f"转换完成！C++ 代码已保存到: {cpp_file_path}")

    except FileNotFoundError:
        print(f"错误：文件未找到: {bin_file_path}")
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("用法: python script.py <input_bin_file> <output_cpp_file>")
    else:
        input_bin_file = sys.argv[1]
        output_cpp_file = sys.argv[2]
        bin_to_cpp_longlong(input_bin_file, output_cpp_file)
