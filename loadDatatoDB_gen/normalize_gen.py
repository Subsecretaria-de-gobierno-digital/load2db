import openpyxl as xl
import unicodedata
from collections import defaultdict

def normalize(input_file):
    wb = xl.load_workbook(input_file, data_only=True)
    sheet = wb.active

    column_names = [unicodedata.normalize('NFKD', cell.value.lower())
                    .encode('ASCII', 'ignore').decode('utf-8')
                    .replace(' ', '_').replace('.', '').replace('-', '_')
                    .replace('(', '').replace(')', '').replace('\n', '').replace('/', '')[:10]
                    if cell.value is not None else ''
                    for cell in sheet[1]]

    column_name_counts = defaultdict(int)
    for i, name in enumerate(column_names):
        column_name_counts[name] += 1
        if column_name_counts[name] > 1:
            column_names[i] = f"{name}_{column_name_counts[name]}"

    output = [[name for name in column_names]]
    for row in sheet.iter_rows(min_row=2):
        row_data = [str(cell.value).replace(',', '  ') if column_names[i] != 'desc_prog_fin' else f'"{cell.value}"'
                    for i, cell in enumerate(row)]
        output.append(row_data)

    return output
