# Frequency-Analyzer
Frequency Analysis is quite a common way to analyze substitution ciphers (can be extended to other encryptions with cleverness).  This tool aims to provide users 
with a quick way to see count and percentage of characters used in the  given text through a python script. This tool can also substitute according to the frequency hierarchy.


The synthax to use this code is as follows-
```
$ python script.py (-s/-f/-sf/-fs/-h/--help) [file]
```

```-f``` would output a table consisting of characters ordered according to their frequency, their count, percentage, and what the expected substitution is according to 
the standard frequency table.

```-s``` would output the text after substitution in correspondence with frequency table.

```-sf/-fs``` would output both the above analysis.
