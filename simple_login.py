class User:
    # User class with login_id and login_pwd
    def __init__(self, login_id, login_pwd):
        self.login_id = login_id
        self.login_pwd = login_pwd
    
    # Returns True if the user exists in the database 
    def check_user(self):
        with open('./users.txt', 'r') as f:
            user_list = f.readlines()
            id_list = []
            for user in user_list:
                id_list.append(user.split(',')[0])
            # print(id_list)
            if self.login_id in id_list:
                return True
            else:
                return False
    
    # Returns True if log in succeeds. It assumes that the user is confirmed to exist in db.
    def log_in(self):
        with open('./users.txt', 'r') as f:
            user_list = f.readlines()
            for user in user_list:
                if self.login_id == user.split(',')[0]:
                    if self.login_pwd == user.split(',')[1].split('\n')[0]:
                        return True
                    else:
                        return False
        return False
                    
def main():
    while(True):
        login_prompt = input("1 for Login, 2 for Create an account\n")
        if login_prompt == '1':
            login_id = input("ID/Email: ")
            login_pwd = input("Password: ")
            current_user = User(login_id, login_pwd)
            if current_user.check_user() == True:
                print("Logging in...\n")
                if current_user.log_in() == True:
                    print("Login Success.\n")
                else:
                    print("Login failed. Please try again.\n")
            else:
                print("Login failed. Please try again.\n")

        elif login_prompt == '2':
            new_id = input("New ID/Email: ")
            new_pwd = input("New Password: ")
            new_user = User(new_id, new_pwd)
            with open('./users.txt', 'a') as f:
                f.write(new_user.login_id + "," + new_user.login_pwd + "\n")
            print(new_user.login_id, new_user.login_pwd)
        else: 
            print("Please only prompt 1 or 2 for the option")
            with open('./users.txt', 'r') as f:
                all = f.readlines()
                print(all)

if __name__ == '__main__':
    main()