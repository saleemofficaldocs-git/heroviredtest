print("hello world")

#list
servers = [ "web-1", "web-02","api-01", "db-01","True","saleem","shaikh",2,3,4 ]
servers.append("api-02") # always add at end
servers.insert(2,"db-2") #add at index
servers.extend(["db-3","web-03","api-3"]) #add multiple

print(servers[1])
print("This is negetive",servers[-2])
print(servers[2])
print("THis is series",servers[1:3])
print("This is slicing",servers[0:4]) #sliceing starts from n-1

print(servers)
servers.remove("db-01") #remove value
print("This is after removing = db-01",servers)
servers.pop()
print("This is pop",servers)
print("This is Count db-3 = ",servers.count("db-3")) # used to count

#servers.sort()
#print("Sort",servers)

servers.reverse()
print("Sort revers",servers)
print(servers[9][1])