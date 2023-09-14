import json
import xml.etree.ElementTree as ET
import yaml
import os

class ConfigFile:
    def __init__(self, name='config', priority_order=['.json', '.xml', '.yaml', '.txt'], directory='.'):
        self.name = name
        self.priority_order = priority_order
        self.directory = directory

    def select_file(self):
        for ext in self.priority_order:
            full_name = f"{self.name}{ext}"
            file_path = os.path.join(self.directory, full_name)  # Create the full path
            if os.path.isfile(file_path):
                return file_path  # Return the full path of the found file
        return None

    def read_config_file(self, file_path=None):
        if file_path is None:
            file_path = self.select_file()
        if not file_path:
            print("No matching configuration file found.")
            return {}

        # Determine the file type based on its extension
        file_extension = file_path.split('.')[-1].lower()
        # Initialize an empty dictionary to store the configuration
        config_data = {}

        try:
            # Read and parse the configuration file based on its type
            if file_extension == 'json':
                with open(file_path, 'r') as json_file:
                    config_data = json.load(json_file)
            elif file_extension == 'xml':
                tree = ET.parse(file_path)
                root = tree.getroot()
                config_data = self.xml_to_dict(root)
            elif file_extension in ['yml', 'yaml']:
                with open(file_path, 'r') as yaml_file:
                    config_data = yaml.safe_load(yaml_file)
            else:
                raise ValueError("Unsupported file type. Supported types: JSON, XML, YAML")

        except Exception as e:
            print(f"Error reading {file_extension} configuration file: {str(e)}")

        return config_data

    @staticmethod
    def xml_to_dict(element):
        data = {}
        for child in element:
            if child:
                child_data = ConfigurationManager.xml_to_dict(child)
                if child.tag in data:
                    if isinstance(data[child.tag], list):
                        data[child.tag].append(child_data)
                    else:
                        data[child.tag] = [data[child.tag], child_data]
                else:
                    data[child.tag] = child_data
            else:
                data[child.tag] = child.text
        return data

if __name__ == "__main__":
    config_manager = ConfigurationManager()
    config_data = config_manager.read_config_file()
    print(config_data)
