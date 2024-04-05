class Star_Cinema:
    def __init__(self):
        self._Hall_List = []
    
    def entry_hall(self, hall):
        self._Hall_List.append(hall)
    def show_hall(self):
        i=1
        for hall in self._Hall_List:
            print(f"Id of hall {i}: ",hall.hall_no)
            i+=1

class Hall(Star_Cinema) :
    def __init__(self,hall_no,rows,cols):
        self.hall_no = hall_no 
        self._show_list = []
        self._seats = {}
        self.rows = rows
        self.cols= cols
        super().__init__()
        self.entry_hall(self)
    
    def entry_show(self, show_id, movie_name, time, date):
        info = (show_id,movie_name,time, date)
        self._show_list.append(info)
    
    def seat_management(self,show_id):
        
        st_arr = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(0)
            st_arr.append(row)

        self._seats[show_id] = st_arr

    def view_show_list(self):
        
        for show in self._show_list:
            print(f'Show ID: {show[0]}, Movie Name: {show[1]}, Time: {show[2]},Date: {show[3]}')

    def view_available_seats(self, show_id):
        found = False
        for show in self._show_list :
            if show_id == show[0]:
                found = True
                break 
        if found == False :
            print("Invalid Show ID")
            return 

        st_available = self._seats[show_id]
        for row in st_available :
            print(row)

    def book_seats(self, show_id, seat_pos):
        found = False
        for show in self._show_list :
            if show_id == show[0]:
                found = True
                break 
        if found == False :
            print("Invalid Show ID")
            return 

        for pos in seat_pos :
            if (pos[0]<1 or pos[0]>self.rows) or (pos[1]<0 or pos[1]>self.cols):
                print("This is Invalid seat position ")
            else :
                st_available = self._seats[show_id]
                st_available[pos[0]][pos[1]]=1

hall1 = Hall(101,5,5)
hall1.entry_show(10,'Jawan','1.00-4.00','20-03-2024')
hall1.seat_management(10)
hall1.entry_show(11,'Pathan','5.00-8.00','20-03-2024')
hall1.seat_management(11)

hall2 = Hall(201,5,5)
hall2.entry_show(20,'Endgame','1.00-4.00','20-03-2024')
hall2.seat_management(20)
hall2.entry_show(21,'Loki','5.00-8.00','20-03-2024')
hall2.seat_management(21)

cinema = Star_Cinema();
cinema.entry_hall(hall1)
cinema.entry_hall(hall2)

while True :
    print(("\n-------------------------------"))
    print("1.View Hall list")
    print("2.View all show today")
    print("3.View available seats")
    print("4.Book Ticket")
    print("5.Exit")

    n = int(input("Enter Option : "))
    print("----------------------------")
    
    if n==1 :
        cinema.show_hall()

    if n==2 :
        hid = int(input("Enter hall id : "))
        if hid==101 :
            hall1.view_show_list()
        elif hid==201 :
            hall2.view_show_list() 
        else :
            print("Invalid Hall ID") 

    if n==3 :
        hid = int(input("Enter hall id : "))
        sid = int(input("Enter show id : "))
        if hid==101:
            hall1.view_available_seats(sid)
        elif hid==201:
            hall2.view_available_seats(sid)
        else :
            print("Invalid Hall ID")

    if n==4 :
        hid = int(input("Enter hall id : "))
        sid = int(input("Enter show id : "))
        tn = int(input("Number of ticket : "))
        pos = []
        for i in range(tn):
            lst = []
            row = int(input("Enter row : "))
            col = int(input("Enter column "))
            lst.append(row)
            lst.append(col)
            pos.append(lst)
        if hid == 101 :
            hall1.book_seats(sid,pos)
        elif hid ==201:
            hall2.book_seats(sid,pos)
        else :
            print("Invalid Hall ID")
    if n==5 :
        break 
        