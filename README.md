# Análise de Vendas — E-commerce 2024

Projeto de análise exploratória de dados de vendas desenvolvido em Python, com geração automática de indicadores de desempenho, visualizações e insights de negócio.

A proposta do projeto é simular as principais atividades realizadas por um analista de dados em um ambiente de e-commerce, contemplando desde a preparação dos dados até a apresentação dos resultados.

---

## Visão geral

A aplicação processa um conjunto de dados de vendas de e-commerce, realiza verificações de qualidade, calcula indicadores estratégicos e gera visualizações para apoiar a análise do desempenho comercial.

Ao final da execução, o projeto disponibiliza:

- Indicadores-chave de desempenho;
- Análises por categoria de produto;
- Análises por região;
- Evolução mensal da receita;
- Distribuição dos status dos pedidos;
- Insights automáticos;
- Gráficos em formato PNG;
- Resumo consolidado em CSV.

---

## Objetivo

Simular o trabalho de um analista de dados em um e-commerce real, abrangendo as seguintes etapas:

1. Limpeza e validação dos dados;
2. Preparação das informações para análise;
3. Cálculo de indicadores-chave de desempenho;
4. Geração de visualizações;
5. Identificação de padrões e tendências;
6. Extração de insights acionáveis para o negócio;
7. Exportação dos resultados.

---

## Estrutura do projeto

```text
ecommerce-analysis/
│
├── analise_vendas.py        # Script principal
│
├── data/
│   └── vendas_ecommerce.csv # Dataset gerado automaticamente
│
├── outputs/
│   ├── 01_receita_mensal.png
│   ├── 02_receita_categoria.png
│   ├── 03_status_pedidos.png
│   ├── 04_avaliacao_categoria.png
│   ├── 05_receita_regiao.png
│   └── resumo_por_categoria.csv
│
└── README.md
```

---

## Funcionalidades

### Limpeza e validação dos dados

O projeto realiza verificações relacionadas a:

- Valores nulos;
- Registros duplicados;
- Tipos de dados;
- Consistência das informações;
- Preparação das colunas utilizadas nas análises.

### Indicadores-chave de desempenho

A análise calcula os seguintes KPIs:

- Receita total;
- Total de pedidos;
- Ticket médio;
- Taxa de cancelamento;
- Avaliação média.

### Análise por categoria

Para cada categoria de produto, são analisados:

- Receita gerada;
- Avaliação média;
- Quantidade de pedidos;
- Volume de cancelamentos.

### Análise por região

A análise regional apresenta:

- Receita por região;
- Ticket médio por região;
- Comparação de desempenho entre localidades.

### Evolução mensal

O projeto acompanha a evolução da receita durante os 12 meses do ano, permitindo identificar:

- Meses de melhor desempenho;
- Oscilações de receita;
- Tendências sazonais.

### Insights automáticos

Ao final da execução, o sistema identifica automaticamente informações como:

- Melhor mês de vendas;
- Produto mais vendido;
- Categoria com maior número de cancelamentos;
- Região com maior ticket médio.

### Exportação de resultados

Os resultados consolidados por categoria são exportados automaticamente em formato CSV.

---

## Visualizações geradas

| Arquivo | Visualização | Descrição |
|---|---|---|
| `01_receita_mensal.png` | Receita mensal | Evolução da receita ao longo dos 12 meses |
| `02_receita_categoria.png` | Receita por categoria | Comparativo de receita entre as categorias de produto |
| `03_status_pedidos.png` | Status dos pedidos | Distribuição entre pedidos entregues, cancelados e demais status |
| `04_avaliacao_categoria.png` | Avaliação por categoria | Nota média de satisfação por categoria |
| `05_receita_regiao.png` | Receita por região | Comparação do desempenho regional de vendas |

Todos os gráficos são armazenados automaticamente no diretório:

```text
outputs/
```

---

## Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python 3.10+ | Linguagem principal do projeto |
| Pandas | Manipulação, limpeza e análise dos dados |
| NumPy | Geração de dados e cálculos numéricos |
| Matplotlib | Criação das visualizações |
| Seaborn | Estilização dos gráficos |

---

## Pré-requisitos

Antes de executar o projeto, verifique se o Python 3.10 ou uma versão superior está instalado.

Para conferir a versão disponível:

```bash
python --version
```

No Windows, também é possível utilizar:

```bash
py --version
```

---

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/ecommerce-analysis.git
```

Acesse a pasta do projeto:

```bash
cd ecommerce-analysis
```

### 2. Instale as dependências

```bash
pip install pandas numpy matplotlib seaborn
```

### 3. Execute a análise

```bash
python analise_vendas.py
```

No Windows, caso o comando `python` não esteja disponível:

```bash
py analise_vendas.py
```

Após a execução, os gráficos e o arquivo CSV de resumo serão gerados automaticamente na pasta:

```text
outputs/
```

---

## Exemplo de resultado

A execução do projeto apresenta um resumo semelhante ao seguinte:

```text
Receita Total     : R$ 2.561.771,64
Total de Pedidos  : 1.200
Ticket Médio      : R$ 2.134,81
Taxa Cancelamento : 9,3%
Avaliação Média   : 3,90 / 5,0

Melhor mês         : Maio
Mais cancelamentos : Eletrônicos
Maior ticket médio : Sudeste (R$ 2.238,57)
```

Os resultados podem variar de acordo com os dados gerados e processados durante a execução.

---

## Resultados gerados

Ao concluir a análise, o projeto cria os seguintes arquivos:

```text
outputs/
├── 01_receita_mensal.png
├── 02_receita_categoria.png
├── 03_status_pedidos.png
├── 04_avaliacao_categoria.png
├── 05_receita_regiao.png
└── resumo_por_categoria.csv
```

O arquivo `resumo_por_categoria.csv` reúne os principais indicadores consolidados por categoria de produto.

---

## Principais análises realizadas

### Receita mensal

Apresenta a evolução da receita ao longo dos 12 meses do ano, permitindo identificar períodos de maior e menor desempenho comercial.

### Receita por categoria

Compara o volume de receita gerado por cada categoria de produto, facilitando a identificação das categorias com maior contribuição para o faturamento.

### Status dos pedidos

Apresenta a distribuição dos pedidos entre entregues, cancelados e demais status presentes no conjunto de dados.

### Avaliação por categoria

Compara a avaliação média dos clientes em cada categoria de produto, auxiliando na identificação de possíveis problemas de satisfação.

### Receita por região

Apresenta o desempenho comercial por região, considerando receita e ticket médio.

---

## Possíveis aplicações

Este projeto pode ser utilizado como base para:

- Estudos de análise exploratória de dados;
- Construção de portfólio profissional;
- Desenvolvimento de dashboards;
- Criação de relatórios automatizados;
- Análise de desempenho comercial;
- Identificação de oportunidades de negócio;
- Monitoramento de indicadores de vendas;
- Projetos freelance de análise de dados.

---

## Sobre o projeto

Este projeto foi desenvolvido para demonstrar habilidades relacionadas a:

- Análise exploratória de dados;
- Limpeza e transformação de dados;
- Cálculo de indicadores de desempenho;
- Visualização de informações;
- Identificação de padrões;
- Geração de insights de negócio;
- Automação de relatórios com Python.

O projeto também pode ser utilizado como parte de um portfólio profissional voltado para oportunidades em análise de dados, business intelligence, dashboards e automações.

---

## Contato

Para dúvidas, sugestões, oportunidades profissionais, autorização de uso ou informações sobre o projeto, entre em contato:

- GitHub: [@LauraTavora](https://github.com/LauraTavora)
- LinkedIn: [Laura Távora](https://www.linkedin.com/in/laura-francisco-távora-946a622b3/?skipRedirect=true)
- E-mail: `laurafranciscotavora5@gmail.com`


---

## Licença e direitos autorais

Copyright © 2026 Laura Távora.

Todos os direitos reservados.

Este projeto, incluindo seu código-fonte, documentação, estrutura e materiais relacionados, não pode ser copiado, modificado, distribuído ou utilizado comercialmente sem autorização prévia e expressa da autora.

Consulte o arquivo [LICENSE](LICENSE) para obter mais informações sobre as condições de uso.
