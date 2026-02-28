courses = df["Course"].unique()
for course in courses:
    df[df["Course"] == course].to_csv(f"../output/{course}_students.csv", index=False)
