import psutil

running_process = psutil.process_iter(attrs=['pid', 'name', 'status'])

for process in running_process:
    process_info=process.info
    pid=process_info['pid']
    name=process_info['name']
    status=process_info['status']

    print(f"PID: {pid}, Name: {name}, Status: {status}")