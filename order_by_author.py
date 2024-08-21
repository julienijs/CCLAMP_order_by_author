import pandas as pd
import os
import shutil

corpus_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'CCLAMP_Network\corpus'))
print(corpus_dir)

corpus_out_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '', 'Corpus_ordered_by_author'))
print(corpus_out_dir)

metadata_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'C-CLAMP_metadata_gender.txt'))
metadata = pd.read_csv(metadata_file_path, sep='\t')
print(metadata)

# Loop over the metadata
for _, row in metadata.iterrows():
    file_name = row['File'] + '.txt'  # Add the .txt extension
    authors = row['Author']

    # Define the source path
    src_path = os.path.join(corpus_dir, file_name)

    # Check if the file exists before proceeding
    if not os.path.exists(src_path):
        print(f"File not found: {src_path}. Skipping.")
        continue

    # Check if authors is a string (i.e., not NaN)
    if isinstance(authors, str):
        # Split multiple authors by ';' and trim whitespace
        authors = [author.strip() for author in authors.split(';')]
    else:
        # Place in "No_Author" folder if author is missing
        authors = ["No_Author"]

    for author in authors:
        # Define the destination path
        dest_dir = os.path.join(corpus_out_dir, author)
        dest_path = os.path.join(dest_dir, file_name)

        # Create the destination directory if it doesn't exist
        os.makedirs(dest_dir, exist_ok=True)

        # Copy the file to the destination directory
        shutil.copy(src_path, dest_path)

print("Files grouped by author successfully!")
