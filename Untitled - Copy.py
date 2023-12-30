#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json

class JsonValidator:
    def __init__(self):
        self.schema = None

    def load_schema(self, schema_file):
        with open(schema_file, 'r') as f:
            self.schema = json.load(f)

    def validate_schema(self, json_file):
        with open(json_file, 'r') as f:
            data = json.load(f)
            
                        

        if self.schema is None:
            raise ValueError("Schema not loaded. Please load the schema first using load_schema method.")

        # Required fields validation
        if 'required' in self.schema:
            for field in self.schema['required']:
                if field not in data:
                    return False

        # At least one of many fields to be present validation
        if 'one_of' in self.schema:
            one_of_fields_present = False
            for field_group in self.schema['one_of']:
                present_fields = [field for field in field_group if field in data]
                if len(present_fields) > 0:
                    one_of_fields_present = True
                    break
            if not one_of_fields_present:
                return False
            
            
            

        # Either one field or another field validation
        if 'either_or' in self.schema:
            either_or_fields = self.schema['either_or']
            either_fields_present = [field for field in either_or_fields if field in data]
            if len(either_fields_present) != 1:
                return False
            
            

        # Mutually exclusive fields validation
        if 'mutually_exclusive' in self.schema:
            mutually_exclusive_groups = self.schema['mutually_exclusive']
            for group in mutually_exclusive_groups:
                present_fields = [field for field in group if field in data]
                if len(present_fields) > 1:
                    return False
                
                

        # Field value to be one of a set of values validation
        if 'enum_values' in self.schema:
            enum_fields = self.schema['enum_values']
            for field, enum_set in enum_fields.items():
                if field in data and data[field] not in enum_set:
                    return False

        return True

    

# Example usage:
validator = JsonValidator()
validator.load_schema('schema.json')  # Load your schema file

# Validate a JSON file against the schema
is_valid = validator.validate_schema('data.json')  # Replace 'data.json' with your JSON file

if is_valid:
    print("Validation successful")
else:
    print("Validation failed")
    
    
    

