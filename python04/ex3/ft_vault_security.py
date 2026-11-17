#!/usr/bin/env python3


def secure_archive(filename: str, op: str = "r",
                   wcontent: str = "") -> tuple[bool, str]:
    is_error: bool = True
    content: str = ""
    try:
        with open(filename, op) as f:
            match op:
                case "r":
                    content = f.read()
                case "w":
                    f.write(wcontent)
                    content = "Content successfully written to file"
                case _:
                    raise Exception("Operation should be either \
'r' (read) or 'w' (write)")
    except Exception as ex:
        is_error = False
        content = f"{ex}"

    return (is_error, content)


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    secure_content: tuple[bool, str] = secure_archive("/non/existing/file")
    print(secure_content)

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    secure_content = secure_archive("/etc/shadow")
    print(secure_content)

    print("\nUsing 'secure_archive' to read from a regular file:")
    secure_content = secure_archive("datashard.txt")
    print(secure_content)

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    secure_content = secure_archive("test", "w", secure_content[1])
    print(secure_content)


if __name__ == "__main__":
    main()
