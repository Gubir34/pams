#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess
import requests
from git import Repo
import time
import sys

# ----------------- Yardımcı Fonksiyonlar -----------------

def format_repo_name(name):
    """Boşlukları alt çizgiye çevir, küçük harf yap"""
    return name.lower().replace(" ", "_")

def print_progress(percent, name):
    bar = "#" * (percent // 2) + "-" * (50 - percent // 2)
    print(f"\r{percent}% [{bar}] Installing {name}...", end="", flush=True)

def get_mainfile_from_pams(path):
    """pams.txt varsa mainfile oku, yoksa main.py kullan"""
    pams_file = os.path.join(path, "pams.txt")
    if os.path.exists(pams_file):
        with open(pams_file, "r") as f:
            for line in f:
                if line.startswith("mainfile"):
                    return line.split("=")[1].strip()
    default_main = os.path.join(path, "main.py")
    if os.path.exists(default_main):
        return "main.py"
    return None

def clone_or_update_repo(repo_url, clone_path):
    """Repo yoksa klonla, varsa pull et"""
    if os.path.exists(clone_path):
        repo = Repo(clone_path)
        repo.remotes.origin.pull()
    else:
        Repo.clone_from(repo_url, clone_path)

# ----------------- PAMS Ana Fonksiyon -----------------

def install_program(program_name):
    print(f"----Python Application Management System----")
    print(f"Installing {program_name}...")

    # GitHub API ile arama
    search_url = f"https://api.github.com/search/repositories?q={program_name}"
    response = requests.get(search_url).json()
    if "items" not in response or len(response["items"]) == 0:
        print(f"Repo {program_name} bulunamadı!")
        return

    # İlk sonucu al, repo adını uygun hale getir
    repo_url = response["items"][0]["clone_url"]
    repo_name = response["items"][0]["name"]
    formatted_name = format_repo_name(repo_name)

    # Repo klonlama dizini
    clone_path = os.path.join("repos", formatted_name)
    os.makedirs("repos", exist_ok=True)

    # Simüle edilmiş yükleme ilerlemesi
    for i in range(0, 101, 5):
        print_progress(i, formatted_name)
        time.sleep(0.03)

    # Repo klonla veya güncelle
    clone_or_update_repo(repo_url, clone_path)

    # Mainfile tespit
    mainfile = get_mainfile_from_pams(clone_path)
    print_progress(100, formatted_name)
    print("\nInstallation complete!")

    # Mainfile çalıştır
    if mainfile:
        mainfile_path = os.path.join(clone_path, mainfile)
        if os.path.exists(mainfile_path):
            subprocess.run([sys.executable, mainfile_path])
        else:
            print(f"{mainfile} bulunamadı!")
    else:
        print("main.py veya pams.txt bulunamadı.")

# ----------------- CLI Entry Point -----------------

def main():
    if len(sys.argv) < 3 or sys.argv[1] != "install":
        print("Usage: pams install <program_name>")
        return
    program_name = sys.argv[2]
    install_program(program_name)

if __name__ == "__main__":
    main()
