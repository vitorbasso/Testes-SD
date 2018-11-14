import grpc
import simpleServer_pb2
import simpleServer_pb2_grpc
from concurrent import futures
import threading
import queue
import time
import tkinter as tk

class Client:

    def __init__(self):
        self.event = threading.Event()
        self.display_queue = queue.Queue(maxsize=-1)
        self.top = tk.Tk()
        self.top.title("Client")

        self.instructions = ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
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

        self.instruction1 = "                 "
        self.instruction2 = "                     INSTRUCTIONS:                     "
        self.instruction3 = "                                                      "
        self.instruction4 = "    * To insert a new value type CREATE <id> <value>   "
        self.instruction5 = "                                                       "
        self.instruction6 = "    * To modify a value type UPDATE <id> <value>       "
        self.instruction7 = "                                                       "
        self.instruction8 = "    * To read a value type READ <id>                   "
        self.instruction9 = "                                                       "
        self.instruction10 = "    * To remove a value type DELETE <id>               "
        self.instruction11 = "                                                       "
        self.instruction12 = "    * To close type '#quit'                            "
        self.instruction13 = "                                                       "

        self.messages_frame = tk.Frame(self.top)
        self.my_msg = tk.StringVar()
        self.my_msg.set("")
        self.instruction_list= tk.Listbox(self.messages_frame, height=15, width=100, bg="grey")
        self.instruction_list.pack(side=tk.TOP)
        self.instruction_list.pack()
        self.instruction_list.insert(tk.END, self.instruction1)
        self.instruction_list.insert(tk.END, self.instruction2)
        self.instruction_list.insert(tk.END, self.instruction3)
        self.instruction_list.insert(tk.END, self.instruction4)
        self.instruction_list.insert(tk.END, self.instruction5)
        self.instruction_list.insert(tk.END, self.instruction6)
        self.instruction_list.insert(tk.END, self.instruction7)
        self.instruction_list.insert(tk.END, self.instruction8)
        self.instruction_list.insert(tk.END, self.instruction9)
        self.instruction_list.insert(tk.END, self.instruction10)
        self.instruction_list.insert(tk.END, self.instruction11)
        self.instruction_list.insert(tk.END, self.instruction12)
        self.instruction_list.insert(tk.END, self.instruction13)
        scrollbar = tk.Scrollbar(self.messages_frame)
        self.msg_list = tk.Listbox(self.messages_frame, height=15, width=100, yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.msg_list.pack(side=tk.LEFT, fill=tk.BOTH)
        self.msg_list.pack()
        self.messages_frame.pack()

        self.entry_field = tk.Entry(self.top, textvariable=self.my_msg)
        self.entry_field.bind("<Return>", self.request)
        self.entry_field.pack()
        self.send_button = tk.Button(self.top, text="Send", command=self.request)
        self.send_button.pack()

        self.top.protocol("WM_DELETE_WINDOW", self.on_closing)

    
    def request(self, garbage = ""):
        self.print_instructions()
        request = self.my_msg.get()
        self.my_msg.set("")
        request = request.split()
        if self.is_valid(request):
            self.display_queue.put(request)
        elif request[0] == "#quit":
            self.event.set()
            time.sleep(5)
            self.top.quit()
        else:
            print("CLIENTE: COMANDO INVALIDO")
            self.my_list.insert(tk.END, "CLIENTE: COMANDO INVALIDO")
            self.my_list.see(tk.END)

    def on_closing(self):
        self.my_msg.set("#quit")
        self.request()

    def is_valid(self, request):
        if len(request) > 1:
            if request[0] == "CREATE" or request[0] == "UPDATE" or request[0] == "READ" or request[0] == "DELETE":
                if request[1].isdigit():
                    if (request[0] == "READ" or request[0] == "DELETE") and len(request) != 2:
                        return False
                    return True
        return False
            

    def display(self):
        while True:
            if not self.display_queue.empty():
                request = self.display_queue.get()
                tipo = request[0]
                id = int(request[1])
                data = " ".join(map(str, request[2:])) if len(request) > 2 else ""
                response = self.stub.Service(simpleServer_pb2.SimpleServerRequest(type=tipo, id=id, data=data)).response
                if (tipo == "CREATE" or tipo == "UPDATE"):
                    msg = "ANSWER FOR REQUISITION '%s %d <%s>':" % (tipo, id, data)
                elif (tipo == "READ" or tipo == "DELETE"):
                    msg = "ANSWER FOR REQUISITION '%s %d':" % (tipo, id)
                print(msg + response)
                self.msg_list.insert(tk.END, msg + response)
                self.msg_list.see(tk.END)

    def print_instructions(self):

        print(self.instructions)
    
    def start(self):
        channel = grpc.insecure_channel('localhost:50051')
        self.stub = simpleServer_pb2_grpc.SimpleServerStub(channel)
        display_thread = threading.Thread(target=self.display)
        display_thread.setDaemon(True)
        display_thread.start()

        tk.mainloop()


if __name__ == '__main__':
    client = Client()
    client.start()