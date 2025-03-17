import os
import shutil
import platform

name = "Autovisor"
system = platform.system()
icon_param = ""

if system == "Darwin":  # macOS系统
    icon_param = "--icon=./res/zhs.icns"
else:  # Windows系统
    icon_param = "--icon=./res/zhs.ico"

pyinstaller_cmd = (
    f"pyinstaller "
    f"--log-level=INFO "
    f"--noconfirm "
    f"-c "
    f"{icon_param} "
    f"--onedir "
    f"--contents-directory=internal "
    f"--name={name} "
    f"./Autovisor.py "
    f"--exclude-module cv2 "
    f"--exclude-module numpy "
)

os.system(pyinstaller_cmd)

# 创建资源目录并复制文件
dist_res_dir = f"./dist/{name}/res"
if not os.path.exists(dist_res_dir):
    os.mkdir(dist_res_dir)
    
shutil.copyfile("./res/QRcode.jpg", f"{dist_res_dir}/QRcode.jpg")
shutil.copyfile("./configs.ini", f"./dist/{name}/configs.ini")
shutil.copyfile("./res/stealth.min.js", f"{dist_res_dir}/stealth.min.js")

# 清理构建文件
shutil.rmtree("./build", ignore_errors=True)
os.remove(f"./{name}.spec")
