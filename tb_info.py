from teambition import *
import json
import csv
import re
client_id = '8xxxxx'
client_secret = 'b57xxxx'
code = '8LFrxxxx'
token = "eyJhbG"
refresh_token = "NLBLyxxxxx"
# print(token)

tb = Teambition(client_id, client_secret, access_token=token)
tb.oauth.check()
task = tb.tasklists.get_tasks(id="5b769418eb6c5800184194cd")
print(task)
# tsk = tb.tasklists.get(project_id='5b769418eb6c5800184194b6')
# proj = tb.projects.get(id='5b769418eb6c5800184194b6')
# print(proj)
# tasks = tb.projects.get_tasks(id='5b769418eb6c5800184194b6', page=2)
# a = 0
# try:
#     for s in tasks:
#         print('name=', s["executor"]["name"])
#         if s["executor"]["name"] == "张全":
#             a += 1
#     print(a)
# except:
#     print('a=', a)
# with open('sth.txt','w') as f:
#     f.write(str(tasks))



# try:
#     me = tb.users.me()
#     # print(me)
#
#     proj_id = '5b769418eb6c5800184194b6'
#     proj = tb.projects.get(id=proj_id, team_id='')
#     # print('proj==', proj)
#
#     tasks = tb.projects.get_tasks(id=proj_id, page=2)
#     print(type(tasks[0]))
#     print(len(tasks))
#     f = csv.writer(open("Z2.csv", "w+"))
#     pattern = re.compile('\d+')
#     for s in tasks:
#         a = str(s["created"])
#         b = str(s['updated'])
#         result = pattern.findall(a)
#         updated = pattern.findall(b)ßß
#         created = '/'.join(result[:-1])
#         updated = '/'.join(updated[:-1])
#         # print('customfields=', s["customfields"][0])
#         if s["customfields"] == []:
#             content = ''
#         else:
#             print('customfields=', s["customfields"][0]['value'][0]['title'])
#             content = s["customfields"][0]["value"][0]["title"]
#
#         if s["executor"]==None:
#             executor = ""
#         else:
#             executor = s["executor"]["name"]
#         f.writerow([s["_id"],
#                     # s["_creatorId"],
#                     # s["_executorId"],
#                     # s["_tasklistId"],
#                     executor,
#                     created,
#                     updated,
#                     content,
#                     s["content"],
#                     ])
#
# except TeambitionException as e:
#     print(e)

