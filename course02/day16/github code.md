## delete folder (local and github)
cd "D:\Nora AI Training"

git rm -r day14
git commit -m "Remove day14 folder"
git push origin main

## delete folder (only github)
cd "d:\Nora AI Training"

git rm -r --cached day18
git commit -m "Remove day18 folder from GitHub"
git push origin main


## add one folder
cd "D:\Nora AI Training"

git add day15
git commit -m "Update day15 only"
git push origin main





## add multiple folders
cd "D:\Nora AI Training"

git add day12 day13 day14
git commit -m "Update day12, day13, and day14"
git push origin main




cd "d:\Nora AI Training"

git rm -r --cached day09 day10 day11  day13 day16 day17 day18 day19 day20
git commit -m "Remove day1 to day 8 folder from GitHub"
git push origin main





cd "D:\Nora AI Training"

git add "course02/day13"
git commit -m "Add course02 day113"
git push origin main