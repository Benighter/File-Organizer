# File Organizer

## Description

This Python script automates the organization of various file types in the Downloads folder into their respective directories. It supports images, music, videos, PDFs, PowerPoint presentations, Excel sheets, executables, and compressed files.

## Features

- Automatically detects and moves files to designated folders.
- Supports a wide range of file extensions.
- Easy to run with a simple double-click on a batch file.

## Prerequisites

- Python installed on your system.
- Necessary read/write permissions for the Downloads folder.

## Usage

To use this script, follow these steps:

1. Ensure Python is installed and properly set up on your system.
2. Download the `organize_files.py` script.
3. Modify the `downloads_path` in the script to match your Downloads folder path.
4. Run the script:
   - Via command line: `python organize_files.py`
   - Via batch file: Double-click `organize_files.bat`

## File Organization

The script organizes files into the following folders:

- `Music`: For `.mp3`, `.wav`, `.aac`, `.flac`, `.alac`, `.ogg` files.
- `Videos`: For `.mp4`, `.m4v`, `.mov`, `.avi`, `.wmv`, `.flv`, `.mkv` files.
- `PDF`: For `.pdf` files.
- `PowerPoint`: For `.ppt`, `.pptx` files.
- `Excel`: For `.xls`, `.xlsx`, `.csv` files.
- `Executables`: For `.exe` files.
- `Compressed`: For `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, `.bz2` files.
- `Images`: For `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.webp` files.

## Contributing

Contributions to improve the script are welcome. Please fork the repository and submit a pull request with your changes.

## License

MIT License

## Disclaimer

Use this script at your own risk. Always back up your data before running the script to prevent any accidental loss of files.
