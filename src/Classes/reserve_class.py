import csv

class Reserve_Class:
    def __init__(self, userId=None, RoomNumber=None, r_start=None, r_end=None, period=None, n_adult=None, n_children=None, add_on=None, total_price=None, status=True):
        self.reserve_Id = self.gen_Id()
        self.userId = userId
        self.RoomNumber = RoomNumber
        self.r_start = r_start
        self.r_end = r_end
        self.period = period
        self.n_adult = n_adult
        self.n_children = n_children
        self.add_on = add_on
        self.total_price = total_price
        self.status = status
        
    def cal_price(self):
        price = 0
        price = self.period * 40
        
        if self.add_on[0]:
            price = price + (7 * self.period)
        if self.add_on[1]:
            price = price + 12
        if self.add_on[2]:
            price = price + (20 * self.period)
        if self.add_on[3]:
            price = price + 9
        if self.add_on[4]:
            price = price + 5
        
        self.total_price = price

    def get_total_price(self):
        return self.total_price
        
    def gen_Id(self):
        with open('DataCSV/reservation_data.csv', newline='') as f: # open user_data.csv to read latest user
                        reader = csv.reader(f)
                        data = list(reader)
                        # print(data)
                        ID = int(data[-1][0])+1
        return ID
    
    def appendReserve(self):
        with open('DataCSV/reservation_data.csv', 'a', newline='') as f: 
            fw = csv.writer(f)
            fw.writerow([
                self.reserve_Id,
                self.userId,
                self.RoomNumber,
                self.r_start,
                self.r_end,
                self.period,
                self.n_adult,
                self.n_children,
                self.add_on,
                str(self.total_price),
                self.status
            ])
        
    
    
