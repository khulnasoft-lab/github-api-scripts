#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Md Sulaiman (infosulaimanbd@gmail.com)"
__version__ = "0.1.0"
__license__ = "MIT"

import os
import json
import string
import base64
import argparse
import logging
import thepower
from pathlib import Path
from datetime import datetime


def main(args):

    power_config = thepower.read_dotcom_config(args.power_config)
    args.extension = power_config.get('dummy_section','file_extension').strip('"')
    args.default_committer = power_config.get('dummy_section','default_committer',).strip('"')

    for fn in ['test-data/App.java_', 'test-data/AppTest.java_']:
        p = Path(fn)
        w = p.name[:-1]
        
        json_file = f"""tmp/{w}.json"""
        with open(p, 'rb') as ct:
           t = {}
           chapter_content = ct.read()
           chapter_base64 = base64.encodebytes(chapter_content)
           t["message"] = f"""A java file."""
           t["committer"] = {}
           t["committer"]["name"] = args.default_committer
           t["committer"]["email"] = f"noreply+{args.default_committer}@example.com"
           t["content"] = chapter_base64.decode('UTF-8')
           with open(json_file, 'w') as out_file:
              out_file.write(json.dumps(t))


    # Create the pom.xml template
    px = open(Path("test-data/java/maven/maven-pom.xml_"), "r")
    px_content= px.read()
    px_template = string.Template(px_content)
    pom_xml_file= Path("tmp/maven-pom.xml")
    values = {}
    values["org"] = power_config.get('dummy_section','org',).strip('"')
    with open(pom_xml_file, "w") as out_file:
        out_file.write(px_template.substitute(values))

    json_file = f"""tmp/maven-pom.json"""
    with open(pom_xml_file, 'rb') as ct:
       t = {}
       chapter_content = ct.read()
       chapter_base64 = base64.encodebytes(chapter_content)
       t["message"] = f"""A java file."""
       t["committer"] = {}
       t["committer"]["name"] = args.default_committer
       t["committer"]["email"] = f"noreply+{args.default_committer}@example.com"
       t["content"] = chapter_base64.decode('UTF-8')
       with open(json_file, 'w') as out_file:
          out_file.write(json.dumps(t))


if __name__ == "__main__":
    """Create files for a maven project."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--power-config", action="store", dest="power_config", default=".gh-api-examples.conf", help="This is the config file to use to access variables for the power.")
    parser.add_argument("-e", "--extension", action="store", dest="extension", default="c")
    args = parser.parse_args()

    main(args)
