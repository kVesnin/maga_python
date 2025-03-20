from latex import generate_latex_table

data = [
    ["Name", "Age", "City"],
    ["Konstantin", 22, "Moscow"],
    ["Aidar", 30, "Kazan"],
    ["Olesya", 23, "Moscow"]
]

latex_table = generate_latex_table(data)

latex_document = f"""\\documentclass{{article}}
\\begin{{document}}
{latex_table}
\\end{{document}}"""

with open("artifacts/usage_latex_example.tex", "w") as f:
    f.write(latex_document)