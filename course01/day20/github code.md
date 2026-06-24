## delete folder (local and github)
cd "D:\Nora AI Training"

git rm -r day14
git commit -m "Remove day14 folder"
git push origin main

## delete folder (only github)
cd "d:\Nora AI Training"

git rm -r --cached day14
git commit -m "Remove day14 folder from GitHub"
git push origin main


## add one folder
cd "D:\Nora AI Training"

git add day20
git commit -m "Update day20 only"
git push origin main





## add multiple folders
cd "D:\Nora AI Training"

git add day12 day13 day14
git commit -m "Update day12, day13, and day14"
git push origin main