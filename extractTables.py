import tabula

tables = tabula.read_pdf("./table.pdf", pages="all")

df = tables[0]

with open("./output/table.txt", "w") as f:
    print(df, file=f)


