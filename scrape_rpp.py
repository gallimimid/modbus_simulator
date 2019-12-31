import modbus_scraper

devices = (0,2,3,18,19,34,35)

first_three_octets = '192.168.1.'

for fourth_octet in range(101,131):
    
    ip_address = first_three_octets + str(fourth_octet)
    
    for device in devices:
        
        ip_list = ip_address.split('.')
        
        ip_list.append(str(device))
        
        output = '_'.join(ip_list) + '.pickle'

        modbus_scraper.main(output=output,
                            port=502,
                            host=ip_address,
                            device=device,
                            range='0:20000',
                            debug=True)