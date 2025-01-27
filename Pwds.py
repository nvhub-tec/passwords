
x = input("input serial number: ")

def find_password():
    
    with open ("passwords.txt", "r") as file:
        latest_password = None
        
        for line in file:
            line = line.strip().split()
            
            if len(line) < 4:
                continue
            
            sn = line[1]
            pw = line[3]
            
            if x == sn:
                latest_password = pw
                
    if latest_password == None:
        print("Serial number not found")
    else:
        print(latest_password)          
find_password()
        
        
        