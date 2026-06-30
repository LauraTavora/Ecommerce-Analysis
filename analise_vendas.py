

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
from datetime import datetime, timedelta
import warnings
import os

warnings.filterwarnings("ignore")

# ── Configurações visuais ──────────────────────────────────
plt.rcParams.update({
    "figure.facecolor": "#F8F9FA",
    "axes.facecolor":   "#F8F9FA",
    "axes.grid":        True,
    "grid.alpha":       0.4,
    "font.family":      "sans-serif",
    "axes.spines.top":  False,
    "axes.spines.right":False,
})
PALETTE = ["#4361EE", "#F72585", "#4CC9F0", "#7209B7", "#3A0CA3"]
OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)


#  1. GERAÇÃO DE DADOS FICTÍCIOS (simulando dataset real)
def gerar_dados(n=1200, seed=42):
    np.random.seed(seed)

    categorias = ["Eletrônicos", "Roupas", "Casa & Jardim", "Esportes", "Beleza"]
    pesos_cat  = [0.30, 0.25, 0.20, 0.15, 0.10]

    status_list  = ["Entregue", "Em trânsito", "Cancelado", "Devolvido"]
    pesos_status = [0.70, 0.15, 0.10, 0.05]

    regioes = ["Sudeste", "Sul", "Nordeste", "Centro-Oeste", "Norte"]
    pesos_reg = [0.40, 0.25, 0.20, 0.10, 0.05]

    datas = [
        datetime(2024, 1, 1) + timedelta(days=int(d))
        for d in np.random.randint(0, 365, n)
    ]

    cat_escolhida = np.random.choice(categorias, n, p=pesos_cat)

    preco_base = {
        "Eletrônicos":  (200, 3000),
        "Roupas":       (40,  400),
        "Casa & Jardim":(30,  800),
        "Esportes":     (50,  600),
        "Beleza":       (20,  250),
    }

    precos = np.array([
        round(np.random.uniform(*preco_base[c]), 2)
        for c in cat_escolhida
    ])

    qtd = np.random.randint(1, 6, n)

    df = pd.DataFrame({
        "order_id":    range(1, n + 1),
        "data":        datas,
        "categoria":   cat_escolhida,
        "produto":     [f"Produto_{np.random.randint(100,999)}" for _ in range(n)],
        "preco_unit":  precos,
        "quantidade":  qtd,
        "receita":     (precos * qtd).round(2),
        "status":      np.random.choice(status_list, n, p=pesos_status),
        "regiao":      np.random.choice(regioes,      n, p=pesos_reg),
        "avaliacao":   np.random.choice([1,2,3,4,5],  n, p=[0.05,0.08,0.12,0.35,0.40]),
    })

    df["mes"]      = df["data"].dt.month
    df["mes_nome"] = df["data"].dt.strftime("%b")
    df["dia_sem"]  = df["data"].dt.day_name()

    os.makedirs("data", exist_ok=True)
    df.to_csv("data/vendas_ecommerce.csv", index=False, encoding="utf-8-sig")
    return df


#  2. LIMPEZA E VALIDAÇÃO
def limpar_dados(df):
    print("\nRELATÓRIO DE QUALIDADE DOS DADOS")
    print("=" * 45)
    print(f"  Linhas totais  : {len(df):,}")
    print(f"  Colunas        : {df.shape[1]}")
    print(f"  Valores nulos  : {df.isnull().sum().sum()}")
    print(f"  Duplicatas     : {df.duplicated().sum()}")

    # Remove duplicatas e nulos (se houver)
    df = df.drop_duplicates().dropna()

    # Garante tipos corretos
    df["data"]       = pd.to_datetime(df["data"])
    df["preco_unit"] = df["preco_unit"].astype(float)
    df["receita"]    = df["receita"].astype(float)

    print(f"\n  Dados prontos para análise: {len(df):,} registros")
    return df


#  3. ANÁLISE EXPLORATÓRIA (EDA)
def eda(df):
    print("\n\nINDICADORES PRINCIPAIS (KPIs)")
    print("=" * 45)

    receita_total   = df["receita"].sum()
    pedidos_total   = df["order_id"].nunique()
    ticket_medio    = receita_total / pedidos_total
    taxa_cancel     = (df["status"] == "Cancelado").mean() * 100
    avaliacao_media = df["avaliacao"].mean()

    print(f"  Receita Total    : R$ {receita_total:,.2f}")
    print(f"  Total de Pedidos : {pedidos_total:,}")
    print(f"  Ticket Médio     : R$ {ticket_medio:,.2f}")
    print(f"  Taxa Cancelamento: {taxa_cancel:.1f}%")
    print(f"  Avaliação Média  : {avaliacao_media:.2f} / 5.0")

    print("\n\nTOP 3 CATEGORIAS POR RECEITA")
    print("=" * 45)
    top_cat = (
        df.groupby("categoria")["receita"]
        .sum()
        .sort_values(ascending=False)
        .head(3)
    )
    for i, (cat, val) in enumerate(top_cat.items(), 1):
        print(f"  {i}. {cat:<18} R$ {val:,.2f}")

    print("\n\nRECEITA POR REGIÃO")
    print("=" * 45)
    reg = df.groupby("regiao")["receita"].sum().sort_values(ascending=False)
    for r, v in reg.items():
        print(f"  {r:<18} R$ {v:,.2f}")

    return receita_total, pedidos_total, ticket_medio


#  4. VISUALIZAÇÕES
def gerar_graficos(df):
    print("\n\nGerando visualizações...")

    # ── Gráfico 1: Receita mensal ──────────────────────────
    fig, ax = plt.subplots(figsize=(12, 5))
    meses_ordem = ["Jan","Feb","Mar","Apr","May","Jun",
                   "Jul","Aug","Sep","Oct","Nov","Dec"]
    rec_mensal = (
        df.groupby("mes_nome")["receita"]
        .sum()
        .reindex(meses_ordem)
        .dropna()
    )
    ax.bar(rec_mensal.index, rec_mensal.values, color=PALETTE[0], alpha=0.85, width=0.6)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"R${x/1000:.0f}k"))
    ax.set_title("Receita Mensal — 2024", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("Mês"); ax.set_ylabel("Receita")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/01_receita_mensal.png", dpi=150)
    plt.close()

    # ── Gráfico 2: Receita por categoria ──────────────────
    fig, ax = plt.subplots(figsize=(9, 5))
    cat_rec = df.groupby("categoria")["receita"].sum().sort_values()
    bars = ax.barh(cat_rec.index, cat_rec.values, color=PALETTE[:len(cat_rec)], alpha=0.85)
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"R${x/1000:.0f}k"))
    ax.set_title("Receita por Categoria", fontsize=14, fontweight="bold", pad=15)
    for bar, val in zip(bars, cat_rec.values):
        ax.text(val + 500, bar.get_y() + bar.get_height()/2,
                f"R${val/1000:.1f}k", va="center", fontsize=9)
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/02_receita_categoria.png", dpi=150)
    plt.close()

    # ── Gráfico 3: Status dos pedidos (pizza) ─────────────
    fig, ax = plt.subplots(figsize=(7, 7))
    status_count = df["status"].value_counts()
    wedges, texts, autotexts = ax.pie(
        status_count.values,
        labels=status_count.index,
        autopct="%1.1f%%",
        colors=PALETTE,
        startangle=140,
        pctdistance=0.82,
    )
    for t in autotexts:
        t.set_fontsize(11); t.set_fontweight("bold")
    ax.set_title("Distribuição de Status dos Pedidos", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/03_status_pedidos.png", dpi=150)
    plt.close()

    # ── Gráfico 4: Avaliação média por categoria ───────────
    fig, ax = plt.subplots(figsize=(9, 5))
    aval_cat = df.groupby("categoria")["avaliacao"].mean().sort_values(ascending=False)
    ax.bar(aval_cat.index, aval_cat.values, color=PALETTE[2], alpha=0.85, width=0.5)
    ax.set_ylim(0, 5.5)
    ax.axhline(aval_cat.mean(), color=PALETTE[1], linestyle="--", linewidth=1.5,
               label=f"Média geral: {aval_cat.mean():.2f}")
    ax.set_title("Avaliação Média por Categoria", fontsize=14, fontweight="bold", pad=15)
    ax.set_ylabel("Nota (1–5)"); ax.legend()
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/04_avaliacao_categoria.png", dpi=150)
    plt.close()

    # ── Gráfico 5: Receita por região ─────────────────────
    fig, ax = plt.subplots(figsize=(9, 5))
    reg_rec = df.groupby("regiao")["receita"].sum().sort_values(ascending=False)
    ax.bar(reg_rec.index, reg_rec.values, color=PALETTE[3], alpha=0.85, width=0.5)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"R${x/1000:.0f}k"))
    ax.set_title("Receita por Região", fontsize=14, fontweight="bold", pad=15)
    ax.set_ylabel("Receita")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/05_receita_regiao.png", dpi=150)
    plt.close()

    print(f" 5 gráficos salvos em /{OUTPUT_DIR}/")


#  5. INSIGHTS AUTOMÁTICOS
def gerar_insights(df):
    print("\n\nINSIGHTS AUTOMÁTICOS")
    print("=" * 45)

    # Melhor mês
    melhor_mes = df.groupby("mes_nome")["receita"].sum().idxmax()
    print(f" Melhor mês em receita : {melhor_mes}")

    # Categoria mais cancelada
    cancel = df[df["status"] == "Cancelado"]
    if not cancel.empty:
        cat_cancel = cancel["categoria"].value_counts().idxmax()
        print(f" Categoria com mais cancelamentos: {cat_cancel}")

    # Produto mais vendido por quantidade
    top_produto = df.groupby("produto")["quantidade"].sum().idxmax()
    print(f" Produto mais vendido  : {top_produto}")

    # Região com maior ticket médio
    ticket_reg = (df.groupby("regiao")["receita"].sum() /
                  df.groupby("regiao")["order_id"].nunique())
    melhor_reg = ticket_reg.idxmax()
    print(f" Maior ticket médio    : {melhor_reg} (R$ {ticket_reg[melhor_reg]:,.2f})")

    # Dia da semana com mais pedidos
    dia_top = df["dia_sem"].value_counts().idxmax()
    print(f" Dia com mais pedidos  : {dia_top}")


#  6. EXPORTAR RESUMO CSV
def exportar_resumo(df):
    resumo = df.groupby("categoria").agg(
        receita_total   =("receita",    "sum"),
        total_pedidos   =("order_id",   "count"),
        ticket_medio    =("receita",    "mean"),
        avaliacao_media =("avaliacao",  "mean"),
        cancelamentos   =("status",     lambda x: (x == "Cancelado").sum()),
    ).round(2).reset_index()

    resumo.to_csv(f"{OUTPUT_DIR}/resumo_por_categoria.csv", index=False, encoding="utf-8-sig")
    print(f"\n Resumo exportado: /{OUTPUT_DIR}/resumo_por_categoria.csv")


#  EXECUÇÃO PRINCIPAL
if __name__ == "__main__":
    print("Iniciando análise de vendas - E-commerce 2024")
    print("=" * 55)

    df_raw    = gerar_dados()
    df        = limpar_dados(df_raw)
    eda(df)
    gerar_graficos(df)
    gerar_insights(df)
    exportar_resumo(df)

    print("\n\nAnálise concluída com sucesso!")
    print(f"   Gráficos e resumos salvos na pasta /{OUTPUT_DIR}/\n")
