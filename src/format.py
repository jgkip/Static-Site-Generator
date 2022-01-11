import os 
import re

tags = {
        '#' : ('<h1>', '</h1>'),
        '##' : ('<h2>', '</h2>'),
        ('__', '**') : ('<b>', '</b>')
        }

pattern_underscore = '__(.*?)__'
pattern_double_ast = '[*]{2}(.*?)[*]{2}'

pattern_ital_one = ''
pattern_ital_two = ''

def headers(line):
    if line.count('#') == 1:
        h = tags['#'][0] + line[line.count('#') + 1:].rstrip() + tags['#'][1]
        #print(header)
    elif line.count('#') == 2:
        h = tags['##'][0] + line[line.count('##') + 1:].rstrip() + tags['##'][1]
        #print(header)
    return h 


def convert_bold(m):
    if m.group(1) is not None:
        return '<b>' + m.group(1) + '</b>'
    if m.group(2) is not None:
        return '<b>' + m.group(2) + '</b>'

#TODO: Optimize... (O(n^2))?
def text_mod(line):    
    #if bool(re.fullmatch(pattern_underscore, line)) or bool(re.fullmatch(pattern_double_ast, line)):
    if bool(re.match(pattern_underscore, line)) or bool(re.match(pattern_double_ast, line)): #change to fullmatch
            h = '<p><b>'+line[2:len(line)-3]+'</b></p>'
            return h
    
    #replace substring with <b>substring</b>
    #h = re.sub(r'[*]{2}(.*?)[*]{2} |__(.*?)__ ', convert_bold, line)
    wlist = line.split()
    for i in range(len(wlist)):
        if bool(re.match(r"__(.*?)__", wlist[i])) or bool(re.match(r"[*]{2}(.*?)[*]{2}", wlist[i])):  
            
            wlist[i] = '<b>' + wlist[i][2:len(wlist[i])-2] + '</b>'

    h = ' '.join([str(e) for e in wlist])
         
    return h

def text_ital(line):
    pass

#get file location
def hyper_link(line):
    #print(line[2:len(line)-6]+'.html')
    return '<a href="' + line[2:len(line)-6] + '.html' + '" target="_blank">' + line[2:len(line)-6] + '</a>'

def gen_html(font, b):    
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
#TODO: linked pages(?) 
def process(name):
    #pd = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #pd += '\\tests\\' + name
    f = open(name, "r")
    
    #convert md to html
    lines = f.readlines()
    c = 0
    body = ''
    #print(name)
    for line in lines: 
        header = ''
        #depending on tags, convert to corresponding html tag 
        if '#' in line:
            header = headers(line)
        elif line.count('#') == 0 and line.isspace() != True: 
            if '**' in line or '__' in line:
                header = text_mod(line)
            elif '[[' in line:
                header = hyper_link(line)
            else:
                header = '<p>' + line.rstrip() + '</p>'

        body += header + '\n'

    fn = name.split("\\")[-1] 
    html = gen_html("'Roboto Mono'", body)
    outpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\output\\'
    hf = open(outpath+fn[:fn.index('.md')]+'.html', 'w')
    hf.write(html)
    hf.close()
    f.close()
