import re

if __name__ == '__main__':
    PAYLOAD_HOME = '/home/playbox/Documents/Github/wordlists/01-attacks/sqli/'
    template_file = PAYLOAD_HOME + 'template_and_helpers/TEMPLATE.txt'
    helper_input_complete = PAYLOAD_HOME + 'template_and_helpers/helper_input_complete.txt'
    helper_force_end = PAYLOAD_HOME + 'template_and_helpers/helper_force_end.txt'
    helper_values = PAYLOAD_HOME + 'template_and_helpers/helper_values.txt'
    js_payloads = []
    new_js_payloads = []
    value_payloads = []
    new_xss_payloads = []

    with open(value_file_path) as value_file:
        value_payloads = value_file.read().splitlines()#parse new line delimited array

    # print(value_payloads)

    with open(javascript_file_path) as js_file:
        js_payloads = js_file.read().splitlines()#parse new line delimited array
        for js_payload in js_payloads:
            for value_payload in value_payloads:
                temp = js_payload.replace('{PAYLOAD}', value_payload)
                new_js_payloads.append(temp)

    # print(new_js_payloads)

    with open(xss_file_path) as xss_file:
        xss_payloads = xss_file.read().splitlines()#parse new line delimited array
        for xss_payload in xss_payloads:
            for js_payload in new_js_payloads:
                temp = xss_payload.replace('{JAVASCRIPT}', js_payload)
                if('{PAYLOAD}' in temp):
                    for value_payload in value_payloads:
                        temp = xss_payload.replace('{PAYLOAD}', value_payload)
                        new_xss_payloads.append(temp)
                else:
                    new_xss_payloads.append(temp)


    # print(new_xss_payloads)

    # handle values in the final javascript file also

    with open(xss_final_payload_path, "w") as xss_final_file:
        for xss_payload in new_xss_payloads:
            xss_final_file.writelines(f"{xss_payload}\n")

    # with open(template_file_path) as file:
    #
    #     while line := file.readline():
    #         print(line.rstrip())
    #         line.replace('{JAVASCRIPT}', )
    #
    #
    #     parse this string, and split by new line
    #     for line in template_file_data:
    #         print(line.rstrip())