# 📊 Análise de Vendas — E-commerce 2024

> Projeto de análise exploratória de dados de vendas com geração automática de KPIs, visualizações e insights de negócio usando Python.

---

## 🎯 Objetivo

Simular o trabalho de um analista de dados em um e-commerce real: limpar os dados, calcular indicadores-chave de desempenho (KPIs), gerar visualizações e extrair insights acionáveis para o negócio.

---

## 📁 Estrutura do Projeto

```
ecommerce-analysis/
│
├── analise_vendas.py        # Script principal
├── data/
│   └── vendas_ecommerce.csv # Dataset gerado automaticamente
├── outputs/
│   ├── 01_receita_mensal.png
│   ├── 02_receita_categoria.png
│   ├── 03_status_pedidos.png
│   ├── 04_avaliacao_categoria.png
│   ├── 05_receita_regiao.png
│   └── resumo_por_categoria.csv
└── README.md
```

---

## 🔍 O que a análise cobre

- ✅ **Limpeza e validação** dos dados (nulos, duplicatas, tipos)
- ✅ **KPIs principais**: receita total, ticket médio, taxa de cancelamento, avaliação média
- ✅ **Análise por categoria**: receita, avaliações, cancelamentos
- ✅ **Análise por região**: receita e ticket médio
- ✅ **Evolução mensal** da receita ao longo do ano
- ✅ **Insights automáticos**: melhor mês, produto mais vendido, categoria mais cancelada
- ✅ **Exportação** de resumo em CSV

---

## 📈 Visualizações geradas

| Gráfico | Descrição |
|---|---|
| Receita Mensal | Evolução da receita ao longo dos 12 meses |
| Receita por Categoria | Comparativo entre categorias de produto |
| Status dos Pedidos | Distribuição entre entregue, cancelado, etc. |
| Avaliação por Categoria | Nota média de satisfação por categoria |
| Receita por Região | Desempenho regional de vendas |

---

## 🛠️ Tecnologias utilizadas

- **Python 3.10+**
- **Pandas** — manipulação e análise de dados
- **NumPy** — geração de dados e cálculos numéricos
- **Matplotlib** — criação de gráficos
- **Seaborn** — estilização das visualizações

---

## ▶️ Como executar

**1. Clone o repositório**
```bash
git clone https://github.com/seu-usuario/ecommerce-analysis.git
cd ecommerce-analysis
```

**2. Instale as dependências**
```bash
pip install pandas numpy matplotlib seaborn
```

**3. Execute a análise**
```bash
python analise_vendas.py
```

Os gráficos e o CSV de resumo serão gerados automaticamente na pasta `/outputs`.

---

## 💡 Principais Insights (exemplo de saída)

```
💰 Receita Total    : R$ 2.561.771,64
📦 Total de Pedidos : 1.200
🎯 Ticket Médio     : R$ 2.134,81
❌ Taxa Cancelamento: 9,3%
⭐ Avaliação Média  : 3,90 / 5,0

📅 Melhor mês       : Maio
⚠️  Mais cancelamentos: Eletrônicos
📍 Maior ticket médio: Sudeste (R$ 2.238,57)
```

---

## 🤝 Sobre

Projeto desenvolvido para demonstrar habilidades em **análise exploratória de dados**, **visualização** e **geração de insights de negócio** com Python.

Disponível para projetos freelance de análise de dados, dashboards e automações.
📬 Entre em contato: [seu-email@email.com](mailto:laurafranciscotavora5@gmail.com)
