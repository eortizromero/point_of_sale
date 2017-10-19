# coding: latin1

class DatabaseManager(object):
    def __init__(self):
        print "DatabaseManager"
        pass

    def login(self, username, password):
        self.username = username
        self.password = password

        if self.username == 'admin':
            print self.username
        elif self.password == 'admin':
            print self.password

        return True
