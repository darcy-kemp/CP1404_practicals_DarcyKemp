"""CP1404 | prac_06 languages | Darcy Kemp
Program to test a class then print ones that meet criteria.
est:30
real:26
"""
from Prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

objects = [python, ruby, visual_basic]
print("The dynamically typed languages are:")

for language in objects:
    if language.is_dynamic():
        print(language.name)
