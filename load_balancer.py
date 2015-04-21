SERVERS = ['APP1', 'APP2', 'APP3']
server_number = 0


def get_server():
    global server_number
    print SERVERS[server_number % len(SERVERS)]
    server_number += 1

## Testing the function
if __name__ == '__main__':
    for i in range(8):
        get_server()

