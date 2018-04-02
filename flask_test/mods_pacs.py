# import arithmetic
# print arithmetic.add(5, 8)
# print arithmetic.subtract(10, 5)
# print arithmetic.multiply(12, 6)


# >>> import urllib
# >>> dir(urllib)
# ['ContentTooShortError', 'FancyURLopener', 'MAXFTPCACHE', 'URLopener', '__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '__version__', '_ftperrors', '_get_proxies', '_get_proxy_settings', '_have_ssl', '_hexdig', '_hextochr', '_hostprog', '_is_unicode', '_localhost', '_noheaders', '_nportprog', '_passwdprog', ...
# >>> help(urllib) # will return a listing of information on the given module


# sample_project
#      |_____ python_file.py
#      |_____ my_modules
#                |_____ __init__.py
#                |_____ test_module.py
#                |_____ another_module.py
#                |_____ third_module.py



# import my_modules.test_module
 

#  #or 

#  from my_modules import test_module





# __init__.py:
# __all__ = ["test_module"]


#*****************USERS**************************************************

# instantiate class User
class User(object):
    # this method to run every time a new object is instantiated
    def __init__(self, name, email):
	# instance attributes 
        self.name = name
        self.email = email
        self.logged = True
    # login method changes the logged status for a single instance (the instance calling the method)
    def login(self):
        self.logged = True
        print self.name + " is logged in."
        return self
    # logout method changes the logged status for a single instance (the instance calling the method)
    def logout(self):
        self.logged = False
        print self.name + " is not logged in"
        return self
    # print name and email of the calling instance
    def show(self):
        print "My name is {}. You can email me at {}".format(self.name, self.email)
        return self
email_name = ('hassan', 'hassanz246@yahoo.com')
print email_name




