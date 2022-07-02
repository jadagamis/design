import psutil
import platform
import cpuinfo
import socket
import uuid
import re


def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


def get_system_info():
    all = []
    system_info = {"Platform": platform.system(),
                   "Platform-Release": platform.release(),
                   "Platform-Version": platform.version(),
                   "Architecture": platform.machine(),
                   "Hostname": socket.gethostname(),
                   "IP-Address": socket.gethostbyname(socket.gethostname()),
                   "AC-Address": ':'.join(re.findall('..', '%012x' % uuid.getnode())),
                   "Processor": platform.processor(),
                   "Processor-Brand": cpuinfo.get_cpu_info()['brand_raw']}

    # print CPU information
    all_cores = []
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        all_cores.append({f"Core {i}": f"{percentage} %"})
    cpu_info = {"Physical cores": psutil.cpu_count(logical=False),
                "Total cores": psutil.cpu_count(logical=True),
                "Total CPU Usage": f"{psutil.cpu_percent()}%",
                "CPU Usage Per Core": all_cores}

    # Memory Information
    svmem = psutil.virtual_memory()
    memory_info = {"Total": get_size(svmem.total),
                   "Available": get_size(svmem.available),
                   "Used": get_size(svmem.used),
                   "Percentage": f"{svmem.percent}%"}

    # Disk Information
    partitions = psutil.disk_partitions()
    all_partitions = []
    for partition in partitions:
        partition_usage = psutil.disk_usage(partition.mountpoint)
        all_partitions.append({"Device": partition.device,
                               "Mountpoint": partition.mountpoint,
                               "File system type": partition.fstype,
                               "Total Size": get_size(partition_usage.total),
                               "Used": get_size(partition_usage.used),
                               "Free": get_size(partition_usage.free),
                               "Percentage": f"{partition_usage.percent}%"
                               })

    disk_io = psutil.disk_io_counters()
    disk_info = {"Partitions and Usage": all_partitions,
                 "Total read": get_size(disk_io.read_bytes),
                 "Total write": get_size(disk_io.write_bytes)}

    net_io = psutil.net_io_counters()
    network_info = {"Total Bytes Sent": get_size(net_io.bytes_sent),
                    "Total Bytes Received": get_size(net_io.bytes_recv)}
    all.extend([system_info, cpu_info, memory_info, disk_info, network_info])
    return all


def display(all):
    parts = ["System Information", "CPU Info", "Memory Information", "Disk Information", "Network Information"]
    for i in range(0, 5):
        print("=" * 40, parts[i], "=" * 40)
        for key, value in all[i].items():
            if type(value) is list:
                for i in range(0, len(value)):
                    for k, v in value[i].items():
                        print(f"{k:20}{v}")
                    print("\n")
            else:
                print(f'{key:20}{value}')


case = get_system_info()
display(case)



