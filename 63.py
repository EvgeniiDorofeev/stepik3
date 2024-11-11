def get_extensions(file_list):
    results = []
    def _get_extension(x):
        if "." in i:
            ext = i.split(".")[-1]
        else:
            ext = ""
        return ext
    for i in file_list:
        results.append(_get_extension(i))
    return results

print(get_extensions(["foo.txt", "bar.mp4", "python3"]))
