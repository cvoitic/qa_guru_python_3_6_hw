import zipfile
import os.path
from os.path import basename
from PyPDF2 import PdfReader
from openpyxl import load_workbook
import csv

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources")  # файлы для архива
path_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "files")
path_zip = os.path.join(path_file, "myzip.zip")  # сам архив
file_dir = os.listdir(path)


# создаю архив
with zipfile.ZipFile(path_zip, mode="w", compression=zipfile.ZIP_DEFLATED) as archive:
    for file in file_dir:
        add_file = os.path.join(path, file)
        archive.write(add_file, basename(add_file))


def test_pdf():
    with zipfile.ZipFile(path_zip) as archive:
        pdf_file = archive.extract("test_PDF.pdf")
        reader = PdfReader(pdf_file)
        page = reader.pages[0]
        text = page.extract_text()
    assert 'Тестовый PDF' in text, f"Expected result: {'Тестовый PDF'}; actual result: {text}"
    os.remove(pdf_file)


def test_xlsx():
    with zipfile.ZipFile(path_zip) as archive:
        xf = archive.extract("excel_XLSX.xlsx")
        xlsx_file = load_workbook(xf)
        sheet = xlsx_file.active
    assert sheet.cell(row=2,column=2).value == "Dulce", f"Expected result: {'Dulce'}, " \
                                                        f"actual result: {sheet.cell(row=2, column=2).value}"
    os.remove(xf)


def test_csv():
    with zipfile.ZipFile(path_zip) as zf:
        cf = zf.extract("test_CSV.csv")
        with open(cf) as csvfile:
            csvfile = csv.reader(csvfile)
            list_csv = []
            for r in csvfile:
                text = "".join(r).replace(";", " ")
                list_csv.append(text)

            assert list_csv[
                       0] == "Test python", f"Expected result: {'Test python'}, " \
                                                            f"actual result: {list_csv[0]}"
        os.remove(cf)


