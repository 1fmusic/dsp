import re

def unique_domains(emails):
    x = []
    domains = []
    
    for z in emails:
        z = z.strip('')
        domain = re.findall('@(\S.*)',z)
        x.append(domain)
    
    for i in x:    
        if i not in domains :
            domains.append(str(i))
        else :
            continue
    
    return domains
