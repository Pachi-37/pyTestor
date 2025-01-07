import pandas as pd

from DOCXUtils import XlsxData


class ParseXlsx:
    @staticmethod
    def read_xlsx(file_path):
        with pd.ExcelFile(file_path, engine='openpyxl') as xlsx:
            sheet_name = xlsx.sheet_names[0]
            df = pd.read_excel(xlsx, sheet_name=sheet_name)

            for index, row in df.iterrows():
                current_data = XlsxData()


if __name__ == '__main__':
    ParseXlsx.read_xlsx("../test.xlsx")
