#! /usr/bin/env python3

from run_book import run_book


book = "generate-course"
inputParameters = {"topic": "Prague history", "language": "Čeština"}
outputParameters = run_book(book, inputParameters)

print('--- output ---')
print(outputParameters)
