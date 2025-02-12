#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2025-02-12
"""
from openai import OpenAI
import os

marker = 'marker'
def func():
    client = OpenAI(api_key=os.getenv("OPEN_KEY"))
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": "Write a haiku about recursion in programming."
            }
        ])
    print(completion.choices[0].message)

def main():
    this_file_name = os.path.basename(__file__)
    print("File being run is:", this_file_name)
    func()

if __name__ == '__main__':
    main()