# 3D GLB Model Downloader (Python Automation)

This project automates the extraction and downloading of `.glb` 3D models using Python.  
Instead of manually saving assets from Chrome DevTools, the script collects all `.glb` links and downloads them automatically.

---

## 📌 Features
- Extracts `.glb` links from text or logs
- Downloads and saves models automatically
- Files open correctly in Blender or online GLTF/GLB viewers
- Clean, lightweight solution (no heavy HAR files in repo)

---

## 🛠️ How It Works
1. Copy `.glb` links from Chrome DevTools → Network tab.  
   *(Tip: Right-click → Copy → Copy all as HAR, then extract only the URLs.)*  
2. Paste the links into a text file (`glb_links.txt`).  
3. Run the script to download all models. 
