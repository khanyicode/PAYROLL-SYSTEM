import json

employees = [
    {"id": 1, "name": "John Loots", "position": "Manager", "salary": 50000},
    {"id": 2, "name": "Jane Nkosi", "position": "Developer", "salary": 45000},
    {"id":3,"name":"John Nolan","position":"Security Guard","salary": 18000},
    {"id":3,"name":"Mpho Dube","position":"Project Manager","salary": 18000},
    {"id":4,"name":"Ayanda Ngobeni","Position":"Director","salary":40000},
    {"id":5,"name":"cindy Dube","Position":"software enginner","slaray":70000}
]

with open('employees.json', 'w') as file:
    json.dump(employees, file)