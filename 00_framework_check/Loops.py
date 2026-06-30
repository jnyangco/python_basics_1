import argparse
import os

parser = argparse.ArgumentParser(conflict_handler='resolve')
parser.add_argument('-test-parameter', help='Test parameter here', default='All')
parser.add_argument('-tag', help='suite1', default='All')

args = parser.parse_args()

print(args.tag)
for root, directories, files in os.walk(args.tag):
    for directory in directories:
        print(directory)

print("========== TAGS ==========")
tags = "@cms1,@login"
for tag in tags.split(","):
    print(tag)

print("========== TAGS ==========")
feature_line_tag = "@cms1  @login"
print(feature_line_tag.split("@"))
if "@" in feature_line_tag:
    for line in feature_line_tag.split("@"):
        print(line.strip())

print("========== FILE ==========")
path1 = "Behave/features/current_regression/cms/cms_access_permission_part2.feature"
folders = path1.split("/")
print(folders[2])

print("========== CHECK RUN SET - TOTAL FEATURE FILES ==========")
run_set = ['test1.feature', 'test2.feature', 'test3.feature']
print(f"Total Run Set = {len(run_set)}")
if len(run_set) == 0:
    print("No Test Selected")

print("========== CHECK RUN SET - TOTAL FEATURE FILES ==========")
path2 = 'Behave/features/current_regression/cms/cms_admin_page_ui.feature'
feature_file = path2.split("/")[-1]
print("Path: path2 = 'Behave/features/current_regression/cms/cms_admin_page_ui.feature'")
print(f"Feature File = {feature_file}")

print("========== SCAN LIST + Print Range ==========")
list1 = ['Test1', 'Test2', 'Test3', 'Test4']
for index, item in enumerate(list1):
    print(f"{index} -- {item.strip()}")
print("---------- starts from 1 ----------")
for index, item in enumerate(list1, 1):
    print(f"{index} -- {item.strip()}")

print("========== GO TO IF + ELIF ==========")
text = "1A"
if "1" in text:
    print("Present -> 1")
elif "A" in text:
    print("Present -> A")

print("========== CHECK IF EMPTY LIST ==========")
list2 =  []
is_empty = False
if not list2: # false (not true)
    print("List 2 is empty")
    is_empty = True
else: # true
    print("List 2 is not empty")

