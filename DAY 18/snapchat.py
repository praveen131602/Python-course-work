class Snapchat:
    def __init__(self, username, password, friends):
        self.username = username      # public
        self.__password = password    # private
        self._friends = friends       # protected

    def getpassword(self):
        return self.__password

    def setpassword(self, new_password):
        self.__password = new_password

    @property
    def oprFriends(self):
        return self._friends

    @oprFriends.setter
    def operFriends(self,newfriend):
        self._friends.append(newfriend)
        


saaketh = Snapchat('saaketh', '12345', ['praveen', 'nikhil'])

print(f'Name before modification: {saaketh.username}')
saaketh.username = 'sapnil'
print(f'Name after modification: {saaketh.username}')

print(f'Password before modification: {saaketh.getpassword()}')
saaketh.setpassword('S@123')
print(f'Password after modification: {saaketh.getpassword()}')

print(f'Friends before modification:{saaketh.operFriends}')
saaketh.operFriends = 'abhinandhan'
print(f'Friends before modification:{saaketh.operFriends}')

