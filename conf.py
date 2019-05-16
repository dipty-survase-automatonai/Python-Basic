#!/usr/bin/python
import io
config_file_handle = io.FileIO("audio.conf")
line = ' '
result = {}
while line != b"":
    line = config_file_handle.readline()    
	if not line.startswith(b'#'):
        #print(line)
        if b'=' in line or b':' in line:
            line = line[:-1]
            print(line)
            key_value = line.split(b'=')
            
            if 1 == len(key_value):
                key_value = line.split(b':')
            print(key_value)
            if b'#' in key_value[1]:
                key_value[1] = key_value[1].split(b'#')[0]
            result[key_value[0]] = key_value[1]
            
print(result)
