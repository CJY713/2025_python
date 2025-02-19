import numpy as np

# Class
class Person:
    # self是一個標記牌子, 告訴別人有self的變數、函數屬於Person類別
    def __init__(self,name,age):
        self.person_name = name
        self.age = age
    def introduce(self):
        # 同一類別的東西可以互相使用,這裡直接把self.person_name跟self.age做使用
        return f"Hello, my name is {self.person_name}.\nI'm {self.age} years old."
    
#實例化
person = Person('John',15)      #也可以設定型態 person: object = Person('John',15)
print(person.age)               #person的age
print(person.person_name)       #person的person_name
print(person.introduce())       #person的介紹函數
    
"""
class 的繼承
新的 class 可以繼承原有的class所有屬性、函數
"""
class Students(Person):
    def __init__(self, name, age, classroom:str, country='台灣'):
        super().__init__(name,age)
        # 把Person的self.person_name和self.age功能繼承過來
        self.classroom = classroom      # 專屬於Students的self.classroom
        self.country = country 
    def where_class(self) -> str:       # -> 通常用於函數或方法的返回值類型指定。
        return f'我在{self.classroom},住在{self.country}'

# 實例化 Students
student1 = Students('Peter',8,'二年二班')
print(student1.person_name)         # student1使用繼承來的age
print(student1.age)                 
print(student1.introduce()) 
print(student1.classroom) 
print(student1.where_class()) 
student2 = Students('Bob',10,'A班','美國')      # 預設台灣,放美國就美國
print(student2.where_class()) 
