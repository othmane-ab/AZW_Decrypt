import ocrmypdf

ocrmypdf.ocr('Book_Test.pdf', 'Book_test_out.pdf', deskew=True, language="jpn")
