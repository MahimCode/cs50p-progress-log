def main():
    spacecraft = {"name": "Voyagrer"}
    spacecraft ["distance"] = 0.015
    print(create_report(spacecraft)) 

def create_report(spacecraft):
    return f"""

============= REPORT ==============

Name: {spacecraft["name"]}
Distance: {spacecraft["distance"]} AU

===================================
"""
main()
