---
id: "regulamento-cmvm-3-2015-anexo-ii-informacao-relativa-a-composicao-da-carteira-e-aqui"
dre_id: "70890433"
title: "Regulamento da CMVM n.º 3/2015, de 3 de novembro — Anexo II — Informação relativa à composição da carteira e aquisição e alienação de…"
type: "Regulamento da CMVM"
number: "3/2015"
year: 2015
date: 2015-11-03
issuer: "Comissão do Mercado de Valores Mobiliários"
status: "em vigor"
text_version: "consolidado"
last_amended: 2020-12-16
source: "https://diariodarepublica.pt/dr/legislacao-consolidada/regulamento-cmvm/2015-216566448"
original_pdf: "https://files.diariodarepublica.pt/2s/2015/11/215000000/3175931763.pdf"
retrieved: 2026-10-21
summary: "Regulamento da CMVM n.º 3/2015 - Capital de Risco, Empreendedorismo Social e Investimento Alternativo Especializado (Revoga o Regulamento da CMVM n.º 1/2008 )"
legal_notice: "Texto consolidado sem valor legal. Confirma no Diário da República antes de o usares. Não substitui aconselhamento jurídico."
part_of: "regulamento-cmvm-3-2015"
part: "Anexo II — Informação relativa à composição da carteira e aquisição e alienação de…"
---

# Regulamento da CMVM n.º 3/2015, de 3 de novembro — Anexo II — Informação relativa à composição da carteira e aquisição e alienação de…

## Anexo II — Informação relativa à composição da carteira e aquisição e alienação de elementos patrimoniais dos organismos de investimento em capital de risco (OICR) [fundos de capital de risco (FCR) e sociedades de investimento em capital de risco (SICR)], sociedades gestoras de fundos de capital de risco (SGFCR), sociedades de capital de risco (SCR), sociedades de empreendedorismo social (SES) e fundos de empreendedorismo social (FES).

O presente Anexo é preenchido nos termos do Regulamento da CMVM n.º 3/2016.

Quanto ao nome do ficheiro:

(ver documento original)

Quanto à estrutura e conteúdo do ficheiro de dados:

As especificações técnicas relativas ao ficheiro "CRT" a enviar à CMVM constam do documento "2020_reporte_CRT_schemas.zip" ou em versões atualizadas do mesmo, disponível no sítio da internet da CMVM.

Opção de reporte com conteúdo

No conteúdo a reportar o elemento ConteudoReporte do cabeçalho deve conter a indicação "REPO" e o elemento identificador de reporte nulo do corpo do ficheiro não deve ser preenchido, sendo preenchidos os restantes elementos do corpo do ficheiro de acordo com as instruções infra.

Bloco de informação n.º 1: Informação sobre a carteira dos organismos de investimento em capital de risco (OICR), das sociedades de capital de risco (SCR), das sociedades gestoras de fundos de capital de risco (SGFCR), sociedades de empreendedorismo social (SES) e fundos de empreendedorismo social (FES), com os seguintes campos:

Código de categoria (Campo 1): Campo de preenchimento obrigatório que identifica o código de categoria do elemento patrimonial, sendo preenchido com o código de categoria da Tabela 1.

Código do elemento (Campo 2): Campo de preenchimento obrigatório que identifica o código do elemento patrimonial, sendo preenchido com:

Para instrumentos financeiros:

O International Standard Identification Number (ISIN), sempre que aplicável;

O Classification of Financial Instruments (CFI), não existindo ISIN;

"NA", para outros elementos patrimoniais que não sejam instrumentos financeiros.

Descrição (Campo 3): Campo de preenchimento obrigatório que identifica a designação do elemento patrimonial.

Mercado de admissão (Campo 4): Campo de preenchimento obrigatório que identifica o mercado onde o elemento patrimonial está admitido à negociação, sendo preenchido com:

Para instrumentos financeiros:

O Market Identifier Code (MIC), para instrumentos financeiros admitidos à negociação em plataformas de negociação (PN);

"XXXX", para instrumentos financeiros não admitidos em PN.

"NA", para outros elementos patrimoniais que não sejam instrumentos financeiros.

Código do emitente (Campo 5): Campo de preenchimento obrigatório que identifica o código da entidade visada pelo investimento em capital de risco, sendo preenchido com:

O Legal Entity Identifier (LEI), sempre que aplicável;

O número de identificação fiscal, não existindo LEI.

Grupo (Campo 6): Campo de preenchimento obrigatório que identifica se o elemento patrimonial é referente à mesma sociedade ou grupo de sociedades, para efeitos de consolidação de contas, de outros elementos patrimoniais da carteira, sendo preenchido com "G" seguido de um número sequencial, com início em "0001" para a primeira sociedade ou grupo de sociedades até "nnnnn" para a n-ésima sociedade ou grupo de sociedades a que o elemento patrimonial é referente.

Data de aquisição (Campo 7): Campo de preenchimento obrigatório que identifica a primeira data de aquisição do elemento patrimonial.

Valor de aquisição (Campo 8): Campo de preenchimento obrigatório que identifica o valor de aquisição à data a que respeita a informação, sendo preenchido com o valor a que o elemento patrimonial foi adquirido e refletindo as posteriores aquisições e alienações.

Fase de investimento (Campo 9): Campo de preenchimento obrigatório que identifica a fase de investimento à primeira entrada no capital da sociedade, sendo preenchido com:

"SSE", para seed capital, start-up ou early stage;

"EXP", para expansão;

"TUR", para turnaround;

"MBO", para management buy-out;

"MBI", para management buy-in;

"OUT", para outra fase de investimento.

Percentagem (Campo 10): Campo de preenchimento obrigatório que identifica a percentagem detida no capital da sociedade a que o elemento patrimonial é referente, sendo preenchido com:

Percentagem detida do capital social da participada, quando o código de categoria do campo 1 do bloco de informação n.º 1 for preenchido com CC01 a CC05 ou CC13;

Percentagem detida do ativo líquido da participada, para os elementos patrimoniais de CC01, CC06 a CC10 ou CC13.

Critério Valorimétrico (Campo 11): Campo de preenchimento obrigatório que identifica o critério valorimétrico utilizado na valorização do elemento patrimonial, sendo preenchido com:

"MER", para instrumentos financeiros admitidos em PN;

"AQU", para valor de aquisição;

"TMR", para transações materialmente relevantes efetuadas nos últimos doze meses face ao momento da avaliação;

"MUL", para múltiplos de sociedades comparáveis;

"DCF", para fluxos de caixa descontados;

"NAV", para net asset value, quando respeite a participações em organismos de investimento coletivo;

"OUT", para outros critérios internacionalmente reconhecidos.

Quantidade (Campo 12): Campo de preenchimento obrigatório que identifica a quantidade do elemento patrimonial, sendo preenchido com:

Número de unidades, quando o código de categoria do campo 1 do bloco de informação n.º 1 for preenchido com CC01 a CC05 ou CC13;

Valor nominal, quando o código de categoria do campo 1 do bloco de informação n.º 1 for preenchido com CC06 a CC10 ou CC13;

Número de contratos, quando o código de categoria do campo 1 do bloco de informação n.º 1 for preenchido com CC11 a CC13.

Código da moeda (Campo 13): Campo de preenchimento obrigatório que identifica o código da moeda em que o elemento patrimonial se encontra denominado.

Valor (Campo 14): Campo de preenchimento obrigatório que identifica o valor em carteira do elemento patrimonial em euros, sendo preenchido com um valor positivo ou negativo, consoante o valor contribua de modo positivo ou negativo para o valor líquido global do OICR ou FES ou para o capital próprio da SCR, SGFCR ou SES.

(ver documento original)

TABELA 1

Códigos de categoria dos elementos patrimoniais

(ver documento original)

Bloco de informação n.º 2: Informação sobre outros ativos e passivos na carteira dos OICR, SCR, SGFCR, SES e FES, com os seguintes campos:

Código de categoria (Campo 1): Campo de preenchimento obrigatório que identifica o código da categoria do ativo ou passivo, sendo preenchido com o código de categoria da Tabela 2.

Descrição (Campo 2): Campo de preenchimento obrigatório que identifica a designação do ativo ou passivo.

Código de moeda (Campo 3): Campo de preenchimento obrigatório que identifica o código de moeda em que o ativo ou passivo se encontra denominado.

Valor (Campo 4): Campo de preenchimento obrigatório que identifica o valor do ativo ou passivo em euros, sendo preenchido com um valor positivo ou negativo, consoante o valor contribua de modo positivo ou negativo para o valor líquido global do OICR ou FES ou para o capital próprio da SCR, SGFCR ou SES.

(ver documento original)

TABELA 2

Códigos de categoria de outros ativos e passivos

(ver documento original)

Bloco de informação n.º 3: Informação sobre os elementos extrapatrimoniais da carteira dos OICR, SCR, SGFCR, SES e FES, com os seguintes campos:

Código de categoria (Campo 1): Campo de preenchimento obrigatório que identifica o código de categoria do elemento extrapatrimonial, sendo preenchido com o código de categoria da Tabela 3.

Código do elemento (Campo 2): Campo de preenchimento obrigatório que identifica o código do elemento extrapatrimonial, sendo preenchido com:

O ISIN, sempre que aplicável;

O CFI, não existindo ISIN.

Descrição (Campo 3): Campo de preenchimento obrigatório que identifica a designação do elemento extrapatrimonial.

Objetivo (Campo 4): Campo de preenchimento obrigatório que identifica a finalidade subjacente à transação do elemento extrapatrimonial, sendo preenchido com:

"E", para beneficiar de diferenças entre o preço de compra e venda;

"H", para cobertura de risco.

Posição (Campo 5): Campo de preenchimento obrigatório que identifica a posição aberta do contrato, sendo preenchido com:

"C", para posições compradoras;

"V", para posições vendedoras.

Quantidade (Campo 6): Campo de preenchimento obrigatório que identifica a quantidade do elemento extrapatrimonial, sendo preenchido com o número de contratos.

Exposição (Campo 7): Campo de preenchimento obrigatório que identifica a exposição inerente ao elemento extrapatrimonial, sendo preenchido com o valor correspondente ao produto entre o número de contratos negociados, a unidade de negociação e o valor de mercado do ativo subjacente.

(ver documento original)

TABELA 3

Códigos de categoria de elementos extrapatrimoniais

(ver documento original)

Bloco de informação n.º 4: Informação adicional sobre a carteira, com os seguintes campos:

Valor líquido global do OICR ou capital próprio da entidade gestora (Campo 1): Campo de preenchimento obrigatório que identifica o valor líquido global dos OICR ou FES ou o valor do capital próprio da SCR, SGFCR ou SES, em euros.

Ativo sob gestão (Campo 2): Campo de preenchimento obrigatório que identifica o ativo sob gestão (AUM) do respetivo OICR ou FES ou o total do ativo sob gestão da SCR, SGFCR ou SES e dos OICR ou FES por si geridos, em euros, sendo calculado nos termos definidos no Regulamento Delegado (UE) n.º 231/2013 da Comissão de 19 de dezembro de 2012.

Ativos líquidos (Campo 4): Campo de preenchimento obrigatório que identifica o valor total de ativos líquidos, em euros; por ativos líquidos entendem-se os previstos no n.º 1 do artigo 416.º do Regulamento (UE) n.º 575/2013, excluindo a condição prevista na alínea d) do n.º 3 do referido artigo, e as disponibilidades e aplicações em outras instituições de crédito com prazo residual inferior a 30 dias ou mobilizáveis sem penalização num prazo máximo de 30 dias

(ver documento original)

Bloco de informação n.º 5: Informação sobre a aquisição e alienação de elementos patrimoniais da carteira, com os seguintes campos:

Tipo de operação (Campo 1): Campo de preenchimento obrigatório que identifica o tipo de operação, sendo preenchido com:

"AQ", para aquisição de elementos patrimoniais;

"AL", para alienação de elementos patrimoniais.

Código de categoria (Campo 2): Campo de preenchimento obrigatório que identifica o código da categoria do elemento patrimonial adquirido ou alienado, sendo preenchido com o código de categoria da Tabela 1.

Descrição (Campo 3): Campo de preenchimento obrigatório que identifica a designação do elemento patrimonial adquirido ou alienado.

Data da operação (Campo 4): Campo de preenchimento obrigatório que identifica a data de aquisição ou da alienação do elemento patrimonial.

Código do emitente (Campo 5): Campo de preenchimento obrigatório que identifica o código da entidade visada pelo elemento patrimonial, sendo preenchido com:

O LEI, sempre que aplicável;

O número de identificação fiscal, não existindo LEI.

Código da contraparte (Campo 6): Campo de preenchimento obrigatório que identifica o código da contraparte que alienou ou adquiriu o elemento patrimonial, sendo preenchido com:

Para operações executadas em plataformas de negociação, o respetivo MIC;

Para operações executadas fora de PN:

O LEI, sempre que aplicável;

O número de identificação fiscal, não existindo LEI.

Designação da contraparte (Campo 7): Campo que identifica a descrição da contraparte que alienou ou adquiriu o elemento patrimonial, sendo de preenchimento obrigatório quando a operação é executada fora de PN.

Jurisdição da contraparte (Campo 8): Campo que identifica o país de residência da contraparte que alienou ou adquiriu o elemento patrimonial, sendo de preenchido obrigatório quando a operação é executada fora de PN.

Valor de aquisição (Campo 9): Campo de preenchimento obrigatório que identifica o valor de aquisição do elemento patrimonial no caso do tipo de operação do campo 1 do bloco de informação n.º 5 ser "AL", sendo preenchido com o valor de aquisição do elemento patrimonial registado na carteira à data de alienação, em euros.

Valor em carteira (Campo 10): Campo de preenchimento obrigatório que identifica o valor do elemento patrimonial no caso do tipo de operação do campo 1 do bloco de informação n.º 5 ser "AL", sendo preenchido com o valor do elemento patrimonial registado na carteira à data de alienação, em euros.

Valor da operação (Campo 11): Campo de preenchimento obrigatório que identifica o valor de aquisição ou alienação do elemento patrimonial, em euros.

(ver documento original)

Bloco de informação n.º 6: Informação sobre o desreconhecimento de elementos patrimoniais da carteira, com os seguintes campos:

Código de categoria (Campo 1): Campo de preenchimento obrigatório que identifica o código do elemento patrimonial desreconhecido, sendo preenchido com o código de categoria da tabela 1.

Descrição (Campo 2): Campo de preenchimento obrigatório que identifica a designação do elemento patrimonial desreconhecido.

Data da operação (Campo 3): Campo de preenchimento obrigatório que identifica a data do desreconhecimento do elemento patrimonial.

Código do emitente (Campo 4): Campo de preenchimento obrigatório que identifica o código da entidade visada pelo elemento patrimonial, sendo preenchido com:

LEI, sempre que aplicável;

O número de identificação fiscal, não existindo LEI.

Valor de aquisição (Campo 5): Campo de preenchimento obrigatório que identifica o valor de aquisição do elemento patrimonial desreconhecido, sendo preenchido com o valor de aquisição à data do desreconhecimento, em euros.

Valor em carteira (Campo 6): Campo de preenchimento obrigatório que identifica o valor em carteira do elemento patrimonial desreconhecido, sendo preenchido com o valor em carteira à data do desreconhecimento, em euros.

(ver documento original)

- *Aditado pelo/a Artigo 5.º do/a [Regulamento da CMVM n.º 6/2020 - Diário da República n.º 243/2020, Série II de 2020-12-16](https://diariodarepublica.pt/dr/detalhe/regulamento-cmvm/6-2020-151322794), em vigor a partir de 2021-07-01*

## Título III — Comercialização

### Artigo 10.º — Investidores qualificados

1 - Para efeitos da comercialização por entidades que não estejam sujeitas às regras aplicáveis à atividade de intermediação financeira previstas no Código dos Valores Mobiliários, aprovado pelo Decreto-Lei n.º 486/99, de 13 de novembro, consideram-se investidores qualificados:

a) Os previstos no n.º 1 do artigo 30.º do Código dos Valores Mobiliários, aprovado pelo Decreto-Lei n.º 486/99, de 13 de novembro; e

b) Os investidores qualificados a pedido, nos termos dos números seguintes.

2 - O investidor não qualificado pode solicitar à entidade responsável pela gestão tratamento como investidor qualificado, para efeitos da subscrição de participações em um ou mais organismos de investimento em capital de risco e sociedades de capital de risco, em fundos de empreendedorismo social e sociedades de empreendedorismo social ou em organismos de investimento alternativo especializado, indicando-os.

3 - A satisfação da solicitação formulada nos termos do número anterior depende de avaliação prévia, a realizar, de forma documentada, pelas entidades referidas no n.º 1 que asseguram a comercialização, dos conhecimentos e experiência do interessado, pela qual se garanta que este tem capacidade para tomar as suas próprias decisões de investimento e que compreende os riscos associados ao investimento em capital de risco, empreendedorismo social ou investimento alternativo especializado.

4 - Para efeitos da avaliação prevista no número anterior, o interessado deve, no mínimo, respeitar dois dos seguintes requisitos:

a) Ter efetuado operações no mercado relevante para as atividades referidas no n.º 2 nos últimos 3 anos;

b) Dispor de uma carteira de instrumentos financeiros, incluindo também depósitos em numerário, que exceda (euro) 500 000;

c) Prestar ou ter prestado funções na área financeira, durante, pelo menos, dois anos, em cargo que exija conhecimento dos serviços ou operações em causa.

5 - Nos casos em que a solicitação tenha sido apresentada por pessoa coletiva, a avaliação prevista no n.º 3 e a relativa ao requisito mencionado na alínea c) do número anterior são feitas relativamente ao responsável pelas atividades de investimento da requerente.

6 - A solicitação de tratamento como investidor qualificado observa os seguintes procedimentos:

a) O interessado solicita à entidade responsável pela gestão, por escrito, tratamento como investidor qualificado;

b) Realizada a avaliação prevista no n.º 3, a entidade responsável pela gestão deve informar o interessado, por escrito, do deferimento do pedido e das consequências da sua qualificação;

c) Recebida tal informação, o interessado deve declarar, por escrito, em documento autónomo, que está ciente das consequências da sua opção.

7 - Compete ao investidor que tenha solicitado tratamento como investidor qualificado manter a entidade responsável pela gestão informada sobre qualquer alteração suscetível de afetar os pressupostos que conduziram à sua qualificação.

8 - A entidade responsável pela gestão que tome conhecimento que um investidor deixou de satisfazer os requisitos de qualificação deve informá-lo que, se não comprovar a manutenção dos requisitos, dentro do prazo por aquela determinado, é tratado como investidor não qualificado.

9 - Sem prejuízo de exigências legais e regulamentares mais rigorosas, as entidades responsáveis pela gestão conservam em arquivo, pelo prazo mínimo de cinco anos, todos os documentos relevantes para efeitos de qualificação do investidor.

### Artigo 11.º — Entidades comercializadoras

1 - Podem ser entidades comercializadoras de unidades de participação:

a) As entidades responsáveis pela gestão;

b) Os depositários;

c) Os intermediários financeiros registados junto da CMVM para o exercício das atividades de colocação em ofertas públicas de distribuição ou de receção e transmissão de ordens por conta de outrem.

2 - As relações entre a entidade responsável pela gestão e as entidades comercializadoras regem-se por contrato escrito.

3 - As entidades comercializadoras respondem perante os participantes pelos danos causados no exercício da sua atividade.

4 - As entidades comercializadoras disponibilizam aos investidores toda a informação que para o efeito lhes seja remetida pela entidade responsável pela gestão.

### Artigo 12.º — Comercialização junto de investidores não qualificados

1 - Os fundos de empreendedorismo social e as sociedades de empreendedorismo social podem ser comercializados junto de investidores não qualificados, desde que estes:

a) Invistam um montante máximo de (euro) 5 000;

b) Declarem por escrito que estão conscientes dos riscos associados ao investimento previsto.

2 - Os requisitos previstos nas alíneas do número anterior não são aplicáveis aos investimentos feitos por dirigentes, diretores ou empregados que participem nas atividades de gestão de fundos ou sociedades de empreendedorismo social quando invistam nos fundos ou sociedades por si geridos.

## Anexo III — Informação relativa ao capital e participantes dos Organismos de Investimento em Capital de Risco (OICR) [Fundos de Capital de Risco (FCR) e Sociedades de Investimento em Capital de Risco (SICR)], fundos de empreendedorismo social (FES) e organismos de investimento alternativo especializado (OIAE), incluindo os OIAE de créditos.

O presente Anexo é preenchido nos termos do Regulamento da CMVM n.º 3/2016.

Quanto ao nome do ficheiro:

(ver documento original)

Quanto à estrutura e conteúdo do ficheiro de dados:

As especificações técnicas relativas ao ficheiro "CEP" a enviar à CMVM constam do documento "2020_reporte_CEP_schemas.zip" ou em versões atualizadas do mesmo, disponível no sítio da internet da CMVM.

Opção de reporte com conteúdo

No conteúdo a reportar o elemento ConteudoReporte do cabeçalho deve conter a indicação "REPO" e o elemento identificador de reporte nulo do corpo do ficheiro não deve ser preenchido, sendo preenchidos os restantes elementos do corpo do ficheiro de acordo com as instruções infra.

Bloco de informação n.º 1: Informação sobre o capital dos fundos de capital de risco (FCR), sociedades de investimento em capital de risco (SICR), fundos de empreendedorismo social (FES) e organismos de investimento alternativo especializado (OIAE), incluindo os OIAE de créditos, com os seguintes campos:

Categoria de unidades de participação (Campo 1): Campo de preenchimento obrigatório que identifica as diferentes categorias de unidades de participação, sendo preenchido com:

"C", seguido de 1 ou 2 carateres, que correspondem à identificação da categoria nos documentos constitutivos;

"NA", sempre que não existam categorias de unidades de participação.

Capital subscrito (Campo 2): Campo de preenchimento obrigatório que identifica o valor do capital subscrito, imputado à respetiva categoria de unidades de participação, à data do reporte, em euros.

Capital realizado (Campo 3): Campo de preenchimento obrigatório que identifica o valor do capital realizado, imputado à respetiva categoria de unidades de participação, à data do reporte, em euros.

Valor líquido global (Campo 4): Campo de preenchimento obrigatório que identifica o VLGF do FCR, SICR, FES e OIAE, incluindo OIAE de créditos, imputado à respetiva categoria de unidades de participação, em euros.

Devolução de capital realizado (Campo 5): Campo de preenchimento obrigatório que identifica o valor acumulado das devoluções de capital realizado efetuadas ao longo da vida do FCR, SICR, FES e OIAE, incluindo OIAE de créditos, imputado à respetiva categoria de unidades de participação, em euros.

Distribuição de rendimentos (Campo 6): Campo de preenchimento obrigatório que identifica o valor acumulado das distribuições de rendimentos efetuados ao longo da vida do FCR, SICR, FES e OIAE, incluindo OIAE de créditos, imputado à respetiva categoria de unidades de participação, em euros.

Quantidade (Campo 7): Campo de preenchimento obrigatório que identifica o número de unidades de participação em circulação de cada categoria de unidades de participação.

(ver documento original)

Bloco de informação n.º 2: Informação sobre os participantes dos FCR, SICR, FES e OIAE, incluindo OIAE de créditos, com os seguintes campos:

Categoria de unidades de participação (Campo 1): Campo de preenchimento obrigatório que identifica as diferentes categorias de unidades de participação, sendo preenchido com:

"C", seguido de 1 ou 2 carateres, que correspondem à identificação da categoria nos documentos constitutivos;

"NA", sempre que não existam categorias de unidades de participação.

Tipo (Campo 2): Campo de preenchimento obrigatório que identifica o tipo de participante, sendo preenchido com um dos seguintes códigos:

"NP", para participantes não profissionais;

"PR", para participantes profissionais;

"CE", para contrapartes elegíveis.

Residência (Campo 3): Campo de preenchimento obrigatório que identifica a residência do participante, sendo preenchido com um dos seguintes códigos:

"R", para participantes residentes em Portugal;

"N", para outros participantes.

Número (Campo 4): Campo de preenchimento obrigatório que identifica o número de participantes, sendo preenchido com o número de cada combinação de tipo e residência do participante.

Quantidade (Campo 5): Campo de preenchimento obrigatório que identifica o número de unidades de participação, sendo preenchido com o número de cada combinação de tipo e residência do participante.

(ver documento original)

- *Aditado pelo/a Artigo 5.º do/a [Regulamento da CMVM n.º 6/2020 - Diário da República n.º 243/2020, Série II de 2020-12-16](https://diariodarepublica.pt/dr/detalhe/regulamento-cmvm/6-2020-151322794), em vigor a partir de 2021-07-01*

## Título IV — Informação

### Artigo 13.º — Regulamento interno

O regulamento interno das sociedades de capital de risco e das sociedades de empreendedorismo social prevê, pelo menos, o seguinte:

a) As regras gerais de funcionamento da sociedade;

b) A política de investimento, quando a sociedade gira carteira própria;

c) As regras de avaliação de ativos;

d) Os procedimentos de investimento e de desinvestimento;

e) A subcontratação de funções;

f) Os procedimentos de prevenção do branqueamento de capitais, de gestão e mitigação de conflitos de interesse e de gestão e controlo de riscos; e

g) Informação sobre a política de acompanhamento das entidades participadas.

### Artigo 14.º — Informação aos investidores

1 - As entidades gestoras de fundos de capital de risco previstas no n.º 2 do artigo 17.º do Regime Jurídico e as sociedades de capital de risco prestam de forma clara e compreensível aos respetivos investidores, antes de estes tomarem decisões de investimento, a informação prevista no artigo 13.º do Regulamento (UE) n.º 345/2013, com as necessárias adaptações.

2 - As entidades gestoras de fundos de empreendedorismo social previstas no n.º 5 do artigo 4.º do Regime Jurídico e as sociedades de empreendedorismo social prestam de forma clara e compreensível aos respetivos investidores, antes de estes tomarem decisões de investimento, a informação prevista no artigo 14.º do Regulamento (UE) n.º 346/2013.

3 - Além da informação prevista no n.º 3 do artigo 5.º do Regime Jurídico, as entidades responsáveis pela gestão de organismos de investimento alternativo especializado disponibilizam aos investidores, de acordo com os respetivos documentos constitutivos e antes de efetuado o investimento nesses organismos, informação quanto aos riscos inerentes aos ativos em que os organismos investem.

4 - Nos OIAE de créditos a informação prévia aos investidores, prestada nos termos do artigo 221.º do Regime Geral dos Organismos de Investimento Coletivo, inclui menção sobre os riscos decorrentes do investimento em créditos e sobre a natureza não garantida do investimento num OIAE de créditos, bem como à possibilidade de iliquidez e perdas no investimento.

- *Alterado pelo/a Artigo 2.º do/a [Regulamento da CMVM n.º 5/2020 - Diário da República n.º 82/2020, Série II de 2020-04-27](https://diariodarepublica.pt/dr/detalhe/regulamento-cmvm/5-2020-132513579), em vigor a partir de 2020-04-28*

### Artigo 15.º — Deveres de informação

1 - As entidades gestoras de fundos de capital de risco e de fundos de empreendedorismo social, em relação a cada fundo gerido, as sociedades de investimento em capital de risco, as sociedades gestoras fundos de capital de risco, as sociedades de capital de risco e as sociedades de empreendedorismo social enviam semestralmente à CMVM, até ao final do segundo mês a que informação respeite, a informação relativa à composição da carteira e aquisição e alienação de elementos patrimoniais, nos termos previstos no Anexo II ao presente regulamento.

2 - As entidades gestoras de fundos de capital de risco, de fundos de empreendedorismo social e de fundos de investimento alternativo especializado e as sociedades gestoras fundos de capital de risco, em relação a cada fundo gerido, as sociedades de investimento em capital de risco e as sociedades de investimento alternativo especializado, enviam semestralmente à CMVM, até ao final do segundo mês a que informação respeite, a informação relativa ao capital e participantes, nos termos previstos no Anexo III ao presente regulamento.

3 - As entidades gestoras de fundos de capital de risco, de fundos de empreendedorismo social e de fundos de investimento alternativo especializado e as sociedades gestoras fundos de capital de risco, em relação a cada fundo gerido, as sociedades de investimento em capital de risco e as sociedades de investimento alternativo especializado, heterogeridas, enviam semestralmente à CMVM, até ao final do segundo mês a que informação respeite, o balanço e demonstração de resultados, nos termos previstos no Anexo IV ao presente regulamento.

4 - As entidades referidas no n.º 2 do artigo 17.º do Regime Jurídico que não sejam sociedades de capital de risco prestam anualmente à CMVM as informações constantes do artigo 13.º do Regime Jurídico nos termos ali previstos.

- *Alterado pelo/a Artigo 4.º do/a [Regulamento da CMVM n.º 6/2020 - Diário da República n.º 243/2020, Série II de 2020-12-16](https://diariodarepublica.pt/dr/detalhe/regulamento-cmvm/6-2020-151322794), em vigor a partir de 2021-07-01*

### Artigo 16.º — Relatório e contas

As entidades gestoras dos fundos de capital de risco, de fundos de empreendedorismo social e de fundos de investimento alternativo especializado, em relação a cada fundo gerido, as sociedades de investimento em capital de risco e as sociedades de investimento alternativo especializado, heterogeridas, enviam anualmente à CMVM, até ao dia 31 de maio do ano subsequente a que a informação respeite:

a) O relatório e contas, nos termos previstos no Anexo V ao presente regulamento;

b) (Revogada.)

c) Relatório de auditoria, nos termos previstos no Anexo VI ao presente regulamento;

d) (Revogada.)

e) (Revogada.)

- *Alterado pelo/a Artigo 4.º do/a [Regulamento da CMVM n.º 6/2020 - Diário da República n.º 243/2020, Série II de 2020-12-16](https://diariodarepublica.pt/dr/detalhe/regulamento-cmvm/6-2020-151322794), em vigor a partir de 2021-07-01*

### Artigo 16.º-A — Informação relativa a OIAE de créditos

A informação anual relativa ao OIAE de créditos, prestada nos termos do n.º 2 do artigo 15.º e do artigo 16.º, inclui:

a) A desagregação dos créditos detidos pelo OIAE de créditos em dívida preferencial garantida, dívida subordinada e dívida intercalar;

b) A desagregação entre os créditos reembolsados de acordo com um plano de pagamentos e os créditos reembolsados numa única prestação;

c) A desagregação do rácio entre o valor do empréstimo e o valor da garantia para cada um dos créditos detidos pelo OIAE de créditos;

d) Informação relativa a exposições em incumprimento e a situações de renegociação, reestruturação e prorrogação de créditos;

e) Alterações significativas à avaliação do crédito e procedimentos de monitorização.

- *Aditado pelo/a Artigo 3.º do/a [Regulamento da CMVM n.º 5/2020 - Diário da República n.º 82/2020, Série II de 2020-04-27](https://diariodarepublica.pt/dr/detalhe/regulamento-cmvm/5-2020-132513579), em vigor a partir de 2020-04-28*

### Artigo 17.º — Envio do Regulamento de Gestão

As entidades gestoras de fundos de capital de risco, de empreendedorismo social e de fundos de investimento alternativo especializado, as sociedades gestoras de fundos de capital de risco, as sociedades de investimento em capital de risco e as sociedades de investimento alternativo especializado, enviam à CMVM, nos termos previstos no Anexo VII ao presente regulamento, o regulamento de gestão atualizado, no prazo de 15 dias a contar da data da sua aprovação ou respetiva alteração

- *Alterado pelo/a Artigo 4.º do/a [Regulamento da CMVM n.º 6/2020 - Diário da República n.º 243/2020, Série II de 2020-12-16](https://diariodarepublica.pt/dr/detalhe/regulamento-cmvm/6-2020-151322794), em vigor a partir de 2021-07-01*

## Anexo IV — Informação financeira relativa ao balanço e demonstração dos resultados dos fundos de capital de risco (FCR), sociedades de investimento em capital de risco (SICR) heterogeridas, fundos de empreendedorismo social (FES), fundos de investimento alternativo especializado (FIAE), sociedades de investimento alternativo especializado (SIAE) heterogeridas e organismos de investimento alternativo especializado (OIAE), incluindo os OIAE de créditos.

O presente Anexo é preenchido nos termos do Regulamento da CMVM n.º 3/2016.

Quanto ao nome do ficheiro:

(ver documento original)

Quanto à estrutura e conteúdo do ficheiro de dados:

As especificações técnicas relativas ao ficheiro "DFI" a enviar à CMVM constam do documento "2020_reporte_DFI_schemas.zip" ou em versões atualizadas do mesmo, disponível no sítio da internet da CMVM.

Opção de reporte com conteúdo

No conteúdo a reportar o elemento ConteudoReporte do cabeçalho deve conter a indicação "REPO" e o elemento identificador de reporte nulo do corpo do ficheiro não deve ser preenchido, sendo preenchidos os restantes elementos do corpo do ficheiro de acordo com as instruções infra.

Bloco de informação n.º 1: Informação sobre as rubricas de balanço dos fundos de capital de risco (FCR), sociedades de investimento em capital de risco (SICR) heterogeridas, fundos de empreendedorismo social (FES), fundos de investimento alternativo especializado (FIAE), sociedades de investimento alternativo especializado (SIAE) heterogeridas e organismos de investimento alternativo especializado (OIAE), incluindo os OIAE de créditos, com os seguintes campos:

Código de conta (Campo 1): Campo de preenchimento obrigatório que identifica o código de conta, sendo preenchido de acordo com o código de conta da Tabela 1.

Valor de conta (Campo 2): Campo de preenchimento obrigatório que identifica o saldo da conta no final de cada período de reporte, sendo preenchido com um valor positivo para as rubricas de ativo e passivo, e com um valor positivo ou negativo para as rubricas de capital próprio.

(ver documento original)

TABELA 1

Códigos de conta das rubricas de balanço

(ver documento original)

Bloco de informação n.º 2: Informação sobre as rubricas da demonstração dos resultados dos FCR, SICR heterogeridas, FES, FIAE, SIAE heterogeridas e OIAE, incluindo OIAE de créditos, com os seguintes campos:

Código de conta (Campo 1): Campo de preenchimento obrigatório que identifica o código de conta, sendo preenchido de acordo com o código de conta da Tabela 2.

Valor de conta (Campo 2): Campo de preenchimento obrigatório que identifica o saldo da conta no final de cada período de reporte, sendo preenchido com um valor positivo ou negativo, consoante a rubrica contribua de modo positivo ou negativo para o resultado líquido do exercício.

(ver documento original)

TABELA 2

Código de conta das rubricas da demonstração dos resultados

(ver documento original)

- *Aditado pelo/a Artigo 5.º do/a [Regulamento da CMVM n.º 6/2020 - Diário da República n.º 243/2020, Série II de 2020-12-16](https://diariodarepublica.pt/dr/detalhe/regulamento-cmvm/6-2020-151322794), em vigor a partir de 2021-07-01*

## Título V — Vicissitudes

### Artigo 18.º — Fusão

1 - A fusão de dois ou mais organismos de investimento em capital de risco, de fundos de empreendedorismo social e de organismos de investimento alternativo especializado, pode realizar-se:

a) Por incorporação de um ou mais organismos, realizada mediante a transferência total do património de um ou mais organismos para o organismo incorporante, com extinção dos organismos incorporados;

b) Por constituição de um novo organismo, para o qual se transfere a totalidade do património dos organismos objeto de fusão, com a extinção dos mesmos.

2 - A fusão de organismos está sujeita a:

a) Comunicação subsequente à CMVM, no prazo de 15 dias após a produção dos seus efeitos, no caso de organismos de investimento exclusivamente dirigidos a investidores qualificados.

b) Comunicação prévia à CMVM, com uma antecedência de 30 dias face à produção dos seus efeitos, no caso dos demais organismos de investimento.

3 - O processo de fusão é instruído e remetido à CMVM com os seguintes elementos:

a) O projeto da fusão, devidamente aprovado em assembleias de participantes dos organismos incorporados e do organismo incorporante, contendo designadamente a seguinte informação:

i) A modalidade, os motivos, as condições e os objetivos da fusão, relativamente a todos os organismos envolvidos;

ii) A data prevista para a produção de efeitos da fusão;

iii) A demonstração da compatibilidade do organismo incorporante ou do novo organismo, consoante os casos, com a respetiva política de investimento e valorização dos ativos;

iv) O balanço de cada um dos organismos intervenientes, donde conste designadamente o valor dos elementos do ativo e do passivo a transferir para o organismo incorporante ou para o novo organismo;

v) Os critérios adotados na avaliação dos ativos e passivos e justos valores utilizados;

vi) A demonstração da relação de troca das unidades de participação ou das ações;

vii) Os critérios de atribuição das unidades de participação ou de ações aos participantes do organismo que resultar da fusão;

viii) Os direitos assegurados pelo organismo incorporante ou pelo novo organismo aos participantes do organismo incorporado que possuam direitos especiais;

ix) A data a partir da qual as operações dos organismos são consideradas, do ponto de vista contabilístico, como efetuadas por conta do organismo incorporante ou do novo organismo;

x) A versão atualizada do regulamento de gestão ou do regulamento interno do organismo incorporante;

xi) Parecer dos revisores oficiais de contas dos organismos envolvidos na fusão;

xii) Relatório de auditor independente registado na CMVM sobre o projeto de fusão, designadamente sobre as matérias enunciadas nas alíneas v), vi) e vii).

b) As declarações de concordância de cada um dos depositários envolvidos na fusão;

c) A aprovação da fusão pelas assembleias de participantes dos organismos envolvidos na fusão, nos casos das operações referidas na alínea a) do n.º 2;

d) Os elementos necessários à constituição do novo organismo, no caso previsto na alínea b) do n.º 1, nomeadamente os documentos constitutivos;

e) A data de produção de efeitos, nos casos das operações referidas na alínea a) do n.º 2.

4 - O balanço referido na subalínea iv) da alínea a) do número anterior pode ser:

a) O balanço do último exercício, desde que tenha sido encerrado nos seis meses anteriores à data do projeto de fusão;

b) Um balanço reportado a uma data que não anteceda o trimestre anterior à data do projeto de fusão.

5 - A fusão produz efeitos na data da subscrição das unidades de participação ou das ações do organismo incorporante, sendo igualmente essa a data relevante para o cálculo dos termos de troca das unidades de participação ou das ações do organismo incorporado por unidades de participação ou por ações do organismo incorporante e, se aplicável, para a determinação do valor patrimonial líquido para os pagamentos em dinheiro.

6 - Os participantes que votarem contra a operação de fusão podem solicitar o reembolso das unidades de participação ou das ações, podendo este direito ser exercido até cinco dias úteis antes da data da produção dos efeitos da fusão.

### Artigo 19.º — Cisão

É aplicável à cisão de organismos de investimento em capital de risco, de fundos de empreendedorismo social e de organismos de investimento alternativo especializado, com as necessárias adaptações, o disposto relativamente à fusão.

## Anexo V — Informação relativa aos documentos de prestação de contas anuais dos fundos de capital de risco (FCR), sociedades de investimento em capital de risco (SICR) heterogeridas, fundos de empreendedorismo social (FES), sociedades de investimento alternativo especializado (SIAE) heterogeridas, fundos de investimento alternativo especializado (FIAE) e organismos de investimento alternativo especializado (OIAE), incluindo os OIAE de créditos.

O presente Anexo é preenchido nos termos do Regulamento da CMVM n.º 3/2016.

Quanto ao nome do ficheiro:

(ver documento original)

- *Aditado pelo/a Artigo 5.º do/a [Regulamento da CMVM n.º 6/2020 - Diário da República n.º 243/2020, Série II de 2020-12-16](https://diariodarepublica.pt/dr/detalhe/regulamento-cmvm/6-2020-151322794), em vigor a partir de 2021-07-01*

## Título VI — Disposições finais

### Artigo 20.º — Entrada em vigor

O presente regulamento entra em vigor no dia seguinte ao da sua publicação.

15 de outubro de 2015. - O Presidente do Conselho de Administração, Carlos Tavares. - O Vogal do Conselho de Administração, Carlos Alves.

209048254

## Anexo VI — Informação relativa ao relatório de auditoria (RDA) dos fundos de capital de risco (FCR), sociedades de investimento em capital de risco (SICR) heterogeridas, fundos de empreendedorismo social (FES), sociedades de investimento alternativo especializado (SIAE) heterogeridas, fundos de investimento alternativo especializado (FIAE) e organismos de investimento alternativo especializado (OIAE), incluindo os OIAE de créditos.

O presente Anexo é preenchido nos termos do Regulamento da CMVM n.º 3/2016.

Quanto ao nome do ficheiro:

(ver documento original)

Quanto à estrutura e conteúdo do ficheiro de dados:

As especificações técnicas relativas ao ficheiro "RDA" a enviar à CMVM constam do documento "2020_reporte_RDA_schemas.zip" ou em versões atualizadas do mesmo, disponível no sítio da internet da CMVM.

Opção de reporte com conteúdo

No conteúdo a reportar o elemento ConteudoReporte do cabeçalho deve conter a indicação "REPO" e o elemento identificador de reporte nulo do corpo do ficheiro não deve ser preenchido, sendo preenchidos os restantes elementos do corpo do ficheiro de acordo com as instruções infra.

Bloco de informação n.º 1: Informação sobre o conteúdo do relatório de auditoria (RDA) dos fundos de capital de risco (FCR), sociedades de investimento em capital de risco (SICR) heterogeridas, fundos de empreendedorismo social (FES), sociedades de investimento alternativo especializado (SIAE) heterogeridas, fundos de investimento alternativo especializado (FIAE) e organismos de investimento alternativo especializado (OIAE), incluindo os OIAE de créditos, com os seguintes campos:

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

- *Aditado pelo/a Artigo 5.º do/a [Regulamento da CMVM n.º 6/2020 - Diário da República n.º 243/2020, Série II de 2020-12-16](https://diariodarepublica.pt/dr/detalhe/regulamento-cmvm/6-2020-151322794), em vigor a partir de 2021-07-01*

## Anexo VII — Informação relativa ao regulamento de gestão dos organismos de investimento em capital de risco (OICR) [Fundos de Capital de Risco (FCR) e Sociedades de Investimento em Capital de Risco (SICR)], fundos de empreendedorismo social (FES) e organismos de investimento alternativo especializado (OIAE), incluindo OIAE de créditos.

O presente Anexo é preenchido nos termos do Regulamento da CMVM n.º 3/2016.

Quanto ao nome do ficheiro:

(ver documento original)

- *Aditado pelo/a Artigo 5.º do/a [Regulamento da CMVM n.º 6/2020 - Diário da República n.º 243/2020, Série II de 2020-12-16](https://diariodarepublica.pt/dr/detalhe/regulamento-cmvm/6-2020-151322794), em vigor a partir de 2021-07-01*

## Anexo — Informação instrutória relativa ao pedido de autorização de Sociedade Gestora de Fundos de Capital de Risco e Sociedade de Investimento em Capital de Risco

(informação prevista no artigo 1.º-A)

O programa de atividades inclui os seguintes elementos:

a) Informação financeira previsional relativa aos três primeiros anos de atividade, agregada e discriminada por área geográfica e por cada atividade para que se pretende obter autorização;

b) Pressupostos da informação financeira previsional, bem como a explicação detalhada dos dados e números apresentados;

c) Relativamente à estrutura organizacional:

(i) Organograma e respetiva descrição organizacional, em particular os sistemas de governação e de controlo interno, os procedimentos de tomada de decisão, os níveis hierárquicos, as linhas de responsabilidade e os canais de relato e de comunicação interna e externa;

(ii) Funções de cada departamento, serviço ou área funcional e o respetivo número de recursos humanos medidos pela disponibilidade;

(iii) Sistemas, políticas e procedimentos adotados para cumprir os requisitos de controlo interno, gestão de riscos e auditoria interna;

(iv) Políticas e procedimentos adotados para cumprir os requisitos relativos à identificação, prevenção, gestão e acompanhamento da ocorrência de conflitos de interesses;

(v) Modelo de risco e políticas e procedimentos adotados para cumprir os requisitos relativos à prevenção da prática do branqueamento de capitais e do financiamento ao terrorismo;

(vi) Políticas e procedimentos adotados para cumprir os requisitos relativos à avaliação de ativos.

d) Relativamente à informação sobre meios humanos, técnicos e materiais:

(i) Nome completo dos titulares dos órgãos sociais e informação sobre a distribuição de pelouros, a exclusividade, a disponibilidade e a discriminação entre membros executivos e não executivos e entre residentes e não residentes em Portugal;

(ii) Nome completo sobre as pessoas responsáveis pela gestão do investimento, controlo interno, gestão de riscos, auditoria interna, prevenção de branqueamento de capitais e financiamento ao terrorismo, avaliação independente de ativos, e informação, para cada uma delas, sobre a exclusividade, a disponibilidade e informação que permita demonstrar a sua experiência, qualificação e competência para o desempenho da função;

(iii) Identificação das aplicações informáticas utilizadas no exercício da atividade, bem como dos procedimentos de segurança da informação.

- *Aditado pelo/a Artigo 4.º do/a [Regulamento da CMVM n.º 5/2020 - Diário da República n.º 82/2020, Série II de 2020-04-27](https://diariodarepublica.pt/dr/detalhe/regulamento-cmvm/5-2020-132513579), em vigor a partir de 2020-04-28*
