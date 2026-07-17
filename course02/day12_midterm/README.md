# Day 12

Build PDF: `pdflatex lesson.tex` or run `scripts/build-all.ps1`.


A
1. Empty cell — Row 3 Shield has no qty.
2. Word instead of number — Row 4 price is fifty, not 50.
3. Extra spaces — Last row has Sword and 200 with spaces.
4. Duplicate row — Row 2 and Row 6 are identical (Potion,2,50,Mon).
5. Blank row — Line 8 is empty

Setup (1-14)
Read data (18-24)
Clean row by row (26-57)
Remove blank rows → Trim whitespace → Convert words to numbers → Delete rows with empty quantity → Deduplicate