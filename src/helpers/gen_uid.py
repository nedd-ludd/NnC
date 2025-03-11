#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2025-02-13
"""
from datetime import datetime
import uuid
import os
marker = 'marker'


def generate_custom_uid():
    """Creates custom uid same char length and format as nextcloud calendar"""
    timestamp = datetime.utcnow().strftime("%Y%m%d")

    static_id = "NnCy-AdDs-tHiS"

    uuid_suffix = str(uuid.uuid4()).replace(
        "-", "")[:12]  # First 12 hex characters
    custom_uid = f"{timestamp}-{static_id}-{uuid_suffix}"

    return custom_uid


def main():
    this_file_name = os.path.basename(__file__)
    print("File being run is:", this_file_name)
    uuid = generate_custom_uid()
    print(uuid)

if __name__ == '__main__':
    main()