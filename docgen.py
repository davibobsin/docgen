from os import listdir, getcwd
import webbrowser
import sys
from os.path import isfile, join, splitext, basename, exists

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

try:
    open_browser = False
    arg_path = '.'

    # Valida parametros passados na chamada
    if len(sys.argv)<1 and len(sys.argv)>3:
        print("É necessário especificar apenas um diretório válido!")
        raise Exception

    for arg in sys.argv:
        if arg=="-o":
            open_browser=True
        else:
            arg_path=arg

    path_referencia = getcwd()+"/"+arg_path
    if path_referencia[-1]!='/':
        path_referencia=path_referencia+'/'
    HTML_FILE = path_referencia+"Principal.html"
    PAPER_PATH = path_referencia+"Artigos/"
    DESC_PATH = path_referencia+"Descricoes/"
   
    # Verifica se existem as pastas base Artigos e Descricoes    
    if not(exists(PAPER_PATH)):
        print("Não existe um repositório para Artigos!")
        raise Exception 
    if not(exists(DESC_PATH)):
        print("Não existe um repositório para Descricoes!")
        raise Exception 

    # Gera a lista de artigos de acordo com os arquivos na pasta de papers
    paper_list = [splitext(f)[0] for f in listdir(PAPER_PATH) if isfile(join(PAPER_PATH, f))]

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


    if open_browser:
        webbrowser.open_new_tab(HTML_FILE)

except:
    print("Documentação não gerada!")
