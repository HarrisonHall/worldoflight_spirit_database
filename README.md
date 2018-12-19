# World of Light Spirit Databasing
I wanted to practice some databasing skills, so I created a short script to pull
spirit data from Super Smash Bros. Ultimate on Fandom into a csv file. At the 
time I figured that fandom would all of the data necessary for the spirits, but 
it appears to be an ongoing effort. Running `parse.py` will remake `spirits.csv` 
with the newest online data.

## Basic Parsing
`spirits.csv` has the format `Spirit, Artwork Origin, Rating, Type, Support Slots, Ability`. 
* Basic command-line sorting
  1. Using `head`, `grep`, and `sort`
     * ex// `head -1 spirits.csv; grep "Mario" spirits.csv | sort -t , -k 6 -n -r`
  2. Using `head`, `awk`, and `sort`
     * ex// `head -1 spirits.csv; awk '/Mario/' spiritis.csv | sort -t , -k 6 -n -r`
* `search.py`
  * Program is self explanatory
  * Launch with `python3 search.py`
* `sqlsearch.py`
  * TODO
