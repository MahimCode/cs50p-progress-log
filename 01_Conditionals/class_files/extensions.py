"""
def main():
    file_name = input("File name: ")
    file_type = get_file_types(file_name)
    print(f"{file_type}")


def get_file_types(file_name):
    if file_name.endswith(".gif"):
        return("image/gif")
    elif file_name.endswith(".jpg"):
        return("image/jpeg")
    elif file_name.endswith(".jpeg"):
        return("image/jpeg")
    elif file_name.endswith(".png"):
        return("image/png")
    elif file_name.endswith(".pdf"):
        return("application/pdf")
    elif file_name.endswith(".txt"):
        return("text/plain")
    elif file_name.endswith(".zip"):
        return("application/zip")
    else:
        return("application/octat-stream")


main()

"""

#dictionary of extensions

MIME_TYPES = {
    "gif": "image/gif",
    "jpg": "image/jpg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain"
}

def main():
    file_name = input("File name: ")
    file_type = get_file_types(file_name)
    print(f"{file_type}")


def get_file_types(file_name):
    ext = file_name.lower().rsplit(".",1)[1] #get the part after the last "."
    return MIME_TYPES.get(ext, "application/octet-stream")

main()