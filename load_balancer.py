import Computer1, Computer2, Computer3

SERVERS = [Computer1, Computer2, Computer3]
server_number = -1


def get_server():
    global server_number
    server_number += 1
    return SERVERS[server_number % len(SERVERS)]

## Testing the function
if __name__ == '__main__':
    from random import randint

    for i in range(13):
        x = randint(5, 99)
        y = randint(5, 99)

        server = get_server()

        print server.print_name()
        print server.multiply_handler(x, y); lmh = str(server.last_multiplied_handler())
        print lmh
        print "-"*len(lmh) + "\n"

