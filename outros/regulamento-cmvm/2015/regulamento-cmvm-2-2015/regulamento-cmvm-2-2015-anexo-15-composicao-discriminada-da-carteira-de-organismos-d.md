---
id: "regulamento-cmvm-2-2015-anexo-15-composicao-discriminada-da-carteira-de-organismos-d"
dre_id: "69828456"
title: "Regulamento da CMVM n.º 2/2015, de 17 de julho — Anexo 15 — Composição discriminada da carteira de organismos de investimento imobiliário…"
type: "Regulamento da CMVM"
number: "2/2015"
year: 2015
date: 2015-07-17
issuer: "Comissão do Mercado de Valores Mobiliários"
status: "em vigor"
text_version: "consolidado"
last_amended: 2020-12-16
source: "https://diariodarepublica.pt/dr/legislacao-consolidada/regulamento-cmvm/2015-216598464"
original_pdf: "https://files.diariodarepublica.pt/2s/2015/07/138000000/1926819314.pdf"
retrieved: 2026-10-21
summary: "Regulamento da CMVM n.º 2/2015 - Organismos de Investimento Coletivo (Mobiliários e Imobiliários) e Comercialização de Fundos de Pensões Abertos de Adesão Individual (Revoga os Regulamentos da CMVM n.os 8/2002 e 5/2013)"
legal_notice: "Texto consolidado sem valor legal. Confirma no Diário da República antes de o usares. Não substitui aconselhamento jurídico."
part_of: "regulamento-cmvm-2-2015"
part: "Anexo 15 — Composição discriminada da carteira de organismos de investimento imobiliário…"
---

# Regulamento da CMVM n.º 2/2015, de 17 de julho — Anexo 15 — Composição discriminada da carteira de organismos de investimento imobiliário…

## Anexo 15 — Composição discriminada da carteira de organismos de investimento imobiliário

Composição discriminada da carteira de organismos de investimento imobiliário

O presente Anexo é preenchido nos termos do Regulamento da CMVM n.º 3/2016.

Quanto ao nome do ficheiro:

(ver documento original)

Quanto à estrutura e conteúdo do ficheiro de dados:

As especificações técnicas relativas ao ficheiro "CFI" a enviar à CMVM constam do documento "2020_reporte_CFI_schemas.zip" ou em versões atualizadas do mesmo, disponível no sítio da internet da CMVM.

Opção de reporte com conteúdo

No conteúdo a reportar o elemento ConteudoReporte do cabeçalho deve conter a indicação "REPO" e o elemento identificador de reporte nulo do corpo do ficheiro não deve ser preenchido, sendo preenchidos os restantes elementos do corpo do ficheiro de acordo com as instruções infra.

Bloco de informação n.º 1: Informação sobre os imóveis da carteira, com os seguintes campos:

Código de categoria (Campo 1): Campo que identifica o código de categoria do elemento patrimonial, sendo preenchido de acordo com o código de categoria da tabela 1.

País do imóvel (Campo 2): É preenchido com a identificação do país do imóvel.

Código do imóvel (Campo 3): Campo que identifica o código do imóvel que integra a carteira sob gestão, sendo preenchido com:

Imóvel sito em Portugal ou direitos sobre esse imóvel: Caso o campo "país do imóvel" seja preenchido com o código "PT", é preenchido com o código que corresponde à sua identificação matricial, tendo por base a seguinte estrutura: XXXXXX.T.YYYYYY.ZZZZZZZZ.AAA, em que:

'XXXXXX' identifica o código da freguesia;

'T' identifica o tipo de prédio preenchido com as constantes 'U', 'R' ou 'O', consoante se trate de prédio urbano, prédio rústico ou prédio omisso;

'YYYYYY' identifica o número do artigo;

'ZZZZZZZZ' identifica a fração ou secção de cada prédio, não podendo ser identificada mais do que uma fração ou secção mesmo que respeitem ao mesmo artigo matricial; e

'AAA' identifica, exclusivamente para prédios rústicos, a árvore/colónia. É preenchido caso os referidos elementos façam parte da identificação matricial.

Imóvel sito fora de Portugal ou direitos sobre esse imóvel: Caso o campo "país do ativo" seja preenchido com o código diferente de "PT", é preenchido com o código que corresponde ao seu registo no país da sua localização.

Descrição do imóvel (Campo 4): Campo que identifica a designação do imóvel, contendo a respetiva natureza e a denominação de acordo com o disposto no n.º 4 do artigo 78.º do Regulamento da CMVM n.º 2/2015, na sua versão atualizada, atendendo, em particular, ao regime de propriedade horizontal.

Código do conjunto imobiliário (Campo 5): Campo que identifica o código do conjunto dos imóveis que integram a carteira sob gestão, sendo preenchido com:

Conjunto de imóveis sitos em Portugal ou direitos sobre esse imóvel: Caso o campo "país do ativo" seja preenchido com o código "PT", é preenchido com o código que corresponde à sua identificação matricial, tendo por base a seguinte estrutura: XXXXXX.T.YYYYYY, em que:

'XXXXXX' identifica o código da freguesia;

'T' identifica o tipo de prédio preenchido com as constantes 'U', 'R' ou 'O', consoante se trate de prédio urbano, prédio rústico ou prédio omisso;

'YYYYYY' identifica o número do artigo;

Conjunto de imóveis sitos fora de Portugal ou direitos sobre esse imóvel: Caso o campo "país do ativo" seja preenchido com o código diferente de "PT", é preenchido com o código que corresponde ao seu registo no país da sua localização.

Município (Campo 6): Campo que identifica o município onde se localiza o imóvel.

Descrição do conjunto imobiliário (Campo 7): Campo que identifica a designação do conjunto imobiliário ou empreendimento em que o imóvel se encontre integrado.

Utilização (Campo 8): Campo que identifica a utilização dada ao imóvel sendo que deve ser preenchido com os códigos:

"H", habitação;

"C", comércio;

"T", turístico, incluindo hotelaria;

"S", serviços;

"I", industrial;

"L", logística; ou

"O", outros.

No que respeito aos terrenos é preenchido com os códigos:

"A", arrendados;

"N", não arrendados;

"FA", florestais arrendados;

"FN", florestais não arrendados.

No que respeito aos direitos é preenchido com os códigos:

"DA", direitos de arrendamento;

"DC", direitos de concessão;

"DE", direitos de exploração;

"DS", direitos de superfície; e

"OD", outros direitos.

Informação sobre o imóvel (Campo 9): Campo que identifica a informação sobre o imóvel e que deve ser preenchido com os códigos:

"H", hipoteca;

"P", penhora;

"A", arresto;

"S", servidões;

"C", comodato;

"CR", consignação de rendimentos;

"DR", direitos de retenção;

"DU", direitos de usufruto;

"DS", direito de superfície; ou

"O", outros/não aplicável.

Caso o imóvel possua mais que um dos ónus ou encargos referidos, deverão ser todos reportados.

Área (Campo 10): Campo que identifica a área bruta do imóvel, em metros quadrados, relevante para efeitos da respetiva avaliação.

Valor da renda (Campo 11): Campo que identifica a renda bruta mensal contratada, em euros, no caso do imóvel se encontrar arrendado.

Data de aquisição (Campo 12): Campo que identifica a data em que foi adquirido o ativo.

Preço de aquisição (Campo 13): Campo que identifica o preço de aquisição, incluindo os custos decorrentes da aquisição e encargos relativos a obras de beneficiação do imóvel.

Data I (Campo 14): Campo que identifica a data relativa ao valor de avaliação I.

Avaliador I (Campo 15): Campo que identifica o número de registo na CMVM do perito responsável pela avaliação I.

Valor da avaliação I (Campo 16): Campo que identifica o valor em euros da menor das avaliações legalmente exigidas.

Data II (Campo 17): Campo que identifica a data relativa ao valor de avaliação II.

Avaliador II (Campo 18): Campo que identifica o número de registo na CMVM do perito responsável pela avaliação II.

Valor da avaliação II (Campo 19): Campo que identifica o valor em euros da maior das avaliações legalmente exigidas.

Data III (Campo 20): Campo que identifica:

A data relativa ao valor da avaliação III, se aplicável;

"NA", caso não aplicável.

Avaliador III (Campo 21): Campo que identifica:

O número de registo na CMVM do perito avaliador responsável pela avaliação III, se aplicável;

"NA", caso não aplicável.

Valor da avaliação III (Campo 22): Campo que identifica:

O valor da terceira avaliação legalmente exigida, se aplicável;

"NA", caso não aplicável.

Código da moeda (Campo 23): Campo que identifica o código da moeda em que o valor originariamente se encontra expresso, sendo preenchido nos termos da norma ISO 4217.

Montante total (Campo 24): Campo que identifica o valor do imóvel na carteira, em euros.

Montante total na moeda de referência da carteira (Campo 25): Campo que identifica o valor total do imóvel na carteira, na moeda de referência da carteira (apenas no caso de ser diferente do euro).

(ver documento original)

TABELA 1

Códigos de categoria dos ativos em carteira nos OII

(ver documento original)

Bloco de informação n.º 2: Informação sobre participações na carteira, com os seguintes campos:

Código de categoria (Campo 1): Campo que identifica o código de categoria do elemento patrimonial, sendo preenchido de acordo com o código de categoria da tabela 2.

Código do ativo (Campo 2): Campo que identifica o código do ativo que integra a carteira sob gestão, sendo preenchido com:

O International Standard Identification Number (ISIN), nos termos definidos na Norma ISO 6166, sempre que aplicável;

O Classification of Financial Instruments (CFI), nos termos definidos na Norma ISO 10962, sempre que não exista ISIN;

"NA" caso não existam ISIN e CFI.

Código da entidade (Campo 3): Campo que identifica o código LEI, em relação à entidade responsável pela gestão do organismo de investimento coletivo, à sociedade imobiliária, ao emitente ou à contraparte, caso aplicável.

Descrição da entidade (Campo 4): Campo que identifica a denominação da entidade responsável pela gestão do organismo de investimento coletivo, da sociedade imobiliária, do emitente ou o nome ou denominação da contraparte, consoante o caso, e caso aplicável.

País da entidade (Campo 5): Campo que identifica o país da entidade responsável pela gestão do organismo de investimento coletivo, da sociedade imobiliária, do emitente ou da contraparte, caso aplicável.

Grupo (Campo 6): Campo que é preenchido, quando aplicável, com as constantes "S" e "N", consoante o ativo ou passivo seja ou não:

Emitido ou garantido por entidades previstas nas alíneas a) a h) do artigo 147.º do RGOIC;

Emitido por organismo de investimento coletivo gerido pela entidade responsável pela gestão do organismo objeto de reporte ou gerido por entidade que com ela se encontre em relação de grupo para efeitos de consolidação de contas, na aceção referida no n.º 13 do artigo 176.º do RGOIC; ou

Emitido por entidade em relação de grupo para efeitos de consolidação de contas, na aceção referida no n.º 13.º do artigo 176.º do RGOIC, com outro emitente de outro ativo em carteira.

Entidade de grupo (Campo 7): Campo que é preenchido, no caso do campo "Grupo" ser igual a "S", do seguinte modo:

Estando em causa a situação prevista na alínea a) do campo "Grupo", é inserida a abreviatura "SG", "DP" ou "OUT" consoante a entidade que tenha emitido esteja relacionada com a entidade responsável pela gestão, com o depositário ou com outra entidade, respetivamente. No caso de a entidade ser enquadrável em mais do que uma opção deverá ser utilizada a abreviatura "SG" em detrimento de "DP" e "OUT" ou "DP" em detrimento de "OUT".

Estando em causa a situação prevista na alínea b) do campo "Grupo", é inserida a abreviatura "OIC"; ou;

Estando em causa a situação prevista na alínea c) do campo "Grupo", é inserido o código de identificação do ativo, utilizando para o efeito a abreviatura "G" seguida de um número sequencial (com início em "00001" para o primeiro grupo até "nnnnn" para o grupo "n"), que se estabeleça uma relação historicamente inequívoca e constante com o grupo. Esta identificação deverá ser igual para todo os fundos geridos por uma entidade responsável pela gestão.

Percentagem adquirida (Campo 8): Campo que é preenchido com a percentagem do capital social da sociedade imobiliária detido em carteira.

Método de avaliação (Campo 9): Campo que identifica o critério adotado na valorização de participações em sociedades imobiliárias, sendo preenchido com:

"D", fluxos de caixa descontados;

"M", múltiplos;

"T", transações; ou

"C", custo.

Tipo de outros valores (Campo 10): Campo que identifica no caso de organismos de investimento imobiliário sob a forma societária autogerida, sendo preenchido com:

"I", caso respeite a outros valores ativos e passivos relativos à carteira de investimento;

"N", caso respeite a outros valores necessários ao desenvolvimento da atividade do organismo.

Quantidade do ativo (Campo 11): Campo que identifica a quantidade do ativo em carteira.

Preço do ativo (Campo 12): Campo que é preenchido com o valor unitário do ativo em carteira na moeda em que foi adquirido.

Código da moeda (Campo 13): Campo que identifica o código da moeda em que o valor originariamente se encontra expresso, sendo preenchido nos termos da norma ISO 4217.

Montante total (Campo 14): Campo que identifica o valor total do ativo em carteira, em euros.

Montante total na moeda de referência da carteira (Campo 15): Campo que identifica o valor total do ativo na carteira, na moeda de referência da carteira (apenas no caso de ser diferente do euro).

(ver documento original)

TABELA 2

Códigos de categoria de participações em carteira nos OII

(ver documento original)

Bloco de informação n.º 3: Informação sobre outros ativos e passivos na carteira, com os seguintes campos:

Código de categoria (Campo 1): Campo que identifica o código de categoria dos ativos e passivos, sendo preenchido com o código da tabela 3.

Descrição do ativo (Campo 2): Campo que identifica a designação do ativo ou passivo.

País do emitente ou da contraparte (Campo 3): Campo que identifica, se aplicável, o país do emitente ou contraparte.

Código do emitente (Campo 4): Campo que identifica, se aplicável, o código LEI relativo ao emitente ou contraparte.

Descrição do emitente ou da contraparte (Campo 5): Campo que identifica, se aplicável, o nome ou denominação do emitente ou contraparte.

Data de emissão (Campo 6): Campo que identifica a data de emissão ou constituição do ativo ou passivo, se aplicável.

Data de maturidade (Campo 7): Campo que identifica a data na qual o valor ativo ou passivo se vence, se aplicável.

Grupo (Campo 8): Campo que é preenchido com "S" ou "N", consoante o ativo ou o passivo seja ou não:

a) Emitido ou garantido por entidade previstas nas alíneas a) a h) do artigo 147.º do RGOIC;

b) Emitido por organismo de investimento coletivo gerido pela entidade responsável pela gestão do organismo objeto de reporte ou gerido por entidade que com ela se encontre em relação de grupo para efeitos de consolidação de contas, na aceção referida no n.º 13 do artigo 176.º do RGOIC; ou

c) Emitido por entidade em relação de grupo para efeitos de consolidação de contas, na aceção referida no n.º 13 do artigo 176.º do RGOIC, com outro emitente de outro ativo em carteira.

Entidade de grupo (Campo 9): Campo que é preenchido caso o campo "Grupo" ser igual a "S", do seguinte modo:

Estando em causa situação prevista na alínea a) do campo "Grupo", é inserida a abreviatura "SG", "DP" ou "OUT" consoante a entidade que tenha emitido ou garantido o ativo ou passivo esteja relacionada com a entidade responsável pela gestão, com o depositário ou com outra entidade, respetivamente. No caso de a entidade ser enquadrável em mais do que uma opção deverá ser utilizada a abreviatura "SG" em detrimento de "DP" e "OUT" ou "DP" em detrimento de "OUT".

Estando em causa a situação prevista na alínea b) do campo "Grupo", é inserida a abreviatura "OIC", ou

Estando em causa a situação prevista na alínea c) do campo "Grupo", é inserido o código de identificação do ativo, utilizando para o efeito a abreviatura "G" seguida de um número sequencial (com início em "00001" para o primeiro grupo até "nnnnn" para o grupo "n"), que estabeleça uma relação historicamente inequívoca e constante com o grupo. Esta identificação deverá ser igual para todos os fundos geridos por uma entidade responsável pela gestão.

Tipo de outros valores (Campo 10): Campo que identifica no caso de organismos de investimento coletivo em valores mobiliários, de organismos de investimento alternativo em valores mobiliários e de organismo de investimento em ativos não financeiros, sob a forma societária autogerida, sendo preenchido com:

"I", caso respeite a outros valores ativos e passivos relativos à carteira de investimento;

"N", caso respeite a outros valores necessários ao desenvolvimento da atividade do organismo.

Código da moeda (Campo 11): Campo que identifica a moeda em que o ativo ou passivo originariamente se encontra expresso, sendo preenchido nos termos da norma ISO 4217.

Montante total (Campo 12): Campo que identifica o valor total do ativo ou passivo na carteira, em euros.

Montante total na moeda de referência da carteira (Campo 13): Campo que identifica o valor total do ativo ou passivo na carteira, na moeda de referência da carteira (apenas no caso de ser diferente do euro).

(ver documento original)

TABELA 3

Códigos de categoria dos outros ativos e passivos dos OII

(ver documento original)

Bloco de informação n.º 4: Informação adicional sobre a carteira, com os seguintes campos:

Código da moeda de referência da carteira (Campo 1): Campo que identifica a moeda de referência da carteira, sendo preenchido nos termos da norma ISO 4217 (apenas no caso de ser diferente do euro).

Valor líquido global (Campo 2): Campo que identifica o valor líquido global do OII em euros.

N.º Unidades de participação total (Campo 3): Campo que identifica o total de unidades de participação em circulação dos OII.

Valor líquido global na moeda de referência da carteira (Campo 4): Campo que identifica o valor líquido global do OII, na moeda de referência da carteira (apenas no caso de ser diferente do euro).

Ativo sob gestão (Campo 5): Campo que identifica o ativo sob gestão (AUM) para o OII, em euros, sendo calculado nos termos definidos no Regulamento Delegado (EU) n.º 231/2013 da Comissão de 19 de dezembro de 2012.

Ativo sob gestão na moeda de referência da carteira (Campo 6): Campo que identifica o ativo sob gestão (AUM) para os OII, na moeda de referência da carteira (apenas no caso de ser diferente do euro), sendo calculado nos termos definidos no Regulamento Delegado (EU) n.º 231/2013 da Comissão de 19 de dezembro de 2012.

Ativos líquidos (Campo 7): Campo que identifica o valor total de ativos líquidos do OII, em euros.

Ativos líquidos na moeda de referência da carteira (Campo 8): Campo que identifica o valor total de ativos líquidos do OII, na moeda de referência da carteira (apenas no caso de ser diferente do euro).

Valor de posições equivalentes nos ativos subjacentes relativamente a instrumentos financeiros derivados detidos (Campo 9): Campo que identifica o valor das posições equivalentes nos ativos subjacentes a instrumentos financeiros derivados detidos, em euros.

Valor de posições equivalentes nos ativos subjacentes relativamente a instrumentos financeiros derivados detidos na moeda de referência da carteira (Campo 10): Campo que identifica o valor das posições equivalentes nos ativos subjacentes a instrumentos financeiros derivados detidos, na moeda de referência da carteira (apenas no caso de ser diferente do euro).

Valor do investimento noutros OIC geridos pela entidade responsável pela gestão (Campo 11): Campo que identifica o valor do investimento noutros OIC detidos pela entidade responsável pela gestão, em euros.

Valor do investimento noutros OIC geridos pela entidade responsável pela gestão na moeda de referência da carteira (Campo 12): Campo que identifica o valor do investimento noutros OIC detidos pela entidade responsável pela gestão, na moeda de referência da carteira (apenas no caso de ser diferente do euro).

(ver documento original)

Bloco de informação n.º 5: Informação sobre as unidades de participação, com os seguintes campos:

Categoria de unidades de participação (Campo 1): Campo de preenchimento obrigatório que identifica as diferentes categorias de unidades de participação, sendo preenchido com:

"C", seguido de 1 ou 2 carateres, que correspondem à identificação da categoria nos documentos constitutivos;

"NA", sempre que não existam categorias de unidades de participação.

N.º Unidades de participação por categoria (Campo 2): Campo que identifica o n.º de unidades de participação por categoria de unidades de participação existente.

Pré-aviso de resgate (Campo 3): Campo que identifica o pré-aviso de resgate em número dias para cada categoria de unidades de participação existente.

(ver documento original)

Bloco de informação n.º 6: Informação sobre as responsabilidades extrapatrimoniais, com os seguintes campos:

Código de categoria (Campo 1): Campo que identifica o código de categoria do elemento extrapatrimonial, sendo preenchido com o código da tabela 4.

Descrição do ativo (Campo 2): Campo que identifica a designação da responsabilidade extrapatrimonial.

País do emitente ou da contraparte (Campo 3): Campo que identifica o país do emitente ou contraparte.

Código do emitente (Campo 4): Campo que identifica o emitente ou contraparte sendo preenchido com o:

O código LEI, quando aplicável:

"NA", quando não aplicável.

Montante total (Campo 5): Campo que identifica o montante total da responsabilidade extrapatrimonial incluindo juros decorridos, em euros.

Montante total na moeda de referência da carteira (Campo 6): Campo que identifica o valor total da responsabilidade extrapatrimonial, na moeda de referência da carteira (apenas no caso de ser diferente do euro).

(ver documento original)

TABELA 4

Códigos de categoria das responsabilidades extrapatrimoniais do OII

(ver documento original)

- *Aditado pelo/a Artigo 3.º do/a [Regulamento da CMVM n.º 6/2020 - Diário da República n.º 243/2020, Série II de 2020-12-16](https://diariodarepublica.pt/dr/detalhe/regulamento-cmvm/6-2020-151322794), em vigor a partir de 2021-07-01*

## Anexo 16 — Valor das unidades de participação de organismos de investimento coletivo

O presente Anexo é preenchido nos termos do Regulamento da CMVM n.º 3/2016.

Quanto ao nome do ficheiro:

(ver documento original)

Quanto à estrutura e conteúdo do ficheiro de dados:

As especificações técnicas relativas ao ficheiro "VUP" a enviar à CMVM constam do documento "2020_reporte_VUP_schemas.zip" ou em versões atualizadas do mesmo, disponível no sítio da internet da CMVM.

Opção de reporte com conteúdo

No conteúdo a reportar o elemento ConteudoReporte do cabeçalho deve conter a indicação "REPO" e o elemento identificador de reporte nulo do corpo do ficheiro não deve ser preenchido, sendo preenchidos os restantes elementos do corpo do ficheiro de acordo com as instruções infra.

Código do OIC (Campo 1): Campo que identifica o código do OIC e com o código do compartimento patrimonial autónomo, ambos atribuídos pela CMVM. Caso o organismo de investimento coletivo não integre compartimentos patrimoniais autónomos a componente do compartimento patrimonial é preenchida com '0000'.

Categoria de unidades de participação (Campo 2): Campo de preenchimento obrigatório que identifica as diferentes categorias de unidades de participação, sendo preenchido com:

"C", seguido de 1 ou 2 carateres, que correspondem à identificação da categoria nos documentos constitutivos;

"NA", sempre que não existam categorias de unidades de participação.

Código da moeda de comercialização (Campo 3): Campo que identifica o código da moeda em que as unidades de participação são comercializadas.

Valor da unidade de participação (Campo 4): Campo que identifica o valor da unidade de participação respeitante à data do ficheiro.

Rendimento distribuído por unidade de participação (Campo 5): Campo que identifica o valor do rendimento distribuído por unidade de participação respeitante à data da carteira utilizada para o cálculo do valor da unidade de participação.

Valor de amortização de capital por unidade de participação (Campo 6): Campo que identifica o valor da amortização de capital por unidade de participação respeitante nas reduções de capital em que não haja reembolso de unidades de participação na data da carteira utilizada para o cálculo do valor da unidade de participação.

(ver documento original)

- *Aditado pelo/a Artigo 3.º do/a [Regulamento da CMVM n.º 6/2020 - Diário da República n.º 243/2020, Série II de 2020-12-16](https://diariodarepublica.pt/dr/detalhe/regulamento-cmvm/6-2020-151322794), em vigor a partir de 2021-07-01*

## Anexo 17 — Documentos constitutivos e outra informação relevante sobre organismos de investimento coletivo

I - Especificidades relativas ao reporte do prospeto

O presente Anexo é preenchido nos termos do Regulamento da CMVM n.º 3/2016.

Quanto ao nome do ficheiro:

(ver documento original)

II - Especificidades relativas ao reporte de informações fundamentais destinadas aos investidores

O presente Anexo é preenchido nos termos do Regulamento da CMVM n.º 3/2016.

Quanto ao nome do ficheiro:

(ver documento original)

III - Especificidades relativas ao reporte do prospeto de oferta pública de distribuição

O presente Anexo é preenchido nos termos do Regulamento da CMVM n.º 3/2016.

Quanto ao nome do ficheiro:

(ver documento original)

IV - Especificidades relativas ao reporte do regulamento de gestão

O presente Anexo é preenchido nos termos do Regulamento da CMVM n.º 3/2016.

Quanto ao nome do ficheiro:

(ver documento original)

V - Especificidades relativas ao reporte do documento informativo

O presente Anexo é preenchido nos termos do Regulamento da CMVM n.º 3/2016.

Quanto ao nome do ficheiro:

(ver documento original)

VI - Especificidades relativas ao reporte de informação relevante

O presente Anexo é preenchido nos termos do Regulamento da CMVM n.º 3/2016.

Quanto ao nome do ficheiro:

(ver documento original)

A - Tabela que identifica a listagem de informação relevante

ZZ - Tipo de Informação objeto de anúncio;

01 - Constituição do OIC;

02 - Alteração da denominação do OIC;

03 - Alteração da Entidade Gestora;

04 - Alteração da Entidade Depositária;

05 - Alteração das Entidades Comercializadoras;

06 - Alteração significativa da política de investimentos;

07 - Alteração da política de distribuição de rendimentos;

08 - Aumento global das comissões de gestão e de depósito;

09 - Outras alterações das comissões;

10 - Aumento de capital;

11 - Redução de capital;

12 - Distribuição de rendimentos;

13 - Erro de valorização;

14 - Disponibilização do Relatório Anual;

15 - Disponibilização do Relatório Semestral;

17 - Anúncio de lançamento de oferta pública de distribuição;

18 - Adenda ao prospeto de oferta pública;

19 - Admissão à negociação;

20 - Fusão;

21 - Transformação;

22 - Liquidação e Extinção;

23 - Prorrogação da duração;

24 - Prorrogação do prazo de liquidação;

25 - Convocatória de Assembleia Geral;

26 - Outros factos relevantes;

28 - Alteração do Auditor do OIC;

29 - Outras alterações da política de investimentos;

30 - Alteração do prazo de cálculo ou de divulgação do valor das unidades de participação;

31 - Cisão;

32 - Factos com impacto no normal funcionamento da atividade do OIC ou dos seus ativos.

- *Aditado pelo/a Artigo 3.º do/a [Regulamento da CMVM n.º 6/2020 - Diário da República n.º 243/2020, Série II de 2020-12-16](https://diariodarepublica.pt/dr/detalhe/regulamento-cmvm/6-2020-151322794), em vigor a partir de 2021-07-01*

## Anexo 18 — Relatórios específicos no âmbito da atividade de gestão de organismos de investimento coletivo

I - Especificidades relativas ao reporte das memórias da evolução do processo de liquidação dos OII a que alude o artigo 43.º n.º 2, alínea b) do RGOIC

O presente Anexo é preenchido nos termos do Regulamento da CMVM n.º 3/2016.

Quanto ao nome do ficheiro:

(ver documento original)

II - Especificidades relativas ao reporte de ponto de situação e memória descritiva das diligências

efetuadas a que alude o artigo 43.º n.º 10, alínea f), ponto iii) do RGOIC

O presente Anexo é preenchido nos termos do Regulamento da CMVM n.º 3/2016.

Quanto ao nome do ficheiro:

(ver documento original)

III - Especificidades relativas ao reporte das operações vedadas a que alude o artigo 147.º n.º 5 do RGOIC

O presente Anexo é preenchido nos termos do Regulamento da CMVM n.º 3/2016.

Quanto ao nome do ficheiro:

(ver documento original)

IV - Especificidades relativas ao reporte dos pareceres quando as avaliações dos OIAnF apresentem valores que divirjam entre si, mais de 20 % a que alude o artigo 33.º, n.º 2 alínea c) do Regulamento da CMVM n.º 2/2015

O presente Anexo é preenchido nos termos do Regulamento da CMVM n.º 3/2016.

Quanto ao nome do ficheiro:

(ver documento original)

- *Aditado pelo/a Artigo 3.º do/a [Regulamento da CMVM n.º 6/2020 - Diário da República n.º 243/2020, Série II de 2020-12-16](https://diariodarepublica.pt/dr/detalhe/regulamento-cmvm/6-2020-151322794), em vigor a partir de 2021-07-01*

## Anexo 19 — Riscos e encargos de organismos de investimento coletivo

O presente Anexo é preenchido nos termos do Regulamento da CMVM n.º 3/2016.

I - Especificidades relativas ao value at risk dos organismos de investimento coletivo VAR

Quanto ao nome do ficheiro:

(ver documento original)

Quanto à estrutura e conteúdo do ficheiro de dados:

As especificações técnicas relativas ao ficheiro "VAR" a enviar à CMVM constam do documento "2020_reporte_VAR_schemas.zip" ou em versões atualizadas do mesmo, disponível no sítio da internet da CMVM.

Opção de reporte com conteúdo

No conteúdo a reportar o elemento ConteudoReporte do cabeçalho deve conter a indicação "REPO" e o elemento identificador de reporte nulo do corpo do ficheiro não deve ser preenchido, sendo preenchidos os restantes elementos do corpo do ficheiro de acordo com as instruções infra.

Código do OIC (Campo 1): Campo que identifica o código de OIC e o código do compartimento patrimonial autónomo, ambos atribuídos pela CMVM. No caso de organismo de investimento coletivo que não integre compartimentos patrimoniais autónomos, a componente do compartimento patrimonial autónomo é preenchida com '0000'.

Data da carteira (Campo 2): Campo que identifica a data da carteira.

Tipo de simulação (Campo 3): Campo que identifica o tipo de simulação:

"M", simulação monte carlo;

"H", simulação histórica;

"P", VaR paramétrico.

Valor do VAR (Campo 4): Campo que identifica o VaR (absoluto), em euros, com referência ao último dia do mês a que respeita o reporte, tendo por pressuposto um intervalo de confiança de 99 % para um período de 250 dias e assumindo um período de detenção de carteira de investimento em 20 dias. Caso a entidade responsável pela gestão calcule o VaR com pressupostos distintos dos anteriormente assumidos, além do valor apurado naqueles termos, reporta igualmente o VaR com os pressupostos por si assumidos.

Percentagem do VLGF (Campo 5): Campo que identifica o valor, em percentagem, correspondente ao quociente entre o VaR e o valor líquido global do organismo.

Pressupostos do VAR (Campo 6): Campo que identifica a entidade responsável pela gestão reporte do VaR com pressupostos diferentes dos referidos no campo "Valor do VAR", com os pressupostos assumidos separados pelo caráter "-", seguindo a seguinte ordem: intervalo de confiança, período de detenção da carteira de investimento (em dias).

(ver documento original)

II - Especificidades relativas à rotação média da carteira e indicador sintético de risco e remuneração

Quanto ao nome do ficheiro:

(ver documento original)

Quanto à estrutura e conteúdo do ficheiro de dados:

As especificações técnicas relativas ao ficheiro "TGC" a enviar à CMVM constam do documento "2020_reporte_TGC_schemas.zip" ou em versões atualizadas do mesmo, disponível no sítio da internet da CMVM.

Opção de reporte com conteúdo

No conteúdo a reportar o elemento ConteudoReporte do cabeçalho deve conter a indicação "REPO" e o elemento identificador de reporte nulo do corpo do ficheiro não deve ser preenchido, sendo preenchidos os restantes elementos do corpo do ficheiro de acordo com as instruções infra.

Código do OIC (Campo 1): Campo que identifica o código de OIC e com o código do compartimento patrimonial autónomo, ambos atribuídos pela CMVM. No caso de organismo de investimento coletivo que não integre compartimentos patrimoniais autónomos, a componente do compartimento patrimonial autónomo é preenchida com '0000'.

Rotação média da carteira (Campo 2): Campo que identifica o valor em percentagem da rotação média da carteira respeitante ao ano civil anterior.

Categoria de unidades de participação (Campo 3): Campo de preenchimento obrigatório que identifica as diferentes categorias de unidades de participação, sendo preenchido com:

"C", seguido de 1 ou 2 carateres, que correspondem à identificação da categoria nos documentos constitutivos;

"NA", sempre que não existam categorias de unidades de participação.

Indicador sintético de risco e de remuneração (Campo 4): Campo que identifica o valor em percentagem da volatilidade subjacente ao indicador sintético de risco e de remuneração em vigor.

(ver documento original)

III - Especificidades relativas aos erros ocorridos no cálculo e divulgação do valor da unidade de participação ERR

O presente Anexo é preenchido nos termos do Regulamento da CMVM n.º 3/2016.

Quanto ao nome do ficheiro:

(ver documento original)

Quanto à estrutura e conteúdo do ficheiro de dados:

As especificações técnicas relativas ao ficheiro "ERR" a enviar à CMVM constam do documento "2020_reporte_ERR_schemas.zip" ou em versões atualizadas do mesmo, disponível no sítio da internet da CMVM.

Opção de reporte com conteúdo

No conteúdo a reportar o elemento ConteudoReporte do cabeçalho deve conter a indicação "REPO" e o elemento identificador de reporte nulo do corpo do ficheiro não deve ser preenchido, sendo preenchidos os restantes elementos do corpo do ficheiro de acordo com as instruções infra.

Bloco de informação n.º 1: Informação sobre o erro no valor da unidade de participação, com os seguintes campos:

Data (Campo 1): Campo que identifica a data a que respeita o valor da unidade de participação.

Valor correto (Campo 2): Campo que identifica o valor correto da unidade de participação.

Valor utilizado (Campo 3): Campo que identifica o valor utilizado da unidade de participação.

Diferença do valor da unidade de participação (Campo 4): Campo que identifica a diferença entre o valor correto e o valor utilizado.

Percentagem da diferença no valor da unidade de participação (Campo 5): Campo que identifica o quociente entre a diferença apurada no campo de informação anterior e o valor utilizado.

Operações (Campo 6): Campo que identifica o código de tipo de operação e deve ser preenchido com os códigos:

"S", caso a operação se trate de subscrição de OIC;

"R", caso a operação se trate de resgate de OIC.

Número de operações (Campo 7): Campo que identifica o número de operações de subscrição ou de resgate realizadas.

Categoria de unidades de participação (Campo 8): Campo de preenchimento obrigatório que identifica as diferentes categorias de unidades de participação, sendo preenchido com:

"C", seguido de 1 ou 2 carateres, que correspondem à identificação da categoria nos documentos constitutivos;

"NA", sempre que não existam categorias de unidades de participação.

Quantidade (Campo 9): Campo que identifica o número de unidades de participação.

Valor apurado (Campo 10): Campo que identifica a diferença total considerando a discrepância entre o valor correto e o valor utilizado.

(ver documento original)

Bloco de informação n.º 2: Informação sobre o ressarcimento, com os seguintes campos:

Entidade (Campo 1): Campo que identifica a entidade em função do código de tipo de ressarcimento e deve ser preenchido com os códigos:

"O", caso a informação respeite ao ressarcimento do OIC;

"P", caso a informação respeite ao ressarcimento dos participantes.

Data (Campo 2): Campo que identifica a data do crédito em conta do organismo de investimento coletivo ou a data do último pagamento para efeitos de conclusão do ressarcimento aos participantes.

Montante (Campo 3): Campo que identifica o valor pago, em euros.

Tipo de operação (Campo 4): Caso o campo "Entidade" seja preenchido com a constante "P", é preenchido com o código de tipo de operação:

"S", caso se trate de subscrições de organismos de investimento coletivo;

"R", caso se trate de resgates de organismos de investimento coletivo.

Número de participantes (Campo 5): Caso o campo "Entidade" seja preenchido com a constante "P", é preenchido com o número de participantes ressarcidos.

(ver documento original)

IV - Especificidades relativas às operações sobre ações ou valores mobiliários que dão direito à sua aquisição e operações sobre unidades de participação

O presente Anexo é preenchido nos termos do Regulamento da CMVM n.º 3/2016.

Quanto ao nome do ficheiro:

(ver documento original)

Quanto à estrutura e conteúdo do ficheiro de dados:

As especificações técnicas relativas ao ficheiro "COP" a enviar à CMVM constam do documento "2020_reporte_COP_schemas.zip" ou em versões atualizadas do mesmo, disponível no sítio da internet da CMVM.

Opção de reporte com conteúdo

No conteúdo a reportar o elemento ConteudoReporte do cabeçalho deve conter a indicação "REPO" e o elemento identificador de reporte nulo do corpo do ficheiro não deve ser preenchido, sendo preenchidos os restantes elementos do corpo do ficheiro de acordo com as instruções infra.

Bloco de informação n.º 1: Informação sobre as operações sobre valores mobiliários, com os seguintes campos:

Tipo de adquirente ou alienante (Campo 1): Campo que identifica o tipo de adquirente e deve ser preenchido com os códigos:

"OA", caso o adquirente ou alienante seja membro do órgão de administração da entidade responsável pela gestão;

"DI", caso o adquirente ou alienante seja responsável pelas decisões de investimento;

"OP", caso seja outra pessoa com relação com membro do órgão de administração ou com o responsável pelas decisões de investimento.

Descrição do adquirente ou alienante (Campo 2): Campo que identifica o nome ou denominação do adquirente ou alienante, sem utilização de abreviaturas.

NIF do adquirente ou alienante (Campo 3): Campo que identifica o número de identificação fiscal do adquirente ou alienante.

Descrição da pessoa de relação (Campo 4): Caso o campo "Tipo de Adquirente ou Alienante" seja preenchido com a abreviatura "OP", é preenchido com o nome da pessoa com a qual o adquirente ou alienante se encontre em relação, sem utilização de abreviaturas.

NIF da pessoa de relação (Campo 5): Caso o campo "Tipo de Adquirente ou Alienante" seja preenchido com a abreviatura "OP", é preenchido com o número de identificação fiscal da pessoa com a qual o adquirente ou alienante se encontre em relação.

Tipo de relação (Campo 6): Caso o campo "Tipo de Adquirente ou Alienante" seja preenchido com a abreviatura "OP", é preenchido com as abreviaturas "OA" ou "DI", consoante a pessoa com a qual o adquirente ou alienante se encontre em relação seja membro do órgão de administração da entidade responsável pela gestão ou responsável pelas decisões de investimento.

Código do Ativo (Campo 7): Campo que identifica o código ISIN do valor mobiliário.

Descrição do Ativo (Campo 8): Campo que identifica a designação do ativo, independentemente da existência de código do ativo.

Operação (Campo 9): Campo que identifica o tipo de operação e deve ser preenchido com os códigos:

"C", caso se trate de uma operação de compra;

"V", caso se trate de uma operação de venda;

"O", caso se trate de outro tipo de operação.

Quantidade (Campo 10): Campo que identifica a quantidade de ativos envolvidos na operação.

Preço (Campo 11): Campo que identifica o preço do ativo ao qual a operação foi concretizada.

Descrição do intermediário financeiro (Campo 12): Campo que identifica a denominação do intermediário financeiro que intermediou a operação, sem utilização de abreviaturas.

(ver documento original)

Bloco de informação n.º 2: Informação sobre a carteira do(s) OIC(s) geridos à data das operações sobre valores mobiliários, com os seguintes campos:

Código do Ativo (Campo 1): Campo que identifica o código ISIN.

Código do OIC (Campo 2): Campo que identifica com o código de OIC e com o código do compartimento patrimonial autónomo, ambos atribuídos pela CMVM. No caso de organismo de investimento coletivo que não integre compartimentos patrimoniais autónomos, a componente do compartimento patrimonial autónomo é preenchida com '0000'.

(ver documento original)

Bloco de informação n.º 3: Informação sobre as transações do(s) OIC(s) geridos à data da operação sobre valores mobiliários, com os seguintes campos:

Código do Ativo (Campo 1): Campo que identifica o código ISIN.

Código do OIC (Campo 2): Campo que identifica com o código de OIC e com o código do compartimento patrimonial autónomo, ambos atribuídos pela CMVM. No caso de organismo de investimento coletivo que não integre compartimentos patrimoniais autónomos, a componente do compartimento patrimonial autónomo é preenchida com '0000'.

Operação (Campo 3): Campo que identifica o tipo de operação e deve ser preenchido com os códigos:

"C", caso se trate de uma operação de compra;

"V", caso se trate de uma operação de venda;

"O", caso se trate de outro tipo de operação.

Quantidade (Campo 4): Campo que identifica a quantidade de ativos envolvidos na operação.

Preço (Campo 5): Campo que identifica o preço do ativo ao qual a operação foi concretizada.

Descrição do intermediário financeiro (Campo 6): Campo que identifica a denominação do intermediário financeiro que intermediou a operação, sem utilização de abreviaturas.

(ver documento original)

Bloco de informação n.º 4: Informação sobre as comunicações de operações sobre unidades de participação realizadas pela entidade responsável pela gestão, com os seguintes campos:

Tipo de adquirente ou alienante (Campo 1): Campo que identifica o tipo de adquirente e deve ser preenchido com os códigos:

"OA", caso o adquirente ou alienante seja membro do órgão de administração da entidade responsável pela gestão;

"DI", caso o adquirente ou alienante seja responsável pelas decisões de investimento;

"OP", caso seja outra pessoa com relação com membro do órgão de administração ou com o responsável pelas decisões de investimento.

Descrição do adquirente ou alienante (Campo 2): Campo que identifica o nome ou denominação do adquirente ou alienante, sem utilização de abreviaturas.

NIF do adquirente ou alienante (Campo 3): Campo que identifica o número de identificação fiscal do adquirente ou alienante.

Descrição da pessoa de relação (Campo 4): Caso o campo "Tipo de Adquirente ou Alienante" seja preenchido com a abreviatura "OP", é preenchido com o nome da pessoa com a qual o adquirente ou alienante se encontre em relação, sem utilização de abreviaturas.

NIF da pessoa de relação (Campo 5): Caso o campo "Tipo de Adquirente ou Alienante" seja preenchido com a abreviatura "OP", é preenchido com o número de identificação fiscal da pessoa com a qual o adquirente ou alienante se encontre em relação.

Tipo de relação (Campo 6): Caso o campo "Tipo de Adquirente ou Alienante" seja preenchido com a abreviatura "OP", é preenchido com as abreviaturas "OA" ou "DI", consoante a pessoa com a qual o adquirente ou alienante se encontre em relação seja membro do órgão de administração da entidade responsável pela gestão ou responsável pelas decisões de investimento.

Código do OIC (Campo 7): Campo que identifica o código de OIC e com o código do compartimento patrimonial autónomo, ambos atribuídos pela CMVM. No caso de organismo de investimento coletivo que não integre compartimentos patrimoniais autónomos, a componente do compartimento patrimonial autónomo é preenchida com '0000'.

Operação (Campo 8): Campo que identifica o tipo de operação e deve ser preenchido com os códigos:

"C", caso se trate de uma operação de compra;

"V", caso se trate de uma operação de venda;

"O", caso se trate de outro tipo de operação.

Quantidade (Campo 9): Campo que identifica a quantidade de ativos envolvidos na operação.

Preço (Campo 10): Campo que identifica o preço do ativo ao qual a operação foi concretizada.

Comissões (Campo 11): Campo que identifica o valor das comissões suportadas.

Percentagem de comissões (Campo 12): Campo que identifica a percentagens de comissões suportadas.

Descrição da entidade comercializadora (Campo 13): Campo que identifica a denominação da entidade comercializadora, sem utilização de abreviaturas. Caso se trate de aquisição ou alienação de unidades de participação admitidas à negociação em mercado, indicar o(s) mercado(s) de realização da operação.

(ver documento original)

- *Aditado pelo/a Artigo 3.º do/a [Regulamento da CMVM n.º 6/2020 - Diário da República n.º 243/2020, Série II de 2020-12-16](https://diariodarepublica.pt/dr/detalhe/regulamento-cmvm/6-2020-151322794), em vigor a partir de 2021-07-01*

## Anexo 20 — Informação financeira relativa ao balanço e demonstração dos resultados de organismos de investimento coletivo

O presente Anexo é preenchido nos termos do Regulamento da CMVM n.º 3/2016.

Quanto ao nome do ficheiro:

(ver documento original)

Quanto à estrutura e conteúdo do ficheiro de dados:

As especificações técnicas relativas ao ficheiro "DEF" a enviar à CMVM constam do documento "2020_reporte_DEF_schemas.zip" ou em versões atualizadas do mesmo, disponível no sítio da internet da CMVM.

Opção de reporte com conteúdo

No conteúdo a reportar o elemento ConteudoReporte do cabeçalho deve conter a indicação "REPO" e o elemento identificador de reporte nulo do corpo do ficheiro não deve ser preenchido, sendo preenchidos os restantes elementos do corpo do ficheiro de acordo com as instruções infra.

Bloco de informação n.º 1: Informação sobre as rubricas de balanço de organismos de investimento coletivo (OIC), com os seguintes campos:

Código de conta (Campo 1): Campo de preenchimento obrigatório que identifica o código de conta, sendo preenchido de acordo com o código de conta da Tabela 1.

Valor de conta (Campo 2): Campo de preenchimento obrigatório que identifica o saldo da conta no final de cada período de reporte, sendo preenchido com um valor positivo para as rubricas de ativo e passivo, e com um valor positivo ou negativo para as rubricas de capital próprio.

(ver documento original)

TABELA 1

Códigos de conta das rubricas de balanço

(ver documento original)

Bloco de informação n.º 2: Informação sobre as rubricas da demonstração dos resultados dos OIC, com os seguintes campos:

Código de conta (Campo 1): Campo de preenchimento obrigatório que identifica o código de conta, sendo preenchido de acordo com o código de conta da Tabela 2.

Valor de conta (Campo 2): Campo de preenchimento obrigatório que identifica o saldo da conta no final de cada período de reporte, sendo preenchido com um valor positivo ou negativo, consoante a rubrica contribua de modo positivo ou negativo para o resultado líquido do exercício.

(ver documento original)

TABELA 2

Códigos de conta das rubricas da demonstração dos resultados

(ver documento original)

- *Aditado pelo/a Artigo 3.º do/a [Regulamento da CMVM n.º 6/2020 - Diário da República n.º 243/2020, Série II de 2020-12-16](https://diariodarepublica.pt/dr/detalhe/regulamento-cmvm/6-2020-151322794), em vigor a partir de 2021-07-01*

## Anexo 21 — Informação relativa aos documentos de prestação de contas semestrais e anuais dos organismos de investimento coletivo

O presente Anexo é preenchido nos termos do Regulamento da CMVM n.º 3/2016.

Quanto ao nome do ficheiro:

(ver documento original)

- *Aditado pelo/a Artigo 3.º do/a [Regulamento da CMVM n.º 6/2020 - Diário da República n.º 243/2020, Série II de 2020-12-16](https://diariodarepublica.pt/dr/detalhe/regulamento-cmvm/6-2020-151322794), em vigor a partir de 2021-07-01*

## Anexo 22 — Informação relativa ao relatório de auditoria dos organismos de investimento coletivo

O presente Anexo é preenchido nos termos do Regulamento da CMVM n.º 3/2016.

Quanto ao nome do ficheiro:

(ver documento original)

Quanto à estrutura e conteúdo do ficheiro de dados:

As especificações técnicas relativas ao ficheiro "RDA" a enviar à CMVM constam do documento "2020_reporte_RDA_schemas.zip" ou em versões atualizadas do mesmo, disponível no sítio da internet da CMVM.

Opção de reporte com conteúdo

No conteúdo a reportar o elemento ConteudoReporte do cabeçalho deve conter a indicação "REPO" e o elemento identificador de reporte nulo do corpo do ficheiro não deve ser preenchido, sendo preenchidos os restantes elementos do corpo do ficheiro de acordo com as instruções infra.

Bloco de informação n.º 1: Informação sobre o conteúdo do relatório de auditoria (RDA) dos organismos de investimento coletivo (OIC), com os seguintes campos:

Tipo de opinião (Campo 1): Campo de preenchimento obrigatório que identifica as caraterísticas do RDA, sendo preenchido com um dos seguintes códigos:

"SRE", para RDA sem reservas e ênfases;

"CRE", para RDA com reservas e ênfases;

"OCR", para RDA com reservas e sem ênfases;

"OCE", para RDA com ênfases e sem reservas;

"EDO", para uma escusa de opinião;

"ADV", para uma opinião adversa.

(ver documento original)

Bloco de informação n.º 2: Informação sobre as reservas no RDA, com os seguintes campos:

Identificação de reservas (Campo 1): Campo de preenchimento obrigatório quando o tipo de opinião no campo 1 do bloco de informação n.º 1 for preenchido com o código "CRE" ou "OCR", e que identifica um número sequencial de 1 a n, sendo n o número total de reservas.

Descrição da reserva (Campo 2): Campo de preenchimento obrigatório quando o tipo de opinião no campo 1 do bloco de informação n.º 1 for preenchido com o código "CRE" ou "OCR", e que identifica o texto da reserva que consta do RDA.

(ver documento original)

Bloco de informação n.º 3: Informação sobre as ênfases no RDA, com os seguintes campos:

Identificação de ênfases (Campo 1): Campo de preenchimento obrigatório quando o tipo de opinião no campo 1 do bloco de informação n.º 1 for preenchido com o código "CRE" ou "OCE", e que identifica um número sequencial de 1 a n, sendo n o número total de ênfases.

Descrição da ênfase (Campo 2): Campo de preenchimento obrigatório quando o tipo de opinião no campo 1 do bloco de informação n.º 1 for preenchido com o código "CRE" ou "OCE", e que identifica o texto da ênfase que consta do RDA.

(ver documento original)

Bloco de informação n.º 4: Informação sobre o auditor que assina o RDA, com os seguintes campos:

Número de registo do revisor oficial de contas (ROC) (Campo 1): Campo de preenchimento obrigatório que identifica o número de registo na CMVM do ROC que assina o RDA.

Número de registo da SROC (Campo 2): Campo que identifica o número de registo na CMVM da SROC a qual pertence o revisor oficial de contas (ROC) que assina o RDA.

(ver documento original)

- *Aditado pelo/a Artigo 3.º do/a [Regulamento da CMVM n.º 6/2020 - Diário da República n.º 243/2020, Série II de 2020-12-16](https://diariodarepublica.pt/dr/detalhe/regulamento-cmvm/6-2020-151322794), em vigor a partir de 2021-07-01*

## Anexo 23 — Informação sobre participações em organismos de investimento coletivo estrangeiros comercializados em Portugal

O presente Anexo é preenchido nos termos do Regulamento da CMVM n.º 3/2016.

Quanto ao nome do ficheiro:

(ver documento original)

Quanto à estrutura e conteúdo do ficheiro de dados:

As especificações técnicas relativas ao ficheiro "OVM" a enviar à CMVM constam do documento "2020_reporte_OVM_schemas.zip" ou em versões atualizadas do mesmo, disponível no sítio da internet da CMVM."

I - Opção de reporte perante inexistência de informação ("reporte nulo")

Na inexistência de informação a enviar para determinado período de referência, o presente ficheiro é enviado à CMVM com a indicação de "NULO" nos elementos ConteudoReporte do cabeçalho e no elemento identificador de reporte nulo do corpo do ficheiro.

Nesta circunstância todos os restantes elementos do corpo do ficheiro não devem ter conteúdo.

II - Opção de reporte com conteúdo

Existindo conteúdo a reportar o elemento ConteudoReporte do cabeçalho deve conter a indicação "REPO" e o elemento identificador de reporte nulo do corpo do ficheiro não deve ser preenchido, sendo preenchidos os restantes elementos do corpo do ficheiro de acordo com as instruções infra.

Código ISIN da Participação (Campo 1): Campo que identifica o código ISIN da participação, ou seja, das unidades de participação ou ações comercializadas (de uma determinada categoria ou classe) em Portugal.

Código OIA (Campo 2): Campo a ser preenchido para os organismos de investimento alternativo que não disponham de informação para preencher o campo "Código ISIN da Participação", sendo preenchido com o código LEI ou, na sua indisponibilidade, com o código da participação atribuído para o efeito pela CMVM, ou seja, das unidades de participação ou ações comercializadas (de um determinado compartimento patrimonial autónomo) em Portugal.

Tipo de investidores (Campo 3): Campo que identifica o tipo de investidores sendo preenchido com um dos seguintes códigos:

"NP", se for investidor não profissional;

"PR", se for investidor profissional; ou

"CE", se for contraparte elegível.

Valor da participação (Campo 4): Campo que identifica o valor das participações em circulação em Portugal, à data de referência da informação, expresso em euros, considerando o câmbio à data da informação, somente no que respeita à atividade da entidade comercializadora em Portugal.

Valor das subscrições/aquisições (Campo 5): Campo que identifica o valor das subscrições/aquisições efetuadas em Portugal, durante o mês, expresso em euros, considerando o câmbio à data da operação, somente no que respeita à atividade da entidade comercializadora em Portugal.

Valor dos resgates/alienações (Campo 6): Campo que identifica o valor dos resgates/alienações efetuadas em Portugal, durante o mês, expresso em euros, considerando o câmbio à data da operação, somente no que respeita à atividade da entidade comercializadora em Portugal.

Número de participantes (Campo 7): Campo que identifica o número de participantes em Portugal, à data de referência da informação, somente no que respeita à atividade da entidade comercializadora em Portugal.

Número de participações (Campo 8): Campo que identifica o número de unidades de participação ou ações detidas em Portugal, à data de referência da informação, somente no que respeita à atividade da entidade comercializadora em Portugal.

(ver documento original)

- *Aditado pelo/a Artigo 3.º do/a [Regulamento da CMVM n.º 6/2020 - Diário da República n.º 243/2020, Série II de 2020-12-16](https://diariodarepublica.pt/dr/detalhe/regulamento-cmvm/6-2020-151322794), em vigor a partir de 2021-07-01*

## Anexo 24 — Receção e transmissão de ordens por conta de outrem

O presente Anexo é preenchido nos termos do Regulamento da CMVM n.º 3/2016.

Quanto ao nome do ficheiro:

(ver documento original)

Quanto à estrutura e conteúdo do ficheiro de dados:

As especificações técnicas relativas ao ficheiro "RTO" a enviar à CMVM constam do documento "2020_reporte_RTO_schemas.zip" ou em versões atualizadas do mesmo, disponível no sítio da internet da CMVM."

I - Opção de reporte perante inexistência de informação ("reporte nulo")

Na inexistência de informação a enviar para determinado período de referência, o presente ficheiro é enviado à CMVM com a indicação de "NULO" nos elementos ConteudoReporte do cabeçalho e no elemento identificador de reporte nulo do corpo do ficheiro.

Nesta circunstância todos os restantes elementos do corpo do ficheiro não devem ter conteúdo.

II - Opção de reporte com conteúdo

Existindo conteúdo a reportar o elemento ConteudoReporte do cabeçalho deve conter a indicação "REPO" e o elemento identificador de reporte nulo do corpo do ficheiro não deve ser preenchido, sendo preenchidos os restantes elementos do corpo do ficheiro de acordo com as instruções infra.

Bloco de informação n.º 1: Informação sobre a atividade de receção e transmissão de ordens por conta de outrem sobre instrumentos financeiros, com os seguintes campos:

Tipo de investidor (Campo 1): Campo que identifica o tipo de investidor que transmitiu a ordem, sendo preenchido com um dos seguintes códigos:

"NP", se for investidor não profissional;

"PR", se for investidor profissional;

"CE", se for contraparte elegível.

Residência do investidor (Campo 2): Campo que identifica a residência do investidor que transmitiu a ordem, sendo preenchido com um dos seguintes códigos:

"R", para investidores residentes em Portugal;

"N", para outros investidores.

Canal de receção da ordem (Campo 3): Campo que identifica o tipo de canal de receção da ordem, sendo preenchido com um dos seguintes códigos:

"I", para ordens recebidas através de sítio da Internet disponibilizado para o efeito;

"E", para ordens recebidas por outros meios eletrónicos de comunicação à distância, nomeadamente terminais que permitam a receção de ordens;

"R", para ordens provenientes de meios de reencaminhamento automático que façam interface com sistemas de outras entidades (order routing);

"T", para ordens recebidas através de telefone, presencialmente nas instalações da entidade ou por fax;

"O", para ordens recebidas através de outros canais.

Tipo de instrumento financeiro (Campo 4): Campo que identifica a tipologia do instrumento financeiro a que se refere a ordem, sendo preenchido com um dos seguintes códigos:

"AC", para ações;

"UP", para unidades de participação em organismos de investimento coletivo não admitidas à negociação;

"EF", para unidades de participação em organismos de investimento coletivo admitidas à negociação (ETF);

"DU", para instrumentos de dívida emitidos pelo Estado ou outros entes públicos e equiparados;

"PC", para papel comercial;

"DI", para outros instrumentos de dívida emitidos por entidades privadas;

"ON", para outros instrumentos financeiros não derivados;

"FT", para contratos de futuros;

"CT" para contratos de forward;

"OC", para contratos de opções de compra;

"OV", para contratos de opções de venda;

"CD", para contratos financeiros por diferenças (CFD);

"SW", para contratos de troca (Swap);

"OD", para outros instrumentos financeiros derivados.

Tipo de subjacente (Campo 5): Campo que identifica a tipologia do subjacente do instrumento financeiro derivado, sendo preenchido com um dos seguintes códigos:

"NA", quando o instrumento financeiro do campo anterior for preenchido com um dos seguintes códigos: "AC", "UP", "EF", "DU", "PC", "DI" ou "ON";

"AC", para ações;

"IN", para índices;

"TJ", para taxas de juro;

"TC", para taxas de câmbio;

"CR", para crédito;

"MC", para mercadorias e licenças de emissão;

"OT", para outros subjacentes não especificados anteriormente.

Tipo de ordem (Campo 6): Campo que identifica o tipo de ordem, sendo preenchido com um dos seguintes códigos:

"C", para ordens de compra;

"V", para ordens de venda.

Montante (Campo 7): Campo que identifica o montante de instrumentos financeiros das ordens executadas, sendo preenchido com:

Montante efetivamente pago ou recebido pela realização da transação, excluindo-se os juros corridos no caso de instrumentos de dívida emitidos pelo Estado, entes públicos ou entidades privadas, quando a tipologia do instrumento financeiro no campo 4 do bloco de informação n.º 1 for preenchido com um dos seguintes códigos: "AC", "UP", "EF", "DU", "PC", "DI" ou "ON";

Montante correspondente ao produto entre o número de contratos negociados, a unidade de negociação dos mesmos e o respetivo preço da transação, quando a tipologia do instrumento financeiro no campo 4 do bloco de informação n.º 1 for preenchido com um dos seguintes códigos: "FT", "CT", "OC", "OV", "CD", "SW" ou "OD".

Local de Execução (Campo 8): Campo que identifica o local onde ocorreu a execução da ordem, sendo preenchido com:

O respetivo Market Identifier Code (MIC), nos termos definidos na Norma ISO 10383, para as ordens executadas em mercado regulamentado, em sistema de negociação multilateral ou em sistema de negociação organizada;

"OEFM", para as ordens executadas fora de plataformas de negociação e em que a entidade, isenta de risco, intermedia o encontro entre a ordem do comprador e a do vendedor.

(ver documento original)

Bloco de informação n.º 2: Informação sobre o detalhe dos instrumentos financeiros objeto da atividade de receção e transmissão de ordens por conta de outrem, com os seguintes campos:

Código do instrumento financeiro (Campo 1): Campo que identifica o código do instrumento financeiro transacionado, sendo preenchido com:

O International Standard Identification Number (ISIN), nos termos definidos na Norma ISO 6166, sempre que aplicável;

Não existindo ISIN, o Classification of Financial Instruments (CFI), nos termos definidos na Norma ISO 10962.

Tipo de código do instrumento financeiro (Campo 2): Campo que identifica o tipo de código do instrumento financeiro transacionado, sendo preenchido com:

"I", quando o código de instrumento financeiro no campo anterior for preenchido com um código ISIN;

"C", quando o código de instrumento financeiro no campo anterior for preenchido com um código CFI.

Designação do instrumento financeiro (Campo 3): Campo que identifica a designação do instrumento financeiro.

Mercado de admissão (Campo 4): Campo que identifica o mercado onde o instrumento financeiro está admitido à negociação, sendo preenchido com:

O respetivo Market Identifier Code (MIC), nos termos definidos na Norma ISO 10383, para as ordens executadas em mercado regulamentado, em sistema de negociação multilateral ou em sistema de negociação organizada;

Deve ser preenchido com o MIC Code do primeiro mercado onde o instrumento financeiro foi admitido à negociação. Caso exista mais do que um mercado nestas circunstâncias, deve ser considerado o mercado mais líquido;

"XXXX", para instrumentos financeiros não admitidos em plataformas de negociação.

Tipo de instrumento financeiro (Campo 5): Campo que identifica a tipologia do instrumento financeiro a que se refere a ordem, sendo preenchido com um dos seguintes códigos:

"AC", para ações;

"UP", para unidades de participação em organismos de investimento coletivo não admitidas à negociação;

"EF", para unidades de participação em organismos de investimento coletivo admitidas à negociação (ETF);

"DU", para instrumentos de dívida emitidos pelo Estado ou outros entes públicos e equiparados;

"PC", para papel comercial;

"DI", para outros instrumentos de dívida emitidos por entidades privadas;

"ON", para outros instrumentos financeiros não derivados;

"FT", para contratos de futuros;

"CT" para contratos de forward;

"OC", para contratos de opções de compra;

"OV", para contratos de opções de venda;

"CD", para contratos financeiros por diferenças (CFD);

"SW", para contratos de troca (Swap);

"OD", para outros instrumentos financeiros derivados.

Tipo de subjacente (Campo 6): Campo que identifica a tipologia do subjacente do instrumento financeiro derivado, sendo preenchido com um dos seguintes códigos:

"NA", quando o instrumento financeiro do campo 5 do bloco de informação n.º 2 for preenchido com um dos seguintes códigos: "AC", "UP", "EF", "DU", "PC", "DI" ou "ON";

"AC", para ações;

"IN", para índices;

"TJ", para taxas de juro;

"TC", para taxas de câmbio;

"CR", para crédito;

"MC", para mercadorias e licenças de emissão;

"OT", para outros subjacentes não especificados anteriormente.

Tipo de ordem (Campo 7): Campo que identifica o tipo de ordem recebida pela entidade, sendo preenchido com um dos seguintes códigos:

"C", para ordens de compra;

"V", para ordens de venda.

Quantidade (Campo 8): Campo identifica a quantidade transacionada de ordens executadas, sendo preenchido com:

Número de unidades, quando a tipologia do instrumento financeiro no campo 5 do bloco de informação n.º 2 for preenchido com um dos seguintes códigos: "AC", "UP", "EF" ou "ON";

Valor nominal, quando a tipologia do instrumento financeiro no campo 5 do bloco de informação n.º 2 for preenchido com um dos seguintes códigos: "DU", "PC", "DI", "SW" ou "ON";

Número de contratos, quando a tipologia do instrumento financeiro no campo 5 do bloco de informação n.º 2 for preenchido com um dos seguintes códigos: "FT", "CT", "OC", "OV", "CD", "SW" ou "OD".

Montante (Campo 9): Campo que identifica o montante de instrumentos financeiros das ordens executadas, sendo preenchido com o:

Montante efetivamente pago ou recebido pela realização da transação, excluindo-se os juros corridos no caso de instrumentos de dívida emitidos pelo Estado, entes públicos ou entidades privadas, quando a tipologia do instrumento financeiro no campo 5 do bloco de informação n.º 2 for preenchido com um dos seguintes códigos: "AC", "UP", "EF", "DU", "PC", "DI" ou "ON".

Montante correspondente ao produto entre o número de contratos negociados, a unidade de negociação dos mesmos e o respetivo preço da transação, quando a tipologia do instrumento financeiro no campo 5 do bloco de informação n.º 2 for preenchido com um dos seguintes códigos: "FT", "CT", "OC", "OV", "CD", "SW" ou "OD".

Local de execução (Campo 10): Campo que identifica o local onde ocorreu a execução da ordem e deve ser preenchido com:

O respetivo Market Identifier Code (MIC), nos termos definidos na Norma ISO 10383, para as ordens executadas em mercado regulamentado, em sistema de negociação multilateral ou em sistema de negociação organizada.

"OEFM", para as ordens executadas fora de plataformas de negociação e em que a entidade, isento de risco, intermedia o encontro entre a ordem do comprador e a do vendedor.

(ver documento original)

- *Aditado pelo/a Artigo 3.º do/a [Regulamento da CMVM n.º 6/2020 - Diário da República n.º 243/2020, Série II de 2020-12-16](https://diariodarepublica.pt/dr/detalhe/regulamento-cmvm/6-2020-151322794), em vigor a partir de 2021-07-01*
