import os

tags = {
        '#' : ('<h1>', '</h1>'),
        '##' : ('<h2>', '</h2>')
        }



def main():
    pd = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pd += '\\tests\\test.md'
    f = open(pd, "r")
    
    #convert md to html
    lines = f.readlines()
    c = 0
    body = ''
    for line in lines: 
        header = ''
        #depending on tags, convert to corresponding html tag 
        if line.count('#') == 1:
            header = tags['#'][0] + line[line.count('#') + 1:].rstrip() + tags['#'][1]
            #print(header)
        elif line.count('#') == 2:
            header = tags['##'][0] + line[line.count('##') + 1:].rstrip() + tags['##'][1]
            #print(header)
        elif line.count('#') == 0 and line.isspace() != True:
            header = '<p>' + line.rstrip() + '</p>'
            #print(header)
        body += header + '\n'
    
    html = '''
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
        '''.format("'Roboto Mono'", body)
    hf = open('index.html', 'w')
    hf.write(html)
    hf.close()
    f.close()
    #print(html)
    print('Finished conversion')




if __name__ == '__main__':
    main()
