import os
import xml.etree.ElementTree as ET

def xml_to_ascii(input_file):
    # Determine the output file path
    base_name = os.path.splitext(input_file)[0]
    output_file = base_name + '_O' + '.txt'

    # Parse the XML file
    tree = ET.parse(input_file)
    root = tree.getroot()

    with open(output_file, 'w', encoding='ascii', errors='ignore') as ascii_file:
        # Extracting Emisor information
        emisor = root.find('.//cfdi:Emisor', namespaces={'cfdi': 'http://www.sat.gob.mx/cfd/4'})
        if emisor is not None:
            ascii_file.write(f"Emisor Nombre: {emisor.attrib.get('Nombre', '')}\n")
            ascii_file.write(f"Emisor RFC: {emisor.attrib.get('Rfc', '')}\n\n")

        # Extracting Receptor information
        receptor = root.find('.//cfdi:Receptor', namespaces={'cfdi': 'http://www.sat.gob.mx/cfd/4'})
        if receptor is not None:
            ascii_file.write(f"Receptor Nombre: {receptor.attrib.get('Nombre', '')}\n")
            ascii_file.write(f"Receptor RFC: {receptor.attrib.get('Rfc', '')}\n\n")

        # Extracting Concepto information
        for concepto in root.findall('.//cfdi:Concepto', namespaces={'cfdi': 'http://www.sat.gob.mx/cfd/4'}):
            descripcion = concepto.attrib.get('Descripcion', '').strip()
            importe = concepto.attrib.get('Importe', '').strip()
            ascii_file.write(f"Descripcion: {descripcion}\n")
            ascii_file.write(f"Importe: {importe}\n\n")

        # Extracting Complemento information (e.g., TimbreFiscalDigital)
        complemento = root.find('.//cfdi:Complemento//tfd:TimbreFiscalDigital', namespaces={
            'cfdi': 'http://www.sat.gob.mx/cfd/4', 
            'tfd': 'http://www.sat.gob.mx/TimbreFiscalDigital'
        })
        if complemento is not None:
            ascii_file.write(f"Timbre Fiscal Digital UUID: {complemento.attrib.get('UUID', '')}\n")
            ascii_file.write(f"Fecha Timbrado: {complemento.attrib.get('FechaTimbrado', '')}\n\n")

# Example usage
xml_to_ascii('C:/Users/glado/Desktop/XMLtoTextProject/MK1-9040000004279.xml')
import os
import xml.etree.ElementTree as ET

def xml_to_ascii(input_file):
    # Determine the output file path
    base_name = os.path.splitext(input_file)[0]
    output_file = base_name + '_O' + '.txt'

    # Parse the XML file
    tree = ET.parse(input_file)
    root = tree.getroot()

    with open(output_file, 'w', encoding='ascii', errors='ignore') as ascii_file:
        data = []

        # Extracting Emisor information
        emisor = root.find('.//cfdi:Emisor', namespaces={'cfdi': 'http://www.sat.gob.mx/cfd/4'})
        if emisor is not None:
            data.append(f"Emisor Nombre: {emisor.attrib.get('Nombre', '')}")
            data.append(f"Emisor RFC: {emisor.attrib.get('Rfc', '')}")

        # Extracting Receptor information
        receptor = root.find('.//cfdi:Receptor', namespaces={'cfdi': 'http://www.sat.gob.mx/cfd/4'})
        if receptor is not None:
            data.append(f"Receptor Nombre: {receptor.attrib.get('Nombre', '')}")
            data.append(f"Receptor RFC: {receptor.attrib.get('Rfc', '')}")

        # Extracting Concepto information (assuming only one Concepto for simplicity)
        concepto = root.find('.//cfdi:Concepto', namespaces={'cfdi': 'http://www.sat.gob.mx/cfd/4'})
        if concepto is not None:
            data.append(f"Descripcion: {concepto.attrib.get('Descripcion', '').strip()}")
            data.append(f"Importe: {concepto.attrib.get('Importe', '').strip()}")

        # Extracting Complemento information (e.g., TimbreFiscalDigital)
        complemento = root.find('.//cfdi:Complemento//tfd:TimbreFiscalDigital', namespaces={
            'cfdi': 'http://www.sat.gob.mx/cfd/4', 
            'tfd': 'http://www.sat.gob.mx/TimbreFiscalDigital'
        })
        if complemento is not None:
            data.append(f"Timbre Fiscal Digital UUID: {complemento.attrib.get('UUID', '')}")
            data.append(f"Fecha Timbrado: {complemento.attrib.get('FechaTimbrado', '')}")

        # Join all data points with commas and write to file
        ascii_file.write(', '.join(data) + '\n')

# Example usage
xml_to_ascii('C:/Users/glado/Desktop/XMLtoTextProject/MK1-9040000004279.xml')