import os
path = "C:\\Users\\karth\\Documents\\py\\frontend\\nwe\\comics_generator-master\\output\\"
for i in os.listdir(path):
   if(i.endswith(".png")):
      os.remove(path+i)