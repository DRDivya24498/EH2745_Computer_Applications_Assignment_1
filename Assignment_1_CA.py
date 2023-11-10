import xml.etree.ElementTree as ET

#parsing the data EQ and SSH file
tree_EQ_BE=ET.parse("MicroGridTestConfiguration_T3_BE_EQ_V2.XML")
tree_SSH_BE=ET.parse("MicroGridTestConfiguration_T3_BE_SSH_V2.XML")
root_EQ_BE = tree_EQ_BE.getroot()
root_SSH_BE = tree_SSH_BE.getroot()
tree_EQ_NL=ET.parse("MicroGridTestConfiguration_T3_NL_EQ_V2.XML")
tree_SSH_NL=ET.parse("MicroGridTestConfiguration_T3_NL_SSH_V2.XML")
root_EQ_NL = tree_EQ_NL.getroot()
root_SSH_NL = tree_SSH_NL.getroot()
cim = "{http://iec.ch/TC57/2013/CIM-schema-cim16#}"
md = "{http://iec.ch/TC57/61970-552/ModelDescription/1#}"
rdf = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"


#class definition for cim objects
class AC_line_segment:
    def __init__(self, rdf_ID, name, equipment_container_rdf_ID, ACLineSegment_r,
                 ACLineSegment_x, bch, gch, length, base_voltage_rdf_ID, ACLineSegment_r_0, ACLineSegment_x_0, bch_0, gch_0, short_circuit_end_temp,nominal_voltage):
        self.rdf_ID = rdf_ID
        self.name = name
        self.equipment_container_rdf_ID = equipment_container_rdf_ID
        self.ACLineSegment_r = ACLineSegment_r
        self.ACLineSegment_x = ACLineSegment_x
        self.bch = bch
        self.gch = gch
        self.length = length
        self.base_voltage_rdf_ID = base_voltage_rdf_ID
        self.ACLineSegment_r_0=ACLineSegment_r_0
        self.ACLineSegment_x_0 = ACLineSegment_x_0
        self.bch_0 = bch_0
        self.gch_0 = gch_0
        self.short_circuit_end_temp=short_circuit_end_temp
        self.type = "ACLineSegment"
        self.nominal_voltage=nominal_voltage
        self.traversal_flag = 0

class base_voltage:
    def __init__(self, rdf_ID, nominal_value,nominal_voltage):
        self.rdf_ID = rdf_ID
        self.nominal_value = nominal_value
        self.nominal_voltage=nominal_voltage

class breaker:
    def __init__(self, rdf_ID, name, state, equipment_container_rdf_ID, base_voltage_rdf_ID,nominal_voltage):
        self.rdf_ID = rdf_ID
        self.name = name
        self.state=state
        self.equipment_container_rdf_ID = equipment_container_rdf_ID
        self.base_voltage_rdf_ID=base_voltage_rdf_ID
        self.type = "Breaker"
        self.nominal_voltage=nominal_voltage
        self.traversal_flag = 0

class busbar_section:
    def __init__(self, rdf_ID, name, equipment_container_rdf_ID, base_voltage_rdf_ID, nominal_voltage, bus):
        self.rdf_ID = rdf_ID
        self.name = name
        self.equipment_container_rdf_ID = equipment_container_rdf_ID
        self.base_voltage_rdf_ID = base_voltage_rdf_ID
        self.nominal_voltage=nominal_voltage
        self.bus=bus
        self.type="BusbarSection"
        self.traversal_flag = 0

class connectivity_node:
    def __init__(self, rdf_ID, name, connectivity_container_rdf_ID, nominal_voltage, CN_bus, CE_bus):
        self.rdf_ID = rdf_ID
        self.name = name
        self.connectivity_container_rdf_ID=connectivity_container_rdf_ID
        self.nominal_voltage=nominal_voltage
        self.count_terminal=0
        self.CN_bus=CN_bus
        self.CE_bus=CE_bus
        self.type="connectivity node"
        self.type_CE = "ConnectivityNodeType"
        self.traversal_flag = 0

class energy_source:
    def __init__(self, rdf_ID, name, equipment_container_rdf_ID, nominal_voltage):
        self.rdf_ID = rdf_ID
        self.name = name
        self.equipment_container_rdf_ID = equipment_container_rdf_ID
        self.nominal_voltage = nominal_voltage

class substation:
    def __init__(self, rdf_ID, name, region_rdf_ID):
        self.rdf_ID = rdf_ID
        self.name = name
        self.region_rdf_ID = region_rdf_ID

class energy_consumer_load:
    def __init__(self, rdf_ID, name, active_power, reactive_power, equipment_container_rdf_ID, base_voltage_rdf_ID):
        self.rdf_ID = rdf_ID
        self.name = name
        self.active_power = active_power
        self.reactive_power = reactive_power
        self.equipment_container_rdf_ID = equipment_container_rdf_ID
        self.base_voltage_rdf_ID=base_voltage_rdf_ID
        self.type = 'EnergyConsumerLoad'
        self.traversal_flag = 0

class linear_shunt_compensator:
    def __init__(self, rdf_ID, name, b_per_section, g_per_section, active_power, reactive_power,
                 equipment_container_rdf_ID, base_voltage_rdf_ID, base_voltage_value,nominal_voltage):
        self.rdf_ID = rdf_ID
        self.name = name
        self.b_per_section = b_per_section
        self.g_per_section = g_per_section
        self.active_power = active_power
        self.reactive_power = reactive_power
        self.equipment_container_rdf_ID = equipment_container_rdf_ID
        self.base_voltage_rdf_ID = base_voltage_rdf_ID
        self.base_voltage_value = base_voltage_value
        self.type = "LinearShuntCompensator"
        self.nominal_voltage=nominal_voltage
        self.traversal_flag = 0

class power_transformer:
    def __init__(self, rdf_ID, name, equipment_container_rdf_ID,nominal_voltage):
        self.rdf_ID = rdf_ID
        self.name = name
        self.equipment_container_rdf_ID = equipment_container_rdf_ID
        self.type="PowerTransformer"
        self.nominal_voltage=nominal_voltage
        self.traversal_flag = 0

class cs_converter:
    def __init__(self,rdf_ID, name, equipment_container_rdf_ID,nominal_voltage):
        self.rdf_ID = rdf_ID
        self.name = name
        self.type = "CSConverter"
        self.equipment_container_rdf_ID = equipment_container_rdf_ID
        self.nominal_voltage=nominal_voltage
        self.traversal_flag = 0

class power_transformer_end_transformer_winding:
    def __init__(self, rdf_ID, name, transformer_r, transformer_x,
                 transformer_rdf_ID, base_voltage_rdf_ID, b, g, nominal_voltage):
        self.rdf_ID = rdf_ID
        self.name = name
        self.transformer_r = transformer_r
        self.transformer_x = transformer_x
        self.transformer_rdf_ID = transformer_rdf_ID
        self.base_voltage_rdf_ID = base_voltage_rdf_ID
        self.b = b
        self.g = g
        self.type = "PowerTransformerEnd"
        self.nominal_voltage=nominal_voltage
        self.traversal_flag = 0

class synchronous_machine:
    def __init__(self, rdf_ID, name, rated_S, active_power, reactive_power,
                 generator_unit_rdf_ID, reg_control_rdf_ID, equipment_container_rdf_ID, base_voltage_rdf_ID,rated_U, max_Q, min_Q,nominal_voltage):
        self.rdf_ID = rdf_ID
        self.name = name
        self.rated_S = rated_S
        self.active_power = active_power
        self.reactive_power = reactive_power
        self.generator_unit_rdf_ID = generator_unit_rdf_ID
        self.reg_control_rdf_ID = reg_control_rdf_ID
        self.equipment_container_rdf_ID = equipment_container_rdf_ID
        self.base_voltage_rdf_ID = base_voltage_rdf_ID
        self.rated_U=rated_U
        self.max_Q=max_Q
        self.min_Q=min_Q
        self.type = 'SynchronousMachine'
        self.nominal_voltage=nominal_voltage
        self.traversal_flag = 0

class equivalent_injection:
    def __init__(self,rdf_ID,name, r, x, base_voltage_rdf_ID):
        self.rdf_ID = rdf_ID
        self.name = name
        self.r = r
        self.x = x
        self.base_voltage_rdf_ID = base_voltage_rdf_ID
        self.traversal_flag = 0

class terminal:
    def __init__(self, rdf_ID, name, CE_rdf_ID, CN_rdf_ID):
        self.rdf_ID = rdf_ID
        self.name = name
        self.CE_rdf_ID = CE_rdf_ID
        self.CN_rdf_ID = CN_rdf_ID
        self.traversal_flag = 0
        self.type="terminal"
        self.type_CE = "Terminal type"

class voltage_level_BE:
    def __init__(self, rdf_ID, name, substation_rdf_ID, base_voltage_rdf_ID, nominal_voltage):
        self.rdf_ID = rdf_ID
        self.name = name
        self.substation_rdf_ID = substation_rdf_ID
        self.base_voltage_rdf_ID = base_voltage_rdf_ID
        self.nominal_voltage=nominal_voltage

class voltage_level_NL:
    def __init__(self, rdf_ID, name, substation_rdf_ID, base_voltage_rdf_ID, nominal_voltage):
        self.rdf_ID = rdf_ID
        self.name = name
        self.substation_rdf_ID = substation_rdf_ID
        self.base_voltage_rdf_ID = base_voltage_rdf_ID
        self.nominal_voltage=nominal_voltage

class conducting_equipment:
    def __init__(self, rdf_ID, name, type_CE, state,nominal_voltage,active_power,reactive_power):
        self.rdf_ID = rdf_ID
        self.name = name
        self.type ="conducting equipment"
        self.type_CE = type_CE
        self.state = state
        self.nominal_voltage=nominal_voltage
        self.active_power=active_power
        self.reactive_power=reactive_power
        self.traversal_flag = 0

#List of objects of all the defined classes
base_voltage_list_BE=[]
substation_list_BE=[]
AC_line_segment_list_BE=[]
breaker_list_BE=[]
busbar_section_list_BE=[]
connectivity_node_list_BE=[]
energy_source_list_BE=[]
energy_consumer_load_list_BE=[]
linear_shunt_compensator_list_BE=[]
power_transformer_list_BE=[]
cs_converter_list_BE=[]
power_transformer_end_transformer_winding_list_BE=[]
synchronous_machine_list_BE=[]
equivalent_injection_list_BE=[]
terminal_list_BE=[]
voltage_level_list_BE=[]
conducting_equipment_list_BE=[]

#Forming the list of Voltage Levels
for voltage_level_xml_BE in root_EQ_BE.iter(cim+'VoltageLevel'):
    voltage_level_list_BE.append(voltage_level_BE(voltage_level_xml_BE.get(rdf+'ID'),
                                            voltage_level_xml_BE.find(cim+'IdentifiedObject.name').text,
                                            voltage_level_xml_BE.find(cim+'VoltageLevel.Substation').get(rdf+'resource'),
                                            voltage_level_xml_BE.find(cim+'VoltageLevel.BaseVoltage').get(rdf+'resource'),""))

#Forming the list of AC Line Segments
for AC_line_segment_xml_BE in root_EQ_BE.iter(cim+'ACLineSegment'):
    AC_line_segment_list_BE.append(AC_line_segment(AC_line_segment_xml_BE.get(rdf+'ID'),
                                                AC_line_segment_xml_BE.find(cim+'IdentifiedObject.name').text,
                                                AC_line_segment_xml_BE.find(cim+'Equipment.EquipmentContainer').get(rdf+'resource'),
                                                AC_line_segment_xml_BE.find(cim+'ACLineSegment.r').text, AC_line_segment_xml_BE.find(cim+'ACLineSegment.x').text,
                                                AC_line_segment_xml_BE.find(cim+'ACLineSegment.bch').text, AC_line_segment_xml_BE.find(cim+'ACLineSegment.gch').text,
                                                AC_line_segment_xml_BE.find(cim+'Conductor.length').text, AC_line_segment_xml_BE.find(cim+'ConductingEquipment.BaseVoltage').get(rdf+'resource'),
                                                AC_line_segment_xml_BE.find(cim+"ACLineSegment.r0"), AC_line_segment_xml_BE.find(cim+"ACLineSegment.x0"),
                                                AC_line_segment_xml_BE.find(cim+"ACLineSegment.b0ch"),AC_line_segment_xml_BE.find(cim+"ACLineSegment.g0ch"),
                                                AC_line_segment_xml_BE.find(cim+"ACLineSegment.shortCircuitEndTemperature"),""))

#Forming the list of Base Voltages
for base_voltage_xml_BE in root_EQ_BE.iter(cim+"BaseVoltage"):
    base_voltage_list_BE.append(base_voltage(base_voltage_xml_BE.get(rdf+"ID"),
                                          base_voltage_xml_BE.find(cim+"BaseVoltage.nominalVoltage").text,""))

#Forming the list of Breakers
for breaker_xml_BE in root_EQ_BE.iter(cim+'Breaker'):
    breaker_list_BE.append(breaker(breaker_xml_BE.get(rdf+'ID'), breaker_xml_BE.find(cim+'IdentifiedObject.name').text,
                                "", breaker_xml_BE.find(cim+'Equipment.EquipmentContainer').get(rdf+'resource'), "",""))

count=0
for breaker_xml_BE in root_SSH_BE.iter(cim+"Breaker"):
    breaker_list_BE[count].state=breaker_xml_BE.find(cim+"Switch.open").text
    count+=1

#Forming the list of Bus Bar sections
for busbar_section_xml_BE in root_EQ_BE.iter(cim+'BusbarSection'):
    busbar_section_list_BE.append(busbar_section(busbar_section_xml_BE.get(rdf+'ID'), busbar_section_xml_BE.find(
        cim+'IdentifiedObject.name').text, busbar_section_xml_BE.find(cim+'Equipment.EquipmentContainer').get(rdf+'resource'), "", "",""))

#Forming the list of Connectivity nodes
for connectivity_node_xml_BE in root_EQ_BE.iter(cim+'ConnectivityNode'):
    connectivity_node_list_BE.append(connectivity_node(connectivity_node_xml_BE.get(
        rdf+'ID'), connectivity_node_xml_BE.find(cim+'IdentifiedObject.name').text,
        connectivity_node_xml_BE.find(cim+"ConnectivityNode.ConnectivityNodeContainer").get(rdf+"resource"),"", "",""))

# Forming the list for energy source
for energy_source_xml_BE in root_EQ_BE.iter(cim+'EnergySource'):
    energy_source_list_BE.append(energy_source(energy_source_xml_BE.get(rdf+'ID'),
                              energy_source_xml_BE.find(cim+'IdentifiedObject.name').text, 
                              energy_source_xml_BE.find(cim+'Equipment.EquipmentContainer').get(rdf+'resource'), ""))

#Forming the list of Energy Consumers
for energy_consumer_load_xml_BE in root_EQ_BE.iter(cim+'EnergyConsumer'):
    energy_consumer_load_list_BE.append(energy_consumer_load(energy_consumer_load_xml_BE.get(rdf+'ID'),
                                                          energy_consumer_load_xml_BE.find(cim+'IdentifiedObject.name').text, "", "",
                                                          energy_consumer_load_xml_BE.find(cim+'Equipment.EquipmentContainer').get(rdf+'resource'), ""))

count=0
for energy_consumer_load_xml_BE in root_SSH_BE.iter(cim+"EnergyConsumer"):
    energy_consumer_load_list_BE[count].active_power=energy_consumer_load_xml_BE.find(cim+"EnergyConsumer.p").text
    energy_consumer_load_list_BE[count].reactive_power=energy_consumer_load_xml_BE.find(cim+"EnergyConsumer.q").text
    count+=1

#Forming the list of Linear Shunt Compensators
for linear_shunt_compensator_xml_BE in root_EQ_BE.iter(cim+'LinearShuntCompensator'):
    linear_shunt_compensator_list_BE.append(linear_shunt_compensator(linear_shunt_compensator_xml_BE.get(rdf+'ID'),
                                                                  linear_shunt_compensator_xml_BE.find(cim+'IdentifiedObject.name').text, linear_shunt_compensator_xml_BE.find(cim+'LinearShuntCompensator.bPerSection').text,
                                                                  linear_shunt_compensator_xml_BE.find(cim+'LinearShuntCompensator.gPerSection').text,"","", linear_shunt_compensator_xml_BE.find(cim+'Equipment.EquipmentContainer').get(rdf+'resource'), "",
                                                                  linear_shunt_compensator_xml_BE.find(cim+'ShuntCompensator.nomU').text,""))

#Forming the list of CS Converters
for cs_converter_xml_BE in root_EQ_BE.iter(cim+'CsConverter'):
    cs_converter_list_BE.append(cs_converter(cs_converter_xml_BE.get(rdf+'ID'),
                                                                  cs_converter_xml_BE.find(cim+'IdentifiedObject.name').text, cs_converter_xml_BE.find(cim+'Equipment.EquipmentContainer').get(rdf+'resource'), ""))

#Forming the list of Power Transfoemrs Windings
for power_transformer_end_transformer_winding_xml_BE in root_EQ_BE.iter(cim+'PowerTransformerEnd'):
    power_transformer_end_transformer_winding_list_BE.append(power_transformer_end_transformer_winding(power_transformer_end_transformer_winding_xml_BE.get(rdf+'ID'),
                                                                                                    power_transformer_end_transformer_winding_xml_BE.find(cim+'IdentifiedObject.name').text,
                                                                                                    power_transformer_end_transformer_winding_xml_BE.find(cim+'PowerTransformerEnd.r').text,
                                                                                                    power_transformer_end_transformer_winding_xml_BE.find(cim+'PowerTransformerEnd.x').text,
                                                                                                    power_transformer_end_transformer_winding_xml_BE.find(cim+'PowerTransformerEnd.PowerTransformer').get(rdf+'resource'),
                                                                                                    power_transformer_end_transformer_winding_xml_BE.find(cim+'TransformerEnd.BaseVoltage').get(rdf+'resource'),
                                                                                                    power_transformer_end_transformer_winding_xml_BE.find(cim+'PowerTransformerEnd.b').text,
                                                                                                    power_transformer_end_transformer_winding_xml_BE.find(cim+'PowerTransformerEnd.g').text,""))

#Forming the list of Power Transformers
for i in voltage_level_list_BE:
    for j in base_voltage_list_BE:
        if i.base_voltage_rdf_ID.replace("#", "") == j.rdf_ID:
            i.nominal_voltage = float(j.nominal_value)

# 2. Assign the nominal voltage to the power transformer
default_nominal_voltage = 15.75  # Set your desired default nominal voltage value here

all_nominal_voltages = []

for power_transformer_xml_BE in root_EQ_BE.iter(cim+'PowerTransformer'):
    transformer_rdf_ID = power_transformer_xml_BE.get(rdf+'ID')
    transformer_name = power_transformer_xml_BE.find(cim+'IdentifiedObject.name').text
    equipment_container_rdf_ID = power_transformer_xml_BE.find(cim+'Equipment.EquipmentContainer').get(rdf+'resource')
    nominal_voltage = []

    for pt_end_xml_BE in power_transformer_end_transformer_winding_list_BE:
        if pt_end_xml_BE.transformer_rdf_ID.replace("#", "") == transformer_rdf_ID:
            base_voltage_rdf_ID = pt_end_xml_BE.base_voltage_rdf_ID.replace("#", "")
            processed_base_voltage_ids = set()
            for voltage_level in voltage_level_list_BE:
                if voltage_level.base_voltage_rdf_ID.replace("#", "") == base_voltage_rdf_ID and base_voltage_rdf_ID not in processed_base_voltage_ids:
                    if voltage_level.nominal_voltage == '':
                        nominal_voltage.append(default_nominal_voltage)
                    else:
                        nominal_voltage.append(voltage_level.nominal_voltage)
                    processed_base_voltage_ids.add(base_voltage_rdf_ID)

            if len(nominal_voltage) == 0:  # If no matching voltage_level found, append the default value
                nominal_voltage.append(default_nominal_voltage)

    print("Nominal Voltage:", nominal_voltage)
    all_nominal_voltages.append(nominal_voltage)
    power_transformer_list_BE.append(power_transformer(transformer_rdf_ID, transformer_name, equipment_container_rdf_ID, nominal_voltage))
print("All Nominal Voltages:", all_nominal_voltages)

#Forming the list of Substations
for substation_xml_BE in root_EQ_BE.iter(cim+"Substation"):
    substation_list_BE.append(substation(substation_xml_BE.get(rdf+"ID"),
                                      substation_xml_BE.find(cim+"IdentifiedObject.name").text,
                                      substation_xml_BE.find(cim+"Substation.Region").get(rdf+"resource")))

#Forming the list of Synchronous Machines
for synchronous_machine_xml_BE in root_EQ_BE.iter(cim+'SynchronousMachine'):
    synchronous_machine_list_BE.append(synchronous_machine(synchronous_machine_xml_BE.get(rdf+'ID'),
                                                        synchronous_machine_xml_BE.find(cim+'IdentifiedObject.name').text,
                                                        synchronous_machine_xml_BE.find(cim+'RotatingMachine.ratedS').text, "", "", synchronous_machine_xml_BE.find(
            cim+'RotatingMachine.GeneratingUnit').get(rdf+'resource'),
                                                        synchronous_machine_xml_BE.find(
                                                            cim+'RegulatingCondEq.RegulatingControl').get(rdf+'resource'),
                                                        synchronous_machine_xml_BE.find(cim+'Equipment.EquipmentContainer').get(rdf+'resource'),"",
                                                        synchronous_machine_xml_BE.find(cim+'RotatingMachine.ratedU').text, synchronous_machine_xml_BE.find(cim+'SynchronousMachine.maxQ').text,
                                                        synchronous_machine_xml_BE.find(cim+'SynchronousMachine.minQ').text,""))

count=0
for synchronous_machine_xml_BE in root_SSH_BE.iter(cim+'SynchronousMachine'):
    synchronous_machine_list_BE[count].active_power = synchronous_machine_xml_BE.find(
        cim+'RotatingMachine.p').text
    synchronous_machine_list_BE[count].reactive_power = synchronous_machine_xml_BE.find(
        cim+'RotatingMachine.q').text
    count += 1

for equivalent_injection_xml_BE in root_EQ_BE.iter(cim+'EquivalentInjection'):
    equivalent_injection_list_BE.append(equivalent_injection(
        equivalent_injection_xml_BE.get(rdf+'ID'),
        equivalent_injection_xml_BE.find(cim+'IdentifiedObject.name').text,
        equivalent_injection_xml_BE.find(cim+'EquivalentInjection.r').text,
        equivalent_injection_xml_BE.find(cim+'EquivalentInjection.x').text,
        equivalent_injection_xml_BE.find(cim+'ConductingEquipment.BaseVoltage').get(rdf+'resource')))

#Forming the list of Terminals
for terminal_xml_BE in root_EQ_BE.iter(cim + 'Terminal'):
    rdf_ID = terminal_xml_BE.get(rdf + 'ID')
    name = terminal_xml_BE.find(cim + 'IdentifiedObject.name').text
    CE_rdf_ID = terminal_xml_BE.find(cim + 'Terminal.ConductingEquipment').get(rdf + 'resource') if terminal_xml_BE.find(cim + 'Terminal.ConductingEquipment') is not None else ""
    CN_rdf_ID = terminal_xml_BE.find(cim + 'Terminal.ConnectivityNode').get(rdf + 'resource') if terminal_xml_BE.find(cim + 'Terminal.ConnectivityNode') is not None else ""
    traversal_flag = 0
    # Create the Terminal object with the extracted data
    terminal_list_BE.append(terminal(rdf_ID, name, CE_rdf_ID, CN_rdf_ID))

#Conducting Equipment List
for i in range(len(synchronous_machine_list_BE)):
    conducting_equipment_list_BE.append(conducting_equipment(
        synchronous_machine_list_BE[i].rdf_ID, synchronous_machine_list_BE[i].name, "SynchronousMachine", "Connected","","",""))

for i in range(len(power_transformer_list_BE)):
    conducting_equipment_list_BE.append(conducting_equipment(
        power_transformer_list_BE[i].rdf_ID, power_transformer_list_BE[i].name, "PowerTransformer", "Connected",power_transformer_list_BE[i].nominal_voltage,"",""))

for i in range(len(cs_converter_list_BE)):
    conducting_equipment_list_BE.append(conducting_equipment(
        cs_converter_list_BE[i].rdf_ID, cs_converter_list_BE[i].name, "CSConverters", "Connected",cs_converter_list_BE[i].nominal_voltage,"",""))

for i in range(len(energy_consumer_load_list_BE)):
    conducting_equipment_list_BE.append(conducting_equipment(
        energy_consumer_load_list_BE[i].rdf_ID, energy_consumer_load_list_BE[i].name, "EnergyConsumerLoad", "Connected","",
        energy_consumer_load_list_BE[i].active_power,energy_consumer_load_list_BE[i].reactive_power))

for i in range(len(energy_source_list_BE)):
    conducting_equipment_list_BE.append(conducting_equipment(energy_source_list_BE[i].rdf_ID, energy_source_list_BE[i].name, "EnergySource", "Connected", "", "", ""))

for i in range(len(breaker_list_BE)):
    conducting_equipment_list_BE.append(conducting_equipment(
        breaker_list_BE[i].rdf_ID, breaker_list_BE[i].name, "Breaker",breaker_list_BE[i].state,"","",""))

for i in range(len(AC_line_segment_list_BE)):
    conducting_equipment_list_BE.append(conducting_equipment(
        AC_line_segment_list_BE[i].rdf_ID, AC_line_segment_list_BE[i].name, "ACLineSegment", "Connected","","",""))

for i in range(len(busbar_section_list_BE)):
    conducting_equipment_list_BE.append(conducting_equipment(
        busbar_section_list_BE[i].rdf_ID, busbar_section_list_BE[i].name, "BusbarSection", "Connected","","",""))

for i in range(len(linear_shunt_compensator_list_BE)):
    conducting_equipment_list_BE.append(conducting_equipment(
        linear_shunt_compensator_list_BE[i].rdf_ID, linear_shunt_compensator_list_BE[i].name, "LinearShuntCompensator", "Connected","","",""))

for i in range(len(power_transformer_end_transformer_winding_list_BE)):
    conducting_equipment_list_BE.append(conducting_equipment(
        power_transformer_end_transformer_winding_list_BE[i].rdf_ID, power_transformer_end_transformer_winding_list_BE[i].name, "PowerTransformerEnd", "Connected","","",""))

for i in range(len(equivalent_injection_list_BE)):
    conducting_equipment_list_BE.append(conducting_equipment(
        equivalent_injection_list_BE[i].rdf_ID, equivalent_injection_list_BE[i].name, "Equivalent injection", "Connected","","",""))

#Base Voltage Calculation

for i in range(len(synchronous_machine_list_BE)):
    req_rdf_ID=synchronous_machine_list_BE[i].equipment_container_rdf_ID
    req_rdf_ID=req_rdf_ID.replace("#", "")
    for j in range(len(voltage_level_list_BE)):
        if req_rdf_ID==voltage_level_list_BE[j].rdf_ID:
            req_base_voltage_rdf_ID=voltage_level_list_BE[j].base_voltage_rdf_ID
            req_base_voltage_rdf_ID=req_base_voltage_rdf_ID.replace("#", "")
            for k in range(len(base_voltage_list_BE)):
                if req_base_voltage_rdf_ID==base_voltage_list_BE[k].rdf_ID:
                    synchronous_machine_list_BE[i].base_voltage_rdf_ID="#" + base_voltage_list_BE[k].rdf_ID

for i in range(len(energy_source_list_BE)):
    buff_rdf_ID = energy_source_list_BE[i].equipment_container_rdf_ID
    buff_rdf_ID = buff_rdf_ID.replace("#", "")
    for j in range(len(voltage_level_list_BE)):
        if buff_rdf_ID == voltage_level_list_BE[j].rdf_ID:
            buff_base_voltage_ID = voltage_level_list_BE[j].base_voltage_rdf_ID
            buff_base_voltage_ID = buff_base_voltage_ID.replace("#", "")
            for k in range(len(base_voltage_list_BE)):
                if buff_base_voltage_ID == base_voltage_list_BE[k].rdf_ID:
                    energy_source_list_BE[i].base_voltage_rdf_ID = "#" + base_voltage_list_BE[k].rdf_ID
                    
for i in range(len(energy_consumer_load_list_BE)):
    buff_rdf_ID = energy_consumer_load_list_BE[i].equipment_container_rdf_ID
    buff_rdf_ID = buff_rdf_ID.replace("#", "")
    for j in range(len(voltage_level_list_BE)):
        if buff_rdf_ID == voltage_level_list_BE[j].rdf_ID:
            buff_base_voltage_ID = voltage_level_list_BE[j].base_voltage_rdf_ID
            buff_base_voltage_ID = buff_base_voltage_ID.replace("#", "")
            for k in range(len(base_voltage_list_BE)):
                if buff_base_voltage_ID == base_voltage_list_BE[k].rdf_ID:
                    energy_consumer_load_list_BE[i].base_voltage_rdf_ID = "#" + base_voltage_list_BE[k].rdf_ID

for i in range(len(breaker_list_BE)):
    buff_rdf_ID = breaker_list_BE[i].equipment_container_rdf_ID
    buff_rdf_ID = buff_rdf_ID.replace("#", "")
    for j in range(len(voltage_level_list_BE)):
        if buff_rdf_ID == voltage_level_list_BE[j].rdf_ID:
            buff_base_voltage_ID = voltage_level_list_BE[j].base_voltage_rdf_ID
            buff_base_voltage_ID = buff_base_voltage_ID.replace("#", "")
            for k in range(len(base_voltage_list_BE)):
                if buff_base_voltage_ID == base_voltage_list_BE[k].rdf_ID:
                    breaker_list_BE[i].base_voltage_rdf_ID = "#"+ base_voltage_list_BE[k].rdf_ID

# Get Energy Consumer rdf ID list
energy_consumer_load_rdf_ID_list_BE=[]
for i in range(len(energy_consumer_load_list_BE)):
    energy_consumer_load_rdf_ID_list_BE.append(energy_consumer_load_list_BE[i].rdf_ID)

# Get Energy Source rdf ID list
energy_source_rdf_ID_list_BE=[]
for i in range(len(energy_source_list_BE)):
    energy_source_rdf_ID_list_BE.append(energy_source_list_BE[i].rdf_ID)

# Get Synchronous Machine rdf ID list
synchronous_machine_rdf_ID_list_BE=[]
for i in range(len(synchronous_machine_list_BE)):
    synchronous_machine_rdf_ID_list_BE.append(synchronous_machine_list_BE[i].rdf_ID)

# Get Linear Shunt Compensator rdf ID List
linear_shunt_compensator_rdf_ID_list_BE=[]
for i in range(len(linear_shunt_compensator_list_BE)):
    linear_shunt_compensator_rdf_ID_list_BE.append(linear_shunt_compensator_list_BE[i].rdf_ID)

# Get Open Breaker rdf ID
breaker_open_rdf_ID_list_BE=[]
for i in range(len(breaker_list_BE)):
    if breaker_list_BE[i].state == "true" :
        breaker_open_rdf_ID_list_BE.append(breaker_list_BE[i].rdf_ID)

# Get Breaker rdf ID List
breaker_rdf_ID_list_BE = []
for i in range(len(breaker_list_BE)):
    breaker_rdf_ID_list_BE.append(breaker_list_BE[i].rdf_ID)

# Get Bus bar rdf ID List
busbar_section_rdf_id_list_BE=[]
for i in range(len(busbar_section_list_BE)):
    busbar_section_rdf_id_list_BE.append(busbar_section_list_BE[i].rdf_ID)

# Get Power Transformer rdf ID list
power_transformer_rdf_id_list_BE=[]
for i in range(len(power_transformer_list_BE)):
    power_transformer_rdf_id_list_BE.append(power_transformer_list_BE[i].rdf_ID)

# Get Power Transformer rdf ID list
cs_converter_rdf_id_list_BE=[]
for i in range(len(cs_converter_list_BE)):
    cs_converter_rdf_id_list_BE.append(cs_converter_list_BE[i].rdf_ID)

# Get Power Transformer end rdf ID list
power_transformer_end_transformer_winding_rdf_id_list_BE = []
for i in range(len(power_transformer_end_transformer_winding_list_BE)):
    power_transformer_end_transformer_winding_rdf_id_list_BE.append(power_transformer_end_transformer_winding_list_BE[i].rdf_ID)

# Get Power Transformer end rdf ID list
equivalent_injection_rdf_ID_BE = []
for i in range(len(equivalent_injection_list_BE)):
    equivalent_injection_rdf_ID_BE.append(equivalent_injection_list_BE[i].rdf_ID)

#List of objects of all the defined classes
base_voltage_list_NL=[]
substation_list_NL=[]
AC_line_segment_list_NL=[]
breaker_list_NL=[]
busbar_section_list_NL=[]
connectivity_node_list_NL=[]
energy_source_list_NL=[]
energy_consumer_load_list_NL=[]
linear_shunt_compensator_list_NL=[]
power_transformer_list_NL=[]
cs_converter_list_NL=[]
power_transformer_end_transformer_winding_list_NL=[]
synchronous_machine_list_NL=[]
equivalent_injection_list_NL=[]
terminal_list_NL=[]
voltage_level_list_NL=[]
conducting_equipment_list_NL=[]

#Forming the list of Voltage Levels
for voltage_level_xml_NL in root_EQ_NL.iter(cim+'VoltageLevel'):
    voltage_level_list_NL.append(voltage_level_NL(voltage_level_xml_NL.get(rdf+'ID'),
                                            voltage_level_xml_NL.find(cim+'IdentifiedObject.name').text,
                                            voltage_level_xml_NL.find(cim+'VoltageLevel.Substation').get(rdf+'resource'),
                                            voltage_level_xml_NL.find(cim+'VoltageLevel.BaseVoltage').get(rdf+'resource'),""))

#Forming the list of AC Line Segments
for AC_line_segment_xml_NL in root_EQ_NL.iter(cim+'ACLineSegment'):
    AC_line_segment_list_NL .append(AC_line_segment(AC_line_segment_xml_NL.get(rdf+'ID'),
                                                AC_line_segment_xml_NL.find(cim+'IdentifiedObject.name').text,
                                                AC_line_segment_xml_NL.find(cim+'Equipment.EquipmentContainer').get(rdf+'resource'),
                                                AC_line_segment_xml_NL.find(cim+'ACLineSegment.r').text, AC_line_segment_xml_NL.find(cim+'ACLineSegment.x').text,
                                                AC_line_segment_xml_NL.find(cim+'ACLineSegment.bch').text, AC_line_segment_xml_NL.find(cim+'ACLineSegment.gch').text,
                                                AC_line_segment_xml_NL.find(cim+'Conductor.length').text, AC_line_segment_xml_NL.find(cim+'ConductingEquipment.BaseVoltage').get(rdf+'resource'),
                                                AC_line_segment_xml_NL.find(cim+"ACLineSegment.r0"), AC_line_segment_xml_NL.find(cim+"ACLineSegment.x0"),
                                                AC_line_segment_xml_NL.find(cim+"ACLineSegment.b0ch"),AC_line_segment_xml_NL.find(cim+"ACLineSegment.g0ch"),
                                                AC_line_segment_xml_NL.find(cim+"ACLineSegment.shortCircuitEndTemperature"),""))

#Forming the list of Base Voltages
for base_voltage_xml_NL in root_EQ_NL.iter(cim+"BaseVoltage"):
    base_voltage_list_NL.append(base_voltage(base_voltage_xml_NL.get(rdf+"ID"),
                                          base_voltage_xml_NL.find(cim+"BaseVoltage.nominalVoltage").text,""))

#Forming the list of Breakers
for breaker_xml_NL in root_EQ_NL.iter(cim+'Breaker'):
    breaker_list_NL.append(breaker(breaker_xml_NL.get(rdf+'ID'), breaker_xml_NL.find(cim+'IdentifiedObject.name').text,
                                "", breaker_xml_NL.find(cim+'Equipment.EquipmentContainer').get(rdf+'resource'), "",""))

count=0
for breaker_xml_NL in root_SSH_NL.iter(cim+"Breaker"):
    for i in range(len(breaker_list_NL)):
        if breaker_list_NL[i].rdf_ID == breaker_xml_NL.get(rdf+"about").lstrip("#"):
            breaker_list_NL[i].state=breaker_xml_NL.find(cim+"Switch.open").text
            count+=1

#Forming the list of Bus Bar sections
for busbar_section_xml_NL in root_EQ_NL.iter(cim+'BusbarSection'):
    busbar_section_list_NL.append(busbar_section(busbar_section_xml_NL.get(rdf+'ID'), busbar_section_xml_NL.find(
        cim+'IdentifiedObject.name').text, busbar_section_xml_NL.find(cim+'Equipment.EquipmentContainer').get(rdf+'resource'), "", "",""))

#Forming the list of Connectivity nodes
for connectivity_node_xml_NL in root_EQ_NL.iter(cim+'ConnectivityNode'):
    connectivity_node_list_NL.append(connectivity_node(connectivity_node_xml_NL.get(
        rdf+'ID'), connectivity_node_xml_NL.find(cim+'IdentifiedObject.name').text,
        connectivity_node_xml_NL.find(cim+"ConnectivityNode.ConnectivityNodeContainer").get(rdf+"resource"),"", "",""))

# Forming the list for energy source
for energy_source_xml_NL in root_EQ_NL.iter(cim+'EnergySource'):
    energy_source_list_NL.append(energy_source(energy_source_xml_NL.get(rdf+'ID'),
                              energy_source_xml_NL.find(cim+'IdentifiedObject.name').text, 
                              energy_source_xml_NL.find(cim+'Equipment.EquipmentContainer').get(rdf+'resource'), ""))

#Forming the list of Energy Consumers
for energy_consumer_load_xml_NL in root_EQ_NL.iter(cim+'EnergyConsumer'):
    energy_consumer_load_list_NL.append(energy_consumer_load(energy_consumer_load_xml_NL.get(rdf+'ID'),
                                                          energy_consumer_load_xml_NL.find(cim+'IdentifiedObject.name').text, "", "",
                                                          energy_consumer_load_xml_NL.find(cim+'Equipment.EquipmentContainer').get(rdf+'resource'), ""))

count=0
for energy_consumer_load_xml_NL in root_SSH_NL.iter(cim+"EnergyConsumer"):
    energy_consumer_load_list_NL[count].active_power=energy_consumer_load_xml_NL.find(cim+"EnergyConsumer.p").text
    energy_consumer_load_list_NL[count].reactive_power=energy_consumer_load_xml_NL.find(cim+"EnergyConsumer.q").text
    count+=1

#Forming the list of Linear Shunt Compensators
for linear_shunt_compensator_xml_NL in root_EQ_NL.iter(cim+'LinearShuntCompensator'):
    linear_shunt_compensator_list_NL.append(linear_shunt_compensator(linear_shunt_compensator_xml_NL.get(rdf+'ID'),
                                                                  linear_shunt_compensator_xml_NL.find(cim+'IdentifiedObject.name').text, linear_shunt_compensator_xml_NL.find(cim+'LinearShuntCompensator.bPerSection').text,
                                                                  linear_shunt_compensator_xml_NL.find(cim+'LinearShuntCompensator.gPerSection').text,"","", linear_shunt_compensator_xml_NL.find(cim+'Equipment.EquipmentContainer').get(rdf+'resource'), "",
                                                                  linear_shunt_compensator_xml_NL.find(cim+'ShuntCompensator.nomU').text,""))

#Forming the list of CS Converters
for cs_converter_xml_NL in root_EQ_NL.iter(cim+'CsConverter'):
    cs_converter_list_NL.append(cs_converter(cs_converter_xml_NL.get(rdf+'ID'),
                                                                  cs_converter_xml_NL.find(cim+'IdentifiedObject.name').text, cs_converter_xml_NL.find(cim+'Equipment.EquipmentContainer').get(rdf+'resource'), ""))

#Forming the list of Power Transfoemrs Windings
for power_transformer_end_transformer_winding_xml_NL in root_EQ_NL.iter(cim+'PowerTransformerEnd'):
    power_transformer_end_transformer_winding_list_NL.append(power_transformer_end_transformer_winding(power_transformer_end_transformer_winding_xml_NL.get(rdf+'ID'),
                                                                                                    power_transformer_end_transformer_winding_xml_NL.find(cim+'IdentifiedObject.name').text,
                                                                                                    power_transformer_end_transformer_winding_xml_NL.find(cim+'PowerTransformerEnd.r').text,
                                                                                                    power_transformer_end_transformer_winding_xml_NL.find(cim+'PowerTransformerEnd.x').text,
                                                                                                    power_transformer_end_transformer_winding_xml_NL.find(cim+'PowerTransformerEnd.PowerTransformer').get(rdf+'resource'),
                                                                                                    power_transformer_end_transformer_winding_xml_NL.find(cim+'TransformerEnd.BaseVoltage').get(rdf+'resource'),
                                                                                                    power_transformer_end_transformer_winding_xml_NL.find(cim+'PowerTransformerEnd.b').text,
                                                                                                    power_transformer_end_transformer_winding_xml_NL.find(cim+'PowerTransformerEnd.g').text,""))

#Forming the list of Power Transformers
for i in voltage_level_list_NL:
    for j in base_voltage_list_NL:
        if i.base_voltage_rdf_ID.replace("#", "") == j.rdf_ID:
            i.nominal_voltage = float(j.nominal_value)

# 2. Assign the nominal voltage to the power transformer
default_nominal_voltage = 15.75  # Set your desired default nominal voltage value here

all_nominal_voltages = []

for power_transformer_xml_NL in root_EQ_NL.iter(cim+'PowerTransformer'):
    transformer_rdf_ID = power_transformer_xml_NL.get(rdf+'ID')
    transformer_name = power_transformer_xml_NL.find(cim+'IdentifiedObject.name').text
    equipment_container_rdf_ID = power_transformer_xml_NL.find(cim+'Equipment.EquipmentContainer').get(rdf+'resource')
    nominal_voltage = []

    for pt_end_xml_NL in power_transformer_end_transformer_winding_list_NL:
        if pt_end_xml_NL.transformer_rdf_ID.replace("#", "") == transformer_rdf_ID:
            base_voltage_rdf_ID = pt_end_xml_NL.base_voltage_rdf_ID.replace("#", "")
            processed_base_voltage_ids = set()
            for voltage_level in voltage_level_list_NL:
                if voltage_level.base_voltage_rdf_ID.replace("#", "") == base_voltage_rdf_ID and base_voltage_rdf_ID not in processed_base_voltage_ids:
                    if voltage_level.nominal_voltage == '':
                        nominal_voltage.append(default_nominal_voltage)
                    else:
                        nominal_voltage.append(voltage_level.nominal_voltage)
                    processed_base_voltage_ids.add(base_voltage_rdf_ID)

            if len(nominal_voltage) == 0:  # If no matching voltage_level found, append the default value
                nominal_voltage.append(default_nominal_voltage)

    print("Nominal Voltage:", nominal_voltage)
    all_nominal_voltages.append(nominal_voltage)
    power_transformer_list_NL.append(power_transformer(transformer_rdf_ID, transformer_name, equipment_container_rdf_ID, nominal_voltage))
print("All Nominal Voltages:", all_nominal_voltages)

#Forming the list of Substations
for substation_xml_NL in root_EQ_NL.iter(cim+"Substation"):
    substation_list_NL.append(substation(substation_xml_NL.get(rdf+"ID"),
                                      substation_xml_NL.find(cim+"IdentifiedObject.name").text,
                                      substation_xml_NL.find(cim+"Substation.Region").get(rdf+"resource")))

#Forming the list of Synchronous Machines
for synchronous_machine_xml_NL in root_EQ_NL.iter(cim+'SynchronousMachine'):
    synchronous_machine_list_NL.append(synchronous_machine(synchronous_machine_xml_NL.get(rdf+'ID'),
                                                        synchronous_machine_xml_NL.find(cim+'IdentifiedObject.name').text,
                                                        synchronous_machine_xml_NL.find(cim+'RotatingMachine.ratedS').text, "", "", synchronous_machine_xml_NL.find(
            cim+'RotatingMachine.GeneratingUnit').get(rdf+'resource'),
                                                        synchronous_machine_xml_NL.find(
                                                            cim+'RegulatingCondEq.RegulatingControl').get(rdf+'resource'),
                                                        synchronous_machine_xml_NL.find(cim+'Equipment.EquipmentContainer').get(rdf+'resource'),"",
                                                        synchronous_machine_xml_NL.find(cim+'RotatingMachine.ratedU').text, synchronous_machine_xml_NL.find(cim+'SynchronousMachine.maxQ').text,
                                                        synchronous_machine_xml_NL.find(cim+'SynchronousMachine.minQ').text,""))

count=0
for synchronous_machine_xml_NL in root_SSH_NL.iter(cim+'SynchronousMachine'):
    synchronous_machine_list_NL[count].active_power = synchronous_machine_xml_NL.find(
        cim+'RotatingMachine.p').text
    synchronous_machine_list_NL[count].reactive_power = synchronous_machine_xml_NL.find(
        cim+'RotatingMachine.q').text
    count += 1

for equivalent_injection_xml_NL in root_EQ_NL.iter(cim+'EquivalentInjection'):
    equivalent_injection_list_NL.append(equivalent_injection(
        equivalent_injection_xml_NL.get(rdf+'ID'),
        equivalent_injection_xml_NL.find(cim+'IdentifiedObject.name').text,
        equivalent_injection_xml_NL.find(cim+'EquivalentInjection.r').text,
        equivalent_injection_xml_NL.find(cim+'EquivalentInjection.x').text,
        equivalent_injection_xml_NL.find(cim+'ConductingEquipment.BaseVoltage').get(rdf+'resource')))

#Forming the list of Terminals
for terminal_xml_NL in root_EQ_NL.iter(cim + 'Terminal'):
    rdf_ID = terminal_xml_NL.get(rdf + 'ID')
    name = terminal_xml_NL.find(cim + 'IdentifiedObject.name').text
    CE_rdf_ID = terminal_xml_NL.find(cim + 'Terminal.ConductingEquipment').get(rdf + 'resource') if terminal_xml_NL.find(cim + 'Terminal.ConductingEquipment') is not None else ""
    CN_rdf_ID = terminal_xml_NL.find(cim + 'Terminal.ConnectivityNode').get(rdf + 'resource') if terminal_xml_NL.find(cim + 'Terminal.ConnectivityNode') is not None else ""
    traversal_flag = 0
    # Create the Terminal object with the extracted data
    terminal_list_NL.append(terminal(rdf_ID, name, CE_rdf_ID, CN_rdf_ID))

#Conducting Equipment List
for i in range(len(synchronous_machine_list_NL)):
    conducting_equipment_list_NL.append(conducting_equipment(
        synchronous_machine_list_NL[i].rdf_ID, synchronous_machine_list_NL[i].name, "SynchronousMachine", "Connected","","",""))

for i in range(len(power_transformer_list_NL)):
    conducting_equipment_list_NL.append(conducting_equipment(
        power_transformer_list_NL[i].rdf_ID, power_transformer_list_NL[i].name, "PowerTransformer", "Connected",power_transformer_list_NL[i].nominal_voltage,"",""))

for i in range(len(cs_converter_list_NL)):
    conducting_equipment_list_NL.append(conducting_equipment(
        cs_converter_list_NL[i].rdf_ID, cs_converter_list_NL[i].name, "CSConverters", "Connected",cs_converter_list_NL[i].nominal_voltage,"",""))

for i in range(len(energy_consumer_load_list_NL)):
    conducting_equipment_list_NL.append(conducting_equipment(
        energy_consumer_load_list_NL[i].rdf_ID, energy_consumer_load_list_NL[i].name, "EnergyConsumerLoad", "Connected","",
        energy_consumer_load_list_NL[i].active_power,energy_consumer_load_list_NL[i].reactive_power))

for i in range(len(energy_source_list_NL)):
    conducting_equipment_list_NL.append(conducting_equipment(energy_source_list_NL[i].rdf_ID, energy_source_list_NL[i].name, "EnergySource", "Connected", "", "", ""))

for i in range(len(breaker_list_NL)):
    conducting_equipment_list_NL.append(conducting_equipment(
        breaker_list_NL[i].rdf_ID, breaker_list_NL[i].name, "Breaker",breaker_list_NL[i].state,"","",""))

for i in range(len(AC_line_segment_list_NL )):
    conducting_equipment_list_NL.append(conducting_equipment(
        AC_line_segment_list_NL [i].rdf_ID, AC_line_segment_list_NL [i].name, "ACLineSegment", "Connected","","",""))

for i in range(len(busbar_section_list_NL)):
    conducting_equipment_list_NL.append(conducting_equipment(
        busbar_section_list_NL[i].rdf_ID, busbar_section_list_NL[i].name, "BusbarSection", "Connected","","",""))

for i in range(len(linear_shunt_compensator_list_NL)):
    conducting_equipment_list_NL.append(conducting_equipment(
        linear_shunt_compensator_list_NL[i].rdf_ID, linear_shunt_compensator_list_NL[i].name, "LinearShuntCompensator", "Connected","","",""))

for i in range(len(power_transformer_end_transformer_winding_list_NL)):
    conducting_equipment_list_NL.append(conducting_equipment(
        power_transformer_end_transformer_winding_list_NL[i].rdf_ID, power_transformer_end_transformer_winding_list_NL[i].name, "PowerTransformerEnd", "Connected","","",""))

for i in range(len(equivalent_injection_list_NL)):
    conducting_equipment_list_NL.append(conducting_equipment(
        equivalent_injection_list_NL[i].rdf_ID, equivalent_injection_list_NL[i].name, "Equivalent injection", "Connected","","",""))

#Base Voltage Calculation

for i in range(len(synchronous_machine_list_NL)):
    req_rdf_ID=synchronous_machine_list_NL[i].equipment_container_rdf_ID
    req_rdf_ID=req_rdf_ID.replace("#", "")
    for j in range(len(voltage_level_list_NL)):
        if req_rdf_ID==voltage_level_list_NL[j].rdf_ID:
            req_base_voltage_rdf_ID=voltage_level_list_NL[j].base_voltage_rdf_ID
            req_base_voltage_rdf_ID=req_base_voltage_rdf_ID.replace("#", "")
            for k in range(len(base_voltage_list_NL)):
                if req_base_voltage_rdf_ID==base_voltage_list_NL[k].rdf_ID:
                    synchronous_machine_list_NL[i].base_voltage_rdf_ID="#" + base_voltage_list_NL[k].rdf_ID

for i in range(len(energy_source_list_NL)):
    buff_rdf_ID = energy_source_list_NL[i].equipment_container_rdf_ID
    buff_rdf_ID = buff_rdf_ID.replace("#", "")
    for j in range(len(voltage_level_list_NL)):
        if buff_rdf_ID == voltage_level_list_NL[j].rdf_ID:
            buff_base_voltage_ID = voltage_level_list_NL[j].base_voltage_rdf_ID
            buff_base_voltage_ID = buff_base_voltage_ID.replace("#", "")
            for k in range(len(base_voltage_list_NL)):
                if buff_base_voltage_ID == base_voltage_list_NL[k].rdf_ID:
                    energy_source_list_NL[i].base_voltage_rdf_ID = "#" + base_voltage_list_NL[k].rdf_ID
                    
for i in range(len(energy_consumer_load_list_NL)):
    buff_rdf_ID = energy_consumer_load_list_NL[i].equipment_container_rdf_ID
    buff_rdf_ID = buff_rdf_ID.replace("#", "")
    for j in range(len(voltage_level_list_NL)):
        if buff_rdf_ID == voltage_level_list_NL[j].rdf_ID:
            buff_base_voltage_ID = voltage_level_list_NL[j].base_voltage_rdf_ID
            buff_base_voltage_ID = buff_base_voltage_ID.replace("#", "")
            for k in range(len(base_voltage_list_NL)):
                if buff_base_voltage_ID == base_voltage_list_NL[k].rdf_ID:
                    energy_consumer_load_list_NL[i].base_voltage_rdf_ID = "#" + base_voltage_list_NL[k].rdf_ID

for i in range(len(breaker_list_NL)):
    buff_rdf_ID = breaker_list_NL[i].equipment_container_rdf_ID
    buff_rdf_ID = buff_rdf_ID.replace("#", "")
    for j in range(len(voltage_level_list_NL)):
        if buff_rdf_ID == voltage_level_list_NL[j].rdf_ID:
            buff_base_voltage_ID = voltage_level_list_NL[j].base_voltage_rdf_ID
            buff_base_voltage_ID = buff_base_voltage_ID.replace("#", "")
            for k in range(len(base_voltage_list_NL)):
                if buff_base_voltage_ID == base_voltage_list_NL[k].rdf_ID:
                    breaker_list_NL[i].base_voltage_rdf_ID = "#"+ base_voltage_list_NL[k].rdf_ID

# Get Energy Consumer rdf ID list
energy_consumer_load_rdf_ID_list_NL=[]
for i in range(len(energy_consumer_load_list_NL)):
    energy_consumer_load_rdf_ID_list_NL.append(energy_consumer_load_list_NL[i].rdf_ID)

# Get Energy Source rdf ID list
energy_source_rdf_ID_list_NL=[]
for i in range(len(energy_source_list_NL)):
    energy_source_rdf_ID_list_NL.append(energy_source_list_NL[i].rdf_ID)

# Get Synchronous Machine rdf ID list
synchronous_machine_rdf_ID_list_NL=[]
for i in range(len(synchronous_machine_list_NL)):
    synchronous_machine_rdf_ID_list_NL.append(synchronous_machine_list_NL[i].rdf_ID)

# Get Linear Shunt Compensator rdf ID List
linear_shunt_compensator_rdf_ID_list_NL=[]
for i in range(len(linear_shunt_compensator_list_NL)):
    linear_shunt_compensator_rdf_ID_list_NL.append(linear_shunt_compensator_list_NL[i].rdf_ID)

# Get Open Breaker rdf ID
breaker_open_rdf_ID_list_NL=[]
for i in range(len(breaker_list_NL)):
    if breaker_list_NL[i].state == "true" :
        breaker_open_rdf_ID_list_NL.append(breaker_list_NL[i].rdf_ID)

# Get Breaker rdf ID List
breaker_rdf_ID_list_NL = []
for i in range(len(breaker_list_NL)):
    breaker_rdf_ID_list_NL.append(breaker_list_NL[i].rdf_ID)

# Get Bus bar rdf ID List
busbar_section_rdf_id_list_NL=[]
for i in range(len(busbar_section_list_NL)):
    busbar_section_rdf_id_list_NL.append(busbar_section_list_NL[i].rdf_ID)

# Get Power Transformer rdf ID list
power_transformer_rdf_id_list_NL=[]
for i in range(len(power_transformer_list_NL)):
    power_transformer_rdf_id_list_NL.append(power_transformer_list_NL[i].rdf_ID)

# Get Power Transformer rdf ID list
cs_converter_rdf_id_list_NL=[]
for i in range(len(cs_converter_list_NL)):
    cs_converter_rdf_id_list_NL.append(cs_converter_list_NL[i].rdf_ID)

# Get Power Transformer end rdf ID list
power_transformer_end_transformer_winding_rdf_id_list_NL = []
for i in range(len(power_transformer_end_transformer_winding_list_NL)):
    power_transformer_end_transformer_winding_rdf_id_list_NL.append(power_transformer_end_transformer_winding_list_NL[i].rdf_ID)

# Get Power Transformer end rdf ID list
equivalent_injection_rdf_ID_NL = []
for i in range(len(equivalent_injection_list_NL)):
    equivalent_injection_rdf_ID_NL.append(equivalent_injection_list_NL[i].rdf_ID)

#List of objects of all the defined classes
base_voltage_list=[]
base_voltage_list = base_voltage_list_BE + base_voltage_list_NL
substation_list=[]
substation_list = substation_list_BE + substation_list_NL
AC_line_segment_list=[]
AC_line_segment_list = AC_line_segment_list_BE + AC_line_segment_list_NL
breaker_list=[]
breaker_list = breaker_list_BE + breaker_list_NL
busbar_section_list=[]
busbar_section_list = busbar_section_list_BE + busbar_section_list_NL
connectivity_node_list=[]
connectivity_node_list = connectivity_node_list_BE + connectivity_node_list_NL
energy_source_list=[]
energy_source_list = energy_source_list_BE + energy_source_list_NL
energy_consumer_load_list=[]
energy_consumer_load_list = energy_consumer_load_list_BE + energy_consumer_load_list_NL
linear_shunt_compensator_list=[]
linear_shunt_compensator_list = linear_shunt_compensator_list_BE + linear_shunt_compensator_list_NL
power_transformer_list=[]
power_transformer_list = power_transformer_list_BE + power_transformer_list_NL
power_transformer_end_transformer_winding_list=[]
power_transformer_end_transformer_winding_list = power_transformer_end_transformer_winding_list_BE + power_transformer_end_transformer_winding_list_NL
synchronous_machine_list=[]
synchronous_machine_list = synchronous_machine_list_BE + synchronous_machine_list_NL
equivalent_injection_list=[]
equivalent_injection_list = equivalent_injection_list_BE + equivalent_injection_list_NL
terminal_list=[]
terminal_list = terminal_list_BE + terminal_list_NL
voltage_level_list=[]
voltage_level_list = voltage_level_list_BE + voltage_level_list_NL
conducting_equipment_list=[]
conducting_equipment_list = conducting_equipment_list_BE + conducting_equipment_list_NL
energy_consumer_load_rdf_ID_list=[]
energy_consumer_load_rdf_ID_list = energy_consumer_load_rdf_ID_list_BE + energy_consumer_load_rdf_ID_list_NL
energy_source_rdf_ID_list=[]
energy_source_rdf_ID_list = energy_source_rdf_ID_list_BE + energy_source_rdf_ID_list_NL
synchronous_machine_rdf_ID_list=[]
synchronous_machine_rdf_ID_list = synchronous_machine_rdf_ID_list_BE + synchronous_machine_rdf_ID_list_NL
linear_shunt_compensator_rdf_ID_list=[]
linear_shunt_compensator_rdf_ID_list = linear_shunt_compensator_rdf_ID_list_BE + linear_shunt_compensator_rdf_ID_list_NL
breaker_open_rdf_ID_list=[]
breaker_open_rdf_ID_list = breaker_open_rdf_ID_list_BE + breaker_open_rdf_ID_list_NL
breaker_rdf_ID_list = []
breaker_rdf_ID_list = breaker_rdf_ID_list_BE + breaker_rdf_ID_list_NL
busbar_section_rdf_id_list=[]
busbar_section_rdf_id_list = busbar_section_rdf_id_list_BE + busbar_section_rdf_id_list_NL
power_transformer_rdf_id_list=[]
power_transformer_rdf_id_list = power_transformer_rdf_id_list_BE + power_transformer_rdf_id_list_NL
power_transformer_end_transformer_winding_rdf_id_list = []
power_transformer_end_transformer_winding_rdf_id_list = power_transformer_end_transformer_winding_rdf_id_list_BE + power_transformer_end_transformer_winding_rdf_id_list_NL
equivalent_injection_rdf_ID = []
equivalent_injection_rdf_ID = equivalent_injection_rdf_ID_BE + equivalent_injection_rdf_ID_NL

# Eroor handling for invalud CN
no_connection_terminal_CE=[]
no_connection_terminal_CN=[]
no_connection_terminal_CE_CN=[]
no_connection_CN=[]
connected_CN=[]

# Missing nodes
count=0
for i in range(len(terminal_list)):
    flag = 0
    for j in range(len(conducting_equipment_list)):
        if terminal_list[i].CE_rdf_ID.replace("#", "") == conducting_equipment_list[j].rdf_ID:
            flag = 1
            break
    if flag == 0:
        no_connection_terminal_CE.append(terminal_list[i])
        #  print("Invalid CE Terminals : ",no_connection_terminal_CE[count].rdf_ID)
        count+=1
# print("The count of terminals with invalid CE: ",count)

count =0
invalid_CN_rdf_ID = set()
for i in range(len(terminal_list)):
    flag = 0
    for j in range(len(connectivity_node_list)):
        if terminal_list[i].CN_rdf_ID.replace("#", "") == connectivity_node_list[j].rdf_ID:
            flag = 1
            connected_CN.append(connectivity_node_list[j])
            break
    if flag == 0:
        no_connection_terminal_CN.append(terminal_list[i])
        invalid_CN_rdf_ID.add(terminal_list[i].CN_rdf_ID.replace("#", ""))
        count+=1
# print(invalid_CN_rdf_ID)
# print("The count of terminals with invalid CN: ",count)

temp_num=0
for rdf_ID in invalid_CN_rdf_ID:
    cn_name="NewConnectivityNode-"+str(temp_num)
    # print("Invalid CN: ", rdf_ID)
    connectivity_node_list.append(connectivity_node(rdf_ID,cn_name,connectivity_node_list[0].connectivity_container_rdf_ID,"","",""))
    temp_num+=1
# print("Connectivity RDF: ",connectivity_node_list[0].connectivity_container_rdf_ID)

#Validation
count =0
invalid_CN_rdf_ID = set()
for i in range(len(terminal_list)):
    flag = 0
    for j in range(len(connectivity_node_list)):
        if terminal_list[i].CN_rdf_ID.replace("#", "") == connectivity_node_list[j].rdf_ID:
            flag = 1
            connected_CN.append(connectivity_node_list[j])
            break
    if flag == 0:
        no_connection_terminal_CN.append(terminal_list[i])
        invalid_CN_rdf_ID.add(terminal_list[i].CN_rdf_ID.replace("#", ""))
        count+=1
        # print(invalid_CN_rdf_ID[i].rdf_ID)
# print("The count of terminals with invalid CN after addition: ",count)

# Network Traversal
# Initialization

CN_CE_CN_stack = []
CN_CE_stack = []

#Get the Terminal ID connected to the bus bars and bus bar ID
terminal_attached_busbar_list=[]
terminal_not_attached_busbar_list=[]
for i in range(len(busbar_section_list)):
    for j in range(len(terminal_list)):
        if busbar_section_list[i].rdf_ID == terminal_list[j].CE_rdf_ID.replace("#", ""):
            # Check if terminal_list[j] is already in terminal_attached_busbar_list
            if terminal_list[j] not in terminal_attached_busbar_list:
                terminal_attached_busbar_list.append(terminal_list[j])


for i in range(len(terminal_list)):
    for j in range(len(terminal_attached_busbar_list)):
        # Check if terminal_list[j] is already in terminal_not_attached_busbar_list
        if terminal_list[i] not in terminal_attached_busbar_list and terminal_list[i] not in terminal_not_attached_busbar_list:
            terminal_not_attached_busbar_list.append(terminal_list[i])

terminal_attached_busbar_rdf_ID_list = []
for i in range(len(terminal_attached_busbar_list)):
    terminal_attached_busbar_rdf_ID_list.append(terminal_attached_busbar_list[i].rdf_ID)
    # print(terminal_attached_busbar_rdf_ID_list)


# Find the Connectivity Node attached and not attached to busbar
connectivity_node_attached_to_busbar_list=[]
connectivity_node_not_attached_to_busbar_list=[]
connectivity_node_attached_to_busbar_rdf_ID_list = []
for i in range(len(terminal_attached_busbar_list)):
    cn_rdf_ID = terminal_attached_busbar_list[i].CN_rdf_ID.replace("#", "")
    for j in range(len(connectivity_node_list)):
        if cn_rdf_ID == connectivity_node_list[j].rdf_ID:
            # Check if connectivity_node_list[j] is already in connectivity_node_attached_to_busbar_list
            if connectivity_node_list[j] not in connectivity_node_attached_to_busbar_list:
                connectivity_node_attached_to_busbar_list.append(connectivity_node_list[j])

for i in range(len(connectivity_node_list)):
    if connectivity_node_list[i] not in connectivity_node_attached_to_busbar_list and connectivity_node_list[i] not in connectivity_node_not_attached_to_busbar_list:
        connectivity_node_not_attached_to_busbar_list.append(connectivity_node_list[i])

for i in range(len(connectivity_node_attached_to_busbar_list)):
    connectivity_node_attached_to_busbar_rdf_ID_list.append(connectivity_node_attached_to_busbar_list[i].rdf_ID)
    # print(connectivity_node_attached_to_busbar_rdf_ID_list)

#--------------------------------------------------TRAVERSAL LOGIC--------------------------------------------
all_stack_list = []
all_stack_node_list = []

# FUnction to print the final traversal 
def print_traversal_final():
    global all_stack_node_list
    print("--------------------Printing the Traversal-------------------")
    for i in all_stack_node_list:
        print("==========================Traversal Tree==========================")
        for j in i:
            print("Node type:",j.type,"Node_id:",j.rdf_ID)
    
# Function to traverse
def traversal(prev,curr):
    if curr.traversal_flag == 0:
        curr.traversal_flag = 1
        global all_stack_list
        global all_stack_node_list
        while find_next_node(prev.rdf_ID, curr.rdf_ID, prev.type, curr.type, print_statements=False) != None:
            z = find_next_node(prev.rdf_ID, curr.rdf_ID, prev.type, curr.type, print_statements=False)
            if len(z) == 1:
                for item in all_stack_node_list:
                    if item[-1] == curr and item [-2] == prev:
                        item.append(z[0])
                        
            elif len(z) > 1:
                to_append = []
                for item in all_stack_node_list:
                    if item[-1] == curr and item[-2] == prev:
                        to_append = item
                for _ in range(len(z)-1):
                    all_stack_node_list.append(list(to_append))
                for element in z:
                    for item in all_stack_node_list:
                        if item[-1] == curr and item[-2] == prev:
                            item.append(element)
                            break
            for i in z:
                traversal(curr, i)
        else:
            return

#Function to print the next node details from the list
def next_node_statistics(x):
    print("The next node details are:")
    for i in x:
        if i != None:
            print("Type, rdf_ID: %s %s",i.type,i.rdf_ID)
        else:
            print("Type, rdf_ID: None None")


# Function to find the next node
def find_next_node(prev_node_rdf_ID, curr_node_rdf_ID, previous_node_type, current_node_type, print_statements):
    next_node = None

    # If the current node is CE, Next node is terminal
    if current_node_type == "conducting equipment":
        if print_statements == True:
            print("\n---------- CE->T ----------\n")
            print("Current node details(Type, rdf_ID): %s %s",current_node_type,curr_node_rdf_ID)
        return_list = []
        for i in range(len(conducting_equipment_list)):
            if curr_node_rdf_ID == conducting_equipment_list[i].rdf_ID:
                for j in range(len(terminal_list)):
                    if curr_node_rdf_ID == terminal_list[j].CE_rdf_ID.replace("#", "") and terminal_list[j].traversal_flag == 0:
                        next_node = terminal_list[j]
                        return_list.append(next_node)
        
    # If the current node is CN, Next node is terminal
    if current_node_type == "connectivity node":
        return_list = []
        if print_statements == True:
            print("\n---------- CN->T ----------\n")
            print("Current node details(Type, rdf_ID): %s %s",current_node_type,curr_node_rdf_ID)
        for k in range(len(connectivity_node_list)):
            if curr_node_rdf_ID == connectivity_node_list[k].rdf_ID:
                for j in range(len(terminal_list)):
                    if curr_node_rdf_ID == terminal_list[j].CN_rdf_ID.replace("#", "") and terminal_list[j].traversal_flag == 0:
                        next_node = terminal_list[j]
                        return_list.append(next_node)
                        
    # If the current node is terminal and previous is CE
    # Next node is CN and Vice versa
    if current_node_type == "terminal" and previous_node_type == "conducting equipment":
        return_list = []
        if print_statements == True:
            print("\n---------- T->CN ----------\n")
            print("Current node details(Type, rdf_ID): %s %s",current_node_type,curr_node_rdf_ID)
        for l in range(len(terminal_list)):
            if curr_node_rdf_ID == terminal_list[l].rdf_ID:
                for j in range(len(conducting_equipment_list)):
                    if prev_node_rdf_ID == conducting_equipment_list[j].rdf_ID:
                        for m in range(len(connectivity_node_list)):
                            if connectivity_node_list[m].rdf_ID == terminal_list[l].CN_rdf_ID.replace("#", "") and connectivity_node_list[m].traversal_flag == 0:
                                next_node = connectivity_node_list[m]
                                return_list.append(next_node)
                                
    if current_node_type == "terminal" and previous_node_type == "connectivity node":
        return_list = []
        if print_statements == True:
            print("\n---------- T->CE ----------\n")
            print("Current node details(Type, rdf_ID): %s %s",current_node_type,curr_node_rdf_ID)
        for n in range(len(terminal_list)):
            if curr_node_rdf_ID == terminal_list[n].rdf_ID:
                for j in range(len(connectivity_node_list)):
                    if prev_node_rdf_ID == connectivity_node_list[j].rdf_ID:
                        for m in range(len(conducting_equipment_list)):
                            if conducting_equipment_list[m].rdf_ID == terminal_list[n].CE_rdf_ID.replace("#", "") and conducting_equipment_list[m].traversal_flag == 0:
                                next_node = conducting_equipment_list[m]
                                return_list.append(next_node)
                                
    if len(return_list) == 0:
        return None

    return return_list
    print("Return list",return_list)

# Appending the traversal flag for all the busbars
for i in busbar_section_list:
    i.traversal_flag = 1

# Appending the traversal flag for all the terminals attached to the busbar
for t in terminal_attached_busbar_list:
    t.traversal_flag = 1
    list_t = []
    list_t.append(t)
    all_stack_node_list.append(list_t)
    for cnb in connectivity_node_attached_to_busbar_list:
        if cnb.rdf_ID == t.CN_rdf_ID.replace("#", ""):
            for element in all_stack_node_list:
                if element[0] == t:
                    element.append(cnb)
            traversal(t,cnb)

# printing the entire traversal
for i in all_stack_node_list:
    if i[-1].type == "terminal":
        for x in i:
            print("Node type:",x.type,"Node_id:",x.rdf_ID)
        if i[-2].type == "conducting equipment":
            for j in connectivity_node_list:
                if i[-1].CN_rdf_ID.replace("#", "") == j.rdf_ID:
                    i.append(j)
                    break
        elif i[-2].type == "connectivity node":
            print("Next node should be conducting equipment")
            for j in conducting_equipment_list:
                if i[-1].CE_rdf_ID.replace("#", "") == j.rdf_ID:
                    i.append(j)
                    break
print_traversal_final()


#Creating the all_stack_list
all_stack_list = [None] * len(all_stack_node_list)
for i in range(len(all_stack_node_list)):
    all_stack_list[i] = []
    for j in range(len(all_stack_node_list[i])):
        all_stack_list[i].append(all_stack_node_list[i][j].type)

#------------------------------------------------------------------PANDA POWER------------------------------------------------------------------

# CN_CE_CN_stack creation
counter=0
for i in all_stack_list:
   for j in range(len(i)):
      if i[j] == 'connectivity node':
        if i[j:j+5] == ['connectivity node', 'terminal', 'conducting equipment', 'terminal', 'connectivity node']:
           CN_CE_CN_stack.append(all_stack_node_list[counter][j:j+5])
   counter +=1

# print("CN_CE_CN_stack type: ", CN_CE_CN_stack)

# CN_CE_stack creation
counter=0
for i in all_stack_list:
   for j in range(len(i)):
      # if i[j] == 'connectivity node' and (j+3 < len(i)):
        if i[j:j+3] == ['connectivity node', 'terminal', 'conducting equipment']:
           CN_CE_stack.append(all_stack_node_list[counter][j:j+3])
   counter +=1
   
# print("CN_CE_stack: ",CN_CE_stack)

# for i in CN_CE_stack:
#     for  j in i:
#         print(j.type_CE)
        
# importing panda power modules
import pandapower as pp
import pandapower.plotting.to_html as kk


# Create Panda Power network
network = pp.create_empty_network()

#Create Buses
# 1.Get the VoltageLevel and baseVoltage for each bus
for i in voltage_level_list:
   for j in base_voltage_list:
      if i.base_voltage_rdf_ID.replace("#", "")==j.rdf_ID:
         i.nominal_voltage=float(j.nominal_value)

default_nominal_voltage = 21.0

for i in busbar_section_list:
    i.nominal_voltage = default_nominal_voltage
    for j in voltage_level_list:
        if j.rdf_ID == i.equipment_container_rdf_ID.replace("#", "") and j.nominal_voltage != '':
           i.nominal_voltage = j.nominal_voltage
           # print(i.nominal_voltage)
           break

# Gather nominal voltage for CNs
default_nominal_voltage = 15.75  # Set your desired default nominal voltage value here

for i in connectivity_node_list:
    i.nominal_voltage = default_nominal_voltage
    for j in voltage_level_list:
        if j.rdf_ID == i.connectivity_container_rdf_ID.replace("#", ""):
            i.nominal_voltage = j.nominal_voltage
            break

#create busbar
existing_bus_names = set()
existing_bus_names_cn = set()
    
# Create buses for busbar sections and connectivity nodes
for Busbar_Section in busbar_section_list:
    if Busbar_Section.name not in existing_bus_names:
        pp.create_bus(network, name=Busbar_Section.name, vn_kv=Busbar_Section.nominal_voltage, type="b")
        existing_bus_names.add(Busbar_Section.name)

for CN in connectivity_node_list:
    if CN.name not in existing_bus_names_cn and CN.name not in existing_bus_names:
        if CN.nominal_voltage is None or CN.nominal_voltage == "":
            CN.nominal_voltage = default_nominal_voltage
        else:
            print("Nominal voltage found for Connectivity Node:", CN.name, CN.nominal_voltage)
        
        pp.create_bus(network, name=CN.name, vn_kv=CN.nominal_voltage, type="n")
        existing_bus_names_cn.add(CN.name)
print("-------------------------------------------------------------------------")
print(network.bus)
                
#create line
added_line_names = set()

for item in CN_CE_CN_stack:
    for lines in item:
        if lines.type_CE == "ACLineSegment":
            line_name = lines.name
            if line_name not in added_line_names:
               from_bus=item[0]
               index_1=pp.get_element_index(network, "bus", from_bus.name)
               to_bus=item[-1]                
               index_2=pp.get_element_index(network, "bus", to_bus.name)
               pp.create_line(network, index_1, index_2, length_km=2, std_type="N2XS(FL)2Y 1x300 RM/35 64/110 kV", name=line_name)
               added_line_names.add(line_name)

# Now you can print the network.line to verify the lines
print("Printing the network line--------")
print(network.line)
print("Printing the network line--------")

#create breaker
added_switch_names = set()

for item in CN_CE_CN_stack:
    for Breaker in item:
        if Breaker.type_CE == "Breaker":
            switch_name = Breaker.name
            if switch_name not in added_switch_names:
                if Breaker.state == "false":
                    from_bus=item[0]
                    index_1=pp.get_element_index(network, "bus", from_bus.name)
                    to_bus=item[-1]                
                    index_2=pp.get_element_index(network, "bus", to_bus.name)
                    pp.create_switch(network, index_1, index_2, et="b", type="CB", closed=True, name=switch_name)
                if Breaker.state == "true":
                    from_bus=item[0]
                    index_1=pp.get_element_index(network, "bus", from_bus.name)
                    to_bus=item[-1]                
                    index_2=pp.get_element_index(network, "bus", to_bus.name)
                    pp.create_switch(network, index_1, index_2, et="b", type="CB", closed=False, name=switch_name)

                added_switch_names.add(switch_name)

# Now you can print the network.switch to verify the switches
print("Printing the network switch--------")
print(network.switch)
print("Printing the network switch--------")

# create load
added_load_names = set()

for item in CN_CE_stack:
    for load in item:
        if load.type_CE == 'EnergyConsumerLoad':
            load_name = load.name
    
            # Check if the load name already exists in the added_load_names set
            if load_name not in added_load_names:
                from_bus=item[0]
                index_1=pp.get_element_index(network, "bus", from_bus.name)
                pp.create_load(network, index_1, load.active_power, load.reactive_power, scaling=0.6, name=load_name)

                added_load_names.add(load_name)
print("Printing the network load--------")
print(network.load)
print("Printing the network load--------")

# create generators
added_generator_names = set()

for item in CN_CE_stack:
    for generator in item:
        if generator.type_CE == "SynchronousMachine":
            generator_name = generator.name

            # Check if the generator name already exists in the added_generator_names set
            if generator_name not in added_generator_names:
                from_bus=item[0]
                index_1=pp.get_element_index(network, "bus", from_bus.name)
                pp.create_gen(network, index_1, p_mw=0.9, q_mvar=0.9, name=generator_name)

                added_generator_names.add(generator_name)
print("Printing the network Generator--------")
print(network.gen)
print("Printing the network Generator--------")

# create energy source
added_sgenerator_names = set()

for item in CN_CE_stack:
    for sgenerator in item:
        if sgenerator.type_CE == "EnergySource":
            sgenerator_name = sgenerator.name

            # Check if the generator name already exists in the added_generator_names set
            if sgenerator_name not in added_sgenerator_names:
                from_bus=item[0]
                index_1=pp.get_element_index(network, "bus", from_bus.name)
                pp.create_sgen(network, index_1, p_mw=0.9, q_mvar=0.9, name=sgenerator_name)

                added_sgenerator_names.add(sgenerator_name)
print("Printing the network Static Generator--------")
print(network.sgen)
print("Printing the network Static Generator--------")

# create Compensator
added_compensator_names = set()

for item in CN_CE_stack:
    for compensator in item:
        if compensator.type_CE == "LinearShuntCompensator":
            compensator_name = compensator.name

            # Check if the compensator name already exists in the added_compensator_names set
            if compensator_name not in added_compensator_names:
                from_bus=item[0]
                index_1=pp.get_element_index(network, "bus", from_bus.name)
                pp.create_shunt(network, index_1, q_mvar=0, p_mw=0, name=compensator_name)

                added_compensator_names.add(compensator_name)

print("Printing the network LinearShuntCompensator--------")
print(network.shunt)
print("Printing the network LinearShuntCompensator--------")

# create transformer
# For transformers the high and low voltage busbars need to be determined
all_nominal_voltages = []  # Initialize list to store all nominal voltages
transformer_dict = {}  # Initialize a dictionary to store transformers based on their names

for item in CN_CE_CN_stack:
    for transformer in item:
        if transformer.type_CE == "PowerTransformer":
            name = transformer.name
            if name not in transformer_dict:
                nominal_voltages = []  # Initialize list to store nominal voltages for current power transformer

                if item[2].nominal_voltage:  # Check if nominal voltage exists for end 1
                    nominal_voltages.append(item[2].nominal_voltage)
                    print(nominal_voltages)

                    for volt in nominal_voltages:
                        if len(volt) == 2:  # Check if both HV and LV values exist
                            all_nominal_voltages.extend(volt)  # Append the nominal voltages to the overall list
                            max_voltage = max(volt)
                            min_voltage = min(volt)
            
                            if volt.index(max_voltage) == 0:
                                index_1 = item[0]
                                busbar_hv = pp.get_element_index(network, "bus", index_1.name)
                                index_2 = item[-1]
                                busbar_lv = pp.get_element_index(network, "bus", index_2.name)
                            else:
                                index_1 = item[-1]
                                busbar_hv = pp.get_element_index(network, "bus", index_1.name)
                                index_2 = item[0]
                                busbar_lv = pp.get_element_index(network, "bus", index_2.name)
                            if busbar_hv is not None and busbar_lv is not None:  # Check if busbars are found
                                pp.create_transformer(network, busbar_hv, busbar_lv, name=name, std_type="25 MVA 110/20 kV")
                                transformer_dict[name] = True  # Mark the transformer as processed in the dictionary
                            else:
                                print("Busbar not found for Power Transformer:", name)
                        else:  
                            volt = sorted(volt)
                            print("Sorted volt: ",volt)
                            all_nominal_voltages.extend(volt)  # Append the nominal voltages to the overall list
                            min_voltage,med_volt, max_voltage = volt
                            index_1 = item[0]
                            busbar_hv = pp.get_element_index(network, "bus", index_1.name)
                            index_2 = item[-1]
                            busbar_lv = pp.get_element_index(network, "bus", index_2.name)
                            for i in range(len(terminal_list)):
                                if item[2].rdf_ID == terminal_list[i].CE_rdf_ID.replace("#","") and item[1].rdf_ID != terminal_list[i].rdf_ID and item[-2].rdf_ID != terminal_list[i].rdf_ID:
                                    index_3 = terminal_list[i].CN_rdf_ID.replace("#","")
                                    for x in connectivity_node_list:
                                        if x.rdf_ID == index_3:
                                            print("Found the connectivity node to this terminal.")
                                            busbar_mv = pp.get_element_index(network, "bus", x.name)
                                            break
                            if busbar_hv is not None and busbar_lv is not None and busbar_mv is not None:  # Check if busbars are found
                                pp.create.create_transformer3w(network, busbar_hv, busbar_mv, busbar_lv, name=name, std_type="63/25/38 MVA 110/20/10 kV")
                                transformer_dict[name] = True  # Mark the transformer as processed in the dictionary
                            else:
                                print("Busbar not found for Power Transformer:", name)
                                                                
                else:
                    print("Missing nominal voltage values for the power transformer.")
            else:
                break

print("All Nominal Voltages:", all_nominal_voltages)
print("Printing the network Powertransformer--------")
print(network.trafo)
print("Printing the network Powertransformer--------")

print(network)

kk(network,"ntwk.html")