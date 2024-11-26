import openpyxl as xl

def normalize(input_file):
    wb = xl.load_workbook(input_file)
    sheet = wb.active

    column_names = [cell.value for cell in sheet[1]]
    column_names = [name.lower().replace(' ', '_').replace('.', '').replace('ó', 'o').replace('-', '_') 
                    for name in column_names]

    data = sheet.iter_rows(min_row=2, values_only=True)

    output = []
    output.append([name for name in column_names if 'descripcion' not in name])

    for row in data:
            if row[column_names.index('ejercicio')] == None:
                break
            row_data = []
            for i, cell in enumerate(row):
                if 'descripcion' not in column_names[i]:
                    value = str(cell).replace(',', '  ')
                    if column_names[i] == 'desc_prog_fin':
                        value = '"' + value + '"'
                    row_data.append(value)
            output.append(row_data)

    return output
