# FP&A Food Delivery Analytics

Projeto completo de **Financial Planning & Analysis (FP&A)** aplicado a um **marketplace de Food Delivery**, com foco em **unit economics, P&L gerencial e suporte à decisão estratégica**.

Este projeto simula uma operação realista de food delivery, integrando **dados operacionais e financeiros** para análise de performance, eficiência e crescimento.

---

## Objetivo do Projeto

Demonstrar, na prática, como um analista de FP&A:
- estrutura dados financeiros e operacionais
- conecta KPIs de negócio ao P&L
- analisa margens, custos e drivers de performance
- gera insights acionáveis para tomada de decisão

---

## Contexto de Negócio

O modelo representa uma empresa de **Food Delivery / Marketplace**, onde:
- clientes realizam pedidos em restaurantes parceiros
- a plataforma monetiza via **comissão** e **taxa de entrega**
- existem **custos variáveis** (logística, subsídios, meios de pagamento)
- e **custos fixos** (tech, marketing, G&A)

O foco do FP&A é entender:
- onde a operação gera (ou destrói) margem
- como escalar mantendo eficiência financeira
- impacto de decisões como subsídio, comissão e crescimento de volume

---

## Estrutura do Banco de Dados

Modelo **estrela**, com 5 tabelas:

| Tabela | Descrição |
|------|----------|
| `orders` | Pedidos (fato principal) |
| `customers` | Dimensão de clientes |
| `restaurants` | Dimensão de restaurantes |
| `cities` | Dimensão geográfica e custo logístico |
| `fixed_costs` | Custos fixos mensais |

### Volume de Dados
- **100.000 pedidos**
- **30.000 clientes**
- **200 restaurantes**
- **5 cidades**
- **3 meses de custos fixos**

---

## Principais Métricas (KPIs)

### Operacionais
- Pedidos
- GMV
- Ticket médio
- Pedidos por cliente
- Pedidos por restaurante

### Financeiros
- Receita de comissão
- Receita total
- Custo variável por pedido
- Margem de contribuição
- Margem por pedido
- EBITDA

### Unit Economics
- Receita por pedido
- Custo por pedido
- Subsídio médio
- Margem por cidade

---

## Estrutura do P&L Gerencial

**Receita**
- Comissão
- Taxa de entrega

**(-) Custos Variáveis**
- Logística
- Subsídios
- Taxas de pagamento

**= Margem de Contribuição**

**(-) Custos Fixos**
- Tecnologia
- Marketing
- G&A

**= EBITDA**

---

## Stack Utilizada

- **Python** – geração de dados sintéticos, simulações e análises
- **PostgreSQL** – modelagem e consultas SQL
- **SQL** – KPIs, P&L e análises financeiras
- **Power BI** – visualização e storytelling executivo
- **Excel** – apoio a budget, forecast e análises pontuais

