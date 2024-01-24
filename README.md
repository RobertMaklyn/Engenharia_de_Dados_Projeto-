# Engenharia-de-Dados-_Projeto   
O objetivo do projeto é consumir dados de uma banco de dados, persisti-los em uma arquitetura de data lake com três camadas, sendo a primeira de dados brutos, a segunda com tratamento nos dados, e a terceira contendo dados analíticos agregados.

camada bronze: recebe os dados brutos e transforma no formato delta, 
camada prata: trata os dados removendo valores nulos,
camada ouro: é feito um join entre as tabelas 

## Arquitetura
![imagem1](/![imagem1](https://github.com/RobertMaklyn/Engenharia_de_Dados_Projeto-/assets/147719579/45ccd112-1811-4310-96f3-8a3b6675fb22)
)  

1 – Na sua conta do Microsoft Azure, crie um grupo de recursos contendo os seguintes recursos:

Azure Data Lake Storage: como datalake

Azure Data Factory: como orquestrador do projeto

Azure Databricks: como ambiente/plataforma de desenvolvimento para código Python/PySpark/SQL

Azure SQL: como banco de dados

Azure Key Vault: para armazenamento seguro de senhas/credenciais, cadeias de conexão por meio de "segredos"

![imagemnova2](/fotos/imagemnova2.PNG)

2 – Crie um contêiner no Azure Data Lake Storage com diretórios landing-zone, bronze, prata e ouro para armazenamento de dados em suas respectivas camadas

3 – Use o Azure Key Vault para armazenar o token de acesso da instância do Azure Databricks e as senhas e a cadeia de conexão do Azure Data Lake Storage.

4 – Inicie a instância do Azure Databricks e crie um escopo para acessar os arquivos do Azure Data Lake Storage e gerar o token de acesso para ser armazenado no Azure Key Vault.

5 – Faça um ponto de montagem para acessar os diretórios do seu contêiner no Azure Data Lake Storage.

6 - Crie pastas contendo os nootbook para cada uma das tabelas em suas respectivas camadas bronze, prata e ouro utilizando Python, PySpark e SQL para realizar as transformações necessárias

7 – Acesse a instância do Azure Data Factory, crie um pipeline, no painel de atividades, expanda a opção databricks, selecione os notebook. Configure serviços vinculados, configure os caminhos do notebook e vincule a execução sequencial de notebooks em caso de execução bem-sucedida.

![imagem3](/fotos/imagem3.PNG)


8 - Valide o pipeline, salve e debug.

9 – Você pode verificar se os dados foram salvos em cada respectivo diretório no Azure Data Lake Storage.

![imagem4](/fotos/imagem4.PNG)

Você pode verificar o código clicando [aqui](https://github.com/RobertMaklyn/Engenharia_de_Dados_Projeto-/tree/master/azure_data_bricks_notbooks)

