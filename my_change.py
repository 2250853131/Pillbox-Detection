import os
import xml.etree.ElementTree as ET

def extract_numbers_from_xml(xml_file_path):
    numbers = []
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    for element in root.iter():
        if element.text and element.text.isdigit():
            numbers.append(element.text)
    return numbers

def main(xml_folder_path, output_folder_path):
    # 遍历文件夹中的每个XML文件
    for filename in os.listdir(xml_folder_path):
        if filename.endswith('.xml'):
            xml_file_path = os.path.join(xml_folder_path, filename)
            # 提取数字
            numbers = extract_numbers_from_xml(xml_file_path)
            # 去除前6个数字
            numbers = numbers[6:]
            # 将后面的数字放在一行，数字之间空一个
            numbers_str = ' '.join(numbers)
            # 写入对应的TXT文件
            txt_file_path = os.path.join(output_folder_path, os.path.splitext(filename)[0] + '.txt')
            with open(txt_file_path, 'w') as f:
                f.write(numbers_str + ' pillbox 0\n')

if __name__ == "__main__":
    xml_folder_path = "pd/label"
    output_folder_path = "pd/txt"
    main(xml_folder_path, output_folder_path)
