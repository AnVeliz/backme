import argparse
import datetime
import os
import tarfile
import glob
from pathlib import Path
from fnmatch import fnmatch


def archive_folder(source_folder: str, target_folder: str, skip_patterns: list) -> str:
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    archive_file = os.path.join(target_folder, f"archive_{timestamp}.tar.gz")

    os.makedirs(target_folder, exist_ok=True)

    with tarfile.open(archive_file, "w:gz") as tar:
        for root, _, files in os.walk(source_folder):
            for file in files:
                file_path = os.path.join(root, file)

                # Check if the file matches any of the skip patterns
                skip = False
                path = Path(source_folder)
                for pattern in skip_patterns:
                    skip_current_pattern_files = list(path.glob(pattern))
                    for skip_current_pattern_file in skip_current_pattern_files:
                        if os.path.abspath(file_path) == os.path.abspath(skip_current_pattern_file):
                            skip = True
                            break

                if not skip:
                    relative_path = os.path.relpath(file_path, source_folder)
                    tar.add(file_path, arcname=relative_path)

    return archive_file


def main():
    parser = argparse.ArgumentParser(description="Archive a folder into a tar.gz file")
    parser.add_argument("-y", "--yes", action="store_true", help="Do not ask to cofirm the operation")
    parser.add_argument("-f", "--folder", default="./data", help="Folder to archive")
    parser.add_argument("-t", "--target", default="./data_archive/", help="Target folder for the archive")
    parser.add_argument("-s", "--skip", default=["**/node_modules/*"], nargs="+", help="Skip patterns using wildcards (* and ?)")

    args = parser.parse_args()

    print(f"Folder to archive: {args.folder}")
    print(f"Target folder: {args.target}")
    print(f"Skip patterns: {args.skip}")

    if not args.yes:
        choice = input("Press Y to start the archiving process (or any other key to cancel): ")
        if choice.lower() != "y":
            print("Archiving process canceled.")
            return

    archive_file = archive_folder(args.folder, args.target, args.skip)
    print(f"Archiving completed. Archive file created at: {archive_file}")


if __name__ == "__main__":
    main()
