import _sqlite3 as lite

#functionality
class DatabaseManage(object):

    def __init__(self):
        global con
        try:
            con = lite.connect('courses.db')
            with con:
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS courses(Id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, price TEXT, is_private BOOLEAN NOT NULL DEFAULT 1)")
        except Exception:
            print("unable to create a DB! ...")

    #create data
    def insert_data(self, data):
        try:
            with con:
                cur = con.cursor()
                cur.execute(
                "INSERT INTO courses(name, description, price, is_private) VALUES(?,?,?,?)", data
                        )
                return  True
        except Exception:
            return False

    #fetch data
    def fetch_data(self):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM courses")
                return cur.fetchall()
        except Exception:
            return  False

    #delete data
    def delete_data(self, id):
        try:
            with con:
                cur = con.cursor()
                sql = "DELETE FROM courses WHERE id = ?"
                cur.execute((sql, [id]))
                return True
        except Exception:
            return False



#TODO interface to user
def main():
    print("*"*40)
    print("\n:: COURSE MANAGEMENT :: \n")
    print("*"*40)
    print("\n")

    db = DatabaseManage()

    print("#"*40)
    print("User Manual :: \n")
    print("#" * 40)

    print('\nPress 1. Insert a new Course\n')
    print('\nPress 2. Show all courses\n')
    print('\nPress 3. Delete a course (NEED OF COURSE)\n')
    print("*" * 40)
    print("\n")

    choice = input("\n Enter a Choice : ")

    if choice == "1":
        name = input("\n Enter Course Name : ")
        description = input("\n Enter Course Description : ")
        price = input("\n Enter Course Price : ")
        private = input("\n Is this Course Private (0/1) : ")

        if db.insert_data([name, description, price, private]):
            print("Course was inserte successfully")
        else:
            print("oops something is wrong ! ...")

    elif choice == "2":
        print("\n:: Course List ::")

        for index,item in enumerate(db.fetch_data()):
            print("\n SL no: " + str(index+1))
            print("\n Course ID: " + str(item[0]))
            print("\n Course Name: " + str(item[1]))
            print("\n Course description: " + str(item[2]))
            print("Course Price :"+ str(item[3]))
            private = 'Yes' if item[4] else 'NO'
            print("Is Private: "+ private)
            print('\n')

    elif choice == "3":
        record_id = input(str("Enter the course ID : "))

        if db.delete_data(record_id):
            print("Course was deleted with a success ")
        else:
            print("oops something is wrong ...!")

    else:
        print("\n Bad Choice")

if __name__ == '__main__':
    main()






