data = """101, "Widget A", $10.50, USA
102, Widget B, $5.00, Canada
103, Widget A, 10.50, USA
"""

with open("sales.csv", "w") as f:
    f.write(data)

print("sales.csv created!")
