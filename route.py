from fastapi import APIRouter, HTTPException, Body
from .config import config
from app.models.settings.crud import settings
import os

bp = APIRouter()

# @bp.post("/listen",description="TODO:拒绝从github以外的来源")
# def read(data = Body(...)):
#     commit_message = data["commits"][0]["message"]
#     print(commit_message)

#     # 如果消息为d则删库
#     if "del_db" in commit_message:
#         request = os.popen("rm -f db.sqlite")
#         print("删除数据库")

#     # delete
#     if "del_settings" in commit_message:
#         request = os.popen("rm -f settings.yml")
#         print("删除settings")

#     # 更新Python包,在import前先录入和更新好
#     if "pk_update" in commit_message:
#         request = os.popen("pip3 install -r requirements.txt")
#         print(request.read())
#     # 备份各样东西
#     # packager.dump()

#     # 
#     if "un_update" not in commit_message:
#         print("不更新")
#         # pull的执行
#         request = os.popen("git pull --ff-only")
    

@bp.post("/{target}",description="TODO:拒绝从github以外的来源")
def read(target:str, data = Body(...)):
    if len(data) != 0:
        commit_message = data["commits"][0]["message"]
        if "-!update-" in commit_message:
            print("do not update")
            return
    path = get_rule()[target]
    request = os.popen(f"git -C {path} pull")
    print(request.read())


# def get_rule():
#     from . import route
#     path = route.__file__[2:-8] + "settings.yml"
#     return settings.load(path)["update_rule"]

