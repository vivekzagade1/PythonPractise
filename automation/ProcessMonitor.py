import psutil


def process_display():
    list_process = []

    for process in psutil.process_iter():
        try:
            process_info = process.as_dict(attrs=['pid', 'name', 'username'])
            process_info['vms'] = process.memory_info().vms / (1024 * 1024)
            list_process.append(process_info)

        except (psutil.NoSuchProcess, psutil.ZombieProcess, psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    return list_process


def main():
    print("Process Monitor")
    list_process = process_display()

    for element in list_process:
        print(element)


if __name__ == '__main__':
    main()
