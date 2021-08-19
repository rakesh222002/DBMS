import subprocess as sp
import pymysql
import pymysql.cursors

########

def displayActor():
    
    try:

        cur.execute('select * from Actor')
        con.commit()
        rows = cur.fetchall()
        wid1=len("Aadhar_ID")
        wid2=len("Name")
        wid3=len("DOB")
        wid4=len("Contact")
        wid5=len("Remuneration")
        wid6=len("Lead or Not")
        wid7=len("Filmography")
        for row in rows:
            wid1=max(wid1,len(str(row['Aadhar_ID'])))
            wid2=max(wid2,len(str(row['Name'])))
            wid3=max(wid3,len(str(row['DOB'])))
            wid4=max(wid4,len(str(row['Contact'])))
            wid5=max(wid5,len(str(row['Remuneration'])))
            wid6=max(wid6,len(str(row['Leadflag'])))
            wid7=max(wid7,len(str(row['Filmography'])))
        print(f"{'Aadhar_ID':<{wid1}s} : {'Name':<{wid2}s} : {'DOB':<{wid3}s} : {'Contact':<{wid4}s} : {'Remuneration':<{wid5}s} : {'Lead or Not':<{wid6}s} : {'Filmography':<{wid7}s}")
        
        
        for row in rows:
            print(f"{str(row['Aadhar_ID']):<{wid1}s} : {str(row['Name']):<{wid2}s} : {str(row['DOB']):<{wid3}s} : {str(row['Contact']):<{wid4}s} : {str(row['Remuneration']):<{wid5}s} : {str(row['Leadflag']):<{wid6}s} : {str(row['Filmography']):<{wid7}s}")


        
    except Exception as e:
        con.rollback()
        print("Failed to get  Actors List")
        print(">>>>>>>>>>>>>", e)

    return

########

def displayDirector():
    
    try:
        cur.execute('select * from Director')
        con.commit()
        rows = cur.fetchall()
        wid1=len("Director_ID")
        wid2=len("Name")
        wid3=len("DOB")
        wid4=len("Filmography")
        wid5=len("Mainflag")
        wid6=len("MainID")
        
        for row in rows:
            wid1=max(wid1,len(str(row['Director_ID'])))
            wid2=max(wid2,len(str(row['Name'])))
            wid3=max(wid3,len(str(row['DOB'])))
            wid4=max(wid4,len(str(row['Filmography'])))
            wid5=max(wid5,len(str(row['Mainflag'])))
            wid6=max(wid6,len(str(row['MainID'])))
            
        print(f"{'Director_ID':<{wid1}s} : {'Name':<{wid2}s} : {'DOB':<{wid3}s} : {'Filmography':<{wid4}s} : {'Main or not':<{wid5}s} : {'MainID':<{wid6}s}")
        
        for row in rows:
            print(f"{str(row['Director_ID']):<{wid1}s} : {str(row['Name']):<{wid2}s} : {str(row['DOB']):<{wid3}s} : {str(row['Filmography']):<{wid4}s} : {str(row['Mainflag']):<{wid5}s} : {str(row['MainID']):<{wid6}s}")
        
    except Exception as e:
        con.rollback()
        print("Failed to get  Directors List")
        print(">>>>>>>>>>>>>", e)

    return

########

def displayAddressofActor():
    
    try:
        Aadhar_ID= int(input("Enter Aadhar_ID of Actor to get Address for : "))
        cur.execute(f'select * from Actor_Address_Country natural join (select * from Actor_Address_City natural join Actor_Address_State)t where Aadhar_ID = {Aadhar_ID}')
        con.commit()
        rows = cur.fetchall()
        wid1=len("City")
        wid2=len("State")
        wid3=len("Country")
        for row in rows:
            wid1=max(wid1,len(str(row['City'])))
            wid2=max(wid2,len(str(row['State'])))
            wid3=max(wid3,len(str(row['Country'])))

        print(f"{'City':<{wid1}s} : {'State':<{wid2}s} : {'Country':<{wid3}s}")
        
        
        for row in rows:
            print(f"{str(row['City']):<{wid1}s} : {str(row['State']):<{wid2}s} : {str(row['Country']):<{wid3}s}")
    
    except Exception as e:
        con.rollback()
        print("Failed to get  Actor's Address List")
        print(">>>>>>>>>>>>>", e)

    return

#########

def displayAddressofDirector():
    
    try:
        Director_ID = input("Enter ID of Director to get Address for : ")
        cur.execute(f'select * from Director_Address_Country natural join (select * from Director_Address_City natural join Director_Address_State)t where Director_ID = {Director_ID}')
        con.commit()
        rows = cur.fetchall()
        wid1=len("City")
        wid2=len("State")
        wid3=len("Country")
        for row in rows:
            wid1=max(wid1,len(str(row['City'])))
            wid2=max(wid2,len(str(row['State'])))
            wid3=max(wid3,len(str(row['Country'])))

        print(f"{'City':<{wid1}s} : {'State':<{wid2}s} : {'Country':<{wid3}s}")
                
        for row in rows:
            print(f"{str(row['City']):<{wid1}s} : {str(row['State']):<{wid2}s} : {str(row['Country']):<{wid3}s}")

    except Exception as e:
        con.rollback()
        print("Failed to get  Director's Address List")
        print(">>>>>>>>>>>>>", e)

    return

########

def displayAccoladesofActor():
    
    try:
        Aadhar_ID= input("Enter Aadhar_ID of Actor to get Accolades for : ")
        cur.execute(f'select * from Actor_Accolades where Aadhar_ID = {Aadhar_ID}')
        con.commit()
        rows = cur.fetchall()
        wid1=len("Accolade")
        for row in rows:
            wid1=max(wid1,len(str(row['Name_of_Accolade'])))

        print(f"{'Accolade':<{wid1}s}")
        
        
        for row in rows:
            print(f"{str(row['Name_of_Accolade']):<{wid1}s}")


        
    except Exception as e:
        con.rollback()
        print("Failed to get  Actor's Accolade List")
        print(">>>>>>>>>>>>>", e)

    return

#########

def displayAccoladesofDirector():
    
    try:
        Director_ID = input("Enter ID of Director to get Accolades for : ")
        cur.execute(f'select * from Director_Accolades where Director_ID = {Director_ID}')
        con.commit()
        rows = cur.fetchall()
        wid1=len("Accolade")
        for row in rows:
            wid1=max(wid1,len(str(row['Name_of_Accolade'])))

        print(f"{'Accolade':<{wid1}s}")
                
        for row in rows:
            print(f"{str(row['Name_of_Accolade']):<{wid1}s}")
      
    except Exception as e:
        con.rollback()
        print("Failed to get  Director's Accolade List")
        print(">>>>>>>>>>>>>", e)
    return

#########

def displayVFX():
    
    try:

        cur.execute('select * from VFX')
        con.commit()
        rows = cur.fetchall()
        wid1=len("Movie_ID")
        wid2=len("Name")
        wid3=len("VFX_Director")
        wid4=len("Avg_Demand")
        for row in rows:
            wid1=max(wid1,len(str(row['Movie_ID'])))
            wid2=max(wid2,len(str(row['Name'])))
            wid3=max(wid3,len(str(row['VFX_Director'])))
            wid4=max(wid4,len(str(row['Avg_Demand'])))

        print(f"{'Movie_ID':<{wid1}s} : {'Name':<{wid2}s} : {'VFX_Director':<{wid3}s} : {'Avg_Demand':<{wid4}s} ")
        
        
        for row in rows:
            print(f"{str(row['Movie_ID']):<{wid1}s} : {str(row['Name']):<{wid2}s} : {str(row['VFX_Director']):<{wid3}s} : {str(row['Avg_Demand']):<{wid4}s} ")
    
    except Exception as e:
        con.rollback()
        print("Failed to get  VFX's List")
        print(">>>>>>>>>>>>>", e)

    return

########

def displaySets():
    
    try:
        cur.execute('Select * from Set_Cost natural join Set_Manpower natural join Set_Location')
        con.commit()
        rows = cur.fetchall()
        wid1=len("Movie_ID")
        wid2=len("VFX_ID")
        wid3=len("Cost")
        wid4=len("Location_Depicted")
        wid5=len("Man_Power")
        
        for row in rows:
            wid1=max(wid1,len(str(row['Movie_ID'])))
            wid2=max(wid2,len(str(row['VFX_ID'])))
            wid3=max(wid3,len(str(row['Cost'])))
            wid4=max(wid4,len(str(row['Location_Depicted'])))
            wid5=max(wid5,len(str(row['Man_Power'])))

        print(f"{'Movie_ID':<{wid1}s} : {'VFX_ID':<{wid2}s} : {'Cost':<{wid3}s} : {'Location_Depicted':<{wid4}s} : {'Man_Power':<{wid5}s} ")
        
        for row in rows:
            print(f"{str(row['Movie_ID']):<{wid1}s} : {str(row['VFX_ID']):<{wid2}s} : {str(row['Cost']):<{wid3}s} : {str(row['Location_Depicted']):<{wid4}s} : {str(row['Man_Power']):<{wid5}s} ")
    
    except Exception as e:
        con.rollback()
        print("Failed to get  Set's List")
        print(">>>>>>>>>>>>>", e)
    return

########### 

def displayAddressofVFX():
    
    try:
        Movie_ID= input("Enter Movie_ID of VFX to get Address for : ")
        cur.execute(f'select * from VFX_Address_Country natural join (select * from VFX_Address_City natural join VFX_Address_State)t where Movie_ID = {Movie_ID}')
        con.commit()
        rows = cur.fetchall()
        wid1=len("City")
        wid2=len("State")
        wid3=len("Country")
        for row in rows:
            wid1=max(wid1,len(str(row['City'])))
            wid2=max(wid2,len(str(row['State'])))
            wid3=max(wid3,len(str(row['Country'])))

        print(f"{'City':<{wid1}s} : {'State':<{wid2}s} : {'Country':<{wid3}s}")
        
        
        for row in rows:
            print(f"{str(row['City']):<{wid1}s} : {str(row['State']):<{wid2}s} : {str(row['Country']):<{wid3}s}")


        
    except Exception as e:
        con.rollback()
        print("Failed to get  Actor's Address List")
        print(">>>>>>>>>>>>>", e)

    return

##########

def displayMovies():
    
    try:

        cur.execute('select * from Movie_info natural join Movie_Profit_or_Loss natural join Movie_Collections')
        con.commit()
        rows = cur.fetchall()
        wid1=len("Movie_ID")
        wid2=len("Name")
        wid3=len("Release_Date")
        wid4=len("Avg_rate")
        wid5=len("Budget")
        wid6=len("Director_ID")
        wid7=len("Film_No")
        wid8=len("Profit_or_Loss")
        wid9=len("Collections")
        for row in rows:
            wid1=max(wid1,len(str(row['Movie_ID'])))
            wid2=max(wid2,len(str(row['Name'])))
            wid3=max(wid3,len(str(row['Release_Date'])))
            wid4=max(wid4,len(str(row['Avg_rate'])))
            wid5=max(wid5,len(str(row['Budget'])))
            wid6=max(wid6,len(str(row['Director_ID'])))
            wid7=max(wid7,len(str(row['Film_No'])))
            wid8=max(wid8,len(str(row['Profit_or_Loss'])))
            wid9=max(wid9,len(str(row['Collections'])))

        print(f"{'Movie_ID':<{wid1}s} : {'Name':<{wid2}s} : {'Release_Date':<{wid3}s} : {'Avg_rate':<{wid4}s} : {'Budget':<{wid5}s} : {'Director_ID':<{wid6}s} : {'Film_No':<{wid7}s} : {'Profit_or_Loss':<{wid8}s} : {'Collections':<{wid9}s}")
        
        
        for row in rows:
            print(f"{str(row['Movie_ID']):<{wid1}s} : {str(row['Name']):<{wid2}s} : {str(row['Release_Date']):<{wid3}s} : {str(row['Avg_rate']):<{wid4}s} : {str(row['Budget']):<{wid5}s} : {str(row['Director_ID']):<{wid6}s} : {str(row['Film_No']):<{wid7}s} : {str(row['Profit_or_Loss']):<{wid8}s} : {str(row['Collections']):<{wid9}s}")
    
    except Exception as e:
        con.rollback()
        print("Failed to get  Movie's List")
        print(">>>>>>>>>>>>>", e)

    return

########

def displayAwardsofMovie():
    
    try:
        Movie_ID= input("Enter Movie_ID of Movie to get Awards for : ")
        cur.execute(f'select * from Movie_Awards where Movie_ID = {Movie_ID}')
        con.commit()
        rows = cur.fetchall()
        wid1=len("Award")
        for row in rows:
            wid1=max(wid1,len(str(row['Award_Name'])))

        print(f"{'Award':<{wid1}s}")
        
        
        for row in rows:
            print(f"{str(row['Award_Name']):<{wid1}s}")


        
    except Exception as e:
        con.rollback()
        print("Failed to get  Movie's Award List")
        print(">>>>>>>>>>>>>", e)

    return

##########

def maxMovieRating():

    try:
        
        cur.execute("select MAX(Avg_rate) from Movie_info")
        con.commit()
        row= cur.fetchall()
        print("Maximum Average Movie Rating is : %s" % (row[0]['MAX(Avg_rate)'])) 
    except Exception as e:
        con.rollback()
        print("Failed to get Max Average")
        print(">>>>>>>>>>>>>", e)

    return

#########

def minMovieRating():
    
    try:
        
        cur.execute("select MIN(Avg_rate) from Movie_info")
        con.commit()
        row= cur.fetchall()
        print("Minimum Average Movie Rating is : %s" % (row[0]['MIN(Avg_rate)'])) 
    except Exception as e:
        con.rollback()
        print("Failed to get Min Average")
        print(">>>>>>>>>>>>>", e)

    return

##########

def AvgBudget():
    
    try:
        
        cur.execute("select AVG(Budget) from Movie_info")
        con.commit()
        row= cur.fetchall()
        print("Average Budget for a Movie is : %s" % (row[0]['AVG(Budget)'])) 
    except Exception as e:
        con.rollback()
        print("Failed to get  Average Budget")
        print(">>>>>>>>>>>>>", e)

    return

###########

def sumBudget():
    
    try:
        
        cur.execute("select SUM(Budget) from Movie_info")
        con.commit()
        row= cur.fetchall()
        print("Total Budget for all Movies allocated till now is : %s crores" % (row[0]['SUM(Budget)'])) 
    except Exception as e:
        con.rollback()
        print("Failed to get  Total Budget")
        print(">>>>>>>>>>>>>", e)

    return

###########

def partialSearch( ):
    
    try:

        paSearch = input("Enter the Name to search for:  ")
        cur.execute(f'select Name from Movie_info where Name like "%{paSearch}%"')
        
        con.commit()
        rows= cur.fetchall()
        print("Names: ") 
        for row in rows:
            print(row['Name']) 
            

        
    except Exception as e:
        con.rollback()
        print("Failed to get  Names in Search")
        print(">>>>>>>>>>>>>", e)

    return

#########

def numSuccDirectors():
    
    try:  
        cur.execute("select AVG(Profit_or_Loss) from Movie_Profit_or_Loss")
        con.commit()
        rowProfit = cur.fetchall()
        avgProfit = rowProfit[0]['AVG(Profit_or_Loss)']
        succIDs = set()      
        cur.execute("select * from Director as dir, Movie_info as mi, Movie_Profit_or_Loss as mpl where dir.Director_ID = mi.Director_ID and mi.Movie_ID = mpl.Movie_ID")
        con.commit()
        rows= cur.fetchall()
        
        for row in rows:
            if row['Profit_or_Loss'] >= avgProfit:
                succIDs.add(row['Director_ID'])
        print(f'Number of successful directors associated are {len(succIDs)}')
         
    except Exception as e:
        con.rollback()
        print("Failed to get successfull directors")
        print(">>>>>>>>>>>>>", e)

    return

#######

def valuedActors():
    
    try:
        thresh = int(input("Enter the threshold experience value actors should possess:  "))
        cur.execute(f'select * from Actor as A, (select Aadhar_ID, COUNT(*) as count from Actor_Accolades group by Aadhar_ID) as B where A.Aadhar_ID = B.Aadhar_ID')
        con.commit()
        rows = cur.fetchall()
        req = 0
        awds = 0
        actedIn = 0
        
        for row in rows:
            awds = 1
            awds += row['count']
            actedIn = row['Filmography']
            
            if ((awds * actedIn) >= thresh):
                req += 1
        print(f'Number of actors with / more than given threshold experience value is {req}') 
        
    except Exception as e:
        con.rollback()
        print("Failed to get actors having more than given threshold experience value")
        print(">>>>>>>>>>>>>", e)
    return

########

def displayMoviesbyYear():
    
    try:

        year = int(input("Enter the year to show movies for:  "))
        cur.execute(f'select * from  Movie_info where YEAR(Release_Date)= {year}')
        con.commit()
        rows = cur.fetchall()
        wid1=len("Movie_ID")
        wid2=len("Name")
        wid3=len("Release_Date")
        wid4=len("Avg_rate")
        wid5=len("Budget")
        wid6=len("Director_ID")
        wid7=len("Film_No")
        for row in rows:
            wid1=max(wid1,len(str(row['Movie_ID'])))
            wid2=max(wid2,len(str(row['Name'])))
            wid3=max(wid3,len(str(row['Release_Date'])))
            wid4=max(wid4,len(str(row['Avg_rate'])))
            wid5=max(wid5,len(str(row['Budget'])))
            wid6=max(wid6,len(str(row['Director_ID'])))
            wid7=max(wid7,len(str(row['Film_No'])))

        print(f"{'Movie_ID':<{wid1}s} : {'Name':<{wid2}s} : {'Release_Date':<{wid3}s} : {'Avg_rate':<{wid4}s} : {'Budget':<{wid5}s} : {'Director_ID':<{wid6}s} : {'Film_No':<{wid7}s}")
        
        
        for row in rows:
            print(f"{str(row['Movie_ID']):<{wid1}s} : {str(row['Name']):<{wid2}s} : {str(row['Release_Date']):<{wid3}s} : {str(row['Avg_rate']):<{wid4}s} : {str(row['Budget']):<{wid5}s} : {str(row['Director_ID']):<{wid6}s} : {str(row['Film_No']):<{wid7}s}")


        
    except Exception as e:
        con.rollback()
        print("Failed to get  Movie by Year")
        print(">>>>>>>>>>>>>", e)

    return

#######

def displayMoviesbyAvgRating():
    
    try:

        rate = input("Enter the threshold of Avg.Rating to show movies for:  ")
        cur.execute(f'select * from  Movie_info where Avg_rate >= {rate}')
        con.commit()
        rows = cur.fetchall()
        wid1=len("Movie_ID")
        wid2=len("Name")
        wid3=len("Release_Date")
        wid4=len("Avg_rate")
        wid5=len("Budget")
        wid6=len("Director_ID")
        wid7=len("Film_No")
        for row in rows:
            wid1=max(wid1,len(str(row['Movie_ID'])))
            wid2=max(wid2,len(str(row['Name'])))
            wid3=max(wid3,len(str(row['Release_Date'])))
            wid4=max(wid4,len(str(row['Avg_rate'])))
            wid5=max(wid5,len(str(row['Budget'])))
            wid6=max(wid6,len(str(row['Director_ID'])))
            wid7=max(wid7,len(str(row['Film_No'])))

        print(f"{'Movie_ID':<{wid1}s} : {'Name':<{wid2}s} : {'Release_Date':<{wid3}s} : {'Avg_rate':<{wid4}s} : {'Budget':<{wid5}s} : {'Director_ID':<{wid6}s} : {'Film_No':<{wid7}s}")
        
        
        for row in rows:
            print(f"{str(row['Movie_ID']):<{wid1}s} : {str(row['Name']):<{wid2}s} : {str(row['Release_Date']):<{wid3}s} : {str(row['Avg_rate']):<{wid4}s} : {str(row['Budget']):<{wid5}s} : {str(row['Director_ID']):<{wid6}s} : {str(row['Film_No']):<{wid7}s}")


        
    except Exception as e:
        con.rollback()
        print("Failed to get  Movie by Year")
        print(">>>>>>>>>>>>>", e)

    return

#########

def insertmovie():

    Avg_rate=""
    Release_Date=""
    Movie_ID=0
    try:

        Movie_ID = int(input("Enter Movie_ID : "))
        if (Movie_ID < 0):
            print("Movie_ID cannot take negative values")
            return
        Movie_name = input("Movie Name : ")
        if (Movie_name == ""):
            print("Name cannot be NULL")
            return
        Release_Date = input("Release Date (yyyy-mm-dd): ")
        Avg_rate = input("Avg_rate : ")
        
        if(Avg_rate!=""):
            Avg_rate=float(Avg_rate)

        if (Avg_rate < 0):
            print("Avg_rate cannot take negative values")
            return
        Budget = int(input("Budget : "))
        if (Budget < 0):
            print("Budget cannot take negative values")
            return
        Director_ID = int(input("Director_ID : "))
        if (Director_ID < 0):
            print("Director_ID cannot take negative values")
            return
        Film_No = int(input("Film_No : "))
        if (Film_No < 0):
            print("Film_No cannot take negative values")
            return
        Movieinfo_query = f'insert into Movie_info (Movie_ID, Name, Budget, Director_ID, Film_No) VALUES ({Movie_ID},"{Movie_name}", {Budget}, {Director_ID}, {Film_No})'
        cur.execute(Movieinfo_query);
        con.commit()

    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)
    
    try:
        if(Avg_rate!=""):
            cur.execute(f'update Movie_info set Avg_rate = {Avg_rate} where Movie_ID={Movie_ID}')
            cur.commit()
    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)
    
    
    try:
        if(Release_Date!=""):
            cur.execute(f'update Movie_info set Release_Date = "{Release_Date}" where Movie_ID={Movie_ID}')
            cur.commit()
    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)
    
    try:

        Collections = input("Collections : ")
        if(Collections!=""):
            Collections=int(Collections)
            if (Collections < 0):
                print("Collections cannot take negative values")
                return
            Movie_Collectionsquery = f'insert into Movie_Collections VALUES ({Movie_ID}, {Collections})'
            cur.execute(Movie_Collectionsquery)
            con.commit()
        else:
            Movie_Collectionsquery = f'insert into Movie_Collections (Movie_ID) VALUES ({Movie_ID})'
            cur.execute(Movie_Collectionsquery)
            con.commit()

    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)

    try:

        profit = input("Profit/Loss +ve/-ve : ")
        if(profit!=""):
            profit=int(profit)
            Movie_Collectionsquery = f'insert into Movie_Profit_or_Loss VALUES ({Movie_ID}, {profit})'
            cur.execute(Movie_Collectionsquery)
            con.commit()
        else:
            Movie_Collectionsquery = f'insert into Movie_Collections (Movie_ID) VALUES ({Movie_ID})'
            cur.execute(Movie_Collectionsquery)
            con.commit()

    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)


    return


def insertMovieAward():
    
    try:
        Movie_ID=input("Movie_ID to enter Award for:")
        Award_Name = input("Award Name recieved by movie: ")
        if(Award_Name==""):
            print("Award Name cannot be empty")
            return
        MovieAwardquery = f'insert into Movie_Awards VALUES ({Movie_ID}, "{Award_Name}")'
        cur.execute(MovieAwardquery)
        con.commit()
    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)


def insertactor():
    try:

        Actor_Aadharid = int(input("Aadhar ID of actor : "))
        if (Actor_Aadharid < 0):
            print("Actor Aadhar_id cannot take negative values")
            return
        Actor_Name = input("Actors Name : ")
        Actor_DOB = input("Actor date of birth (yyyy-mm-dd): ")
        Actor_Contact = input("Actors Contact number : ")
        if (Actor_Contact < 0):
            print("Actors Contact cannot take negative values")
            return
        Actor_Remuneration = float(input("Actor Remuneration : "))
        if (Actor_Remuneration < 0):
            print("Actors Remuneration cannot take negative values")
            return
        Actor_Leadflag = input("enter 1 if he is main actor,otherwise 0 : ")
        if(not(Actor_Leadflag==1 or Actor_Leadflag==0)):
            print("Invalid Input")
            return
        Actor_Filmography = int(input("No of films he acted "))
        if (Actor_Filmography < 0):
            print("Actors filmography cannot take negative values")
            return        
        Actorinfoquery = f'insert into Actor VALUES ({Actor_Aadharid},"{Actor_Name}", "{Actor_DOB}", "{Actor_Contact}", {Actor_Remuneration}, "{Actor_Leadflag}", {Actor_Filmography})'
        cur.execute(Actorinfoquery)
        con.commit()
    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)

    return

def insertActorAccolades():

    try:
        Actor_Aadharid = int(input("Actor Aadhar ID : "))
        if (Actor_Aadharid < 0):
            print("Actors Aadhar id cannot take negative values")
            return
        Actor_Accolades = input("Award Name recieved by actor : ")
        if(Actor_Accolades==""):
            print("It cannot be empty")
            return
        Actor_Accoladesquery = f'insert into Actor_Accolades VALUES ({Actor_Aadharid}, "{Actor_Accolades}")'
        cur.execute(Actor_Accoladesquery)
        con.commit()
    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)
    return


def insertActorAddress():
    
    Actor_Aadharid = int(input("Actors Aadhar ID : "))

    Actor_Address_City = input("Actors city name : ")
    if(Actor_Address_City==""):
        print("It cannot be empty")
        return

    Actor_Address_State = input("Actors state name : ")
    if(Actor_Address_State==""):
        print("It cannot be empty")
        return

    Actor_Address_Country = input("Actors country name : ")
    if(Actor_Address_City==""):
        print("It cannot be empty")
        return
    
    try:

        Actor_Address_Cityquery = f'insert into Actor_Address_City VALUES ({Actor_Aadharid}, "{Actor_Address_City}")'
        cur.execute(Actor_Address_Cityquery)
        con.commit()
    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)

    try:
        
        Actor_Address_Statequery = f'insert into Actor_Address_State VALUES ({Actor_Aadharid},"{Actor_Address_City}", "{Actor_Address_State}")'
        cur.execute(Actor_Address_Statequery)
        con.commit()
    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)

    try:

        Actor_Address_Countryquery = f'insert into Actor_Address_Country VALUES ({Actor_Aadharid},"{Actor_Address_State}", "{Actor_Address_Country}")'
        cur.execute(Actor_Address_Countryquery)
        con.commit()

    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)
    
    return

def insertDirectorAddress():
    
    Directorid = int(input(" Director ID : "))

    Director_Address_City = input("Director's city name : ")
    if(Director_Address_City==""):
        print("It cannot be empty")
        return

    Director_Address_State = input("Director's state name : ")
    if(Director_Address_State==""):
        print("It cannot be empty")
        return

    Director_Address_Country = input("Director's country name : ")
    if(Director_Address_City==""):
        print("It cannot be empty")
        return
    
    try:

        Director_Address_Cityquery = f'insert into Director_Address_City VALUES ({Directorid}, "{Director_Address_City}")'
        cur.execute(Director_Address_Cityquery)
        con.commit()
    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)

    try:
        
        Director_Address_Statequery = f'insert into Director_Address_State VALUES ({Directorid},"{Director_Address_City}", "{Director_Address_State}")'
        cur.execute(Director_Address_Statequery)
        con.commit()
    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)

    try:

        Director_Address_Countryquery = f'insert into Director_Address_Country VALUES ({Directorid},"{Director_Address_State}", "{Director_Address_Country}")'
        cur.execute(Director_Address_Countryquery)
        con.commit()

    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)
    
    return

def insertVFXAddress():
    
    VFXid = int(input("VFX Movie ID : "))

    VFX_Address_City = input("VFX city name : ")
    if(VFX_Address_City==""):
        print("It cannot be empty")
        return

    VFX_Address_State = input("VFX state name : ")
    if(VFX_Address_State==""):
        print("It cannot be empty")
        return

    VFX_Address_Country = input("VFX country name : ")
    if(VFX_Address_City==""):
        print("It cannot be empty")
        return
    
    try:

        VFX_Address_Cityquery = f'insert into VFX_Address_City VALUES ({VFXid}, "{VFX_Address_City}")'
        cur.execute(VFX_Address_Cityquery)
        con.commit()
    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)

    try:
        
        VFX_Address_Statequery = f'insert into VFX_Address_State VALUES ({VFXid},"{VFX_Address_City}", "{VFX_Address_State}")'
        cur.execute(VFX_Address_Statequery)
        con.commit()
    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)

    try:

        VFX_Address_Countryquery = f'insert into VFX_Address_Country VALUES ({VFXid},"{VFX_Address_State}", "{VFX_Address_Country}")'
        cur.execute(VFX_Address_Countryquery)
        con.commit()

    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)
    
    return



def insertdirector(): 
    Main_ID=""
    Director_ID=0
    try:

        Director_ID = int(input("Director ID : "))
        if (Director_ID < 0):
            print("Director_ID cannot take negative values")
            return
        Director_Name = input("Director Name : ")
        if(Director_Name==""):
            print("Cannot be empty")
            return
        Director_DOB = input("Director Date of Birth (yyyy-mm-dd): ")
        if(Director_DOB==""):
            print("Cannot be empty")
            return

        Director_Filmography = int(input("Director Filmography : "))
        if (Director_Filmography < 0):
            print("Filmography cannot take negative values")
            return
        Director_Mainflag = int(input("Enter '1' if he is main director,otherwise '0' : "))
        if(not(Director_Mainflag==1 or Director_Mainflag==0)):
            print("Invalid Input")
            return

        if (Director_Mainflag == 0):
            Main_ID = int(input("Main ID of the assistant director : "))
        else:
            Main_ID = "NULL"
        Directorinfoquery = f'insert into Director (Director_ID, Name, DOB, Filmography ,Mainflag) VALUES ({Director_ID}, "{Director_Name}", "{Director_DOB}", {Director_Filmography}, "{Director_Mainflag}")'
        cur.execute(Directorinfoquery)
        con.commit()
    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)
    try:
        if(Main_ID!="NULL"):
            cur.execute(f'update Director set MainID={Main_ID} where Director_ID = {Director_ID}')
            con.commit()
    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)
    return
    

def insertDirector_Accolades():
    Director_ID = int(input("Director ID : "))
    try:


        Director_Accolades = input("Director_Accolades : ")
        if(Director_Accolades==""):
            print("Cannot be empty")
            return
        Director_Accoladesquery = f'insert into Director_Accolades VALUES ({Director_ID},"{Director_Accolades}")'
        cur.execute(Director_Accoladesquery)
        con.commit()
    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)

    return


def insertVFX():
    try:

        VFX_Director = input("VFX Directors name : ")
        if(VFX_Director==""):
            print("Cannot be empty")
            return
        Avg_Demand = float(input("Average demand of VFX Studio : "))
        if (Avg_Demand < 0):
            print("Average demand cannot take negative values")
            return
        VFX_NAME = input("VFX studio name : ")
        if(VFX_NAME==""):
            print("Cannot be empty")
            return
        Movie_ID = int(input("Movie ,the VFX studio working on : "))
        cur.execute(f'insert into VFX VALUES ("{VFX_Director}", {Avg_Demand}, "{VFX_NAME}", {Movie_ID})')
        con.commit()

    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)



def insertset():

    Movie_ID=0
    Location_Depicted=""
    VFX_ID=0

    try:

        Movie_ID = int(input("Movie ID for which the set is created : "))
        Location_Depicted = input("Set location : ")
        if(Location_Depicted==""):
            print("Cannot be empty")
            return
        VFX_ID = int(input("VFX id associated with that set : "))
        cur.execute(f'insert into Set_Location VALUES ({Movie_ID}, "{Location_Depicted}", {VFX_ID})')
        con.commit()
    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)
    try:
        Man_Power = int(input("Number of people working for the Set"))
        if (Man_Power < 0):
            print("Man power cannot take negative values")
            return
        curr.execute(f'insert into Set_Manpower VALUES ({Movie_ID}, {Man_Power},{VFX_ID}, "{Location_Depicted}")')
        con.commit()
    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)

    try:
        Set_Cost = int(input("Cost for the cration os set : "))
        if (Set_Cost < 0):
            print("Cost cannot take negative values")
            return
        curr.execute(f'insert into Set_Cost VALUES ({Movie_ID}, {Set_Cost},{VFX_ID}, "{Location_Depicted}")')
        con.commit()

    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)
    return



def insertCOORDINATES_WITH():
    try:
        Movie_ID = int(input("Id of the VFX STUDIO: "))
        Director_ID = int(input("Director ID: "))
        cur.execute(f'insert into COORDINATES_WITH VALUES ({Movie_ID}, {Director_ID}')
    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)

    return

def insertREQUIRES():
    
    Movie_ID = int(input("Movie ID : "))
    Director_ID = int(input("Director ID : "))
    noofactors = int(input("Number of Actors in this movie : "))
    if (noofactors < 0):
        print("Number of actors cannot take negative values")
        return
    Actors = []
    for ind in range(noofactors):
        Aadhar_ID = int(input(f'Enter Aadhar_ID of Actor {ind+1}'))
        Actors.append(Aadhar_ID)
    noofsets = int(input("No of sets : "))
    Sets = []
    if (noofsets < 0):
        print("Number of sets cannot take negative values")
        return    
    for ind in range(noofsets):
        Set_ID = int(input(f'Enter Set_ID of Set {ind+1}'))
        Sets.append(Set_ID)
    for x in Actors:
        for y in Sets:
            try:

                cur.execute(f'insert into COORDINATES_WITH VALUES ({x}, {Director_ID}, {Movie_ID}, {y})')
                con.commit()
            except Exception as e:
                con.rollback()
                print(">>>>>>>>>>>>>", e)

    return

def updatemovie():
    
    try:

        Movie_ID = int(input("Movie_ID of movie that need to updated: "))
        if (Movie_ID < 0):
            print("Movie_ID cannot take negative values")
            return
        print("What do you want to Update?")
        print("1.Name")
        print("2.Release_Date")
        print("3.Avg_rate")
        print("4.Budget")
        print("5.Director_ID")
        print("6.Film_No")
        print("7.Profit/Loss")
        print("8.Collections")
        op=int(input("Enter Option:"))
        newvalue=input("Enter new Value:")
        if(newvalue==""):
            print("Cannot update to empty")
            return
            
        if(op==1):
            
            cur.execute(f'Update Movie_info set Name="{newvalue}" where Movie_ID={Movie_ID}')
            con.commit()

        elif(op==2):
            cur.execute(f'Update Movie_info set Release_Date="{newvalue}" where Movie_ID={Movie_ID}')
            con.commit()
            
        elif(op==3):
            newvalue=float(newvalue)
            if(newvalue<0):
                print("Invalid")
                return
            cur.execute(f'Update Movie_info set Avg_rate="{newvalue}" where Movie_ID={Movie_ID}')
            con.commit()
        elif(op==4):
            newvalue=int(newvalue)
            if(newvalue<0):
                print("Invalid")
                return
            cur.execute(f'Update Movie_info set Budget="{newvalue}" where Movie_ID={Movie_ID}')
            con.commit()
            
        elif(op==5):
            newvalue=int(newvalue)
            if(newvalue<0):
                print("Invalid")
                return
            cur.execute(f'Update Movie_info set Director_ID="{newvalue}" where Movie_ID={Movie_ID}')
            con.commit()
            
        elif(op==6):
            newvalue=int(newvalue)
            if(newvalue<0):
                print("Invalid")
                return
            cur.execute(f'Update Movie_info set Film_No="{newvalue}" where Movie_ID={Movie_ID}')
            con.commit()
        elif(op==7):
            newvalue=int(newvalue)
            cur.execute(f'Update Movie_Profit_or_Loss set Profit_or_Loss="{newvalue}" where Movie_ID={Movie_ID}')
            con.commit()
        elif(op==8):
            newvalue=int(newvalue)
            if(newvalue<0):
                print("Invalid")
                return
            cur.execute(f'Update Movie_Collections set Collection ="{newvalue}" where Movie_ID={Movie_ID}')
            con.commit()
            
        else:
            print("Invalid Option")
            return
        
        
    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)

    return

def updateactor():
    
    try:

        Aadhar_ID = int(input("Movie_ID of movie that need to updated: "))
        if (Aadhar_ID < 0):
            print("Aadhar_ID cannot take negative values")
            return
        print("What do you want to Update?")
        print("1.Name")
        print("2.DOB")
        print("3.Contact")
        print("4.Remuneration")
        print("5.LeadFlag")
        print("6.Filmography")
        op=int(input("Enter Option:"))
        newvalue=input("Enter new Value:")
        if(newvalue==""):
            print("Cannot update to empty")
            return
            
        if(op==1):

            cur.execute(f'Update Actor set Name="{newvalue}" where Aadhar_ID={Aadhar_ID}')
            con.commit()

        elif(op==2):
            cur.execute(f'Update Actor set DOB="{newvalue}" where Aadhar_ID={Aadhar_ID}')
            con.commit()
            
        elif(op==3):
            newvalue=int(newvalue)
            if(newvalue<0):
                print("Invalid")
                return
            cur.execute(f'Update Actor set Contact={newvalue} where Aadhar_ID={Aadhar_ID}')
            con.commit()
        elif(op==4):
            newvalue=int(newvalue)
            if(newvalue<0):
                print("Invalid")
                return
            cur.execute(f'Update Actor set Remuneration ={newvalue} where Aadhar_ID={Aadhar_ID}')
            con.commit()
            
        elif(op==5):
            newvalue=int(newvalue)
            if(not(newvalue == 1 or newvalue == 0)):
                print("Invalid")
                return
            cur.execute(f'Update Actor set LeadFlag={newvalue} where Aadhar_ID={Aadhar_ID}')
            con.commit()
            
        elif(op==6):
            newvalue=int(newvalue)
            if(newvalue<0):
                print("Invalid")
                return
            cur.execute(f'Update Actor set Filmography={newvalue} where Aadhar_ID={Aadhar_ID}')
            con.commit()
        else:
            print("Invalid Option")
            return
        
        
    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)

    return



def updatedirector():
    
    try:

        Director_ID = int(input("Movie_ID of movie that need to updated: "))
        if (Director_ID < 0):
            print("Director_ID cannot take negative values")
            return
        print("What do you want to Update?")
        print("1.Name")
        print("2.DOB")
        print("3.Filmography")
        print("4.Mainflag")
        print("5.MainID")
        op=int(input("Enter Option:"))
        newvalue=input("Enter new Value:")
        if(newvalue==""):
            print("Cannot update to empty")
            return
            
        if(op==1):

            cur.execute(f'Update Director set Name="{newvalue}" where Director_ID={Director_ID}')
            con.commit()

        elif(op==2):
            cur.execute(f'Update Director set DOB="{newvalue}" where Director_ID={Director_ID}')
            con.commit()
            
        elif(op==3):
            newvalue=int(newvalue)
            if(newvalue<0):
                print("Invalid")
                return
            cur.execute(f'Update Director set Filmography={newvalue} where Director_ID={Director_ID}')
            con.commit()
        elif(op==4):
            newvalue=int(newvalue)
            if(newvalue!=1):
                print("Invalid: Only Promotion Allowed")
                return
            cur.execute(f'Update Actor set Mainflag = 1 , MainID = NULL where Director_ID={Director_ID}')
            con.commit()
            
        elif(op==5):
            newvalue=int(newvalue)
            cur.execute(f'select Mainflag from Actor where Director_ID={Director_ID}')
            con.commit()
            ans=cur.fetchone()
            if(ans is None):
                print("Director does not exist")
                return;
            if(ans['Mainflag']==1):
                print("This Director is a main Director cannot add MainID")
                return
            cur.execute(f'Update Director set Main_ID={newvalue} where Director_ID={Director_ID}')
            con.commit()
            
        else:
            print("Invalid Option")
            return
        
        
    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)

    return

def updateSET():
    
    try:

        Movie_ID = int(input("Movie_ID of movie that need to updated: "))
        oldlocation = input("Enter the Location Depicted by the Set: ")
        if (Movie_ID < 0):
            print("Movie_ID cannot take negative values")
            return
        print("What do you want to Update?")
        print("1.Location Depicted")
        print("2.Cost")
        print("3.ManPower")
        op=int(input("Enter Option:"))
        newvalue=input("Enter new Value:")
        if(newvalue==""):
            print("Cannot update to empty")
            return
            
        if(op==1):

            cur.execute(f'Update Set_Locaton set Location_Depicted ="{newvalue}" where Movie_ID={Movie_ID} and Location_Depicted= "{oldlocation}"')
            con.commit()

        elif(op==2):
            
            newvalue=int(newvalue)
            if(newvalue<0):
                print("Invalid")
                return
            cur.execute(f'Update Set_Cost set Cost ={newvalue} where Movie_ID={Movie_ID} and Location_Depicted= "{oldlocation}"')
            con.commit()
            
        elif(op==3):
            newvalue=int(newvalue)
            if(newvalue<0):
                print("Invalid")
                return
            cur.execute(f'Update Set_Manpower set Man_Power ={newvalue} where Movie_ID={Movie_ID} and Location_Depicted= "{oldlocation}"')
            con.commit()
            
        else:
            print("Invalid Option")
            return
        
        
    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)

    return

def updateVFX():
    
    try:

        Movie_ID = int(input("Movie_ID of movie that need to updated: "))
        if (Movie_ID < 0):
            print("Movie_ID cannot take negative values")
            return
        print("What do you want to Update?")
        print("1.Name")
        print("2.VFX_Director")
        print("3.Avg_Demand")
        op=int(input("Enter Option:"))
        newvalue=input("Enter new Value:")
        if(newvalue==""):
            print("Cannot update to empty")
            return
            
        if(op==1):

            cur.execute(f'Update VFX set Name ="{newvalue}" where Movie_ID={Movie_ID}')
            con.commit()

        elif(op==2):
            
            cur.execute(f'Update VFX set VFX_Director = "{newvalue}" where Movie_ID={Movie_ID}')
            con.commit()
            
        elif(op==3):
            newvalue=int(newvalue)
            if(newvalue<0):
                print("Invalid")
                return
            cur.execute(f'Update VFX set Avg_Demand ={newvalue} where Movie_ID={Movie_ID}')
            con.commit()
            
        else:
            print("Invalid Option")
            return
        
        
    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)

    return
   
def updateREQUIRES():
    try:
        Aadhar_IDold = int(input("old Aadhar ID : "))
        Movie_IDold = int(input("old VFX ID : "))
        Set_IDold = int(input("old Set ID : "))
        Director_IDold = int(input("Old director ID : "))
        Aadhar_IDnew = int(input("new Aadhar ID : "))
        Movie_IDnew = int(input("new VFX ID : "))
        Set_IDnew = int(input("new Set ID : "))
        Director_IDnew = int(input("new director ID : "))
        cur.execute(f'update REQUIRES SET Aadhar_ID = {Aadhar_IDnew}, Director_ID = {Director_IDnew}, Movie_ID = {Movie_IDnew}, SET_ID = {Set_IDnew} where Aadhar_ID = {Aadhar_IDold} and Director_ID = {Director_IDold} and Movie_ID = {Movie_IDold} and SET_ID = Set_IDold')
        con.commit()

    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)

    return

def updateCOORDINATES_WITH():
    try:

        Director_IDold = int(input("Old director id : "))
        Movie_IDold = int(input("Old VFX studio ID : "))
        Director_IDnew = int(input("New director id : "))
        Movie_IDnew = int(input("New VFX studio ID : "))
        cur.execute(f'update COORDINATES_WITH SET Director_ID = {Director_IDnew}, Movie_ID = {Movie_IDnew} where Director_ID = {Director_IDold} and Movie_ID = {Movie_IDold}')
        con.commit()

    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)

    return




def REQUIRES_del():
    try:

        Dir = int(input("Enter the Director ID of row to delete :  "))
        Mov = int(input("Enter the Movie ID of row to delete :  "))
        Aad = int(input("Enter the Aadhar ID of row to delete :  "))
        Set= int(input("Enter the Set ID of row to delete :  "))
        cur.execute(f'delete from REQUIRES where Aadhar_ID={Aad} and Director_ID={Dir} and Movie_ID={Mov} and SET_ID={Set}')
        con.commit()
        


        
    except Exception as e:
        con.rollback()
        print("Failed to Delete from REQUIRES")
        print(">>>>>>>>>>>>>", e)

    return


def Actor_del():
    
    try:

        Aad = int(input("Enter the Aadhar ID of Actor to delete :  "))
        cur.execute(f'delete from Actor where Aadhar_ID={Aad}')
        con.commit()
        


        
    except Exception as e:
        con.rollback()
        print("Failed to Delete from Actor")
        print(">>>>>>>>>>>>>", e)

    return

def Director_del():
    
    try:

        Dir = int(input("Enter the Director ID of Director to delete :  "))
        cur.execute(f'delete from Director where Director_ID={Dir}')
        con.commit()
        


        
    except Exception as e:
        con.rollback()
        print("Failed to Delete from Director")
        print(">>>>>>>>>>>>>", e)

    return


def Movie_del():
    
    try:

        Mov = int(input("Enter the Movie ID of Movie to delete :  "))
        cur.execute(f'delete from Movie_info where Movie_ID={Mov}')
        con.commit()
        


        
    except Exception as e:
        con.rollback()
        print("Failed to Delete from Movie")
        print(">>>>>>>>>>>>>", e)

    return


def VFX_del():
    
    try:

        Mov = int(input("Enter the Movie ID of VFX to delete :  "))
        cur.execute(f'delete from VFX where Movie_ID={Mov}')
        con.commit()
        


        
    except Exception as e:
        con.rollback()
        print("Failed to Delete from VFX")
        print(">>>>>>>>>>>>>", e)

    return

def Actor_Add_del():
        
    Aadhar_ID=0
    City=""
    State=""
    Country=""
    try:

        Aadhar_ID = int(input("Enter the Aadhar_ID of Actor to delete Address for :  "))
        City = input("Enter the City of the Address to delete: ")
        cur.execute(f'select State from Actor_Address_State where Aadhar_ID={Aadhar_ID} and City="{City}"')
        con.commit()
        State=fetchone()
        if(State is None):
            print("Cannot find State for given data")
            return
        else:
            State=State['State']
        cur.execute(f'select Country from Actor_Address_Country where Aadhar_ID={Aadhar_ID} and State="{State}"')
        con.commit()
        Country=fetchone()
        if(Country is None):
            print("Cannot find Country for given data")
            return
        else:
            Country=Country['Country']
        cur.execute(f'delete from Actor_Address_Country where Aadhar_ID={Aadhar_ID} and State="{State}"')
        con.commit()
        cur.execute(f'delete from Actor_Address_State where Aadhar_ID={Aadhar_ID} and City="{City}"')
        con.commit()
        cur.execute(f'delete from Actor_Address_City where Aadhar_ID={Aadhar_ID} and City="{City}"')
        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to Delete from Address")
        print(">>>>>>>>>>>>>", e)
        return
    
    return

def Director_Add_del():
        
    Director_ID=0
    City=""
    State=""
    Country=""
    try:

        Director_ID = int(input("Enter the Director_ID of Director to delete Address for :  "))
        City = input("Enter the City of the Address to delete: ")
        cur.execute(f'select State from Director_Address_State where Director_ID={Director_ID} and City="{City}"')
        con.commit()
        State=fetchone()
        if(State is None):
            print("Cannot find State for given data")
            return
        else:
            State=State['State']
        cur.execute(f'select Country from Director_Address_Country where Director_ID={Director_ID} and State="{State}"')
        con.commit()
        Country=fetchone()
        if(Country is None):
            print("Cannot find Country for given data")
            return
        else:
            Country=Country['Country']
        cur.execute(f'delete from Director_Address_Country where Director_ID={Director_ID} and State="{State}"')
        con.commit()
        cur.execute(f'delete from Director_Address_State where Director_ID={Director_ID} and City="{City}"')
        con.commit()
        cur.execute(f'delete from Director_Address_City where Director_ID={Director_ID} and City="{City}"')
        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to Delete from Address")
        print(">>>>>>>>>>>>>", e)
        return
    
    return

def VFX_Add_del():
        
    Director_ID=0
    City=""
    State=""
    Country=""
    try:

        Movie_ID = int(input("Enter the Movie_ID of VFX to delete Address for :  "))
        City = input("Enter the City of the Address to delete: ")
        cur.execute(f'select State from VFX_Address_State where Director_ID={Director_ID} and City="{City}"')
        con.commit()
        State=fetchone()
        if(State is None):
            print("Cannot find State for given data")
            return
        else:
            State=State['State']
        cur.execute(f'select Country from Director_Address_Country where Director_ID={Director_ID} and State="{State}"')
        con.commit()
        Country=fetchone()
        if(Country is None):
            print("Cannot find Country for given data")
            return
        else:
            Country=Country['Country']
        cur.execute(f'delete from Director_Address_Country where Director_ID={Director_ID} and State="{State}"')
        con.commit()
        cur.execute(f'delete from Director_Address_State where Director_ID={Director_ID} and City="{City}"')
        con.commit()
        cur.execute(f'delete from Director_Address_City where Director_ID={Director_ID} and City="{City}"')
        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to Delete from Address")
        print(">>>>>>>>>>>>>", e)
        return
    
    return


    


def SET_del():
    
    try:

        Mov = int(input("Enter the Movie ID of SET to delete :  "))
        loc= input("Enter the Location of SET to delete :  ")
        cur.execute(f'delete from Set_Location where Movie_ID={Mov} and Location_Depicted = "{loc}"')
        con.commit()
        cur.execute(f'delete from Set_Cost where Movie_ID={Mov} and Location_Depicted = "{loc}"')
        con.commit()
        cur.execute(f'delete from Set_Manpower where Movie_ID={Mov} and Location_Depicted = "{loc}"')
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to Delete from SET")
        print(">>>>>>>>>>>>>", e)

    return


def COORDINATES_WITH_del():

    try:

        Mov = int(input("Enter the Movie ID of tuple to delete :  "))
        Dir = int(input("Enter the Director ID of tuple to delete :  "))
        cur.execute(f'delete from COORDINATES_WITH where Movie_ID={Mov} and Director_ID = {Dir}')
        con.commit()
        
    except Exception as e:
        con.rollback()
        print("Failed to Delete from VFX")
        print(">>>>>>>>>>>>>", e)

    return

def showREQUIRES():

    try:
        cur.execute('Select * from REQUIRES')
        con.commit()
        rows = cur.fetchall()
        wid1=len("Movie_ID")
        wid2=len("Aadhar_ID")
        wid3=len("Director_ID")
        wid4=len("SET_ID")
        
        for row in rows:
            wid1=max(wid1,len(str(row['Movie_ID'])))
            wid2=max(wid2,len(str(row['Aadhar_ID'])))
            wid3=max(wid3,len(str(row['Director_ID'])))
            wid4=max(wid4,len(str(row['SET_ID'])))

        print(f"{'Movie_ID':<{wid1}s} : {'Aadhar_ID':<{wid2}s} : {'Director_ID':<{wid3}s} : {'SET_ID':<{wid4}s} ")
        
        for row in rows:
            print(f"{str(row['Movie_ID']):<{wid1}s} : {str(row['Aadhar_ID']):<{wid2}s} : {str(row['Director_ID']):<{wid3}s} : {str(row['SET_ID']):<{wid4}s}")
    
    except Exception as e:
        con.rollback()
        print("Failed to get  REQUIRES List")
        print(">>>>>>>>>>>>>", e)
    return

def showCOORDINATES_WITH():

    try:
        cur.execute('Select * from COORDINATES_WITH')
        con.commit()
        rows = cur.fetchall()
        wid1=len("Movie_ID")
        wid2=len("Director_ID")
        
        for row in rows:
            wid1=max(wid1,len(str(row['Movie_ID'])))
            wid2=max(wid2,len(str(row['Director_ID'])))

        print(f"{'Movie_ID':<{wid1}s} : {'Director_ID':<{wid2}s}")
        
        for row in rows:
            print(f"{str(row['Movie_ID']):<{wid1}s} : {str(row['Director_ID']):<{wid2}s}")
    
    except Exception as e:
        con.rollback()
        print("Failed to get  COORDINATES_WITH List")
        print(">>>>>>>>>>>>>", e)
    return

def Movie_Award_del():
    
    try:

        Mov = int(input("Enter the Movie ID of Award to delete :  "))
        name= input("Enter the name  of award to delete :  ")
        cur.execute(f'delete from Movie_Awards where Movie_ID={Mov} and Award_Name = "{name}"')
        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to Delete from Awards")
        print(">>>>>>>>>>>>>", e)

    return

def Actor_Accolade_del():
    
    try:

        Aad = int(input("Enter the Aadhar ID of Accolade to delete :  "))
        name= input("Enter the name  of Accolade to delete :  ")
        cur.execute(f'delete from Actor_Accolades where Aadhar_ID={Aad} and Name_of_Accolade= "{name}"')
        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to Delete from Accolades")
        print(">>>>>>>>>>>>>", e)

    return

def Director_Accolade_del():
    
    try:

        Dir = int(input("Enter the Director ID of Accolade to delete :  "))
        name= input("Enter the name  of Accolade to delete :  ")
        cur.execute(f'delete from Director_Accolades where Director_ID={Dir} and Name_of_Accolade= "{name}"')
        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to Delete from Accolades")
        print(">>>>>>>>>>>>>", e)

    return

def dispatch(ch):


    if(ch == 1):
        maxMovieRating()
    elif(ch == 2):
        minMovieRating()
    elif(ch == 3):
        AvgBudget()
    elif(ch == 4):
        sumBudget()
    elif(ch == 5):
        partialSearch()
    elif(ch == 6):
        displayMoviesbyYear()
    elif (ch == 7):
        displayMoviesbyAvgRating()
    elif (ch == 8):
        valuedActors()
    elif (ch == 9):
        numSuccDirectors()
    elif (ch == 10):
        displayMovies()
    elif (ch == 11):
        displayAwardsofMovie()
    elif (ch == 12):
        displayDirector()
    elif (ch == 13):
        displayAccoladesofDirector()
    elif (ch == 14):
        displayAddressofDirector()
    elif (ch == 15):
        displayActor()
    elif (ch == 16):
        displayAccoladesofActor()
    elif (ch == 17):
        displayAddressofActor()
    elif (ch == 18):
        displaySets()
    elif (ch == 19):
        displayVFX()
    elif (ch == 20):
        displayAddressofVFX()
    elif (ch == 21):
        showREQUIRES()
    elif (ch == 22):
        showCOORDINATES_WITH()
    elif (ch == 23):
        insertmovie()
    elif (ch == 24):
        insertMovieAward()
    elif (ch == 25):
        insertdirector()
    elif (ch == 26):
        insertDirector_Accolades()
    elif (ch == 27):
        insertDirectorAddress()
    elif (ch == 28):
        insertactor()
    elif (ch == 29):
        insertActorAccolades()
    elif (ch == 30):
        insertActorAddress()
    elif (ch == 31):
        insertset()
    elif (ch == 32):
        insertVFX()
    elif (ch == 33):
        insertVFXAddress()
    elif (ch == 34):
        insertREQUIRES()
    elif (ch == 35):
        insertCOORDINATES_WITH()
    elif (ch == 36):
        updatemovie()
    elif (ch == 37):
        updatedirector()
    elif (ch == 38):
        updateactor()
    elif (ch == 39):
        updateSET()
    elif (ch == 40):
        updateVFX()
    elif (ch == 41):
        updateREQUIRES()
    elif (ch == 42):
        updateCOORDINATES_WITH()
    elif (ch == 43):
        Movie_del()
    elif (ch == 44):
        Movie_Award_del()
    elif (ch == 45):
        Director_del()
    elif (ch == 46):
        Director_Accolade_del()
    elif (ch == 47):
        Director_Add_del()
    elif (ch == 48):
        Actor_del()
    elif (ch == 49):
        Actor_Accolade_del()
    elif (ch == 50):
        Actor_Add_del()
    elif (ch == 51):
        SET_del()
    elif (ch == 52):
        VFX_del()
    elif (ch == 53):
        VFX_Add_del()
    elif (ch == 54):
        REQUIRES_del()
    elif (ch == 55):
        COORDINATES_WITH_del()
    else:
        print("Error: Invalid Option")




while(1):
    tmp = sp.call('clear', shell=True)
    username = input("Username: ")
    password = input("Password: ")


    try:
        
        con = pymysql.connect(host='localhost',
                              user=username,
                              port=5005,
                              password=password,
                              db='MOVIE_STUDIO',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)
                print("1. Display Maximum Average Movie Rating")
                print("2. Display Minimum Average Movie Rating") 
                print("3. Display Average Budget on a Movie")
                print("4. Display Total Budget allocated on Movies till now")
                print("5. Partial Search for Movie Names")
                print("6. Project Movies Released in a Particular Year")
                print("7. Project Movies with Avg. Rating Greater than or equal to input value")
                print("8. Number of actors above given threshold value")
                print("9. Display the number of successful directors associated with")
                print("10.Show all Movies")
                print("11.Show all Awards of a Movie given its Movie_ID")
                print("12.Show all Directors")
                print("13.Show all Accolades of a Director given his ID")
                print("14.Show all Addresses of a Director")
                print("15.Show all Actors")
                print("16.Show all Accolades of an Actor given his Aadhar_ID")
                print("17.Show all Addresses of an Actor given his Aadhar_ID")
                print("18.Show all Sets")
                print("19.Show all VFX Studios")
                print("20.Show all Addressess of a VFX Studio given Movie_ID")
                print("21.Show REQUIRES Relation") 
                print("22.Show COORDINATES_WITH Relation")
                print("23.Insert a Movie")
                print("24.Insert an Award for a Movie given Movie_ID")
                print("25.Insert a Director")
                print("26.Insert an Accolade for a Director given his Director_ID ")
                print("27.Insert an Address for a Director")
                print("28.Insert an Actor")
                print("29.Insert an Accolade for an Actor")
                print("30.Insert an Address for an Actor")
                print("31.Insert a Set")
                print("32.Insert a VFX STUDIO")
                print("33.Insert an Address for a VFX Studio")
                print("34.Insert into REQUIRES relation")
                print("35.Insert into COORDINATES_WITH relation")
                print("36.Update a Movie")
                print("37.Update a Director")
                print("38.Update an Actor")
                print("39.Update a Set")
                print("40.Update a VFX Studio")
                print("41.Update REQUIRES Relation")
                print("42.Update COORDINATES_WITH Relation")
                print("43.Delete a Movie")
                print("44.Delete an Award for a Movie") 
                print("45.Delete a Director")
                print("46.Delete a Director Accolade") 
                print("47.Delete a Director Address")
                print("48.Delete an Actor")
                print("49.Delete an Accolade of an Actor ") 
                print("50.Delete an Address of an Actor")
                print("51.Delete a Set")
                print("52.Delete a VFX Studio")
                print("53.Delete a VFX Studio Address")
                print("54.Delete a tuple from REQUIRES relation")
                print("55.Delete a COORDINATES_WITH relation")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if (ch == 56):
                    break
                else :
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except:
        tmp = sp.call('clear', shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
        