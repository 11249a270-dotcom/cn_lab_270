import socket


def file_transfer_server():
    server_socket = None

    try:
        # 1. Create TCP socket
        server_socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        # 2. Prevent address reuse error
        server_socket.setsockopt(
            socket.SOL_SOCKET,
            socket.SO_REUSEADDR,
            1
        )

        # 3. Bind to localhost and port
        server_socket.bind(("127.0.0.1", 12345))

        # 4. Listen for connections
        server_socket.listen(1)

        print("Server listening on port 12345...")

        # 5. Accept connection
        connection, client_address = server_socket.accept()

        print(f"Connected by {client_address}")

        # 6. Receive filename
        filename = connection.recv(1024).decode()

        print(f"Receiving file: {filename}")

        # 7. Open file in binary write mode
        with open(f"received_{filename}", "wb") as file:
            while True:
                data = connection.recv(1024)

                if not data:
                    break

                file.write(data)

        print(f"File saved as received_{filename}")

        # 8. Close client connection
        connection.close()

    except Exception as e:
        print("Error:", e)

    finally:
        # 9. Close server socket
        if server_socket:
            server_socket.close()


if __name__ == "__main__":
    file_transfer_server()
