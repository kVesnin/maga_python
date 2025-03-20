from latexlib_kavesnin import generate_latex_image, generate_latex_table

data = [
    ["Name", "Age", "City"],
    ["Konstantin", 22, "Moscow"],
    ["Aidar", 30, "Kazan"],
    ["Olesya", 23, "Moscow"]
]
latex_table = generate_latex_table(data)

latex_image = generate_latex_image("artifacts/geometry.png")

latex_document = f"""\\documentclass{{article}}
\\usepackage{{graphicx}}
\\begin{{document}}
{latex_table}

{latex_image}
\\end{{document}}"""

with open("artifacts/final_image_with_table.tex", "w") as f:
    f.write(latex_document)

import os
os.system("pdflatex -output-directory=artifacts artifacts/final_image_with_table.tex")