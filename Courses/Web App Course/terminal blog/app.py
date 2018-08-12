__author__ = 'mike'

import pymongo
from pprint import pprint


uri = 'mongodb://127.0.0.1:27017'
client = pymongo.MongoClient(uri)
database = client['fullstack']
collection = database['students']

students = collection.find({})
#student_list = []

for i in students:
    print (i)

student_list = [student for student in collection.find({})]
new_list = [student for student in collection.find({}) if student['mark'] > 50]
#adding list comprehension

print (new_list)

#student_list = [student['mark'] for student in collection.find({})] #grab only mark
print (student_list)

for i in student_list:
    print (i['name'])
    print (i['_id'])





# client = pymongo.MongoClient('localhost',27017)
# db = client.fullstack
# collection = db.students.find()
#
# for i in collection:
#     print (i)
# print ('down here')
#
#
#
# uri = 'mongodb://127.0.0.1:27017'
# client = pymongo.MongoClient(uri)
# database = client.fullstack
# collection = database.students.find()
#
# print ('test')
#
# for i in collection:
#     print(i)



# stud = collection.find()
# print (stud)
#
# for student in stud:
#     print ('test')
#     print (student)