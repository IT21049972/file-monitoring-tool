import os
import tempfile
from unittest.mock import patch
from tkinter import filedialog
from main import calculate_file_hash

@patch('main.calculate_file_hash', return_value='hash_value')
def test_addPath(mock_hash, tmpdir):
    temp_dir = tmpdir.mkdir("temp_directory")  # Create a temporary directory

   # mock_askdirectory = patch.object(filedialog, 'askdirectory', return_value=str(temp_dir)).start()
    #mock_askdirectory.return_value = str(temp_dir)

    # Create temporary files inside the temporary directory
    temp_file1 = temp_dir.join("file1.txt")
    temp_file2 = temp_dir.join("file2.txt")
    temp_file1.write("Content of file1")
    temp_file2.write("")

    # Call calculate_file_hash directly without calling addPath
    hash_value1 = calculate_file_hash(str(temp_dir), "file1.txt")
    hash_value2 = calculate_file_hash(str(temp_dir), "file2.txt")

    #mock_askdirectory.assert_called_once()
    #mock_hash.assert_any_call(str(temp_dir), "file1.txt")
    #mock_hash.assert_any_call(str(temp_dir), "file2.txt")

    # assert hash_value1 == "0adb783b2345f60b24ef878e27e40fadd7cdbd51837ec0e5d98271ceb3e5bf3f71556968416a877f836b861490f0976443cf8625e65847511fb057a7db4cab5b"
    assert hash_value2 == "cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e"

    # Write file paths and hash values to a text file
    baseline_file = "Testbase.txt"
    with open(baseline_file, 'w') as f:
        f.write(f"file1.txt|{hash_value1}\n")
        f.write(f"file2.txt|{hash_value2}\n")

    assert os.path.isfile(baseline_file)  # Check if the file was created

    # Add any additional assertions as needed

