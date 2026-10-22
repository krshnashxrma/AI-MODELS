import ctypes
from ctypes import wintypes
import urllib.request
import urllib.error
import json
import subprocess
import os

class CREDENTIAL(ctypes.Structure):
    _fields_ = [
        ('Flags', wintypes.DWORD),
        ('Type', wintypes.DWORD),
        ('TargetName', wintypes.LPWSTR),
        ('Comment', wintypes.LPWSTR),
        ('LastWritten', wintypes.FILETIME),
        ('CredentialBlobSize', wintypes.DWORD),
        ('CredentialBlob', ctypes.POINTER(ctypes.c_byte)),
        ('Persist', wintypes.DWORD),
        ('AttributeCount', wintypes.DWORD),
        ('Attributes', ctypes.c_void_p),
        ('TargetAlias', wintypes.LPWSTR),
        ('UserName', wintypes.LPWSTR),
    ]

def get_token():
    CredRead = ctypes.windll.advapi32.CredReadW
    CredRead.argtypes = [wintypes.LPCWSTR, wintypes.DWORD, wintypes.DWORD, ctypes.POINTER(ctypes.POINTER(CREDENTIAL))]
    CredRead.restype = wintypes.BOOL
    p_cred = ctypes.POINTER(CREDENTIAL)()
    res = CredRead('GitHub - https://api.github.com/krshnashxrma', 1, 0, ctypes.byref(p_cred))
    if not res:
        raise Exception("Could not read token from Credential Manager")
    cred = p_cred.contents
    return ctypes.string_at(cred.CredentialBlob, cred.CredentialBlobSize).decode('utf-8').strip()

def create_private_repo(token, repo_name="AI-MODELS"):
    url = "https://api.github.com/user/repos"
    payload = json.dumps({
        "name": repo_name,
        "private": True,
        "description": "AOMe Curated Open-Source AI Models Catalog, Parameter Tiers & Architecture Registry",
        "auto_init": False
    }).encode('utf-8')
    req = urllib.request.Request(url, data=payload, headers={
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "AOMe-Setup"
    }, method="POST")
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            print(f"Created private repository: {data.get('html_url')} (private={data.get('private')})")
            return data.get('clone_url')
    except urllib.error.HTTPError as e:
        err_body = e.read().decode()
        if "already exists" in err_body:
            print(f"Repository {repo_name} already exists, proceeding to push.")
            return f"https://github.com/krshnashxrma/{repo_name}.git"
        else:
            raise Exception(f"HTTP Error {e.code}: {err_body}")

def run_git(args, cwd):
    git_bin = r"C:\Users\WELCOME\AppData\Local\GitHubDesktop\app-3.6.6\resources\app\git\cmd\git.exe"
    res = subprocess.run([git_bin] + args, cwd=cwd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Git command failed: {' '.join(args)}\nSTDOUT: {res.stdout}\nSTDERR: {res.stderr}")
    return res

def main():
    token = get_token()
    repo_url = create_private_repo(token, "AI-MODELS")
    repo_dir = r"E:\AOMe\AI-MODELS"

    # Git init
    if not os.path.exists(os.path.join(repo_dir, ".git")):
        run_git(["init", "-b", "main"], cwd=repo_dir)

    run_git(["config", "user.name", "Krishna Sharma"], cwd=repo_dir)
    run_git(["config", "user.email", "krishna442600s@gmail.com"], cwd=repo_dir)

    # Git add and commit
    run_git(["add", "."], cwd=repo_dir)
    run_git(["commit", "-m", "feat: initialize AOMe open-source AI models catalog and parameter hierarchy"], cwd=repo_dir)

    # Set remote with authenticated token
    auth_remote = f"https://krshnashxrma:{token}@github.com/krshnashxrma/AI-MODELS.git"
    clean_remote = "https://github.com/krshnashxrma/AI-MODELS.git"

    # Check if origin exists
    remotes = run_git(["remote"], cwd=repo_dir).stdout
    if "origin" in remotes:
        run_git(["remote", "set-url", "origin", auth_remote], cwd=repo_dir)
    else:
        run_git(["remote", "add", "origin", auth_remote], cwd=repo_dir)

    # Push to origin main
    print("Pushing to GitHub...")
    push_res = run_git(["push", "-u", "origin", "main", "--force"], cwd=repo_dir)
    if push_res.returncode == 0:
        print("Push successful!")
    else:
        print(f"Push output: {push_res.stderr}")

    # Clean remote to not expose token in .git/config
    run_git(["remote", "set-url", "origin", clean_remote], cwd=repo_dir)
    print("Remote sanitized to clean URL.")

if __name__ == "__main__":
    main()
