import pandas as pd
import xml.etree.ElementTree as ET


def extract_nodes_and_relationships(**params):

    data_directory = params.get("data_directory")
    models = params.get("models")
    structural_elements = params.get("structural_elements")
    mechanical_elements = params.get("mechanical_elements")
    architectural_elements = params.get("architectural_elements")


    for model_type in models:

        if model_type == "Structural":
            # Initialize an empty DataFrame
            df_structural = pd.DataFrame(columns=structural_elements)
            print("getting the nodes from structural ifcxml file...")
            # Parse the IFCXML file
            tree = ET.parse(data_directory + model_type + ".ifcxml")
            # Collect tag texts for each element type
            tag_texts_by_element = {}
            # Initialize lists to store tag texts and element types
            all_tags = []
            all_element_types = []
            for element_type in structural_elements:
                elements = tree.findall('.//{http://www.iai-tech.org/ifcXML/IFC2x2/FINAL}uos/{http://www.iai-tech.org/ifcXML/IFC2x3/FINAL}' + f"{element_type}" \
                                        + "/{http://www.iai-tech.org/ifcXML/IFC2x3/FINAL}Tag")
                tag_texts = [tag.text for tag in elements]
                tag_texts_by_element[element_type] = tag_texts
                tags = [tag.text for tag in elements]
                element_types = [element_type] * len(tags)
                # Append to the lists
                all_tags.extend(tags)
                all_element_types.extend(element_types)
            # Create a DataFrame from the collected data
            df_structural = pd.DataFrame({"Tag": all_tags, "Element_Type": all_element_types})


        elif model_type == "Mechanical":
            df_mechanical = pd.DataFrame(columns=mechanical_elements)
            print("getting the nodes from mechanical ifcxml file...")
            tree = ET.parse(data_directory + model_type + ".ifcxml")
            tag_texts_by_element = {}
            all_tags = []
            all_element_types = []
            for element_type in mechanical_elements:
                elements = tree.findall('.//{http://www.iai-tech.org/ifcXML/IFC2x2/FINAL}uos/{http://www.iai-tech.org/ifcXML/IFC2x3/FINAL}' + f"{element_type}" \
                                        + "/{http://www.iai-tech.org/ifcXML/IFC2x3/FINAL}Tag")
                tag_texts = [tag.text for tag in elements]
                tag_texts_by_element[element_type] = tag_texts
                tags = [tag.text for tag in elements]
                element_types = [element_type] * len(tags)
                all_tags.extend(tags)
                all_element_types.extend(element_types)
            df_mechanical = pd.DataFrame({"Tag": all_tags, "Element_Type": all_element_types})


        elif model_type == "Architectural":
            df_architectural = pd.DataFrame(columns=architectural_elements)
            print("getting the nodes from architectural ifcxml file...")
            tree = ET.parse(data_directory + model_type + ".ifcxml")
            tag_texts_by_element = {}
            all_tags = []
            all_element_types = []
            for element_type in architectural_elements:
                elements = tree.findall('.//{http://www.iai-tech.org/ifcXML/IFC2x2/FINAL}uos/{http://www.iai-tech.org/ifcXML/IFC2x3/FINAL}' + f"{element_type}" \
                                        + "/{http://www.iai-tech.org/ifcXML/IFC2x3/FINAL}Tag")
                tag_texts = [tag.text for tag in elements]
                tag_texts_by_element[element_type] = tag_texts
                tags = [tag.text for tag in elements]
                element_types = [element_type] * len(tags)
                all_tags.extend(tags)
                all_element_types.extend(element_types)
            df_architectural = pd.DataFrame({"Tag": all_tags, "Element_Type": all_element_types})


    return df_structural, df_mechanical