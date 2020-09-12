def finder(files, queries):
    file_names = {}
    for path in files:
        file_name = path.split("/")[-1]
        if file_name in file_names:
            file_names[file_name].append(path)
        else:
            file_names[file_name] = [path]

    return [path for paths in [file_names[query]
                               for query in queries if query in file_names] for path in paths]


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
