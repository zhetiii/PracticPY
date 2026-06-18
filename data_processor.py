import json
import xml.etree.ElementTree as ET
from db_manager import connect_to_storage, logger

def save_to_json(output_path):
    conn = connect_to_storage()
    curr = conn.cursor()
    curr.execute('SELECT id, customer_id, order_date, status, total FROM orders')
    rows = curr.fetchall()
    conn.close()

    serialized_data = []
    for item in rows:
        serialized_data.append({
            "order_number": item[0],
            "client_code": item[1],
            "created_at": item[2],
            "state": item[3],
            "amount_rub": item[4]
        })
    
    with open(output_path, 'w', encoding='utf-8') as json_file:
        json.dump(serialized_data, json_file, ensure_ascii=False, indent=4)
    logger.info(f"Данные сохранены в файл конфигурации JSON: {output_path}")

def save_to_xml(output_path):
    conn = connect_to_storage()
    curr = conn.cursor()
    curr.execute('SELECT id, customer_id, order_date, status, total FROM orders')
    rows = curr.fetchall()
    conn.close()

    xml_root = ET.Element("delivery_data")
    for item in rows:
        node = ET.SubElement(xml_root, "order_record")
        ET.SubElement(node, "uid").text = str(item[0])
        ET.SubElement(node, "client_uid").text = str(item[1])
        ET.SubElement(node, "date_str").text = item[2]
        ET.SubElement(node, "status_str").text = item[3]
        ET.SubElement(node, "price_val").text = str(item[4])

    xml_tree = ET.ElementTree(xml_root)
    xml_tree.write(output_path, encoding='utf-8', xml_declaration=True)
    logger.info(f"Данные сохранены в разметку XML: {output_path}")
