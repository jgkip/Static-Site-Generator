''' Convert markdown files to html 

This script converts an input markdown file to its equivalent html.

This script accepts markdown files only. 

This script requires the re and os modules that come with the Python stdlib.

This script can be imported as a module and contains the following functions:

    * headers - converts markdown header strings to equivalent html header strings
    * text_bold - converts markdown bold strings to equivalent html bold strings
    * hyper_link - generates hperlink for a markdown file 
    * gen_html - generates html to be written to output file 
    * process - processes input file line by line, applying necessary conversions 

'''

import os 
import re

tags = {
        '#' : ('<h1>', '</h1>'),
        '##' : ('<h2>', '</h2>'),
        ('__', '**') : ('<b>', '</b>')
        }

pattern_underscore = '__(.*?)__'
pattern_double_ast = '[*]{2}(.*?)[*]{2}'

alpha_num = "[^a-zA-Z0-9]*"

pattern_ital_one = ''
pattern_ital_two = ''


def headers(line):
    '''
    Formats markdown headers to equivalent html header tags

    Args:
        line (str): The line that contains the header to be converted

    Returns:
        str: The equivalent html bold string 

    '''
    h = ''
    if line.count('#') == 1:
        h = tags['#'][0] + line[line.count('#') + 1:].rstrip() + tags['#'][1]
    elif line.count('#') == 2:
        h = tags['##'][0] + line[line.count('##') + 1:].rstrip() + tags['##'][1]

    return h 

#TODO: Optimize... (O(n^2))?
def text_bold(line):     
    '''
    Formats markdown bold strings to equivalent html bold strings

    Args:
        line (str): The line that contains (or is) the text to be converted

    Returns:
        str: The equivalent html bold string

    '''
    if bool(re.match(pattern_underscore, line)) or bool(re.match(pattern_double_ast, line)): #change to fullmatch
            #h = '<p><b>' + line[2:len(line)-3] + '</b></p>'
            h = '<p><b>' + ''.join(re.split(alpha_num, line)) + '</b></p>'
            return h
    
    #replace substring with <b>substring</b>
    #h = re.sub(r'[*]{2}(.*?)[*]{2} |__(.*?)__ ', convert_bold, line)
    wlist = line.split()
    for i in range(len(wlist)):
        if bool(re.match(r"__(.*?)__", wlist[i])) or bool(re.match(r"[*]{2}(.*?)[*]{2}", wlist[i])):              
            wlist[i] = '<b>' + wlist[i][2:len(wlist[i])-2] + '</b>'
            #wlist[i] = '<b>' + ''.join(re.split(alpha_num, wlist[i])) + '</b>'

    h = ' '.join([str(e) for e in wlist])
         
    return h

def text_ital(line):
    pass

#get file location
def hyper_link(line):
    '''
    Generates hyper link to a new webpage

    Args:
        line (str): The name of the (markdown) file to generate hyperlink from

    Returns:
        str: The hyperlink string of the file
    '''
    c = ''.join(re.split(alpha_num, line))
    c = c[:c.index('md')]
    return '<a href="' + c + '.html' + '" target="_blank">' + c + '</a>'
   #return '<a href="' + line[2:len(line)-6] + '.html' + '" target="_blank">' + line[2:len(line)-6] + '</a>'

def gen_html(font, b):    
    '''
    Generates html that is written to file 

    Args:
        font (str): The font of the webpage to be generated
        b (str): The body (content) of the webpage 

    Returns:
        str: The html of webpage to be generated as a string
    '''
    res = '''
        <html>
            <head>
                <link href='https://fonts.googleapis.com/css?family=Roboto Mono' rel='stylesheet'>
                <style>
                    html * {{
                        font-family: {};
                    }}
                </style>
            </head>
            <body>
                {} 
            </body>
        </html>
        '''.format(font, b)

    return res 

def gen_list(line):
    if bool(re.match(r"- (.*?)", line)):
        pass

#TODO: Better way to handle header tags (other tags, too)
#TODO: italics, bold/italics combo, lists
def process(name):
    '''
    Processes input markdown file and returns equivalent html file

    Args:
        name (str): The name of the markdown file

    Returns:
        file: An equivalent html file 
    '''
#    pd = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#    pd += '\\tests\\' + name
    f = open(name, "r")
    
    #convert md to html
    lines = f.readlines()
    c = 0
    body = ''
    #print(lines)
    for index, line in enumerate(lines): 
#        print(line)
        header = ''
        #depending on tags, convert to corresponding html tag 
        if '#' in line:
            header = headers(line)
        elif line.count('#') == 0 and line.isspace() != True: 
            #print('element')
            if '**' in line or '__' in line:
                header = text_bold(line)
                if '[[' in header:
                    header = hyper_link(header)
            elif '[[' in line:
                header = hyper_link(line)
                '''
                if line[0] == '-':
                    print('Dealing with list')
                    header = '<ul>'
                    while lines[index][0] == '-':
                        header += '<li>'+line[1:]+'</li>\n'
                        index += 1
                    header += '</ul>'
                '''
            else: 
                header = '<p>' + line.rstrip() + '</p>'

        body += header + '\n'

    fn = name.split("\\")[-1] 
    html = gen_html("'Roboto Mono'", body)
    outpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\output\\'
    hf = open(outpath+fn[:fn.index('.md')]+'.html', 'w')
    #hf = open(name[:name.index('.md')]+'.html', 'w')
    hf.write(html)
    hf.close()
    f.close()
