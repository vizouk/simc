import sys
import re
import json

def get_file_as_lines( input, out_line_length ):
    out = []
    with open( input ) as f:
        str = f.read()
        str = re.sub( " ", "", str )
        str = re.sub( "\n", "", str )
        str = json.dumps(str).strip('"') # Misuse to build a C string with escaped characters
        out = [str[x:x+out_line_length] for x in range(0,len(str),out_line_length)]
    return out
            
def print_as_char_array( name, input_list ):
    out = ("static const char* %s[] = {\n"%(name))
    for line in input_list:
        out += "\"%s\",\n"%(line)
    out += "};";
    return out
        
def main():
    with open( "report_data.inc", "w") as f:
        f.write( "// Automatically generated report data.\n\n")
        f.write( print_as_char_array( "__logo", get_file_as_lines( "simc_logo.txt", 80 ) ) )
        f.write( "\n\n" )
        f.write( print_as_char_array( "__image_load_script", get_file_as_lines( "image_load_script.js", 80 ) ) )
    print( "done")
    
if __name__ == "__main__":
    main()
         