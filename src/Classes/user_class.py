import csv

class User_Class:
    def __init__(self, Id=None, name=None, surname=None, email=None, tel=None, password=None, point=None):
        self.Id = Id
        self.name = name
        self.surname = surname
        self.email = email
        self.tel = tel
        self.password = password
        self.point = point
        
    def get_name(self):
        return self.name

    def appendUser(self):
        with open('DataCSV/user_data.csv', 'a', newline='') as f: # Write append the user data
            fw = csv.writer(f)
            fw.writerow([
                    self.Id,
                    self.name,
                    self.surname,
                    self.email,
                    self.tel,
                    self.password,
                    self.point
            ])
                        
    def readById(self, Id):
        select_user = 0
        with open('DataCSV/user_data.csv', newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
            for i in data:
                if i[0] == Id:
                    select_user = i
            
            self.Id = select_user[0]
            self.name = select_user[1] 
            self.surname = select_user[2]
            self.email = select_user[3]
            self.tel = select_user[4]
            self.password = select_user[5]
            self.point = select_user[6]
