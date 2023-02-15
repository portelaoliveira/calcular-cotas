<div><link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Trirong">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Oswald">
<style type="text/css">
    h1 {
        text-align: center;
    }
    h1,h2,h3,h4 {        
        font-family: "Trirong", serif;
    }
    p {
        text-indent: 1rem;
        font-family: "Oswald", sans-serif;
        text-align: center;
    }
    img {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    img[alt=tela] {
        width: 80%;
    }
    .legend {
        text-align:center;
        font-size:0.8rem;
    }
</style>
</div>  
  
#  Problema das cotas
  
  
##  Documentação de uso do programa
  
  
    Discente: Danilo Portela de Oliveira
    Matrícula: 222105229
    Disciplina: PROGRAMAÇÃO PARA GEOCIÊNCIAS
  
O programa foi desenvolvido com o objetivo de calcular cotas de pontos intermediários a outros com cotas previamente medidas. A Figura 1 mostra a arquitetura do projeto, onde no arquivo functions.py encontra-se as funções necessárias para o desenvolvimento do programa, o arquivo main.py é o arquivo principal, ou seja, toda árvore de componetes é desenvolvida nesse arquivo, na pasta "datas" encontra-se o arquivo dados.txt (mostrado na Figura 2) contendo o ID do Marco Topográfico, a cota (metros) dos pontos medidos, que estão igualmente espaçados em superfície, sendo o espaçamento entre eles (100 metros) e o arquivo "requirements.txt" é o arquivo com as vesões das bibliotecas instaladas.
  
![tela](./tutorial/img/estrutura_projeto.png )
  
<p class="legend"> Figura 1: Arquitetura do porjeto. </p>
  
![tela](./tutorial/img/estrutura_dados_de_entrada.png )
  
<p class="legend"> Figura 2: Estrutura dos dados de entrada. </p>
  
![tela](./tutorial/img/tela_3.png )
  
<p class="legend"> Figura 3: Tela 3. </p>
  
![tela](./tutorial/img/tela_4.png )
  
<p class="legend"> Figura 4: Tela 4. </p>
  
![tela](./tutorial/img/tela_5.png )
  
<p class="legend"> Figura 5: Tela 5. </p>
  
  
```
source ./venv/bin/activate
```
  
###  Exemplo de uso:
  
  
####  Passo 1:
  
  
O usuário preenche os campos com as informações relevantes (Figuras 6 a 9). Nos campos de "Atividade de campo", "Equipe técnica", "Veículos" e "Equipamentos" as informações são inseridas após clicar no menu desejado e marcar as caixas de seleção. Para selecionar a pasta para upload no DropBox, basta ir no campo "Arquivos para upload". O usuário tem a opção de selecionar a empresa em "Empresa", subpasta 1 e 2, e local.
  
![tela](tutorial/img/preenchimento_atividade.png )
  
<p class="legend"> Figura 6: Preenchimento de atividades. </p>
  
![tela](tutorial/img/preenchimento_equipe.png )
  
<p class="legend"> Figura 7: Preenchimento de equipe. </p>
  
![tela](tutorial/img/preenchimento_base.png )
  
<p class="legend"> Figura 8: Preenchimento de equipamentos e seleção de base. </p>
  
![tela](tutorial/img/preenchimento_pasta.png )
  
<p class="legend"> Figura 9: Preenchimento das pastas de upload. </p>
  
Se nas atividades de campo houver "Lidar" ou "Ortofoto" o campo de "Número de voos" é mostrado (Figura 10).
  
![tela](tutorial/img/preenchimento_voos.png )
  
<p class="legend"> Figura 10: Campo com número de voos realizados na atividade. </p>
  
Caso queira criar uma nova pasta, basta escrever o nome da pasta no campo de seleção (Figura 11).
  
![tela](tutorial/img/nova_pasta.png )
  
<p class="legend"> Figura 11: Criação de pasta. </p>
  
- **Arquivos para Upload**: Nesse campo, o usuário seleciona a pasta com os dados de aquisição que serão enviados para o DropBox.
  
- **Seleção de fotos para RDO**: Nesse campo, o usuário seleciona a pasta com as fotos que serão inseridas no relatório (caso existam). A imagem da base deve possuir nome "base_NOMEDABASE", a imagem de NA deve possuir nome "na" e a imagem de batimetria deve possuir nome "bat". Outra observação importante é que caso seja necessário adicionar os NAs, o usuário deverá ir na pasta que o executável do Software encontra-se, procurar a pasta "Templates" e nela copiar o arquivo Excel "modelo_planilha.xlsx" para pasta desejada, e nesse arquivo preencher com as informações desejadas para o NA (Figura 13) e selecionar a pasta com esse arquivo no campo "Seleção de fotos para RDO". As fotos (caso existam) e esse arquivo preenchido devem estar na mesma pasta (como é mostrado na Figura 12). Uma observação importante é que nessa pasta deve existir somente um arquivo Excel e as imagens devem ser nomeadas de acordo com a Figura 12.
  
![](tutorial/img/nomear_imgs.png )
  
<p class="legend"> Figura 12: Estrutura dos arquivos na paste que deve ser selecionada no campo "Seleção de fotos para RDO". </p>
  
![](tutorial/img/nas_excel.png )
  
<p class="legend"> Figura 13: Planilha "modelo_planilha.xlsx". </p>
  
####  Passo 2:
  
  
Após preencher com as informações necessárias, o usuário deve clicar em "Finish" (Figura 5). Caso algum campo opcional não seja preenchido, uma mensagem de "Warning" aparece (Figura 14), e os campos opcionais ficam marcados de laranja, caso algum campo obrigatório não seja preenchido os campos ficam marcados de vermelho (Figura 15). Para continuar, basta clicar em "Sim", caso contrário, clique em "Não" e preencha os campos faltantes e novamente clique em "Finish".
  
![tela](tutorial/img/aviso_campos.png )
  
<p class="legend"> Figura 14: Mensagem de aviso de campos faltantes. </p>
  
![tela](tutorial/img/campo_obrigatorio.png )
  
<p class="legend"> Figura 15: Campos opcionais marcados de laranja e campos obrigatórios marcados de vermelho. </p>
  
####  Passo 3:
  
  
Após preencher com as informações necessárias, o documento Word é aberto automaticamente. Se o usuário ver no documento Word que todas as informações que deseja encontram-se corretas, basta fechar o documento Word e na mensagem de confirmação (Figura 11) clicar em "Sim" e o upload com os arquivos e o relatório diário de obras será enviado para o Dropbox.
  
![tela](tutorial/img/aviso_rdo.png )
  
<p class="legend"> Figura 16: Confirmação do upload. </p>
  
O progresso é então mostrado na barra de progresso (Figura 17). Se desejar cancelar o upload, basta clicar no botão de "Cancel".
  
![tela](tutorial/img/progresso.png )
  
<p class="legend"> Figura 17: Progresso de upload. </p>
  
No fim do processo de upload é então mostrado um aviso de envio concluído (Figura 18).
  
![tela](tutorial/img/finalizado.png )
  
<p class="legend"> Figura 18: Upload finalizado. </p>
  
###  Inserção de informações
  
  
Para inserir informações basta clicar no botão de "+", presente ao lado do título em todas as telas. Será aberta uma tela com informações que podem ser inseridas (Figura 19).
  
![](tutorial/img/tela_info.png )
  
<p class="legend"> Figura 19: Tela de inserção de informações. </p>
  
####  Atividade
  
  
Para inserir uma nova atividade basta preencher o campo "Atividade" (Figura 20) e clicar em "Ok!".
  
![](tutorial/img/add_atividade.png )
  
<p class="legend"> Figura 20: Tela de inserção de atividades. </p>
  
####  Base
  
  
Para inserir uma nova base basta preencher o campo "Nome" com o nome da base, e os campos "Norte", "Este" e "Altitude" com os valores desejados (Figura 21) e clicar em "Ok!".
  
![](tutorial/img/add_base.png )
  
<p class="legend"> Figura 21: Tela de inserção de bases. </p>
  
Caso se deseje atualizar a base basta que o nome da base seja igual ao de alguma base já cadastrada. Para apagar a base preencha o campo "Nome" com o nome da base que se deseja apagar e os campos "Norte", "Este" e "Altitude" com o valor 0.
  
####  Equipamento
  
  
Para inserir um novo equipamento basta preencher o campo "Tipo" com o tipo de equipamento, e o campo "Modelo" com o modelo do equipamento (Figura 22) e clicar em "Ok!".
  
![](tutorial/img/add_equip.png )
  
<p class="legend"> Figura 22: Tela de inserção de equipamentos. </p>
  
Para apagar um equipamento preencha o campo "Modelo" com o modelo do equipamento que se deseja apagar e o campo "Tipo" deixe em branco.
  
####  Funcionário
  
  
Para inserir um novo funcionário basta preencher o campo "Nome" com o nome do funcionário, e o campo "Função" com sua função (Figura 23) e clicar em "Ok!".
  
![](tutorial/img/add_funcionario.png )
  
<p class="legend"> Figura 23: Tela de inserção de funcionários. </p>
  
Para apagar um registro de funcionário preencha o campo "Nome" com o nome do funcionário que se deseja apagar e o campo "Função" deixe em branco.
  
####  Veículo
  
  
Para inserir um novo veículo basta preencher o campo "Modelo" com o modelo do veículo, e o campo "Placa" com sua placa (Figura 24) e clicar em "Ok!".
  
![](tutorial/img/add_veiculo.png )
  
<p class="legend"> Figura 24: Tela de inserção de veículos. </p>
  
Para apagar um veículo preencha o campo "Placa" com a placa do veículo que se deseja apagar e o campo "Modelo" deixe em branco.
  