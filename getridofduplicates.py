student = { "id1":{
    "name":"lebronjames",
    "class":"V",
    "age":"13",
    "subject":['english','maths','computer']
},
 "id2":{
    "name":"ishowspeed",
    "class":"VI",
    "age":"10",
    "subject":['PE','accounts','art']
},
 "id3":{
    "name":"lebronjames",
    "class":"V",
    "age":"13",
    "subject":['english','maths','computer']
},
 "id4":{
    "name":"michael",
    "class":"VII",
    "age":"100",
    "subject":['english','maths','computer']
}
}
new_student = {}
for key,value in student.items():
    if value not in new_student.values():
            new_student[key] = value
print(student)
print("unique dictionary : ")
print(new_student)

