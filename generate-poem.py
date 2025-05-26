#! /usr/bin/env python3

from run_book import run_book


book = "generate-poem"
inputParameters = {"topic": "Prague", "author": "Franz Kafka"}
outputParameters = run_book(book, inputParameters)

print('--- output ---')
print(outputParameters)
