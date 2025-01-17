import requests
import json
import os
import random


urls = [
    'https://drive.google.com/drive/folders/121R3kcfJr25VN3TyNutQEabWplv2BudB?usp=sharing',
    'https://drive.google.com/drive/folders/1q99l3xMxSpzJJz2KGQIfqHKv2Fc1KxAN?usp=sharing',
    'https://drive.google.com/drive/folders/1_7H8-FL1JdccOzsbW0UOOUCICi1FER7b?usp=sharing',
    'https://drive.google.com/drive/folders/10Vcn8zs9utM5DF1zzaY3YBG3Y9cVqQ5m?usp=sharing',
    'https://drive.google.com/drive/folders/1Ymy67akfLh1PNyj9bBq4ZowYSXgEWnqz?usp=sharing',
    'https://drive.google.com/drive/folders/1Z0HWqXZQvZhIqJXOY2Gc-O0tKb5XjDVw?usp=sharing',
    'https://drive.google.com/drive/folders/1pP5eiQ0bCrGjUUvnDTLW8Fp8ltSU6WZY?usp=sharing',
    'https://drive.google.com/drive/folders/1A5Z1GBJ4Fi3D9gTui2req9HeH21I3CGt?usp=sharing',
    'https://drive.google.com/drive/folders/1JU4jcFTnL-OPyKnvmo9S2WJiHfnAFDlv?usp=sharing',
    'https://drive.google.com/drive/folders/1XSTDUIBvZniEBYrEGy2Ewg4T_McNatWK?usp=sharing',
    'https://drive.google.com/drive/folders/1is4qolLClvVtljApPcU4jrfXgAsFpiUk?usp=sharing',
    'https://drive.google.com/drive/folders/1E8h_fA6OMB_Sm6tkKTJAk5nsolnehRlq?usp=sharing',
    'https://drive.google.com/drive/folders/16Rhy0Lc7XmAhGRwm1vwSoUTFeQcST27X?usp=sharing',
    'https://drive.google.com/drive/folders/1_KQvAYDfYkqvNOT6g8Lh3spWrA94EVtT?usp=sharing',
    'https://drive.google.com/drive/folders/1Ho2kAKh_BehZ3O-OJWSIa8zJtb_NreeH?usp=sharing',
    'https://drive.google.com/drive/folders/1Cae-m4jWKuFzZ0Eqa439Re_No-S0sXzG?usp=sharing',
    'https://drive.google.com/drive/folders/11gGVtle-wPKBhEDrHkdayv48RxiOK5FW?usp=sharing',
    'https://drive.google.com/drive/folders/1kSDjTIm82b1v-hlsdoy14geIiisLuTVL?usp=sharing',
    'https://drive.google.com/drive/folders/1EAPyGH03vfLi0oUuuA2rMPzl9kk-v0j9?usp=sharing',
    'https://drive.google.com/drive/folders/1tjsoWoLapvp4WJLwj5JSEr63et1IFNIJ?usp=sharing',
    'https://drive.google.com/drive/folders/1JqrkWLkGUo57b7C1dViDjxDgBMleF09b?usp=sharing',
    'https://drive.google.com/drive/folders/1XW071JPCdvV2ivlPfok3oJ18Tfqj1eys?usp=sharing',
    'https://drive.google.com/drive/folders/1FQov2cqCKJsKinPMkjrhm-bx65_jOpFD?usp=sharing',
    'https://drive.google.com/drive/folders/1dWFNxlnjF8PlD5-tYdSGkBlIau-TE8fr?usp=sharing',
    'https://drive.google.com/drive/folders/1dCpihOoQsqyQFDn8GxzoNcirxePCm7Ar?usp=sharing',
    'https://drive.google.com/drive/folders/1w34pthAwTnM1iakrOrkb60LUGzhZMbHP?usp=sharing',
    'https://drive.google.com/drive/folders/1lzq0hePA4XRShOKi1M6cKctt4F-dCges?usp=sharing',
    'https://drive.google.com/drive/folders/1eaSP2cj_QkxWlQ5-odFvdTts5tD9ACrw?usp=sharing',
    'https://drive.google.com/drive/folders/1qANIUJmmfgZ72ecVFsM7UMPNpdayuPI_?usp=sharing',
    'https://drive.google.com/drive/folders/10dh5DN3KlRhPkxrLX9dDml39CXa7CXP-?usp=sharing',
    'https://drive.google.com/drive/folders/1V1fGfxmq77xlOA6e5gitNWpF_njLIcuN?usp=sharing',
    'https://drive.google.com/drive/folders/1yiWYLK_9ZoNfqWMNND6pVDMrbnSghrQF?usp=sharing',
    'https://drive.google.com/drive/folders/12N4xGf96shXke8X9btbowq5giZAmxeL_?usp=sharing',
]


def site_url(site):
    links = {}

    with open('nomes_cursos.txt', 'r+') as s:
        lista = s.readlines()
        for i, nome in enumerate(lista):
            lista[i] = lista[i].rstrip('\n')
            links[lista[i]] = urls[i]
    return links[str(site)]


class TelegramBot:
    def __init__(self):
        self.site_nome = ' '
        self.url = ' '
        self.contador = 0
        self.certo = False
        self.sites = self.ler_sites()
        self.email = 'ocoisa081@gmail.com'
        self.senha = '18020301.pP'
        iTOKEN  = '1723578764:AAHqoQKbR5R19dREGQOAJUW9NKOxB9fTVSc'
        self.iURL = f'https://api.telegram.org/bot{iTOKEN}/'


    def Iniciar(self):
        iUPDATE_ID = None
        try:
            while True:
                iATUALIZACAO = self.ler_novas_mensagens(iUPDATE_ID)
                IDADOS = iATUALIZACAO["result"]
                if IDADOS:
                    for dado in IDADOS:
                        iUPDATE_ID = dado['update_id']
                        mensagem = str(dado['message']['text'])
                        chat_id = dado["message"]["from"]["id"]
                        primeira_mensagem = int(dado["message"]["message_id"]) == 1
                        resposta = self.gerar_respostas(mensagem, primeira_mensagem)
                        print('usuário: ' + str(mensagem))
                        self.responder(resposta, chat_id)
                        if self.certo:
                            self.contador += 1
                        print('contador: ' + str(self.contador))
        except requests.exceptions.ConnectionError:
            return 'Foram excedidas as tentativas de conexão com o servidor'

    def ler_novas_mensagens(self, iUPDATE_ID):
        iLINK_REQ = f'{self.iURL}getUpdates?timeout=100'
        if iUPDATE_ID:
            iLINK_REQ = f'{iLINK_REQ}&offset={iUPDATE_ID + 1}'
        iRESULT = requests.get(iLINK_REQ)
        return json.loads(iRESULT.content)

    def gerar_respostas(self, mensagem, primeira_mensagem):
        if primeira_mensagem == True:
            return f'Bem-vindo ao PegasusCloud! Digite o site de sua preferência.'
        
        if mensagem == '/start':
            self.contador = 0
            self.certo = False
            return 'Digite o site de sua preferência.'

        if mensagem.lower() in ('olá', 'ola', 'oi'):
            return random.choice(['Olá!', 'Oi!', 'Fala aê!'])

        if mensagem.lower() in ('bom dia', 'boa tarde', 'boa noite'):
            if mensagem.lower() == 'bom dia':
                return 'Bom dia, humano!'
            else:
                return 'Boa' + mensagem.lower()[3:] + ', humano!'

        if self.contador == 0:
            if mensagem.lower() in self.sites:
                self.certo = True
                self.url = site_url(mensagem.lower())
                self.site_nome = mensagem.lower()
                return f'Ótimo! O site {mensagem.title()} está cadastrado.{os.linesep}Agora, por favor, informe seu email.'
            else:
                with open('sites_errados.txt', 'a') as novo_site:
                    novo_site.write(mensagem)
                    novo_site.write('\n')
                self.certo = False
                return f'Ah que pena! Não há nenhum site chamado {mensagem.title()} cadastrado.{os.linesep}Incluiremos este site em nossos bancos de dados para que, mais tarde, analisemos.'

        elif self.contador == 1:
            if mensagem.lower().strip() == self.email:
                self.certo = True
                return f'Email confere!{os.linesep}Agora, nos informe sua senha.'
            else:
                self.certo = False
                return 'Hum, eu não conheço esse email!'

        elif self.contador == 2:
            if mensagem.strip() == self.senha:
                self.certo = True
                if self.site_nome in ['ferreto', 'medcel', 'eduk']:
                    self.contador = 5
                    return f'Maravilha!! Seu login foi efetuado com sucesso! Agora você terá acesso ao curso!{os.linesep}Este curso está disponível no Google drive do @eusiim. Clique neste link para acessa-lo: {self.url}'
                else:
                    return f'''Maravilha!! Seu login foi efetuado com sucesso! Agora você terá acesso ao curso!{os.linesep}Me diz, você possui um servidor próprio? Sim ou Não?'''
            else:
                self.certo = False
                return 'Opa! Esta senha está errada, humano!'

        elif self.contador == 3:  
            while True:
                if mensagem.lower() in ['não', 'nao', 'n']:
                    self.certo = True 
                    return f'Tudo bem! Então você terá acesso ao servidor do @eusiim.{os.linesep}Basta acessar este link: {self.url}{os.linesep}Bons estudos!'
                elif mensagem.lower() in ['sim', 's']:
                    self.certo = True
                    return f'Ótimo! Digite /download para baixar o conteúdo. Certifique-se de ser encaminhado ao seu servidor.{os.linesep}Bons estudos!'
                else:
                    self.certo = False
                    return 'Não entendi o que quis me dizer. Sim ou Não?'

        elif self.contador == 4 and mensagem == '/download':
            self.certo = False
            return self.sites_arquivos()

        else:
            self.certo = False
            return f'Hummmm... o que será que você quis me dizer?!.{os.linesep}Digite /start para reiniciar o processo.'

    def responder(self, resposta, chat_id):
        iLINK_REQ = f'{self.iURL}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(iLINK_REQ)
        print("respondi: " + str(resposta))

    def ler_sites(self):
        with open('nomes_cursos.txt', 'r+') as arq:
            sites = arq.readlines()
            for i in range(len(sites)):
                sites[i] = sites[i].rstrip('\n').lower()
            return sites

    def sites_arquivos(self):
        mensagem = self.site_nome
        if mensagem.lower() == 'alura':
            import Alura
            Alura.Downloader().index()
        elif mensagem.lower() in ['aulatica', 'aulática']:
            import Aulatica
            Aulatica.Downloader().index()
        elif mensagem.lower() == 'balta':
            import balta
            balta.Downloader().index()
        elif mensagem.lower() == 'b7':
            import b7
            b7.Downloader().index()
        elif mensagem.lower() == 'cursosmed':
            import cursosmed
            cursosmed.Downloader().index()
        elif mensagem.lower() == 'dankicode':
            import dankicode
            dankicode.Downloader().index()
        elif mensagem.lower() == 'desec':
            import desec
            desec.Download().index()
        elif mensagem.lower() == 'desenvolvedor.io':
            import desenvolvedor_io
            desenvolvedor_io.Downloader().index()            
        elif mensagem.lower() == 'escola espartana':
            import escola_espartana
            escola_espartana.Downloader().index()
        elif mensagem.lower() in ['estrategia', 'estratégia']:
            import estrategia
            estrategia.Downloader().index()
        elif mensagem.lower() == 'estratega vest&mili':
            import estrategia_vestibulares
            estrategia_vestibulares.Downloader().index()
        elif mensagem.lower() == 'filonared':
            import filo
            filo.Downloader().index()
        elif mensagem.lower() == 'kuadro':
            import Kuadro
            Kuadro.Downloader().index()
        elif mensagem.lower() == 'percurso':
            import percurso
            percurso.Downloader().index()
        elif mensagem.lower() == 'proenem':
            import proenem
            proenem.Downloader().index()
        elif mensagem.lower() == 'promilitares':
            import promilitares
            promilitares.Downloader().index()
        elif mensagem.lower() == 'rockseat':
            import rockseat
            rockseat.Downloader().main()
        elif mensagem.lower() == 'sala do saber':
            import Sala_do_Saber_Downloader
            Sala_do_Saber_Downloader.Downloader().index()
        elif mensagem.lower() == 'sanarflix':
            import sanarflix
            sanarflix.Downloader().index()
        elif mensagem.lower() == 'stoodi':
            import stoodi
            stoodi.Downloader().index()
        elif mensagem.lower() == 'terra negra':
            import terra_negra
            terra_negra.Downloader().index()
        elif mensagem.lower() == 'treinaweb':
            import treina_web
            treina_web.Downloader().index()
        elif mensagem.lower() == 'upinside':
            import upinside
            upinside.Download().index()
        elif mensagem.lower() in ['waldematica', 'waldemática']:
            import waldematica
            waldematica.Downloader().index()


bot = TelegramBot()


if __name__ == '__main__':
    bot.Iniciar()
