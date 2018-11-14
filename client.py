import grpc
import simpleServer_pb2
import simpleServer_pb2_grpc
from concurrent import futures
import threading
import queue
import time

class Client:

    def __init__(self):
        self.event = threading.Event()
        self.display_queue = queue.Queue(maxsize=-1)
    
    def request(self):
        while not self.event.is_set():
            self.print_instructions()
            request = input("Request: ")
            request = request.split()
            if self.is_valid(request):
                self.display_queue.put(request)
            elif request[0] == "#quit":
                self.event.set()
                break
            else:
                print("CLIENTE: COMANDO INVALIDO")

    def is_valid(self, request):
        if len(request) > 1:
            if request[0] == "CREATE" or request[0] == "UPDATE" or request[0] == "READ" or request[0] == "DELETE":
                if request[1].isdigit():
                    if (request[0] == "READ" or request[0] == "DELETE") and len(request) != 2:
                        return False
                    return True
        return False
            

    def display(self):
        while not self.event.is_set():
            if not self.display_queue.empty():
                request = self.display_queue.get()
                tipo = request[0]
                id = int(request[1])
                data = " ".join(map(str, request[2:])) if len(request) > 2 else ""
                response = self.stub.Service(simpleServer_pb2.SimpleServerRequest(type=tipo, id=id, data=data)).response
                if (tipo == "CREATE" or tipo == "UPDATE"):
                    msg = "\nANSWER FOR REQUISITION '%s %d <%s>':\n" % (tipo, id, data)
                elif (tipo == "READ" or tipo == "DELETE"):
                    msg = "\nANSWER FOR REQUISITION '%s %d':\n" % (tipo, id)
                print(msg + response)

    def print_instructions(self):

        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
              "~                     INSTRUCTIONS:                     ~\n"
              "~                                                       ~\n"
              "~    * To insert a new value type CREATE <id> <value>   ~\n"
              "~                                                       ~\n"
              "~    * To modify a value type UPDATE <id> <value>       ~\n"
              "~                                                       ~\n"
              "~    * To read a value type READ <id>                   ~\n"
              "~                                                       ~\n"
              "~    * To remove a value type DELETE <id>               ~\n"
              "~                                                       ~\n"
              "~    * To close type '#quit'                            ~\n"
              "~                                                       ~\n"
              "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    
    def start(self):
        channel = grpc.insecure_channel('localhost:50051')
        self.stub = simpleServer_pb2_grpc.SimpleServerStub(channel)

        self.request_thread = threading.Thread(target=self.request)
        self.request_thread.setDaemon(True)
        self.request_thread.start()

        try:
            self.display()
        except KeyboardInterrupt:
            print("\nTerminado pelo usuario\n")
        self.display()
        print("\nClosing...\n")
        time.sleep(5)
        self.event.set()


if __name__ == '__main__':
    client = Client()
    client.start()