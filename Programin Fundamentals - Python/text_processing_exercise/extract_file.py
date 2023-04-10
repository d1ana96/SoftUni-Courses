path_file = input()

path_file_args = path_file.split("\\")
path_name_with_extension = path_file_args[-1]

path_name_parts = path_name_with_extension.split(".")
extension = path_name_parts.pop()
print(f'File name: {".".join(path_name_parts)}')
print(f'File extension: {extension}')
