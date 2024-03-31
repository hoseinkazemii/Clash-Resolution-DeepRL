import pandas as pd
import xml.etree.ElementTree as ET


def extract_clash_edges(**params):
    data_directory = params.get("data_directory")
    clash_report_file = params.get("clash_report_file")

    print("reading clash edges from Navisworks XML output...")

    # Parse the XML file
    tree = ET.parse(data_directory + clash_report_file + ".xml")
    root = tree.getroot()

    clashes_data = []

    # Iterate over clash results
    for clashresult in root.findall('.//batchtest/clashtests/clashtest/clashresults/clashresult'):
        # Extract result status
        resultstatus = clashresult.find('resultstatus').text

        # Extract element IDs for both nodes
        element_ids = []
        for clashobject in clashresult.findall('.//clashobject'):
            element_id = clashobject.find(".//objectattribute[name='Element ID']/value").text
            element_ids.append(element_id)

        # Append extracted data to clashes_data list
        clashes_data.append({"Node1": element_ids[0], "Node2": element_ids[1], "Status": resultstatus})

    # Create DataFrame from the extracted data
    df_clash_edges = pd.DataFrame(clashes_data)

    return df_clash_edges