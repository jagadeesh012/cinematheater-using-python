import mysql.connector
movie1tickets =30;
movie2tickets =40;

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="jagadeesh12",
  database="cinematheatre"
)

mycursor = mydb.cursor()
foodprice=0
uname=input("Enter user name:");
print("welcome",uname)
bc=int(input("enter 1:booking 2:cancel :"));
if bc==1:
    movie1="abcd";
    movie2="wxyz";
    print("Enter movie you want to watch");
    print("1.",movie1,"2.",movie2);
    movie=int(input());
    if movie==1:
        moviename=movie1;
    else:
        moviename=movie2;
    ticketsnumber=int(input("enter number of tickets:"));
    price=ticketsnumber*150;
    temp=price;
    print("press 1:confirm");
    print("      2:cancel");
    option=int(input());
    if  option==1:
        print("The ticket price is",price);
        print("Do you want food:")
        print("press yes/no");
        optionfood=input();
        if  optionfood=="yes":
            print("combo 1: 300");
            print("combo 2: 250");
            print("combo 3: 100");
            print("combo 4: 150");
            print("please choose any one:");
            optioncombo=int(input());
            if  option==1:
                print("how much quantity do you want:");
                qty=int(input());
                qtyprice=qty*300;
                price=price+qtyprice;
            elif  option==2:
                print("how much quantity do you want:");
                qty=int(input());
                qtyprice=qty*250;
                price=price+qtyprice;
            elif  option==3:
                print("how much quantity do you want:");
                qty=int(input());
                qtyprice=qty*100;
                price=price+qtyprice;
            elif  option==4:
                print("how much quantity do you want:");
                qty=int(input());
                qtyprice=qty*150;
                price=price+qtyprice;
            else:
                print("choose a valid combo:");
            foodprice=price-temp;
            
    elif option==2:
        print("thankyou");
    else:
        print("try again");
    print("total price=",price);
    print();
    print();
    print();
    tup=(moviename,ticketsnumber,temp,foodprice,price);
    print("movie ticket booked for:",tup[0]);
    print("number of ticket booked:",tup[1]);
    print("movie tickets prrice:",tup[2]);
    print("food price:",tup[3]);
    print("total prrice:",tup[4]);
    final_tuple=(uname,moviename,ticketsnumber,foodprice+price)
    query="insert into customer_table (name,movie_name,quantity,price) values(%s,%s,%s,%s)"
    mycursor.execute(query,final_tuple)
    mydb.commit()
    
if bc==2:
    query="select name,movie_name,quantity,price from customer_table where name='%s'"%(uname)
    mycursor.execute(query)
    confirm=list(mycursor.fetchall())[0]
    
    
    #tup=("abcd",2,300,600,900);
    print("your order is");
    print("name:",confirm[0]);
    print("movie name:",confirm[1]);
    print("number of ticket booked:",confirm[2]);
    print("movie tickets prrice:",confirm[3]);
    print("press 1: to conifm cancel");
    print("press 2  for not canceling");
    check=int(input("Enter a key"))
    if check==1:
        otp=8974;
        readotp=int(input("enter otp:"));
        if otp==readotp:
            query="delete from customer_table where name='%s'"%(uname)
            mycursor.execute(query)
            mydb.commit()
            print("cancelled successfully");
            print("refund initated...");
        else:
            print("enter correct otp and try again");
    else:exit()
