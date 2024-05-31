def append_data_to_exe(input_exe, output_exe, data_file=None, padding_size=0):
    with open(input_exe, 'rb') as exe_file:
        exe_content = exe_file.read()
    
    if data_file:
        with open(data_file, 'rb') as data_file:
            data_content = data_file.read()
    else:
        data_content = b'\x00' * padding_size

    with open(output_exe, 'wb') as out_file:
        out_file.write(exe_content + data_content)
        

append_data_to_exe('mini-exe.exe', 'big-exe.exe', padding_size=800 * 1024 * 1024) # 800 MB * 1024 * 1024
