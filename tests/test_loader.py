import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.loader import load_pdf, load_excel, load_txt

def test_load_pdf_invalid_path():
    try:
        load_pdf("nonexistent.pdf")
        assert False, "Should have raised FileNotFoundError"
    except FileNotFoundError:
        assert True

def test_load_excel_invalid_path():
    try:
        load_excel("nonexistent.xlsx")
        assert False, "Should have raised FileNotFoundError"
    except FileNotFoundError:
        assert True

def test_load_txt_invalid_path():
    try:
        load_txt("nonexistent.txt")
        assert False, "Should have raised FileNotFoundError"
    except FileNotFoundError:
        assert True

def test_load_excel_unsupported_format():
    try:
        load_excel("file.mp4")
        assert False, "Should have raised ValueError"
    except (FileNotFoundError, ValueError):
        assert True