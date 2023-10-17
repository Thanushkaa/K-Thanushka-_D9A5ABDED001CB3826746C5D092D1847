#leap year

def checkYear(year): 

    

    # Return true if year is a multiple 

    # of 4 and not multiple of 100. 

    # OR year is multiple of 400. 

    import calendar

    return(calendar.isleap(year)) 

    
# Driver Code  

year = 2000

if (checkYear(year)): 

    print("Leap Year") 

else: 

    print("Not a Leap Year") 

        
# This code is contributed by Chin9