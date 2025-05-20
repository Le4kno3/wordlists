import re

if __name__ == '__main__':
    ATTACK_HOME_TEMP = '/home/playbox/Documents/Github/wordlists/01-attacks/command-injection/'
    ATTACK_HOME = '/Users/takshil/Documents/Github/wordlists/01-attacks/command-injection/'
    template_file_path = ATTACK_HOME + 'command-injection-template.txt'
    helper_commands_path = ATTACK_HOME + 'helper_commands.txt'
    helper_separators = []
    helper_separator_path = ATTACK_HOME + 'helper_separator.txt'
    helper_commands = []

    final_ci_payloads_path = ATTACK_HOME + 'command-injection-payloads.txt'
    temp1_ci_payloads = []
    ci_payloads = []
    new_ci_payloads = []

    # Prepare Payload - values
    with open(helper_commands_path) as file_data:
        helper_commands = file_data.read().splitlines()#parse new line delimited array

    # Prepare Payload - values
    with open(helper_separator_path) as file_data:
        helper_separators = file_data.read().splitlines()#parse new line delimited array

    # Generate payloads now
    with open(template_file_path) as template_file:
        ci_payloads = template_file.read().splitlines()#parse new line delimited array
        for ci_payload in ci_payloads:
            # resolve input complete
            if('{SEPARATOR}' in ci_payload):
                for separator in helper_separators:
                    temp1 = ci_payload.replace('{SEPARATOR}', separator, 2)
                    temp1_ci_payloads.append(temp1)
            else:
                temp1_ci_payloads.append(ci_payload)

        for ci_payload in temp1_ci_payloads:
            if('{COMMAND}' in temp1_ci_payloads):
                for command in helper_commands:
                    temp1 = ci_payload.replace('{COMMAND}', command)
                    new_ci_payloads.append(temp1)
                    temp2 = '$(' + temp1 + ')'
                    new_ci_payloads.append(temp2)
                    temp3 = '$((' + temp1 + '))'
                    new_ci_payloads.append(temp3)
                    temp4 = '`' + temp1 + '`'
                    new_ci_payloads.append(temp4)
    # Finally Write lines in output file which will have the list of all sqli final payloads.
    with open(final_ci_payloads_path, "w") as ci_final_file:
        for ci_payload in new_ci_payloads:
            ci_final_file.writelines(f"{ci_payload}\n")