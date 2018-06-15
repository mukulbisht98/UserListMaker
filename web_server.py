from http.server import HTTPServer , BaseHTTPRequestHandler
from socketserver import TCPServer
import cgi
# import CRUD Operations from Lesson 1 ##
from database_setup import Base, Users
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create session and connect to DB ##
engine = create_engine('sqlite:///users.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

main_page = str(open('template.html','r').read().replace('\n','').replace('\t',''))

add_user = str(open('NewUserTemplate.html','r').read().replace('\n','').replace('\t',''))


class webServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:

            if self.path.endswith("/"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write("<p>open <a href='/users'>localhost:8080/users</a> to access the users list.</p>".encode())
                return

            if self.path.endswith("/users"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                users = session.query(Users).all()
                content = ''
                output = ""
                for user in users:
                    output += "<li class = 'list'>"+str(user.id)+" "+user.name+"<br><a href='/users/"+str(user.id)+"/edit'" +  """onclick = "return confirm('are you sure?')" """+">Edit</a> <a href='/users/"+str(user.id)+"/delete'"+"""onclick = "return confirm('are you sure?')" """+"><span style='color: red;'>Delete</span></a></li>"
                content = main_page.format(list_of_users=output)
                self.wfile.write(content.encode())
                outfile = open('userList.html','w')
                outfile.write(content)
                outfile.close()
                return

            if self.path.endswith('/users/new'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ''
                output +=add_user
                self.wfile.write(output.encode())

            if self.path.endswith('/delete'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                print("delete")
                print(self.path)
                path = self.path.split('/')[2]
                print(path)
                session.delete(session.query(Users).filter_by(id = int(path)).one())
                session.commit()
                self.send_header('Location', '/users')
                self.end_headers()

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        try:
            if self.path.endswith('/users/new'):
                ctype, pdict = cgi.parse_header(self.headers['content-type'])
                pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    Uname = fields.get('username')
                    print(Uname)
                    # Create new user Object
                    newUser = Users(name = Uname[0].decode("utf-8"))
                    session.add(newUser)
                    session.commit()
                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/users')
                    self.end_headers()
        except:
            print("error in post")

def main():
    try:
        server =  HTTPServer(('', 8080), webServerHandler)
        print ('Web server running.. open localhost:8080/users in your browser')
        server.serve_forever()
    except KeyboardInterrupt:
        print (' received, shutting down server')
        server.socket.close()


if __name__ == '__main__':
    main()
