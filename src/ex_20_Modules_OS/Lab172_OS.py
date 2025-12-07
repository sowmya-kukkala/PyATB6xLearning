import os

print(os.name) # nt
print(os.getcwd()) # C:\Users\Sowmya\PycharmProjects\PyATB6xLearning\src\ex_20_Modules_OS

# print(os.mkdir("AI")) # Creates a folder under current path (in above)
print(os.listdir()) # ['AI', 'Lab172_OS.py']

# Note: create a AI.txt file to run the below command
# print(os.remove("AI.txt"))

# Note: create a AI.txt file to run the below command
# print(os.rename("AI.txt", "testdata.txt")) # Renames the AI.txt file to testdata.txt

# To get the environment variable
print(os.environ.get('PATH'))

# C:\Users\Sowmya\PycharmProjects\PyATB6xLearning\.venv\Scripts;C:\Program Files\Common Files\Oracle\Java\javapath;C:\Program Files (x86)\VMware\VMware Workstation\bin\;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Windows\System32\OpenSSH\;C:\Program Files\dotnet\;C:\Program Files (x86)\NVIDIA Corporation\PhysX\Common;C:\Program Files\NVIDIA Corporation\NVIDIA App\NvDLISR;C:\Program Files\nodejs\node_modules;C:\Program Files\Java\jdk-17\bin;C:\Program Files\Git\cmd;C:\Users\Sowmya\AppData\Local\Programs\Python\Python313\Scripts\;C:\Users\Sowmya\AppData\Local\Programs\Python\Python313\;C:\Users\Sowmya\AppData\Local\Microsoft\WindowsApps;C:\Users\Sowmya\AppData\Roaming\npm;C:\Program Files\JetBrains\PyCharm 2025.2.1\bin;C:\Users\Sowmya\AppData\Local\Programs\Ollama