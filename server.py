import socketserver

class ClientHandler(socketserver.BaseRequestHandler):
  
  def handle(self):
    encrypted_key = self.request.recv(1024).strip()
    print("Implement decryption of data " + encrypted_key )
    #
    #   Decryption Code Here
    #
    self.request.sendall("send key back")
if _name_ == "_main_":
  HOST, PORT = "", 1337
  
  tcpServer = socketserver.TCPServer((HOST, PORT), ClientHandler)
  try:
    tcpServer.serve_forever()
  except:
    print("There was an error")
