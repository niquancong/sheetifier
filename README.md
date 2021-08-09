# sheetifier: a quick and dirty script to convert the mappool from a discord message to a spreadsheet

## getting started
* make sure you have python 3
* copy the mappool message into a text file (defaulted to message.txt)
* press enter and watch it work
* make sure the message is in the format of
```
skill 1
... - song name 1 (mapper 1) [diff name 1]
... - song name 2 (mapper 2) [diff name 2]

skill 2
...

```

## if the script doesn't work
* the script checks between ` - ` and `[...]` for the song name, and any text inside the last set of brackets will be deemed as the mapper
* anything inside the square brackets will be deemed as the diff name

## final notes
I'm too lazy to read the osu api to fetch teh sr and od lol sorry
Also the final .csv output might need a bit of tweaking in case the original message contains mistakes
good luck!
