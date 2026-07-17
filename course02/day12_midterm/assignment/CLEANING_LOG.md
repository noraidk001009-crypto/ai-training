# Midterm cleaning log

- Input file: `messy_shop.csv` (6 data rows)
- Output file: `clean_shop.csv` (4 data rows)
- Total issues handled: 4

## Per-row fixes

- Row 3: qty was empty, row removed.
- Row 4: price was word 'fifty', converted to '50'.
- Row 6: duplicate of existing record (Potion,2,50,Mon), removed.
- Row 7: fields had extra whitespace, trimmed.
