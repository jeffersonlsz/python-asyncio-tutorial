import requests
from bs4 import BeautifulSoup
import re
import os
import asyncio
import pdb

payload = {}
headers = {
  'authority': 'fatalmodel.com',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
  'cache-control': 'no-cache',
  'cookie': '_ce.irv=new; cebs=1; _ce.clock_event=1; jsCookieTerm18=true; _ce.clock_data=4108%2C45.224.199.176%2C1%2C36489d387fc8bef5e6ceaf2293b7a987; __trf.src=encoded_eyJmaXJzdF9zZXNzaW9uIjp7InZhbHVlIjoiKG5vbmUpIiwiZXh0cmFfcGFyYW1zIjp7fX0sImN1cnJlbnRfc2Vzc2lvbiI6eyJ2YWx1ZSI6Iihub25lKSIsImV4dHJhX3BhcmFtcyI6e319LCJjcmVhdGVkX2F0IjoxNzExMDI4NzQxNjMzfQ==; _gid=GA1.2.398204582.1711028742; rdtrk=%7B%22id%22%3A%228838471b-49a5-470c-bbfb-5a7d64b6b1c0%22%7D; _ga=GA1.1.2091954953.1711027588; slug-city=maceio; user_configs_v2=eyJpdiI6ImFrZEJTcmVmMFdvVTQ3UFBIRmEzbFE9PSIsInZhbHVlIjoiOGxYT3c1S2FrTmxHWmpzT0JCdVBlSjdXY0YwVUVxZWllTVJSbWFRaEh2TlF2emtHWGorMHNCNGFTRlRXOXE0RDZGZExjMXIzTFZQdzVYSGdoL0Z4d0J6aTc3VkwrZ1lUK0ZyeEd0blBndTBPRjdaYmNVQnJDaWJodFRwc09kZXNEUFdEalZxTHRMNGoyaFVpZU9na1JGcWZwZ3E5cW1Ka015RlNuZWFpekZ4d2t6UDBHY3ExUFErZWRxcEd6ZnRzTGQ4dTRQUW1oYy81RVo5MmgrOXEycFRUM0xFQk0wOEVoTzVkYlVBQUc3S2QreGF2cmlXMXBNSUZzK2huY0owYTdKclV6QkQyaW8zVjB0STR4bCtqVENmQjM4TzF2L05sN2FLUlhYT1R0TTA9IiwibWFjIjoiYmEzY2NhNTRiOTgxMmIxYmM4OWQ1Y2QzMzUyNTQ5MDA1NzEyMDRjNDZkZjdiMzM2NDliNjcwNjNmM2ZmZDYzOSIsInRhZyI6IiJ9; __cflb=0H28vgyx35NNX8FcqgmsmWsXQssub2fWsE3ej5ExFAd; _ga_80KGM2NV62=GS1.1.1711073061.2.1.1711073500.0.0.0; cebsp_=34; _ce.s=v~417959571a3e17d7187e852ae1d7c4362597f71b~lcw~1711073508287~lva~1711027587774~vpv~0~as~false~v11.fhb~1711073061617~v11.lhb~1711073482508~v11.cs~408548~v11.s~7fbd3e20-e7f0-11ee-ba4d-857c75837c02~v11.sla~1711073508286~gtrk.la~lu20zjx5~v11.send~1711073508294~lcw~1711073508294; selected_city=eyJpdiI6IlcxZEZ4dTRIK1Zpa0MwcDBaanZUSFE9PSIsInZhbHVlIjoib1NNN21sWTc0SGsrdzB0Qmt5Nmh5UT09IiwibWFjIjoiYjQ0MDg3NGU4ZTUxNTdiZTc5ZTM2YmY1OWMzZGE3NTE5NWUyZTU4N2ZjNDUyNDQ3MGQ2OWRhZWRjMGYwN2M3NiIsInRhZyI6IiJ9; selected_state=eyJpdiI6IlQ0WG1PdlN6dGVwU1J4WE9pU2lic2c9PSIsInZhbHVlIjoiL1VRTW01L3h5U20yaDRCV29PTDRDcldOOTJmVVB4YWoxSWNqSXJMK2NTND0iLCJtYWMiOiI2ZjYxMDY0NzU0MmU4MGY2NTlkZDJmNGU2YmI1NGFmZTA2MWFjZTM2MWJiNDJhZTA3MjYxNWQyNzcxYTBmODE3IiwidGFnIjoiIn0%3D; selected_state_letter=eyJpdiI6Im5GUGFxWnpjekhLU2dXTDgzeWQ5Wnc9PSIsInZhbHVlIjoiaCtac1BRblJ0OTdIblpwdFVtOVVsQT09IiwibWFjIjoiZjU4MDFjODEyNGNiZWMyODc1Yjg5N2VjZGI1YzVmZjk3Y2Q3OTBiYTdjYzlmNmM4NTBhZGRlY2FjODMxNDIzZSIsInRhZyI6IiJ9',
  'pragma': 'no-cache',
  'referer': 'https://fatalmodel.com/',
  'sec-ch-ua': '"Not A(Brand";v="99", "Opera";v="107", "Chromium";v="121"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0'
}


def get_chave_model_url(url) -> None:
    # Dividir a URL em partes usando o método split("/")
    parts = url.split("/")
    # Selecionar a informação após a penúltima barra
    informacao = parts[-2:]
    # Juntar os elementos selecionados usando o método join("/")
    informacao_final = "/".join(informacao)
    return informacao_final

#melhor pegar por cidade, pois estado por demorar muito
def get_links_cidade(chavecidade, siglaestado):
    linkscity = []
    acaboucidade=False
    for i in range(1,30):
        if acaboucidade:
            break
        url = f"https://fatalmodel.com/acompanhantes-{chavecidade}-{siglaestado}?page={i}"
        response = requests.request("GET", url, headers=headers, data=payload)    
        site = BeautifulSoup(response.text, "html.parser")
        subsite = site.find_all('section')[3]
        #print(subsite)
        #pdb.set_trace()
        pattern_geral_classe = re.compile(r'^no-tap-highlight rounded-xl.*')
        elementos_classes_iniciam_com = subsite.find_all(attrs={"class": pattern_geral_classe})
        for elemento in elementos_classes_iniciam_com:
            trecho = BeautifulSoup(str(elemento), "html.parser")
            tag_a = trecho.find('a')
                    
            url_model = tag_a.get('href')
            chave_model = get_chave_model_url(url_model)
            #print(chave_model)
            if chave_model in linkscity:
                acaboucidade = True
                break
            else:
              linkscity.append(chave_model)


    return linkscity


#formato sigla: ma, sp, df, go....
def get_lista_links_estado(sigla_estado):
    
    url = f"https://fatalmodel.com/acompanhantes-{sigla_estado}"

    response = requests.request("GET", url, headers=headers, data=payload)    
    site = BeautifulSoup(response.text, "html.parser")
    #print(site.prettify())
    tag = site.find('search-cities-alphabet')
    #print(tag.decode)

    pattern = r'\/acompanhantes-(.*?)-{sigla_estado}'
    
    acaboucidade = False
   
    lista_geral_estado = []
    for city in re.findall(pattern.format(sigla_estado=sigla_estado), str(tag)):
        print(f"https://fatalmodel.com/acompanhantes-{city}-{sigla_estado}")
        prof=15
        for i in range(0,prof):
            if acaboucidade:
                break
            lista_chaves_ac = []
            url_city = f"https://fatalmodel.com/acompanhantes-{city}-{sigla_estado}?page={i}"
            #print(url_city + " ---- >")
            paginaacompanhates = requests.request("GET", url_city, headers=headers, data=payload)
            site = BeautifulSoup(paginaacompanhates.text, "html.parser")
            
            pattern_geral_classe = re.compile(r'^no-tap-highlight rounded-xl.*')
            elementos_classes_iniciam_com = site.find_all(attrs={"class": pattern_geral_classe})
            #print("rttat " + str(elementos_classes_iniciam_com))
            for elemento in elementos_classes_iniciam_com:
                trecho = BeautifulSoup(str(elemento), "html.parser")
                tag_a = trecho.find('a')
                
                url_model = tag_a.get('href')
                chave_model = get_chave_model_url(url_model)
                
                if chave_model not in lista_chaves_ac:
                    lista_chaves_ac.append(chave_model)
                    lista_geral_estado.append(chave_model)
                else:
                    acaboucidade = True
                    #print(lista_chaves_ac)
                    break
            
    return set(lista_geral_estado)        

async def extrair_imagens_link(estado, chave):
    url_model = f"https://fatalmodel.com/{chave}"
    print(url_model)
    try:
      response =  requests.request("GET", url_model, headers=headers, data=payload)    
      site = BeautifulSoup(response.text, "html.parser")
      print(tag_video.get('poster'))
    except:
        pass
    tag_video = site.find('video')
    
    #salvar imagem localmente
    diretorio_destino = 'D:\\temp\\test-palmas'

    # Verificando se o diretório de destino existe, se não, criá-lo
    if not os.path.exists(diretorio_destino):
        os.makedirs(diretorio_destino)

    # Nome do arquivo de destino
    nome_arquivo = f"{chave.replace('/', '_')}.jpg"

    # Caminho completo do arquivo de destino
    caminho_destino = os.path.join(diretorio_destino, nome_arquivo)

    # Salvando a imagem localmente
    salvar_imagem(tag_video.get('poster'), caminho_destino)
    
def salvar_imagem(url, caminho_local):
    # Fazendo a requisição para obter a imagem
    resposta = requests.get(url)
    
    # Verificando se a requisição foi bem-sucedida
    if resposta.status_code == 200:
        # Abrindo o arquivo local para escrita em modo binário
        with open(caminho_local, 'wb') as arquivo_local:
            # Escrevendo o conteúdo da resposta (imagem) no arquivo local
            arquivo_local.write(resposta.content)
        print("Imagem salva com sucesso em:", caminho_local)
    else:
        print("Falha ao baixar a imagem. Código de status:", resposta.status_code)      

async def main():
    linkscity = get_links_cidade("palmas", "to")
    print('LISTA CIDADE ' + str(len(linkscity)))
    
    for el in linkscity:
         print(el)
         await extrair_imagens_link("to", el)
      
if __name__ == "__main__":
    asyncio.run(main())

    
