# Debug journal

## Bug
- `range(1, 5)` only adds 1–4, so output was 10 instead of 55.

## AI prompts (max 3)
- What will `range(1, 5)` output when summing 1..10?
- How is `range(1, 5)` different from `range(1, 11)`?
- Is `range(1, 11)` correct for sum 1..10?

## Fix
- Changed `range(1, 5)` to `range(1, 11)`. Output is now 55.
