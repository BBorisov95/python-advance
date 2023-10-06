import os.path

while True:
    user_input = input()
    if user_input == 'End':
        break

    commands, file_name, *args = user_input.split('-')

    if commands == 'Create':
        open(file_name, 'w').close()
    elif commands == 'Add':
        with open(file_name, 'a') as f:
            f.write(f'{args[0]}\n')
    elif commands == 'Replace':
        try:
            with open(file_name, 'r') as f:
                content = f.read()
        except FileNotFoundError:
            print('An error occurred')
        else:
            with open(file_name, 'w') as f:
                content = content.replace(args[0], args[1])
                f.write(content)
    elif commands == 'Delete':
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print('An error occurred')

