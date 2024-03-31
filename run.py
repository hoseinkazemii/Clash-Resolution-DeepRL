from Preprocessing import *






def run():
    
    general_settings = {
    'data_directory' : './Data/',
    "clash_report_file": "StrAndMEPClashReport",
    "clash_edges_file":"clash_edges",
    'models': ['Structural', 'Mechanical'],
    "structural_elements":[
        "IfcWall", "IfcDoor", "IfcBeam", "IfcColumn", 
        "IfcOpeningElement",
        "IfcSlab", "IfcStair", "IfcRoof", "IfcMember", 
        "IfcPlate"
    ],
    "mechanical_elements" : [
        "IfcDuctSegment", "IfcPipeSegment", "IfcPipeFitting",
        "IfcUnitaryEquipment","IfcBuildingElementProxy",
        "IfcLightFixture","IfcFan","IfcUnitaryEquipment",
        "IfcDuctFitting","IfcAirToAirHeatRecovery",
        "IfcCableCarrierSegment","IfcPump",
        "IfcElectricDistributionBoard","IfcCableCarrierFitting",
        
        "IfcCableSegment", "IfcEquipment", "IfcFitting", 
        "IfcFlowTerminal", "IfcSpace", "IfcOpeningElement"
    ],
    "architectural_elements" : [
        "IfcWall", "IfcDoor", 
        "IfcWindow", "IfcFloor", "IfcRoof", 
        "IfcBuildingElementProxy", "IfcSpace", "IfcOpeningElement"
    ],







    }


    myData = PreprocessData(**general_settings)
    myData._load_and_preprocess_data()







if __name__ == '__main__':
    run()