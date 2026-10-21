---
id: "regulamento-cmvm-2-2015-anexo-12-composicao-discriminada-da-carteira-de-organismos-d"
dre_id: "69828456"
title: "Regulamento da CMVM n.º 2/2015, de 17 de julho — Anexo 12 — Composição discriminada da carteira de organismos de investimento coletivo em…"
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
part: "Anexo 12 — Composição discriminada da carteira de organismos de investimento coletivo em…"
---

# Regulamento da CMVM n.º 2/2015, de 17 de julho — Anexo 12 — Composição discriminada da carteira de organismos de investimento coletivo em…

## Anexo 12 — Composição discriminada da carteira de organismos de investimento coletivo em valores mobiliários de organismos de investimento alternativo em valores mobiliários e de organismos de investimento em ativos não financeiros

O presente Anexo é preenchido nos termos do Regulamento da CMVM n.º 3/2016.

Quanto ao nome do ficheiro:

(ver documento original)

Quanto à estrutura e conteúdo do ficheiro de dados:

As especificações técnicas relativas ao ficheiro "CFM" a enviar à CMVM constam do documento "2020_reporte_CFM_schemas.zip" ou em versões atualizadas do mesmo, disponível no sítio da internet da CMVM.

Opção de reporte com conteúdo

No conteúdo a reportar o elemento ConteudoReporte do cabeçalho deve conter a indicação "REPO" e o elemento identificador de reporte nulo do corpo do ficheiro não deve ser preenchido, sendo preenchidos os restantes elementos do corpo do ficheiro de acordo com as instruções infra.

Bloco de informação n.º 1: Informação sobre instrumentos financeiros admitidos, em processo de admissão ou não admitidos à negociação em plataformas de negociação, com os seguintes campos:

Código de categoria (Campo 1): Campo que identifica o código de categoria do instrumento financeiro, sendo preenchido com o código da tabela 1.

Código do instrumento financeiro 1 (Campo 2): Campo que identifica o código do instrumento financeiro que integra a carteira sob gestão, sendo preenchido com:

O International Standard Identification Number (ISIN), nos termos definidos na Norma ISO 6166, sempre que aplicável, e

"NA" caso não exista ISIN.

Código do instrumento financeiro 2 (Campo 3): Campo que identifica código adicional do instrumento financeiro que integra a carteira sob gestão, sendo preenchido com o Classification of Financial Instruments (CFI), nos termos definidos na Norma ISO 10962.

Descrição do instrumento financeiro (Campo 4): Campo que identifica a designação do instrumento financeiro.

Código do mercado (Campo 5): Campo que identifica a plataforma de negociação onde o instrumento financeiro se encontra admitido à negociação ou no qual será admitido para os instrumentos financeiros em processo de admissão, sendo preenchido com:

O respetivo Market Identifier Code (MIC), nos termos definidos na Norma ISO 10383, para os instrumentos financeiros admitidos, ou em processo de admissão, à negociação em mercado regulamentado, em sistema de negociação multilateral ou em sistema de negociação organizada.

Caso o instrumento se encontre admitido em mais do que uma plataforma de negociação, o campo deve ser preenchido com o MIC Code do mercado onde o mesmo é normalmente transacionado pela entidade responsável pela gestão.

"XXXX", para os instrumentos financeiros não admitidos à negociação.

Tipo de OIC (Campo 6): Campo que é preenchido com:

"S", tratando-se de OICVM estabelecidos ou não em território nacional;

"N", tratando-se de OIC, que não sejam OICVM estabelecidos ou não em território nacional;

"NA", quando não aplicável (para os códigos de categoria (campo 1) que não sejam CC05, CC18 e CC31).

País do emitente (Campo 7): Campo que identifica o país do emitente do instrumento financeiro.

Código do emitente (Campo 8): Campo que identifica o código LEI relativo ao emitente do instrumento financeiro. Caso não seja aplicável, este campo deverá ser preenchido com "NA".

Descrição do emitente (Campo 9): Campo que identifica o nome ou denominação do emitente do instrumento financeiro.

Descrição do ativo subjacente (Campo 10): Campo que identifica a designação do(s) ativo(s) subjacente(s) (qualquer que seja o instrumento financeiro derivado).

Notação de risco da emissão ou do emitente (Campo 11): Campo que é preenchido com:

A notação de risco da emissão do título de dívida, ou na sua inexistência, notação do risco do emitente à data da carteira, atribuído por agências internacionalmente reconhecidas. No caso da existência de duas ou mais notações, corresponde à notação mais baixa.

"NA", no caso de inexistência de notação de risco da emissão ou do emitente.

Tipo de notação de risco (Campo 12): Campo que é preenchido com:

"O", se o campo anterior tiver sido preenchido com notação de risco da emissão;

"E", se o campo anterior tiver sido preenchido com notação de risco do emitente;

"NA", se o campo anterior tiver sido preenchido com "NA".

Grupo (Campo 13): Campo que é preenchido com "S" ou "N", consoante o instrumento financeiro seja ou não:

a) Emitido ou garantido por entidade previstas nas alíneas a) a h) do artigo 147.º do RGOIC;

b) Emitido por organismo de investimento coletivo gerido pela entidade responsável pela gestão do organismo objeto de reporte ou gerido por entidade que com ela se encontre em relação de grupo para efeitos de consolidação de contas, na aceção referida no n.º 13 do artigo 176.º do RGOIC; ou

c) Emitido por entidade em relação de grupo para efeitos de consolidação de contas, na aceção referida no n.º 13 do artigo 176.º do RGOIC, com outro emitente de outro ativo em carteira.

Entidade de grupo (Campo 14): Campo que é preenchido caso o campo "Grupo" ser igual a "S", do seguinte modo:

Estando em causa situação prevista na alínea a) do campo "Grupo", é inserida a abreviatura "SG", "DP" ou "OUT" consoante a entidade que tenha emitido ou garantido o ativo ou passivo esteja relacionada com a entidade responsável pela gestão, com o depositário ou com outra entidade, respetivamente. No caso de a entidade ser enquadrável em mais do que uma opção deverá ser utilizada a abreviatura "SG" em detrimento de "DP" e "OUT" ou "DP" em detrimento de "OUT".

Estando em causa a situação prevista na alínea b) do campo "Grupo", é inserida a abreviatura "OIC".

Estando em causa a situação prevista na alínea c) do campo "Grupo", é inserido o código de identificação do ativo, utilizando para o efeito a abreviatura "G" seguida de um número sequencial (com início em "00001" para o primeiro grupo até "nnnnn" para o grupo "n"), que estabeleça uma relação historicamente inequívoca e constante com o grupo. Esta identificação deverá ser igual para todos os fundos geridos por uma entidade responsável pela gestão.

Código da moeda (Campo 15): Campo que identifica a moeda em que o preço do instrumento financeiro originariamente se encontra expresso, sendo preenchido nos termos da norma ISO 4217.

Quantidade do instrumento financeiro (Campo 16): Campo que identifica a quantidade ou valor nominal do instrumento financeiro em carteira.

Preço do instrumento financeiro (Campo 17): Campo que é preenchido com o valor unitário do ativo em carteira na moeda em que foi adquirido ou em percentagem quando se trate de instrumento representativo de dívida.

Indicação do preço do instrumento financeiro (Campo 18): Campo preenchido com "V", caso o campo anterior tenha sido preenchido com valor, "P", caso tenha sido preenchido em percentagem.

Tipo de preço do instrumento financeiro (Campo 19): Campo que identifica o tipo de preço do instrumento financeiro sendo preenchido com:

"N", caso o preço tenha por base, o preço praticado no mercado em que o instrumento financeiro se encontre admitido à negociação;

"B", caso o preço tenha por base o valor médio das ofertas de compra e venda firmes;

"O", caso o preço tenha por base o valor médio das ofertas de compra e venda definidas através de entidades especializadas;

"V", caso o preço tenha por base o valor médio das ofertas de compra difundidas através de entidades especializadas;

"A", caso o preço tenha por base os modelos de avaliação utilizados e reconhecidos universalmente nos mercados financeiros;

"U", caso o preço tenha por base o último valor da unidade de participação divulgado ao mercado pela respetiva entidade responsável pela gestão.

Data do preço do instrumento financeiro (Campo 20): Campo que identifica a data do preço do instrumento financeiro.

Montante total (Campo 21): Campo que identifica o montante total do instrumento financeiro na carteira, incluindo juros corridos se aplicável, em euros.

Montante total na moeda de referência da carteira (Campo 22): Campo que identifica o montante total do instrumento financeiro na carteira, incluindo juros corridos se aplicável, na moeda de referência da carteira (apenas no caso de ser diferente do euro).

(ver documento original)

TABELA 1

Códigos de categoria dos ativos em carteira nos OICVM, OIAVM e OIAnF

(ver documento original)

Bloco de informação n.º 2: Informação sobre ativos não financeiros da carteira, com os seguintes campos:

Código de categoria (Campo 1): Campo que identifica o código de categoria do ativo, sendo preenchido com o código da tabela 2.

Descrição do ativo (Campo 2): Campo que identifica a designação do ativo.

Grupo (Campo 3): Campo que é preenchido com "S" ou "N", consoante o ativo seja ou não:

a) Emitido ou garantido por entidades previstas nas alíneas a) a h) do artigo 147.º do RGOIC;

b) Emitido por organismo de investimento coletivo gerido pela entidade responsável pela gestão do organismo objeto de reporte ou gerido por entidade que com ela se encontre em relação de grupo para efeitos de consolidação de contas, na aceção referida no n.º 13 do artigo 176.º do RGOIC; ou

c) Emitido por entidade em relação de grupo para efeitos de consolidação de contas, na aceção referida no n.º 13 do artigo 176.º do RGOIC, com outro emitente de outro ativo em carteira.

Entidade de grupo (Campo 4): Campo que é preenchido caso o campo "Grupo" ser igual a "S", do seguinte modo:

Estando em causa situação prevista na alínea a) do campo "Grupo", é inserida a abreviatura "SG", "DP" ou "OUT" consoante a entidade que tenha emitido ou garantido o ativo ou passivo esteja relacionada com a entidade responsável pela gestão, com o depositário ou com outra entidade, respetivamente. No caso de a entidade ser enquadrável em mais do que uma opção deverá ser utilizada a abreviatura "SG" em detrimento de "DP" ou "OUT".

Estando em causa a situação prevista na alínea b) do campo "Grupo", é inserida a abreviatura "OIC", ou

Estando em causa a situação prevista na alínea c) do campo "Grupo", é inserido o código de identificação do ativo, utilizando para o efeito a abreviatura "G" seguida de um número sequencial (com início em "00001" para o primeiro grupo até "nnnnn" para o grupo "n"), que estabeleça uma relação historicamente inequívoca e constante com o grupo. Esta identificação deverá ser igual para todos os fundos geridos por uma entidade responsável pela gestão.

Código da moeda (Campo 5): Campo que identifica a moeda em que o preço do ativo originariamente se encontra expresso, sendo preenchido nos termos da norma ISO 4217.

Quantidade do ativo (Campo 6): Campo que identifica a quantidade do ativo em carteira.

Montante total (Campo 7): Campo que identifica o montante total do ativo na carteira, em euros.

Montante total na moeda de referência da carteira (Campo 8): Campo que identifica o montante total do ativo na carteira, na moeda de referência da carteira (apenas no caso de ser diferente do euro).

(ver documento original)

TABELA 2

Códigos de categoria dos ativos em carteira nos OICVM, OIAVM, OIAnF

(ver documento original)

Bloco de informação n.º 3: Informação sobre outros ativos e passivos da carteira, com os seguintes campos:

Código de categoria (Campo 1): Campo que identifica o código de categoria dos outros ativos e passivos, sendo preenchido com o código da tabela 3.

Descrição do ativo ou passivo (Campo 2): Campo que identifica a designação do ativo ou passivo.

Código da entidade relevante (Campo 3): Campo que identifica a entidade junto da qual a entidade responsável pela gestão contratou os ativos e passivos, sendo preenchido com:

O código LEI, quando aplicável;

"NA", quando não aplicável.

Descrição da entidade relevante (Campo 4): Campo que identifica o nome ou denominação da entidade junto da qual a entidade responsável pela gestão contratou os ativos e passivos, sendo preenchido com:

O nome ou denominação da entidade, quando aplicável;

"NA", quando não aplicável.

Data de emissão (Campo 5): Campo que identifica a data de contratação do ativo ou passivo, se aplicável.

Data de maturidade (Campo 6): Campo que identifica a data na qual o valor ativo ou passivo se vence, se aplicável.

Grupo (Campo 7): Campo que é preenchido com "S" ou "N", consoante o ativo ou o passivo seja ou não:

a) Emitido ou garantido por entidade previstas nas alíneas a) a h) do artigo 147.º do RGOIC;

b) Emitido por entidade em relação de grupo para efeitos de consolidação de contas, na aceção referida no n.º 13 do artigo 176.º do RGOIC, com outro emitente de outro ativo em carteira.

Entidade de grupo (Campo 8): Campo que é preenchido caso o campo "Grupo" ser igual a "S", do seguinte modo:

Estando em causa situação prevista na alínea a) do campo "Grupo", é inserida a abreviatura "SG", "DP" ou "OUT" consoante a entidade que tenha emitido ou garantido o ativo ou passivo esteja relacionada com a entidade responsável pela gestão, com o depositário ou com outra entidade, respetivamente. No caso de a entidade ser enquadrável em mais do que uma opção deverá ser utilizada a abreviatura "SG" em detrimento de "DP" e "OUT" ou "DP" em detrimento de "OUT".

Estando em causa a situação prevista na alínea b) do campo "Grupo", é inserida a abreviatura "OIC", ou

Estando em causa a situação prevista na alínea c) do campo "Grupo", é inserido o código de identificação do ativo, utilizando para o efeito a abreviatura "G" seguida de um número sequencial (com início em "00001" para o primeiro grupo até "nnnnn" para o grupo "n"), que estabeleça uma relação historicamente inequívoca e constante com o grupo. Esta identificação deverá ser igual para todos os fundos geridos por uma entidade responsável pela gestão.

Tipo de outros valores (Campo 9): Campo que identifica no caso de organismos de investimento coletivo em valores mobiliários, de organismos de investimento alternativo em valores mobiliários e de organismo de investimento em ativos não financeiros, sob a forma societária autogerida, sendo preenchido com:

"I", caso respeite a outros valores ativos e passivos relativos à carteira de investimento;

"N", caso respeite a outros valores necessários ao desenvolvimento da atividade do organismo;

Código da moeda (Campo 10): Campo que identifica a moeda em que o ativo ou passivo originariamente se encontra expresso, sendo preenchido nos termos da norma ISO 4217.

Montante total (Campo 11): Campo que identifica o montante total do valor do ativo ou

Montante total na moeda de referência da carteira (Campo 12): Campo que identifica o montante total do ativo ou passivo na carteira, na moeda de referência da carteira (apenas no caso de ser diferente do euro).

(ver documento original)

TABELA 3

Códigos de categoria dos outros ativos e passivos dos OICVM, OIAVM e OIAnF

(ver documento original)

Bloco de informação n.º 4: Informação adicional sobre a carteira, com os seguintes campos:

Código da moeda de referência da carteira (Campo 1): Campo que identifica a moeda de referência da carteira, sendo preenchido nos termos da norma ISO 4217 (apenas no caso de ser diferente do euro).

Valor líquido global (Campo 2): Campo que identifica o valor líquido global, em euros.

N.º Unidades de participação total (Campo 3): Campo que identifica o total de unidades de participação em circulação.

Valor líquido global na moeda de referência da carteira (Campo 4): Campo que identifica o valor líquido global na moeda de referência da carteira (apenas no caso de ser diferente do euro).

Ativo sob gestão (Campo 5): Campo que identifica o ativo sob gestão (AUM), em euros, sendo calculado nos termos definidos no Regulamento Delegado (EU) n.º 231/2013 da Comissão de 19 de dezembro de 2012.

Ativo sob gestão na moeda de referência da carteira (Campo 6): Campo que identifica o ativo sob gestão (AUM), na moeda de referência da carteira (apenas no caso de ser diferente do euro), sendo calculado nos termos definidos no Regulamento Delegado (EU) n.º 231/2013 da Comissão de 19 de dezembro de 2012.

Ativos líquidos (Campo 7): Campo que identifica o valor total de ativos líquidos, em euros; por ativos líquidos entendem-se os previstos no n.º 1 do artigo 416.º do Regulamento (EU) n.º 575/2013, excluindo a condição prevista na alínea d) do n.º 3 do referido artigo e as disponibilidades e aplicações em outras instituições de crédito com prazo residual inferior a 30 dias ou mobilizáveis sem penalização num prazo máximo de 30 dias.

Ativos líquidos na moeda de referência da carteira (Campo 8): Campo que identifica o valor total de ativos líquidos, na moeda de referência da carteira (apenas no caso de ser diferente do euro), por ativos líquidos entendem-se os previstos no n.º 1 do artigo 416.º do Regulamento (EU) n.º 575/2013, excluindo a condição prevista na alínea d) do n.º 3 do referido artigo e as disponibilidades e aplicações em outras instituições de crédito com prazo residual inferior a 30 dias ou mobilizáveis sem penalização num prazo máximo de 30 dias.

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

Código de categoria (Campo 1): Campo que identifica o código de categoria das responsabilidades extrapatrimoniais, sendo preenchido com o código da tabela 4.

Código do instrumento financeiro 1 (Campo 2): Campo que identifica o código do instrumento financeiro que integra a carteira sob gestão, sendo preenchido com:

O International Standard Identification Number (ISIN), nos termos definidos na Norma ISO 6166, sempre que aplicável;

"NA" caso não exista ISIN.

Código do instrumento financeiro 2 (Campo 3): Campo que identifica adicionalmente o código do instrumento financeiro que integra a carteira sob gestão, sendo preenchido com o Classification of Financial Instruments (CFI), nos termos definidos na Norma ISO 10962.

Descrição do instrumento financeiro (Campo 4): Campo que identifica a designação do instrumento financeiro.

Mercado (Campo 5): Campo que identifica a plataforma de negociação onde o instrumento financeiro se encontra admitido à negociação ou no qual será admitido para os instrumentos financeiros em processo de admissão, sendo preenchido com:

O respetivo Market Identifier Code (MIC), nos termos definidos na Norma ISO 10383, para os instrumentos financeiros admitidos à negociação em mercado regulamentado, em sistema de negociação multilateral ou em sistema de negociação organizada.

"XXXX", para os instrumentos financeiros não admitidos à negociação.

Descrição do ativo subjacente (Campo 6): Campo que identifica a designação do(s) ativo(s) subjacente(s).

Data de maturidade (Campo 7): Campo que identifica a data na qual o instrumento financeiro se vence, se aplicável.

Código da moeda (Campo 8): Campo que identifica a moeda em que o instrumento originariamente se encontra expresso, sendo preenchido nos termos da norma ISO 4217.

Quantidade do instrumento financeiro (Campo 9): Campo que identifica a quantidade do instrumento financeiro em carteira. As posições vendedoras deverão ser precedidas de sinal negativo no campo de valor total (com exceção dos derivados cambiais em que o subjacente é a moeda de referência do fundo, nos quais as posições compradoras deverão ser precedidas de sinal negativo no campo de valor total).

Preço do instrumento financeiro (Campo 10): Campo que é preenchido com a valorização do instrumento financeiro.

Tipo de preço do instrumento financeiro (Campo 11): Campo que identifica o tipo de preço sendo preenchido com:

"N", caso o preço tenha por base, o preço praticado no mercado em que o ativo se encontre admitido à negociação;

"B", caso o preço tenha por base o valor médio das ofertas de compra e venda firmes;

"O", caso o preço tenha por base o valor médio das ofertas de compra e venda definidas através de entidades especializadas;

"V", caso o preço tenha por base o valor médio das ofertas de compra difundidas através de entidades especializadas;

"A", caso o preço tenha por base os modelos de avaliação utilizados e reconhecidos universalmente nos mercados financeiros.

Data do preço (Campo 12): Campo que identifica a data do preço utilizado.

Exposição (Campo 13): Campo que identifica a exposição inerente aos instrumentos financeiros derivados, expresso em euros. As posições vendedoras deverão ser precedidas de sinal negativo (com exceção dos derivados cambiais em que o subjacente é a moeda de referência do fundo, nos quais as posições compradoras deverão ser precedidas de sinal negativo no campo de valor total).

Objetivo do derivado (Campo 14): Campo que identifica o objetivo que o instrumento financeiro derivado em carteira pretenda concretizar sendo preenchido com:

''C", caso se destina a cobertura de riscos;

"O", outros.

Montante total (Campo 15): Campo que identifica o montante total da responsabilidade extrapatrimonial incluindo juros decorridos, em euros.

Montante total na moeda de referência da carteira (Campo 16): Campo que identifica o montante total do valor integrante da carteira, na moeda de referência da carteira (apenas no caso de ser diferente do euro).

(ver documento original)

TABELA 4

Códigos de categoria de informação sobre as responsabilidades extrapatrimoniais dos OICVM, OIAVM e OIAnF

(ver documento original)

- *Alterado pelo/a Artigo 3.º do/a [Regulamento da CMVM n.º 6/2020 - Diário da República n.º 243/2020, Série II de 2020-12-16](https://diariodarepublica.pt/dr/detalhe/regulamento-cmvm/6-2020-151322794), em vigor a partir de 2021-07-01*

## Anexo 13 — Informação sobre a atividade de organismos de investimento coletivo

I - Especificidades relativas à atividade dos OICVM, OIAVM e OIAnF

O presente Anexo é preenchido nos termos do Regulamento da CMVM n.º 3/2016.

Quanto ao nome do ficheiro:

(ver documento original)

Quanto à estrutura e conteúdo do ficheiro de dados:

As especificações técnicas relativas ao ficheiro "AFM" a enviar à CMVM constam do documento "2020_reporte_AFM_schemas.zip" ou em versões atualizadas do mesmo, disponível no sítio da internet da CMVM.

Opção de reporte com conteúdo

No conteúdo a reportar o elemento ConteudoReporte do cabeçalho deve conter a indicação "REPO" e o elemento identificador de reporte nulo do corpo do ficheiro não deve ser preenchido, sendo preenchidos os restantes elementos do corpo do ficheiro de acordo com as instruções infra.

Bloco de informação n.º 1: Informação sobre o número de participantes e unidades de participação, com os seguintes campos:

Tipo de participantes (Campo 1): Campo que identifica o código do tipo de participante:

"NP", se for investidor não profissional;

"PR", se for investidor profissional;

"CE", se for contraparte elegível.

Categoria de unidades de participação (Campo 2): Campo de preenchimento obrigatório que identifica as diferentes categorias de unidades de participação, sendo preenchido com:

"C", seguido de 1 ou 2 carateres, que correspondem à identificação da categoria nos documentos constitutivos;

"NA", sempre que não existam categorias de unidades de participação.

Número de participantes (Campo 3): Campo que identifica o número de participantes para cada registo.

Quantidade de unidades de participação (Campo 4): Campo que identifica o número de unidades de participação detidas.

(ver documento original)

Bloco de informação n.º 2: Informação sobre a comercialização de unidades de participação, com os seguintes campos:

Tipo de operação (Campo 1): Campo que identifica o código de operação:

"S", subscrição de OIC aberto;

"R", resgate de OIC aberto;

"SI", subscrição inicial OIC fechado;

"A", aumento de capital OIC fechado;

"RC", redução de capital OIC fechado;

"RF", reembolso total ou parcial de capital OIC fechado.

Tipo de participante (Campo 2): Campo que identifica o código do tipo de participante:

"NP", se for investidor não profissional;

"PR", se for investidor profissional;

"CE", se for contraparte elegível.

Categoria de unidades de participação (Campo 3): Campo de preenchimento obrigatório que identifica as diferentes categorias de unidades de participação, sendo preenchido com:

"C", seguido de 1 ou 2 carateres, que correspondem à identificação da categoria nos documentos constitutivos;

"NA", sempre que não existam categorias de unidades de participação.

Valor da operação (Campo 4): Campo que identifica o valor de cada operação, em euros, excluindo os encargos de transação.

Número de participantes (Campo 5): Campo que identifica o número de participantes associado a cada tipo de operação.

Quantidade de unidades de participação (Campo 6): Campo que identifica o número de unidades de participação associado a cada tipo de operação.

(ver documento original)

Bloco de informação n.º 3: Informação sobre as transações de ativos, com os seguintes campos:

Local de Execução (Campo 1): Campo que identifica o local onde foi efetuada a transação, sendo preenchido com:

O respetivo Market Identifier Code (MIC), nos termos definidos na Norma ISO 10383, para as transações executadas em mercado regulamentado, em sistema de negociação multilateral ou em sistema de negociação organizada;

"XXXX", para as transações executadas fora de plataformas de negociação.

Código do ativo (Campo 2): Campo que identifica o código do ativo:

"AC", Ações;

"CD", Contracts for Diference;

"CF", Contratos de futuro;

"CO", Contratos de opções;

"CS", Credit Default Swaps;

"DP", Dívida pública;

"DR", Direitos;

"FP", Fundos públicos e equiparados;

"FW", Forwards;

"OD", Obrigações diversas;

"SW", Swaps;

"TP", Títulos de participação;

"UH", Unidades de participação de organismos de investimento coletivo em valores mobiliários;

"UN", Unidades de participação de organismos de investimento alternativo excluindo os organismos de investimento imobiliário;

"WA", Warrants autónomos;

"PC", Papel comercial

"EF", Exchange Traded Fund;

"ON", para outros instrumentos financeiros;

"AnF", Ativos Não Financeiros;

"Imo", Imóveis;

"POII", Participações em organismos de investimento imobiliário;

"ASI", Ações emitidas por sociedades imobiliárias;

"OT", para outros ativos.

Tipo de operação (Campo 3): Campo que identifica o tipo de operação, sendo preenchido com um dos seguintes códigos:

"C", para aquisições, incluindo subscrições de OIC;

"V", para alienações, incluindo resgates de OIC.

Valor da transação (Campo 4): Campo que identifica o valor da transação em euros excluindo os custos associados à mesma.

Encargos da transação (Campo 5): Campo que identifica o valor dos encargos da transação em euros.

(ver documento original)

II - Especificidades relativas à atividade dos organismos de investimento imobiliário

O presente Anexo é preenchido nos termos do Regulamento da CMVM n.º 3/2016.

Quanto ao nome do ficheiro:

(ver documento original)

Quanto à estrutura e conteúdo do ficheiro de dados:

As especificações técnicas relativas ao ficheiro "AFI" a enviar à CMVM constam do documento "2020_reporte_AFI_schemas.zip" ou em versões atualizadas do mesmo, disponível no sítio da internet da CMVM.

Opção de reporte com conteúdo

No conteúdo a reportar o elemento ConteudoReporte do cabeçalho deve conter a indicação "REPO" e o elemento identificador de reporte nulo do corpo do ficheiro não deve ser preenchido, sendo preenchidos os restantes elementos do corpo do ficheiro de acordo com as instruções infra.

Bloco de informação n.º 1: Informação sobre o número de participantes e unidades de participação, com os seguintes campos:

Tipo de participante (Campo 1): Campo que identifica o código do tipo de participante, sendo preenchido com:

"NP", se for investidor não profissional;

"PR", se for investidor profissional;

"CE", se for contraparte elegível.

Categoria de unidades de participação (Campo 2): Campo de preenchimento obrigatório que identifica as diferentes categorias de unidades de participação, sendo preenchido com:

"C", seguido de 1 ou 2 carateres, que correspondem à identificação da categoria nos documentos constitutivos;

"NA", sempre que não existam categorias de unidades de participação.

Número de participantes (Campo 3): Campo que identifica o número de participantes relativo a cada tipo de participante.

Quantidade de unidades de participação (Campo 4): Campo que identifica o número de unidades de participação detidas.

(ver documento original)

Bloco de informação n.º 2: Informação sobre a comercialização de unidades de participação, com os seguintes campos:

Tipo de operação (Campo 1): Campo que identifica o código do tipo de operação, sendo preenchido com:

"S", Subscrições de OII Abertos;

"R", Resgates de OII Abertos;

"SI", Subscrição Inicial de OII Fechado;

"A", Aumento de Capital de OII Fechado;

"RC", Redução de Capital de OII Fechado;

"RF", Reembolso Total ou Parcial de OII Fechado.

Tipo de participante (Campo 2): Campo que identifica o código do tipo de participante:

"NP", se for investidor não profissional;

"PR", se for investidor profissional;

"CE", se for contraparte elegível.

Categoria de unidades de participação (Campo 3): Campo de preenchimento obrigatório que identifica as diferentes categorias de unidades de participação, sendo preenchido com:

"C", seguido de 1 ou 2 carateres, que correspondem à identificação da categoria nos documentos constitutivos;

"NA", sempre que não existam categorias de unidades de participação.

Valor da operação (Campo 4): Campo que identifica o valor de cada operação, em euros, excluindo os encargos de transação.

Número de participantes (Campo 5): Campo que identifica o número de participantes associado a cada tipo de operação.

Quantidade de unidades de participação (Campo 6): Campo que identifica o número de unidades de participação associado a cada tipo de operação.

(ver documento original)

Bloco de informação n.º 3: Informação sobre os imóveis arrendados a entidades que representem 20 % ou mais do ativo total, com os seguintes campos:

País do arrendatário (Campo 1) - Campo que identifica o país de residência do arrendatário.

Código do arrendatário (Campo 2) - Campo que identifica o código da entidade arrendatária sendo preenchido com:

Código LEI da entidade arrendatária;

Na ausência do código LEI, este campo é preenchido com o respetivo número de identificação fiscal.

Descrição do arrendatário (Campo 3) - Campo que identifica o nome ou a denominação do arrendatário sem utilização de abreviaturas.

País do ativo imobiliário (Campo 4) - Campo que identifica o país onde está localizado o imóvel arrendado.

Código do ativo imobiliário (Campo 5) - Campo que identifica o imóvel em função do país, sendo preenchido com:

Código que corresponde a sua estrutura matricial quando o país do imóvel é Portugal. Este código tem por base a estrutura XXXXXX.T.YYYYYY.ZZZZZZZZ.AAA sendo que, "XXXXXX" identifica o código da freguesia, "T" identifica o tipo de prédio ("U" para prédio urbano, "R" para prédio rústico e "O" para prédio omisso), "ZZZZZZZZ" identifica a fração ou secção de cada prédio (não podendo ser identificada mais do que uma fração ou secção, mesmo que respeitem ao mesmo artigo matricial) e "AAA" (exclusivamente para prédios rústicos, caso os elementos referentes a árvore/colónia façam parte da identificação matricial);

Código de registo que corresponde ao número de registo de imóvel cuja localização seja em país diferente de Portugal.

Descrição do ativo imobiliário (Campo 6) - Campo que identifica a natureza e a denominação do imóvel de acordo com o disposto no n.º 4 do artigo 78.º do Regulamento da CMVM n.º 2/2015.

Valor do ativo imobiliário (Campo 7) - Campo preenchido com o valor do imóvel em euros.

(ver documento original)

Bloco de informação n.º 4: Informação sobre as transações de ativos imobiliários (imóveis, direitos ou participações em sociedades imobiliárias) adquiridos ou vendidos no mês, com os seguintes campos:

Tipo de transação (Campo 1) - Campo que informa sobre o tipo de transação, sendo preenchido com

"C", Compra;

"V", Venda;

"PA", Permuta Adquirido;

"PC", Permuta Cedido.

País do ativo imobiliário (Campo 2) - Campo que informa sobre o país onde está localizado o ativo imobiliário no qual o OII detém a participação.

Código do ativo imobiliário (Campo 3) - Campo que identifica o imóvel, sendo preenchido com:

Código que corresponde a sua estrutura matricial quando o país do imóvel é Portugal. Este código tem por base a estrutura XXXXXX.T.YYYYYY.ZZZZZZZZ.AAA sendo que, "XXXXXX" identifica o código da freguesia, "T" identifica o tipo de prédio ("U" para prédio urbano, "R" para prédio rústico e "O" para prédio omisso), "ZZZZZZZZ" identifica a fração ou secção de cada prédio (não podendo ser identificada mais do que uma fração ou secção, mesmo que respeitem ao mesmo artigo matricial) e "AAA" (exclusivamente para prédios rústicos, caso os elementos referentes a árvore/colónia façam parte da identificação matricial);

Código de registo que corresponde ao número de registo de imóvel cuja localização seja em país diferente de Portugal.

Código LEI da Sociedade Imobiliária. Na ausência do código LEI, é preenchido com o respetivo número de identificação fiscal.

Descrição do ativo imobiliário (Campo 4) - Campo que identifica a natureza e a denominação do ativo imobiliário, sendo preenchido com:

Natureza e denominação no caso de imóvel ou direito, nos termos do disposto no n.º 4 do artigo 78.º do Regulamento da CMVM n.º 2/2015;

Denominação social da sociedade imobiliária, sem utilização de abreviaturas.

País da contraparte (Campo 5) - Campo que identifica o país de residência da contraparte da transação.

Código da contraparte (Campo 6) - Campo que identifica a contraparte na transação, sendo preenchido com:

Código LEI da entidade contraparte;

Número de identificação fiscal, não existindo código LEI.

Descrição da contraparte (Campo 7) - Campo preenchido com o nome ou denominação da contraparte, sem utilização de abreviaturas.

Tipo de contraparte (Campo 8) - Campo que identifica a relação da contraparte com a entidade responsável pela gestão, sendo preenchido com:

"SG", Contraparte é parte relacionada com a entidade responsável pela gestão;

"DP", Entidade participante é parte relacionada com o depositário;

"OUT", Entidade participante é parte relacionada com outra entidade prevista no artigo 147.º do RGOIC;

"OIC" Entidade participante corresponde a organismo de investimento coletivo objeto de reporte ou gerido por entidade que com ela se encontre em relação de grupo para efeitos de consolidação de contas, na aceção referida no n.º 13 do artigo 176.º do RGOIC;

"NA", caso a entidade participante não corresponda a nenhuma das entidades previstas no artigo 147.º do RGOIC.

Valor de avaliação 1 (Campo 9) - Campo que identifica o valor de uma das avaliações previstas na alínea b) do n.º 1 do artigo 144.º do RGOIC.

Data I (Campo 10) - Campo preenchido com a data da avaliação I.

Avaliador I (Campo 11) - Campo que identifica o avaliador I do ativo imobiliário e é preenchido com o respetivo n.º de perito responsável pela avaliação I.

Valor de avaliação II (Campo 12) - Campo que identifica o valor de uma das avaliações previstas na alínea b) do n.º 1 do artigo 144.º do RGOIC.

Data II (Campo 13) - Campo preenchido com a data da avaliação II.

Avaliador II (Campo 14) - Campo que identifica o avaliador II do ativo imobiliário e é preenchido com o respetivo n.º de perito responsável pela avaliação II.

Data do contrato promessa de compra e venda (Campo 15) - Campo que, caso exista, identifica a data relativa à celebração do contrato de promessa de compra e venda.

Data da transação (Campo 16) - Campo que identifica a data de transação do ativo imobiliário.

Valor da transação (Campo 17) - Campo preenchido com o valor da transação em euros.

Meio de pagamento (Campo 18) - Campo que identifica o meio de pagamento da transação sendo preenchido com:

"ESP", pagamento efetuado em espécie;

"NUM", pagamento efetuado em numerário;

"CHQ", pagamento em cheque;

"TRB", pagamento efetuado através de transferência bancária.

(ver documento original)

Bloco de informação n.º 5: Informação sobre os imóveis arrendados no mês, com os seguintes campos:

País do arrendatário (Campo 1) - Campo que identifica o país de residência do arrendatário.

Código do arrendatário (Campo 2) - Campo que identifica a entidade arrendatária e é preenchido com:

Código LEI da entidade arrendatária;

N.º de identificação fiscal, na ausência de código LEI.

Descrição do arrendatário (Campo 3) - Campo preenchido com o nome ou a denominação do arrendatário, sem utilização de abreviaturas.

País do ativo imobiliário (Campo 4) - Campo que identifica o país onde está localizado o imóvel.

Código do ativo imobiliário (Campo 5) - Campo que identifica o imóvel, sendo preenchido com:

Código que corresponde a sua estrutura matricial quando o país do imóvel é Portugal. Este código tem por base a estrutura XXXXXX.T.YYYYYY.ZZZZZZZZ.AAA sendo que, "XXXXXX" identifica o código da freguesia, "T" identifica o tipo de prédio ("U" para prédio urbano, "R" para prédio rústico e "O" para prédio omisso), "ZZZZZZZZ" identifica a fração ou secção de cada prédio (não podendo ser identificada mais do que uma fração ou secção mesmo que respeitem ao mesmo artigo matricial) e "AAA" (exclusivamente para prédios rústicos, caso os elementos referentes a árvore/colónia façam parte da identificação matricial);

Código de registo que corresponde ao número de registo de imóvel cuja localização seja em país diferente de Portugal.

Descrição do ativo imobiliário (Campo 6) - Campo preenchido com a natureza e a denominação do imóvel de acordo com o disposto no n.º 4 do artigo 78.º do Regulamento da CMVM n.º 02/2015.

Contrato de arrendamento (Campo 7) - Campo que identifica se os contratos de arrendamento são novos ou se apenas foram alterados, sendo a data de aquisição sendo considerada como data de arrendamento e sendo preenchido com:

"N" - Novo contrato de arrendamento;

"A" - Alteração de contrato de arrendamento já existente.

Data do arrendamento (Campo 8) - Campo que identifica a data de celebração ou de alteração do contrato de arrendamento vigente (data de aquisição considerada como a data de arrendamento.

Data de vencimento do contrato (Campo 9) - Campo que identifica a data de vencimento do contrato de arrendamento.

Valor da renda (Campo 10) - Campo preenchido com o valor da renda mensal contratada em euros.

Tipo de Opção (Campo 11) - Campo que regista a existência de uma opção sobre o imóvel pelo arrendatário ou OII, sendo preenchido com:

"C", opção de compra do imóvel pelo arrendatário;

"V", opção de venda do imóvel pelo OII.

Preço de exercício da opção (Campo 12) - Campo preenchido com o preço de exercício da opção em euros. É preenchido com "NA" quando não é determinável.

(ver documento original)

Bloco de informação n.º 6: Informação sobre as rendas e os valores de venda em mora, com os seguintes campos:

País do ativo imobiliário (Campo 1) - Campo que informa sobre o país onde está localizado o ativo imobiliário no qual o OII detém a participação.

Código do ativo imobiliário (Campo 2) - Campo que identifica o imóvel, sendo preenchido com:

Código que corresponde a sua estrutura matricial quando o país do imóvel é Portugal. Este código tem por base a estrutura XXXXXX.T.YYYYYY.ZZZZZZZZ.AAA sendo que, "XXXXXX" identifica o código da freguesia, "T" identifica o tipo de prédio ("U" para prédio urbano, "R" para prédio rústico e "O" para prédio omisso), "ZZZZZZZZ" identifica a fração ou secção de cada prédio (não podendo ser identificada mais do que uma fração ou secção mesmo que respeitem ao mesmo artigo matricial) e "AAA" (exclusivamente para prédios rústicos, caso os elementos referentes a árvore/colónia façam parte da identificação matricial);

Código de registo que corresponde ao número de registo de imóvel cuja localização seja em país diferente de Portugal.

Descrição do ativo imobiliário (Campo 3) - Campo preenchido com a natureza e a denominação do imóvel de acordo com o disposto no n.º 4 do artigo 78.º do Regulamento da CMVM n.º 02/2015.

Tipo de valor em dívida (Campo 4) - Campo que identifica o código de tipo de valor em divida sendo preenchido com:

"R", para um valor de dívida decorrente de renda;

"V", para um valor de dívida decorrente de venda.

País do devedor (Campo 5) - Campo preenchido com a identificação do país de residência do devedor.

Código do devedor (Campo 6) - Campo que identifica a entidade devedora, sendo preenchido com:

Código LEI da entidade contraparte;

Número de identificação fiscal, não existindo código LEI.

Descrição do devedor (Campo 7) - Campo preenchido com a natureza e a denominação do devedor, sem utilização de abreviaturas.

Valor em dívida (Campo 8) - Campo preenchido com o valor em dívida em euros.

Data de mora (Campo 9) - Campo preenchido com a data a partir da qual se gerou a situação de mora.

(ver documento original)

Bloco de informação n.º 7: Informação sobre os imóveis objeto de benfeitorias no mês, com os seguintes campos:

País do ativo imobiliário (Campo 1) - Campo que informa sobre o país onde está localizado o ativo imobiliário no qual o OII detém a participação.

Código do ativo imobiliário (Campo 2) - Campo que identifica o imóvel, sendo preenchido com:

Código que corresponde a sua estrutura matricial quando o país do imóvel é Portugal. Este código tem por base a estrutura XXXXXX.T.YYYYYY.ZZZZZZZZ.AAA sendo que, "XXXXXX" identifica o código da freguesia, "T" identifica o tipo de prédio ("U" para prédio urbano, "R" para prédio rústico e "O" para prédio omisso), "ZZZZZZZZ" identifica a fração ou secção de cada prédio (não podendo ser identificada mais do que uma fração ou secção mesmo que respeitem ao mesmo artigo matricial) e "AAA" (exclusivamente para prédios rústicos, caso os elementos referentes a árvore/colónia façam parte da identificação matricial);

Código de registo que corresponde ao número de registo de imóvel cuja localização seja em país diferente de Portugal.

Descrição do ativo imobiliário (Campo 3) - Campo preenchido com a natureza e a denominação do imóvel de acordo com o disposto no n.º 4 do artigo 78.º do Regulamento da CMVM n.º 02/2015.

Valor da benfeitoria (Campo 4) - Campo preenchido com o valor da benfeitoria reconhecido no mês (montante incorporado no valor de aquisição do imóvel refletido na correspondente subconta das rubricas 31 - Terrenos ou 32 - Construções do Plano de Contas dos OII.

(ver documento original)

Bloco de informação n.º 8: Informação sobre a constituição de depósitos (empréstimos) bancários no mês, com os seguintes campos:

País da instituição de crédito (Campo 1) - Campo que informa sobre o país onde está localizada a instituição de crédito onde o OII contratou o depósito (empréstimo).

Código da instituição de crédito (Campo 2) - Campo que identifica a instituição de crédito, sendo preenchido com:

Código LEI da entidade contraparte;

Número de identificação fiscal, não existindo código LEI.

Descrição da instituição de crédito (Campo 3) - Campo preenchido com a denominação da instituição de crédito onde foi constituído o depósito (empréstimo), de acordo com o disposto no n.º 4 do artigo 78.º do Regulamento da CMVM n.º 02/2015.

Tipo de depósito (Campo 4) - Campo que identifica o código de tipo de depósito (empréstimo), sendo preenchido com

"O", para um depósito à ordem;

"P", para um depósito a prazo;

"E", para um empréstimo;

"D", para um descoberto.

Data de constituição (Campo 5) - Campo preenchido com a data de constituição do depósito (empréstimo).

Data de vencimento (Campo 6) - Campo preenchido com a data de vencimento do depósito (empréstimo).

Código da moeda (Campo 7) - Campo preenchido com a moeda do depósito (empréstimo).

Valor do depósito (Campo 8) - Campo preenchido com o valor do depósito (empréstimo) em euros.

Valor da taxa de juro (Campo 9) - Campo preenchido com a percentagem da taxa de juro do depósito (empréstimo).

(ver documento original)

Bloco de informação n.º 9: Informação sobre os contratos de promessa de compra e de venda em vigor, com os seguintes campos:

Tipo de transação (Campo 1) - Campo que informa sobre o tipo de transação, sendo preenchido com:

"C", Compra;

"V", Venda;

"PA", Permuta Adquirido;

"PC", Permuta Cedido.

País do ativo imobiliário (Campo 2) - Campo que informa sobre o país onde está localizado o ativo imobiliário no qual o OII detém a participação.

Código do ativo imobiliário (Campo 3) - Campo que identifica o imóvel, sendo preenchido com:

Código que corresponde a sua estrutura matricial quando o país do imóvel é Portugal. Este código tem por base a estrutura XXXXXX.T.YYYYYY.ZZZZZZZZ.AAA sendo que, "XXXXXX" identifica o código da freguesia, "T" identifica o tipo de prédio ("U" para prédio urbano, "R" para prédio rústico e "O" para prédio omisso), "ZZZZZZZZ" identifica a fração ou secção de cada prédio (não podendo ser identificada mais do que uma fração ou secção, mesmo que respeitem ao mesmo artigo matricial) e "AAA" (exclusivamente para prédios rústicos, caso os elementos referentes a árvore/colónia façam parte da identificação matricial);

Código de registo que corresponde ao número de registo de imóvel cuja localização seja em país diferente de Portugal.

Descrição do ativo imobiliário (Campo 4) - Campo que identifica a natureza e a denominação do ativo imobiliário, sendo preenchido com:

Natureza e denominação no caso de imóvel ou direito, nos termos do disposto no n.º 4 do artigo 78.º do Regulamento da CMVM n.º 2/2015;

Denominação social da sociedade imobiliária, sem utilização de abreviaturas.

País da contraparte (Campo 5) - Campo que identifica o país de residência da contraparte da transação.

Código da contraparte (Campo 6) - Campo que identifica a contraparte na transação, sendo preenchido com:

Código LEI da entidade contraparte;

Número de identificação fiscal, não existindo código LEI.

Descrição da contraparte (Campo 7) - Campo preenchido com o nome ou denominação da contraparte, sem utilização de abreviaturas.

Tipo de contraparte (Campo 8) - Campo que identifica a relação da contraparte com a entidade responsável pela gestão, sendo preenchido com:

"SG", Contraparte é parte relacionada com a entidade responsável pela gestão;

"DP", Entidade participante é parte relacionada com o depositário;

"OUT", Entidade participante é parte relacionada com outra entidade prevista no artigo 147.º do RGOIC;

"OIC" Entidade participante corresponde a organismo de investimento coletivo objeto de reporte ou gerido por entidade que com ela se encontre em relação de grupo para efeitos de consolidação de contas, na aceção referida no n.º 13 do artigo 176.º do RGOIC;

"NA", caso a entidade participante não corresponda a nenhuma das entidades previstas no artigo 147.º do RGOIC.

Valor de avaliação 1 (Campo 9) - Campo que identifica o valor de uma das avaliações previstas na alínea b) do n.º 1 do artigo 144.º do RGOIC.

Data I (Campo 10) - Campo preenchido com a data da avaliação I.

Avaliador I (Campo 11) - Campo que identifica o avaliador I do ativo imobiliário e é preenchido com o respetivo n.º de perito responsável pela avaliação I.

Valor de avaliação II (Campo 12) - Campo que identifica o valor de uma das avaliações previstas na alínea b) do n.º 1 do artigo 144.º do RGOIC.

Data II (Campo 13) - Campo preenchido com a data da avaliação II.

Avaliador II (Campo 14) - Campo que identifica o avaliador II do ativo imobiliário e é preenchido com o respetivo n.º de perito responsável pela avaliação II.

Data do contrato promessa de compra e venda (Campo 15) - Campo que identifica a data de celebração do contrato de promessa de compra e venda.

Data prevista para celebração da escritura (Campo 16) - Campo preenchido com a última data em que, nos termos contratuais, a escritura pode ocorrer.

Valor adiantado (Campo 17) - Campo preenchido com o valor pago ou recebido, até à data, em euros.

Valor prometido (Campo 18) - Campo preenchido com o valor acordado transacionar em euros.

(ver documento original)

- *Alterado pelo/a Artigo 3.º do/a [Regulamento da CMVM n.º 6/2020 - Diário da República n.º 243/2020, Série II de 2020-12-16](https://diariodarepublica.pt/dr/detalhe/regulamento-cmvm/6-2020-151322794), em vigor a partir de 2021-07-01*

## Anexo 14 — Realização de operações sobre ativos admitidos à negociação em mercado regulamentado ou sistema de negociação multilateral, fora de mercado regulamentado

(informação prevista no artigo 79.º)

Designação da entidade responsável pela gestão:

Designação do organismo de investimento coletivo (OIC):

Cód. OIC:

(ver documento original)

208770198
