import PySimpleGUI as sg

class telaPython:
    def __init__(self):
        sg.change_look_and_feel('DarkBlue')
        # Layout
        layout = [
            [sg.Text('Nome', size=(5,0)), sg.Input(size=(15,0), key='nome')],
            [sg.Text('Idade', size=(5,0)), sg.Input(size=(15,0), key='idade')],
            [sg.Text('Estados Visitados', size=(15,0))],
            [sg.Checkbox('MG', key = 'mg'), sg.Checkbox('RJ', key='rj'),
                sg.Checkbox('ES', key = 'es'), sg.Checkbox('SP', key='sp')],
            [sg.Text('Receber e-mail', size=(15,0))],
            [sg.Radio('Sim','emailrd', key = 'recebeSim'),
                sg.Radio('Não', 'rdemailrd', key = 'recebeNao')],
            [sg.Slider(range=(0,200), default_value=0, orientation='h',
                size=(15,20), key='sliderVelocidade')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(25,15))]
        ]
        # Janela
        self.janela = sg.Window('Cadastro').layout(layout)

    def iniciar(self):
        while True:
            # Extrair dados da tela
            self.button, self.values = self.janela.Read()
            nomeUser = self.values['nome']
            idadeUser = self.values['idade']
            visitouMG = self.values['mg']
            visitouRJ = self.values['rj']
            visitouSP = self.values['sp']
            visitouES = self.values['es']
            receberEmailSIM = self.values['recebeSim']
            receberEmailNAO = self.values['recebeNao']
            velocidadeScript = self.values['sliderVelocidade'],
            print(f'nome: {nomeUser}')
            print(f'idade: {idadeUser}')
            print(f'MG: {visitouMG}')
            print(f'RJ: {visitouRJ}')
            print(f'SP: {visitouSP}')
            print(f'ES: {visitouES}')
            print(f'Velocidade do Script: {velocidadeScript}')




tela = telaPython()
tela.iniciar()