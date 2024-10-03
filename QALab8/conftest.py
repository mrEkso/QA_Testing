import subprocess
import paramiko
import pytest

server_ip = '192.168.56.10'
username = 'main'
password = 'root'

@pytest.fixture(scope='function')
def server():
    try:
        # SSH connection setup
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(server_ip, username=username, password=password)

        # Start iperf server
        stdin, stdout, stderr = ssh_client.exec_command('iperf3 -s')

        yield ''.join(stderr.readlines())

    finally:
        # Close SSH connection
        ssh_client.close()


@pytest.fixture(scope='function')
def client(server):
    try:
        # Connect to the server and execute iperf client command
        command = f'iperf3 -c {server_ip}'
        process = subprocess.Popen(command, shell=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

        yield output.decode(), error.decode()

    except Exception as e:
        # Handle connection or command execution errors
        yield None, str(e)
