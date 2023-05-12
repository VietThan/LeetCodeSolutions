"""
Adversaries often use compromised IP addresses and random domains to serve malicious traffic for phishing, C&C, etc.  In this problem, we want you to help us identify IP addresses and domains that form malicious infrastructure groups. 
 
Input:
     domain2ips: a mapping between malicious domains and IP addresses these domains resolve to
    
Example:
     domain2ip = {
        "qdwmrz.com": ['43.218.229.148', '162.216.20.226', '128.108.179.34', '210.31.78.207'],
        "nsh5fu.com": ['83.208.127.163', '151.51.55.181'],
        "b8cczdf.com": ['210.31.78.207', '185.165.242.200', '159.65.113.202'],
        "m4x9845jp4q.com": ['128.108.179.34', '70.203.24.225', '174.248.119.178'],
        "hacrhcd4j6.biz": ['76.110.36.206', '188.45.118.95'],
        "42t5pv.cz": ['128.108.179.34', '159.65.113.202', '210.31.78.207', '174.248.119.178'],
        "iwn53f4c0.com": ['7.203.41.49', '83.208.127.163'],
    }

Those domains form three malicious infrastructure groups because domains within the same group share some IP address with each other

Group1: 
qdwmrz.com      ['210.31.78.207', '128.108.179.34', '43.218.229.148', '162.216.20.226', ]
b8cczdf.com     ['210.31.78.207', '185.165.242.200', '159.65.113.202']
m4x9845jp4q.com ['70.203.24.225', '128.108.179.34', '174.248.119.178'
42t5pv.cz       ['128.108.179.34', '159.65.113.202','174.248.119.178', '210.31.78.207']

Group2:
nsh5fu.com    ['83.208.127.163', '151.51.55.181']
iwn53f4c0.com ['83.208.127.163', '7.203.41.49']

Group3:
hacrhcd4j6.biz ['76.110.36.206', '188.45.118.95']


Expected Output:
    a list of list: each list is a malicious infrastructure group (order can be arbitrary, but should be unique)

       [
           ['qdwmrz.com', 'm4x9845jp4q.com', '42t5pv.cz', 'b8cczdf.com', '43.218.229.148', '162.216.20.226', '128.108.179.34', '70.203.24.225', '174.248.119.178', '159.65.113.202', '210.31.78.207', '185.165.242.200'],
           ['nsh5fu.com', 'iwn53f4c0.com', '83.208.127.163', '7.203.41.49', '151.51.55.181'],
           ['hacrhcd4j6.biz', '76.110.36.206', '188.45.118.95'],
       ] 
"""

import pprint
def find_malicious_groups(domain2ips: dict[str, list[str]]):
    list_of_sets = []
    for domain, ips in domain2ips.items():
        s = set()
        s.add(domain)
        s.update(ips)
        list_of_sets.append(s)

    def find_intersection(m_list: list[set[str]]):
        for i, s in enumerate(m_list):
            for j, s_2 in enumerate(m_list[i+1:], i+1):
                print(f"i: {i}, j: {j}")
                if s & s_2:
                    m_list[i] = s.union(m_list.pop(j))
                    return find_intersection(m_list)
        return m_list

    return find_intersection(list_of_sets)

# Test the function with the provided example
domain2ip = {
    "qdwmrz.com": ['43.218.229.148', '162.216.20.226', '128.108.179.34', '210.31.78.207'],
    "nsh5fu.com": ['83.208.127.163', '151.51.55.181'],
    "b8cczdf.com": ['210.31.78.207', '185.165.242.200', '159.65.113.202'],
    "m4x9845jp4q.com": ['128.108.179.34', '70.203.24.225', '174.248.119.178'],
    "hacrhcd4j6.biz": ['76.110.36.206', '188.45.118.95'],
    "42t5pv.cz": ['128.108.179.34', '159.65.113.202', '210.31.78.207', '174.248.119.178'],
    "iwn53f4c0.com": ['7.203.41.49', '83.208.127.163'],
}

malicious_groups = find_malicious_groups(domain2ip)
pprint.pprint(malicious_groups)