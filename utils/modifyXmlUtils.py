import zipfile
import os
from xml.etree.ElementTree import parse


class XMLUtils:
    @staticmethod
    def modify_document_xml(doc_path, output_path, temp_dir="temp_docx", modify_index=0):

        try:
            # 解压提取目标文件
            os.makedirs(temp_dir, exist_ok=True)
            with zipfile.ZipFile(doc_path, 'r') as zip_ref:
                zip_ref.extractall(temp_dir)

            xml_file_path = os.path.join(temp_dir, "word", 'document.xml')
            tree = parse(xml_file_path)
            root = tree.getroot()
            ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

            current_index = 0
            for sym in root.findall('.//w:sym', ns):
                if sym.attrib[f'{{{ns["w"]}}}char'] == "00A8" or sym.attrib[f'{{{ns["w"]}}}char'] == "00FE":
                    current_index = current_index + 1
                    if modify_index == current_index:
                        sym.set(f'{{{ns["w"]}}}char', "00FE")
                    else:
                        sym.set(f'{{{ns["w"]}}}char', "00A8")

            if os.path.exists(output_path):
                os.remove(output_path)
            tree.write(xml_file_path, encoding='utf-8', xml_declaration=True)

            # 将临时目录下的所有文件重新打包为 .docx 文件
            with zipfile.ZipFile(output_path, 'w') as zipf:
                for foldername, subfolders, filenames in os.walk(temp_dir):
                    for filename in filenames:
                        file_path = os.path.join(foldername, filename)
                        arcname = os.path.relpath(file_path, temp_dir)
                        zipf.write(file_path, arcname)

            return True
        except Exception as e:
            import traceback
            print(traceback.print_exc())
            for root, dirs, files in os.walk(temp_dir, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
            os.rmdir(temp_dir)
            return False

    @staticmethod
    def modify(index):
        XMLUtils.modify_document_xml('../test.docx', 'modified_example.docx', modify_index=index)
