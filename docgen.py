from os import listdir, getcwd
from os.path import isfile, join, splitext, basename 

HTML_FILE = "Principal.html"
PAPER_PATH = "Artigos/"
DESC_PATH = "Descricoes/"

def html_header():
    html = open(HTML_FILE,"w+")
    header = """<!DOCTYPE html>
    <html> 
    <meta charset="UTF-8">
	<head>
    <title>"""+basename(getcwd())+"""</title>
	</head>
	<body>
    <h1>"""+basename(getcwd())+"""</h1>
	<table border = 1>
        <col width="300">
		<tr bgcolor=#3399ff>
			<th>Artigo</th>
			<th>Utilidade</th>
		</tr>"""
    html.write(header)
    html.close()

def html_footer():
    html = open(HTML_FILE,"a")
    footer = """</table>
	</body>
    </html>"""
    html.write(footer)
    html.close()

def html_table_gen(file_names):
    for fn in file_names:
        f = open(DESC_PATH+fn+".txt")
        title = f.readline()
        content = f.read()
        f.close()

        html = open(HTML_FILE,"a")
        html.write("\n\t\t<tr><td><a href=\""+PAPER_PATH+fn+".pdf"+"\">"+title+"</a></td><td>"+content+"</td></tr>")

paper_list = [splitext(f)[0] for f in listdir(PAPER_PATH) if isfile(join(PAPER_PATH, f))]

try:
    for paper_file in paper_list:
        if not(isfile(DESC_PATH+paper_file+".txt")):
           f= open(DESC_PATH+paper_file+".txt","w+")
           f.write("NOME DO ARTIGO "+paper_file+"\n")
           f.write("Descrição aqui")
           f.close()
           print("Artigo \""+paper_file+"\" adicionado!")

    html_header()
    html_table_gen(paper_list)
    html_footer()
    print("** Documentação criada com sucesso **")
except:
    print("Erro ao criar documentação!")
