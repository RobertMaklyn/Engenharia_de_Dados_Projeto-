# Engenharia_de_Dados_Projeto   
O objetivo do projeto é consumir dados de uma banco de dados, persisti-los em uma arquitetura de data lake com três camadas, sendo a primeira de dados brutos, a segunda com tratamento nos dados, e a terceira contendo dados analíticos agregados.

camada bronze: recebe os dados brutos e transforma no formato delta, 
camada prata: trata os dados removendo valores nulos,
camada ouro: é feito um join entre as tabelas 

## Arquitetura
![imagem1](https://github.com/RobertMaklyn/Engenharia_de_Dados_Projeto-/assets/147719579/4a89586d-4f9c-4528-b412-27d41dba67b0)


1 – Na sua conta do Microsoft Azure, crie um grupo de recursos contendo os seguintes recursos:

Azure Data Lake Storage: como datalake

Azure Data Factory: como orquestrador do projeto

Azure Databricks: como ambiente/plataforma de desenvolvimento para código Python/PySpark/SQL

Azure SQL: como banco de dados

Azure Key Vault: para armazenamento seguro de senhas/credenciais, cadeias de conexão por meio de "segredos"

![imagemnova2](https://github.com/RobertMaklyn/Engenharia_de_Dados_Projeto-/assets/147719579/4c32efaf-450b-4441-99f8-a98c1a4ef549)

2 – Crie um contêiner no Azure Data Lake Storage com diretórios landing-zone, bronze, prata e ouro para armazenamento de dados em suas respectivas camadas

3 – Use o Azure Key Vault para armazenar o token de acesso da instância do Azure Databricks e as senhas e a cadeia de conexão do Azure Data Lake Storage.

4 – Inicie a instância do Azure Databricks e crie um escopo para acessar os arquivos do Azure Data Lake Storage e gerar o token de acesso para ser armazenado no Azure Key Vault.

5 – Faça um ponto de montagem para acessar os diretórios do seu contêiner no Azure Data Lake Storage.

6 - Crie pastas contendo os nootbook para cada uma das tabelas em suas respectivas camadas bronze, prata e ouro utilizando Python, PySpark e SQL para realizar as transformações necessárias

7 – Acesse a instância do Azure Data Factory, crie um pipeline, no painel de atividades, expanda a opção databricks, selecione os notebook. Configure serviços vinculados, configure os caminhos do notebook e vincule a execução sequencial de notebooks em caso de execução bem-sucedida.

![imagem3](https://github.com/RobertMaklyn/Engenharia_de_Dados_Projeto-/assets/147719579/44416e3a-8f43-4c5f-b060-30294400d277)


8 - Valide o pipeline, salve e debug.

9 – Você pode verificar se os dados foram salvos em cada respectivo diretório no Azure Data Lake Storage.

![imagem4](https://github.com/RobertMaklyn/Engenharia_de_Dados_Projeto-/assets/147719579/d36b98f0-1346-4bb1-b6d1-240b9b10bec8)


Você pode verificar o código clicando [aqui](https://github.com/RobertMaklyn/Engenharia_de_Dados_Projeto-/tree/master/azure_data_bricks_notbooks)

