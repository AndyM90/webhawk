import xlsxwriter

heating_and_cooling_websites = []
carpet_cleaning_websites = []
electrician_websites = []
plumbing_websites = []
cleaning_websites = []


workbook = xlsxwriter.Workbook('keyword_urls.xlsx')
worksheet = workbook.add_worksheet('urls')

with open('domain_list.txt') as file:
    for line in file:
        if 'carpet' in line:
            print('Possible Carpet Cleaning Website: ' + line)
            carpet_cleaning_websites.append(line)
        elif 'cleaning' in line:
            print('Possible Carpet Cleaning Website: ' + line)
            carpet_cleaning_websites.append(line)
        elif 'rug' in line:
            if 'drug' in line:
                pass
            else:
                print('Possible Carpet Cleaning Website: ' + line)
                carpet_cleaning_websites.append(line)
        elif 'couch' in line:
            print('Possible Carpet Cleaning Website: ' + line)
            carpet_cleaning_websites.append(line)
        elif 'sofa' in line:
            print('Possible Carpet Cleaning Website: ' + line)
            carpet_cleaning_websites.append(line)
        elif 'upholstery' in line:
            print('Possible Carpet Cleaning Website: ' + line)
            carpet_cleaning_websites.append(line)
        elif 'alfombra' in line:
            print('Possible Carpet Cleaning Website: ' + line)
            carpet_cleaning_websites.append(line)

        if 'heat' in line:
            print('Possible Hvac Website: ' + line)
            heating_and_cooling_websites.append(line)
        elif 'cool' in line:
            print('Possible Hvac Website: ' + line)
            heating_and_cooling_websites.append(line)
        elif 'hvac' in line:
            print('Possible Hvac Website: ' + line)
            heating_and_cooling_websites.append(line)
        elif 'acrepair' in line:
            print('Possible Hvac Website: ' + line)
            heating_and_cooling_websites.append(line)
        elif 'aircond' in line:
            print('Possible Hvac Website: ' + line)
            heating_and_cooling_websites.append(line)
        elif 'temperature' in line:
            print('Possible Hvac Website: ' + line)
            heating_and_cooling_websites.append(line)
        elif 'cold' in line:
            print('Possible Hvac Website: ' + line)
            heating_and_cooling_websites.append(line)
        elif 'ductless' in line:
            print('Possible Hvac Website: ' + line)
            heating_and_cooling_websites.append(line)
        elif 'thermostat' in line:
            print('Possible Hvac Website: ' + line)
            heating_and_cooling_websites.append(line)
        elif 'condicionado' in line:
            print('Possible Hvac Website: ' + line)
            heating_and_cooling_websites.append(line)
        elif 'calefaccion' in line:
            print('Possible Hvac Website: ' + line)
            heating_and_cooling_websites.append(line)
        elif 'ventilacion' in line:
            print('Possible Hvac Website: ' + line)
            heating_and_cooling_websites.append(line)

        if 'plumb' in line:
            print('Possible Plumbing Website: ' + line)
            plumbing_websites.append(line)
        elif 'faucet' in line:
            print('Possible Plumbing Website: ' + line)
            plumbing_websites.append(line)
        elif 'leak' in line:
            print('Possible Plumbing Website: ' + line)
            plumbing_websites.append(line)
        elif 'drain' in line:
            print('Possible Plumbing Website: ' + line)
            plumbing_websites.append(line)
        elif 'clogg' in line:
            print('Possible Plumbing Website: ' + line)
            plumbing_websites.append(line)
        elif 'boiler' in line:
            print('Possible Plumbing Website: ' + line)
            plumbing_websites.append(line)
        elif 'drain' in line:
            print('Possible Plumbing Website: ' + line)
            plumbing_websites.append(line)
        elif 'plomero' in line:
            print('Possible Plumbing Website: ' + line)
            plumbing_websites.append(line)
        elif 'fontanero' in line:
            print('Possible Plumbing Website: ' + line)
            plumbing_websites.append(line)

        if 'electrician' in line:
            print('Possible Electrician Website: ' + line)
            electrician_websites.append(line)
        elif 'electrical' in line:
            print('Possible Electrician Website: ' + line)
            electrician_websites.append(line)

        if 'clean' in line:
            print('Possible Cleaning Website: ' + line)
            cleaning_websites.append(line)
        elif 'maid' in line:
            print('Possible Cleaning Website: ' + line)
            cleaning_websites.append(line)
        elif 'washing' in line:
            print('Possible Cleaning Website: ' + line)
            cleaning_websites.append(line)
        elif 'window' in line:
            print('Possible Cleaning Website: ' + line)
            cleaning_websites.append(line)
        elif 'handyman' in line:
            print('Possible Cleaning Website: ' + line)
            cleaning_websites.append(line)
        elif 'garage' in line:
            print('Possible Cleaning Website: ' + line)
            cleaning_websites.append(line)
        elif 'repair' in line:
            print('Possible Cleaning Website: ' + line)
            cleaning_websites.append(line)
        elif 'reparacion' in line:
            print('Possible Cleaning Website: ' + line)
            cleaning_websites.append(line)
        elif 'residential' in line:
            print('Possible Cleaning Website: ' + line)
            cleaning_websites.append(line)
        elif 'housecall' in line:
            print('Possible Cleaning Website: ' + line)
            cleaning_websites.append(line)
        elif 'contractor' in line:
            print('Possible Cleaning Website: ' + line)
            cleaning_websites.append(line)
        elif 'servicecall' in line:
            print('Possible Cleaning Website: ' + line)
            cleaning_websites.append(line)
        elif 'landscaping' in line:
            print('Possible Cleaning Website: ' + line)
            cleaning_websites.append(line)
        elif 'maintenance' in line:
            print('Possible Cleaning Website: ' + line)
            cleaning_websites.append(line)
        elif 'mantenimiento' in line:
            print('Possible Cleaning Website: ' + line)
            cleaning_websites.append(line)
        elif 'commercial' in line:
            print('Possible Cleaning Website: ' + line)
            cleaning_websites.append(line)
        elif 'autodetail' in line:
            print('Possible Cleaning Website: ' + line)
            cleaning_websites.append(line)
        elif 'cardetail' in line:
            print('Possible Cleaning Website: ' + line)
            cleaning_websites.append(line)

cell_format = workbook.add_format({'bold': True, 'font_color': 'black'})
worksheet.write('A1', 'CARPET CLEANING', cell_format)
worksheet.write('B1', 'HVAC', cell_format)
worksheet.write('C1', 'PLUMBING', cell_format)
worksheet.write('D1', 'ELECTRICIAN', cell_format)
worksheet.write('E1', 'CLEANING', cell_format)
worksheet.write_column('A2', carpet_cleaning_websites)
worksheet.write_column('B2', heating_and_cooling_websites)
worksheet.write_column('C2', plumbing_websites)
worksheet.write_column('D2', electrician_websites)
worksheet.write_column('E2', cleaning_websites)
print("[*]Excel Sheet Saved\nKeyword Extraction is finished!")
workbook.close()
