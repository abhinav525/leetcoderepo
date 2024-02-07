import re# 0005-0001-9999 (no 0000)
number_plate="LCNO-KAR-05-2014-0005"   
res = re.search(r'LCNO-(KAR|KER|APN|TND|TEL|MAH)-(([0-6][1-9])|70|71|72|73))- (2[0-9][0-9][1-9])-([0-9][0-9][0-9][1-9])',number_plate)
if res:
    print("match found")
else:
    print("not found")
