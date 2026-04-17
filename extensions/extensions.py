def main():
    extension = str((input("File Name: ").strip().replace("jpg", "jpeg").lower()))
    E = extension
    P = "."
    filetype = E.rpartition(P)[2]
    match filetype:
            case "gif"| "jpeg"| "png":
                print(f"image/{filetype}")
            case "zip"| "pdf":
                print(f"application/{filetype}")
            case "txt":
                print("text/plain")
            case _:
                print("application/octet-stream")

main()
