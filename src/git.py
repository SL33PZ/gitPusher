import os
import shutil
from subprocess import PIPE, Popen, run
from threading import Thread



class gitPusher(Thread):
    def __init__(self,repo_path="", dirs=".", message="", repo_url="", branch="master", access_token=""):
        Thread.__init__(self)
        self.repo_path = repo_path
        self.dirs = dirs
        self.message = message
        self.repo_url = repo_url
        self.branch = branch
        self.access_token = access_token
    
    def run(self):
        os.chdir(self.repo_path)
        
        if os.path.exists(".git"):
            shutil.rmtree(".git")    
                
        self.initialize()
        self.add()
        self.status()
        self.commit()
        self.remote()
        print(f"""
              
              
              
              Access Token: {self.access_token}
              
              
              
              """)
        self.push()

    def initialize(self) -> None:
        run("git init", shell=True)

    def add(self) -> str:
        run(f"git add {self.dirs}", shell=True)
    
    def status(self) -> None:
        run("git status", shell=True)
    
    def commit(self) -> str:
        run(f"git commit -m '{self.message}'", shell=True)
    
    def remote(self) -> str:
        run(f"git remote add origin {self.repo_url}", shell=True)
    
    def push(self):    
        p = Popen(f"git push origin master", shell=True, stdin=PIPE)
        stdout, stderr = p.communicate()