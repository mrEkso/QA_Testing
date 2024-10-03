import subprocess
import re

# Підключення до сервера
def client(server_ip):
    command = f"iperf3 -c {server_ip}"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result, error = process.communicate()

    return result, error

# Парсинг виводу iperf на клієнті
def parser(output):
    intervals = []
    lines = output.splitlines()
    for line in lines:
        interval_match = re.search(r'([\d.]+-[\d.]+)\s+sec\s+([\d.]+\s+\w?Bytes)\s+([\d.]+\s+\w?bits/sec)\s+([\d.]+)\s+([\d.]+\s+\w?Bytes)', line)
        if interval_match:
            interval_data = {
                'Interval': interval_match.group(1),
                'Transfer': interval_match.group(2),
                'Bitrate': interval_match.group(3),
                'Retr': interval_match.group(4),
                'Cwnd': interval_match.group(5)
            }
            intervals.append(interval_data)

    return intervals

# IP-адреса iperf3 сервера
server_ip = '192.168.56.10'
result, error = client(server_ip)

if error:
    print(f"Error occurred: {error.decode('utf-8')}")
else:
    result_list = parser(result.decode('utf-8'))
    for value in result_list:
        transfer = float(str(value['Transfer']).split(' ')[0])
        bitrate = float(str(value['Bitrate']).split(' ')[0])
        if transfer > 1 and bitrate > 1:
            print(value)
