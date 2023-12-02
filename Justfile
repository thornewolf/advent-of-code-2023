_:
    just --list
# Create advent of code solution for the day.
day day:
    cp template.py d{{day}}.py
    code d{{day}}.py

commit:
    git add .
    git commit -m "Posting solution."
    git push