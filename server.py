import grpc
from concurrent import futures
import simpleServer_pb2
import simpleServer_pb2_grpc
import time
import threading
import queue

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class Server(simpleServer_pb2_grpc.SimpleServerServicer):

    def __init__(self):
        self.database = {}
        self.recv_request = queue.Queue(maxsize=-1)
        self.execute_request = queue.Queue(maxsize=-1)
        self.log_request = queue.Queue(maxsize=-1)
        self.send_response = queue.Queue(maxsize=-1)
        self.event = threading.Event()
        self.run()

    def loadDatabase(self):
        try:
            with open('logfile.txt', 'r') as log:
                print("LOADING DATABASE")
                for line in log:
                    self.executeLog(line.rstrip())
                print("SUCCEEDED!\n")
        except:
            pass
                    

    def executeLog(self, line):
        query = line.split()
        data = " ".join(map(str, query[2:])) if len(query) > 2 else ""
        if query[0] == "CREATE":
            self.create(int(query[1]), data)
        elif query[0] == "UPDATE":
            self.update(int(query[1]), data)
        elif query[0] == "DELETE":
            self.delete(int(query[1]))
        elif query[0] == "READ":
            pass
        else:
            print("Something went wrong restoring the log")



    """def Service(self, request, context):
        pipe = queue.Queue()
        response = simpleServer_pb2.SimpleServerResponse()
        self.recv_request.put((request, response))
        while not response.response:
            pass
        return response
"""
    def Service(self, request, context):
        marioPipe = queue.Queue()
        self.recv_request.put((request, marioPipe))
        response = marioPipe.get()
        del marioPipe
        return simpleServer_pb2.SimpleServerResponse(response=response)

    def transportRequest(self):
        while not self.event.is_set():
            if not self.recv_request.empty():
                request, response = self.recv_request.get()
                self.execute_request.put((request, response))
                self.log_request.put(request)

    def logRequest(self):
        while not self.event.is_set():
            if not self.log_request.empty():
                request = self.log_request.get()
                if not request.type == "READ":
                    logOutput = str(request.type) + " " + str(request.id) + " " + str(request.data) +"\n"
                    try:
                        with open("logfile.txt", "a") as log:
                            log.write(logOutput)
                    except:
                        pass

    def executeRequest(self):
        while not self.event.is_set():
            if not self.execute_request.empty():
                request, reply = self.execute_request.get()
                if request.type == "CREATE":
                    response = self.create(request.id, request.data)                
                elif request.type == "UPDATE":
                    response = self.update(request.id, request.data)
                elif request.type == "READ":
                    response = self.read(request.id)
                elif request.type == "DELETE":
                    response = self.delete(request.id)
                else:
                    response = "SERVIDOR: COMANDO NAO RECONHECIDO"
                try:
                    reply.put(response)
                except:
                    pass
                #return  simpleServer_pb2.SimpleServerResponse(response=response)

    def create(self, id, data):
        if not id in self.database:
            self.database[id] = data
            response = "SUCCEEDED: CREATED DATA <%s> WITH ID %d" % (data, id)
        else:
            response = "FAILED: THERE IS ALREADY AN ENTRY WITH ID %d" % id
        return response

    def update(self, id, data):
        if id in self.database:
            self.database[id] = data
            response = "SUCCEEDED: UPDATED ID %d WITH DATA <%s>" % (id, data)
        else:
            response = "FAILED: THERE IS NO ENTRY WITH ID %d" % id
        return response

    def read(self,id):
        if id in self.database:
            data = self.database[id]
            response = "SUCCEEDED: ENTRY WITH ID %d IS DATA <%s>" % (id, data)
        else:
            response = "FAILED: THERE IS NO ENTRY WITH ID %d" % id
        return response

    def delete(self, id):
        if id in self.database:
            data = self.database[id]
            del self.database[id]
            response = "SUCCEEDED: ENTRY WITH ID %d AND DATA <%s> WAS DELETED" % (id, data)
        else:
            response = "FAILED: THERE IS NO ENTRY WITH ID %d" % id
        return response

    def run(self):
        self.loadDatabase()

        transport_thread = threading.Thread(target=self.transportRequest)
        transport_thread.setDaemon(True)
        transport_thread.start()

        execute_thread = threading.Thread(target=self.executeRequest)
        execute_thread.setDaemon(True)
        execute_thread.start()

        log_thread = threading.Thread(target=self.logRequest)
        log_thread.setDaemon(True)
        log_thread.start()



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    o = Server()
    simpleServer_pb2_grpc.add_SimpleServerServicer_to_server(o, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("serving\n")
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        print("\nTerminated by admin\n")
        o.event.set()
        server.stop(0)

if __name__ == '__main__':
    serve()