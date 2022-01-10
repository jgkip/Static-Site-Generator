import os 
import re

tags = {
        '#' : ('<h1>', '</h1>'),
        '##' : ('<h2>', '</h2>')
        }

def headers(line):
    if line.count('#') == 1:
        h = tags['#'][0] + line[line.count('#') + 1:].rstrip() + tags['#'][1]
        #print(header)
    elif line.count('#') == 2:
        h = tags['##'][0] + line[line.count('##') + 1:].rstrip() + tags['##'][1]
        #print(header)
    return h 

def text_mod(line):
    if bool(re.match(r"__(.*?)__", line)) or bool(re.match(r"[*]{2}(.*?)[*]{2}", line)): #change this to match exactly 2 *
            h = '<p><b>'+line[2:len(line)-3]+'</b></p>'
            return h
    
    wlist = line.split()
    for i in range(len(wlist)):
        if bool(re.match(r"__(.*?)__", wlist[i])) or bool(re.match(r"[*]{2}(.*?)[*]{2}", wlist[i])):  
            
            wlist[i] = '<b>' + wlist[i][2:len(wlist[i])-2] + '</b>'

    h = ' '.join([str(e) for e in wlist])
            
    return h

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
    pd = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pd += '\\tests\\' + name
    f = open(pd, "r")
    
    #convert md to html
    lines = f.readlines()
    c = 0
    body = ''
    for line in lines: 
        header = ''
        #depending on tags, convert to corresponding html tag 
        if '#' in line:
            header = headers(line)
        elif line.count('#') == 0 and line.isspace() != True: 
            if '**' in line or '__' in line:
                header = text_mod(line)
            else:
                header = '<p>' + line.rstrip() + '</p>'


        body += header + '\n'
    
    html = gen_html("'Roboto Mono'", body)
    hf = open('index.html', 'w')
    hf.write(html)
    hf.close()
    f.close()
    
