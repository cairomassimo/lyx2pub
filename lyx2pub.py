"""LyX2Pub -- combine LyX with any LaTeX template for publishing.

Usage:
  lyx2pub [options] <file.lyx>

Options:
  <file.lyx>  
  -t --template=<template.tex>  Template file (where %DOCUMENT% is replaced with the content)
"""
import re
import subprocess

from docopt import docopt

document_replace = "%DOCUMENT%"

document_re = re.compile(r"\\begin\{document\}(.*)\\end\{document\}", flags=re.DOTALL)


def lyx2pub(input_path, template_path):
    export_path = "lyx2pub_export.tex"
    output_path = "lyx2pub_output.tex"
    
    subprocess.run(
        [
            "lyx",
            "-E", "pdflatex", export_path,
            input_path,
        ],
    )

    with open(export_path) as f:
        data = f.read()

    with open(template_path) as f:
        template = f.read()

    content = document_re.search(data).group(1)
    assert document_replace in template
    combined = template.replace(document_replace, content)

    with open(output_path, "w") as f:
        f.write(combined)


def main():
    args = docopt(__doc__)

    lyx2pub(
        input_path=args["<file.lyx>"],
        template_path=args["--template"],
    )
