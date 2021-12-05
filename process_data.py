import os
import shutil
import os

def get_category(age):
  if age == 1:
    return "1"
  elif age >= 2 and age <= 5:
    return "2-5"
  elif age >= 6 and age <= 8:
    return "6-8"
  elif age >= 9 and age <= 11:
    return "9-11"
  elif age >= 12 and age <= 14:
    return "12-14"
  elif age >= 15 and age <= 18:
    return "15-18"
  elif age >= 19 and age <= 25:
    return "19-25"
  elif age >= 26 and age <= 34:
    return "26-34"
  elif age >= 35 and age <= 54:
    return "35-54"
  elif age >= 55 and age <= 54:
    return "35-54"
  else:
    return "65+"

labels = ["1", "2-5", "6-8", "9-11", "12-14", "15-18",
          "19-25", "26-34", "35-54", "55-64", "65+"]


# make directory for each age category
for l in labels:
  path = os.path.join("face_age", l)
  if not os.path.exists(path):
    os.makedirs(path)

main_dir = "face_age"
    
directories = os.listdir(main_dir)
    
# for file_name in file_names:
#     shutil.move(os.path.join(source_dir, file_name), target_dir)

for dir in directories:
  try:
    age = int(dir)
    target_dir = os.path.join(main_dir, get_category(age))
    source_dir = os.path.join(main_dir, dir)
    for file_name in os.listdir(source_dir):
      shutil.move(os.path.join(source_dir, file_name), target_dir)
    os.rmdir(source_dir)
  except:
    continue

os.rmdir(os.path.join(main_dir, "face_age"))
