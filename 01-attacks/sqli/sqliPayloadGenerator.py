import re

if __name__ == '__main__':
    ATTACK_HOME = '/home/playbox/Documents/Github/wordlists/01-attacks/sqli/'
    template_file_path = ATTACK_HOME + 'templates_and_helpers/TEMPLATE.txt'
    helper_input_complete_path = ATTACK_HOME + 'templates_and_helpers/helper_input_complete.txt'
    helper_input_complete = []
    helper_force_end_path = ATTACK_HOME + 'templates_and_helpers/helper_force_end.txt'
    helper_force_end = []
    helper_values_path = ATTACK_HOME + 'templates_and_helpers/helper_values.txt'
    helper_values = []
    helper_toggle_TF_path = ATTACK_HOME + 'templates_and_helpers/helper_toggle_TF.txt'
    helper_toggle_TF = []
    helper_NOSQLi_path = ATTACK_HOME + 'templates_and_helpers/helper_NO_SQLi.txt'
    helper_NOSQLi = []
    sqli_final_payload_path = ATTACK_HOME + 'FINAL_ALL_sqli_payloads'
    sqli_tf_payload_path = ATTACK_HOME + 'FINAL_tf_payloads'
    sqli_tf_payloads = []
    nosqli_payload_path = ATTACK_HOME + 'FINAL_nosqli_payloads'
    nosqli_payloads = []

    temp1_sqli_payloads = []
    temp2_sqli_payloads = []
    temp3_sqli_payloads = []
    new_sqli_payloads = []

    # Prepare Payload - values
    with open(helper_values_path) as file_data:
        helper_values = file_data.read().splitlines()#parse new line delimited array

    # Prepare Payload - toggle true false (TF)
    with open(helper_toggle_TF_path) as file_data:
        helper_toggle_TF = file_data.read().splitlines()#parse new line delimited array

    # Prepare Payload - force end
    with open(helper_force_end_path) as file_data:
        helper_force_end = file_data.read().splitlines()#parse new line delimited array

    # Prepare Payload - input complete
    with open(helper_input_complete_path) as file_data:
        payloads = file_data.read().splitlines()#parse new line delimited array
        for payload in payloads:
            for value_payload in helper_values:
                temp = payload.replace('{VALUE}', value_payload)
                helper_input_complete.append(temp)

    # Prepare Payload - NO SQLi
    with open(helper_NOSQLi_path) as file_data:
        helper_NOSQLi = file_data.read().splitlines()#parse new line delimited array

    # Generate payloads now
    with open(template_file_path) as template_file:
        sqli_payloads = template_file.read().splitlines()#parse new line delimited array
        for sqli_payload in sqli_payloads:
            # resolve input complete
            if('{INPUT_COMPLETE}' in sqli_payload):
                for input_complete in helper_input_complete:
                    temp1 = sqli_payload.replace('{INPUT_COMPLETE}', input_complete)
                    temp1_sqli_payloads.append(temp1)
        
        for sqli_payload in temp1_sqli_payloads:
            # resolve force end
            if('{FORCE_END}' in sqli_payload):
                for force_end in helper_force_end:
                    temp1 = sqli_payload.replace('{FORCE_END}', force_end)
                    temp2_sqli_payloads.append(temp1)

        # We dont need to resovle values, as it is already resolved by Input Complete but still if {VALUE} in final template then
        for sqli_payload in temp2_sqli_payloads:
            # resolve toggle TF
            if('{VALUE}' in sqli_payload):
                for value in helper_values:
                    temp2 = sqli_payload.replace('{VALUE}', value)
                    temp3_sqli_payloads.append(temp2)
            else:
                temp3_sqli_payloads.append(sqli_payload)
        
        # remove toggle_TF from this list and add it to a seperate true-false list.
        for sqli_payload in temp3_sqli_payloads:
            # resolve toggle TF
            if('{TOGGLE_TF}' in sqli_payload):
                for toggle_TF in helper_toggle_TF:
                    temp3 = sqli_payload.replace('{TOGGLE_TF}', toggle_TF)
                    new_sqli_payloads.append(temp3) # because we need all payloads
                    sqli_tf_payloads.append(temp3)
            else:
                new_sqli_payloads.append(sqli_payload)

        # Append all NO SQLi payloads, currently the NO SQLi payloads are not customizable. 
        for nosqli_payload in helper_NOSQLi:
            new_sqli_payloads.append(nosqli_payload)
            

    # Finally Write lines in output file which will have the list of all sqli final payloads.
    with open(sqli_final_payload_path, "w") as sqli_final_file:
        for sqli_payload in new_sqli_payloads:
            sqli_final_file.writelines(f"{sqli_payload}\n")
    
    # Write SQLi true false payloads in a separate file.
    with open(sqli_tf_payload_path, "w") as sqli_tf_file:
        for sqli_payload in sqli_tf_payloads:
            sqli_tf_file.writelines(f"{sqli_payload}\n")
    
    # Write NOSQLi payloads in a separate file.
    with open(nosqli_payload_path, "w") as nosqli_file:
        for nosqli_payload in helper_NOSQLi:
            nosqli_file.writelines(f"{nosqli_payload}\n")