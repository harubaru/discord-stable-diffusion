try:
    file_path = 'venv\\lib\\site-packages\\torch\\distributed\\elastic\\timer\\file_based_local_timer.py'
    with open(file_path, 'r+') as file:
        old = file.read()
        if 'SIGKILL' not in old:
            print(file_path + ' already patched!')
            exit(0)
        file.seek(0)
        file.write(old.replace('SIGKILL', 'SIGINT'))
    print('Patched ' + file_path)
except Exception as e:
    print('Patch failed! Please report this either on github or to salt#7234\nReason: ' + str(e))
