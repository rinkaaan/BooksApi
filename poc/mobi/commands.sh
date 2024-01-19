# Install ebook-convert
brew install calibre --cask

# Convert mobi to txt
ebook-convert test.mobi test.txt

# Get thumbnail
ebook-meta test.mobi --get-cover test.jpg --to-opf test.opf
