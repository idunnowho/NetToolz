import socket

def run_client():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = '127.0.0.1'
    server_port = 8000

    client.connect((server_ip, server_port))

    try:
        while True:
            # send messages 
            msg = input("Enter a message: ")
            client.send(msg.encode("utf-8")[:1024])

            # receive messages in english
            response = client.recv(1024)
            response = response.decode("utf-8")

            # check to see if server sent us closed
            if response.lower() == 'closed':
                break

            print(f"Received: {response}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # close client socket/connection
        client.close()
        print("Connection to server closed")

run_client()
             
