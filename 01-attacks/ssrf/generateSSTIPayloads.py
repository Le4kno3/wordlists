import re

if __name__ == '__main__':
    ATTACK_HOME = '/home/playbox/Documents/Github/wordlists/01-attacks/ssrf/'
    ATTACK_HOME_TEMP = '/Users/takshil/Documents/Github/wordlists/01-attacks/ssrf/'
    template_file_path = ATTACK_HOME + 'SSRF-TEMPLATE.txt'
    helper_hostnames_path = ATTACK_HOME + 'helper_hostnames.txt'
    helper_hostnames = []
    helper_ports_path = ATTACK_HOME + 'helper_ports.txt'
    helper_ports = []

    final_ssrf_payloads_path = ATTACK_HOME + 'ssrf-payloads.txt'
    temp1_ssrf_payloads = []
    ssrf_payloads = []
    new_ssrf_payloads = []

    # Prepare Payload - values
    with open(helper_hostnames_path) as file_data:
        helper_hostnames = file_data.read().splitlines()#parse new line delimited array

    # Prepare Payload - values
    with open(helper_ports_path) as file_data:
        helper_ports = file_data.read().splitlines()#parse new line delimited array

    # Generate payloads now
    with open(template_file_path) as template_file:
        ssrf_payloads = template_file.read().splitlines()#parse new line delimited array
        for ssrf_payload in ssrf_payloads:
            # resolve input complete
            if('{HOSTNAME}' in ssrf_payload):
                for host in helper_hostnames:
                    temp1 = ssrf_payload.replace('{HOSTNAME}', host)
                    temp1_ssrf_payloads.append(temp1)
            else:
                temp1_ssrf_payloads.append(ssrf_payload)

        for ssrf_payload in temp1_ssrf_payloads:
            if('{PORT}' in ssrf_payload):
                for port in helper_ports:
                    temp1 = ssrf_payload.replace('{PORT}', port)
                    new_ssrf_payloads.append(temp1)
            else:
                new_ssrf_payloads.append(ssrf_payload)

    # Finally Write lines in output file which will have the list of all sqli final payloads.
    with open(final_ssrf_payloads_path, "w") as final_file:
        for ssrf_payload in new_ssrf_payloads:
            final_file.writelines(f"{ssrf_payload}\n")