

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

for kv in users:
    # if kv == "Instructors":
    print kv
    tim=1
    for i in users[kv]:
        print tim,"-",i["first_name"],i["last_name"],"-",len(i["first_name"])+len(i["last_name"])
        tim+=1
     
            