class User():
    def __init__(self, first_name, last_name,login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts
    def describe_user(self):
        print(f'{self.first_name} {self.last_name}')
    def greet_user(self):
        print( f'Hello {self.first_name} {self.last_name}!')
    def increment_login_attempts(self,tries=1):
        self.login_attempts += tries
    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name,privileges=[]):
        super().__init__(first_name,last_name)
        self.privileges = privileges
    def show_privileges(self):
        print(self.privileges)

class Privileges(Admin):
    Admin.show_privileges()

# Dmytro = User('Dmytro','Dmytro')
# Dmytro.describe_user()
# Dmytro.greet_user()
# Dmytro.increment_login_attempts()
# print(Dmytro.login_attempts)
# Dmytro.reset_login_attempts()
# print(Dmytro.login_attempts)

Natalia =  Admin(first_name='Natalia', last_name='Natalia', privileges=["«Allowed to add message»", "«Allowed to delete users»", "«Allowed to ban users»" ])
Natalia.show_privileges()
