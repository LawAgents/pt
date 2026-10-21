---
id: "regulamento-cmvm-2-2015-anexo-25-gestao-de-carteiras-por-conta-de-outrem-a-anexo-28"
dre_id: "69828456"
title: "Regulamento da CMVM n.º 2/2015, de 17 de julho — Anexo 25 — Gestão de carteiras por conta de outrem a Anexo 28 — Modelo de divulgação da…"
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
part: "Anexo 25 — Gestão de carteiras por conta de outrem a Anexo 28 — Modelo de divulgação da…"
---

# Regulamento da CMVM n.º 2/2015, de 17 de julho — Anexo 25 — Gestão de carteiras por conta de outrem a Anexo 28 — Modelo de divulgação da…

## Anexo 25 — Gestão de carteiras por conta de outrem

O presente Anexo é preenchido nos termos do Regulamento da CMVM n.º 3/2016.

Quanto ao nome do ficheiro:

(ver documento original)

Quanto à estrutura e conteúdo do ficheiro de dados:

As especificações técnicas relativas ao ficheiro "CCG" a enviar à CMVM constam do documento "2020_reporte_CCG_schemas.zip" ou em versões atualizadas do mesmo, disponível no sítio da internet da CMVM."

I - Opção de reporte perante inexistência de informação ("reporte nulo")

Na inexistência de informação a enviar para determinado período de referência, o presente ficheiro é enviado à CMVM com a indicação de "NULO" nos elementos ConteudoReporte do cabeçalho e no elemento identificador de reporte nulo do corpo do ficheiro.

Nesta circunstância todos os restantes elementos do corpo do ficheiro não devem ter conteúdo.

II - Opção de reporte com conteúdo

Existindo conteúdo a reportar o elemento ConteudoReporte do cabeçalho deve conter a indicação "REPO" e o elemento identificador de reporte nulo do corpo do ficheiro não deve ser preenchido, sendo preenchidos os restantes elementos do corpo do ficheiro de acordo com as instruções infra.

Bloco de informação n.º 1: Informação sobre o perfil de carteira definido nos contratos de gestão de carteiras e/ou condições particulares celebrados com os clientes, com os seguintes campos:

Código de identificação de perfil de carteira (Campo 1): Campo que identifica, de forma unívoca, o código do perfil de carteira definido nos contratos de gestão de carteiras e/ou condições particulares celebrados com os clientes. É preenchido com um código interno definido pela entidade que presta a atividade de gestão de carteiras por conta de outrem e é repetido nos reportes subsequentes enquanto este perfil estiver em vigor. Caso se trate de um perfil de carteira que não se enquadre em qualquer dos perfis padronizados é preenchido com o código "PNP".

Designação de perfil de carteira (Campo 2): Denominação do perfil de carteira definido nos contratos de gestão de carteiras e/ou condições particulares celebrados com os clientes. Caso o campo 1 do bloco de informação n.º 1 tenha sido preenchido com o código "PNP", este campo deve ser preenchido com a seguinte designação "Perfil não padronizado".

Número de carteiras individuais sob gestão (Campo 3): Campo que informa sobre o número de carteiras individuais sob gestão por conta de outrem para cada perfil de carteira à data de referência do reporte.

Montante global sob gestão (Campo 4): Campo que informa sobre o montante global sob gestão para cada perfil de carteira à data de referência do reporte. O montante é preenchido em euro.

Objetivo de referência ou de rentabilidade (Campo 5): Campo que informa sobre o objetivo definido para cada perfil de carteira.

Este campo é preenchido com um dos seguintes códigos:

"B", se o perfil de carteira identificar um objetivo de referência;

"R", se o perfil de carteira identificar um objetivo de rentabilidade;

"NA" caso não esteja definido objetivo ou caso o campo 1 do bloco de informação n.º 1 tenha sido preenchido com o código "PNP".

Descrição do objetivo do perfil de carteira (Campo 6): Campo que descreve o objetivo do perfil de carteira.

Este campo é preenchido com:

Descrição do objetivo de referência do perfil de carteira se o campo 5 do bloco de informação n.º 1 tiver sido preenchido com "B". Caso o objetivo de referência do perfil da carteira corresponda a um compósito de vários índices, cada um com uma determinada ponderação, deverá ser identificada a ponderação associada a cada um dos índices.

Quantificação do objetivo de rentabilidade do perfil de carteira se o campo 5 do bloco de informação n.º 1 tiver sido preenchido com "R".

"NA" caso não esteja definido objetivo ou caso o campo 1 do bloco de informação n.º 1 tenha sido preenchido com o código "PNP".

Instrumentos financeiros derivados (Campo 7): Campo que informa se o perfil de carteira pode incluir posições em instrumentos financeiros derivados ou transações com passivos contingentes.

Este campo é preenchido com um dos seguintes códigos:

"PC" se o perfil da carteira admitir a inclusão de passivos contingentes.

"DR" se o perfil da carteira admitir a inclusão de instrumentos financeiros derivados.

"PD" se o perfil de carteira admitir a inclusão de passivos contingentes e instrumentos financeiros derivados.

"NA" se o perfil de carteira não admitir passivos contingentes nem instrumentos financeiros derivados ou caso o campo 1 do bloco de informação n.º 1 tenha sido preenchido com o código "PNP".

Caraterização de moeda (Campo 8): Campo que informa se o perfil de carteira inclui exposição a moedas diferentes do euro.

Este campo é preenchido com um dos seguintes códigos:

"S", se o perfil de carteira admitir a exposição a moedas diferentes do euro;

"N", se o perfil de carteira não admitir a exposição a moedas diferentes do euro;

"NA" se não houver critério em relação à admissão de moedas diferentes do euro ou caso o campo 1 do bloco de informação n.º 1 tenha sido preenchido com o código "PNP".

(ver documento original)

Bloco de informação n.º 2: Informação sobre os limites referentes ao perfil de carteira indicado no campo 1 do bloco de informação n.º 1, de acordo com o definido nos contratos de gestão de carteiras e/ou condições particulares celebrados com os clientes, com os seguintes campos. Caso o campo 1 do bloco de informação n.º 1 tenha sido preenchido com o código "PNP" este bloco não é incluído.

Código de identificação de perfil de carteira (Campo 1): Campo que identifica, de forma unívoca, o código do perfil de carteira definido nos contratos de gestão de carteiras e/ou condições particulares celebrados com os clientes. É preenchido com um código interno definido pela entidade que presta a atividade de gestão de carteiras por conta de outrem e é repetido nos reportes subsequentes enquanto este perfil estiver em vigor. Devem ser utilizados os mesmos códigos utilizados para o preenchimento do campo 1 do bloco de informação n.º 1.

Limite mínimo de exposição a ações/similares (Campo 2): Campo que informa sobre o limite inferior, para cada perfil de carteira, referente a ações, fundos de ações, unit linked ou outros ativos com exposição a ações. Deve ser preenchido com o valor percentual correspondente à exposição da carteira a esta categoria de ativo. Caso não esteja definido limite, este campo deverá ser preenchido com "NA".

Limite máximo de exposição a ações/similares (Campo 3): Campo que informa sobre o limite superior, para cada perfil de carteira, referente a ações, fundos de ações, unit linked ou outros ativos com exposição a ações. Deve ser preenchido com o valor percentual correspondente à exposição da carteira a esta categoria de ativo. Caso não esteja definido limite, este campo deverá ser preenchido com "NA".

Limite mínimo de exposição a obrigações/similares (Campo 4): Campo que informa sobre o limite inferior, para cada perfil de carteira, referente a obrigações, fundos de obrigações, unit linked ou outros ativos com exposição a risco de crédito e de taxa de juro. Deve ser preenchido com o valor percentual correspondente à exposição da carteira a esta categoria de ativo. Caso não esteja definido limite, este campo deverá ser preenchido com "NA".

Limite máximo de exposição a obrigações/similares (Campo 5): Campo que informa sobre o limite superior, para cada perfil de carteira, referente a obrigações, fundos de obrigações, unit linked ou outros ativos com exposição a risco de crédito e de taxa de juro. Deve ser preenchido com o valor percentual correspondente à exposição da carteira a esta categoria de ativo. Caso não esteja definido limite, este campo deverá ser preenchido com "NA".

Limite mínimo de exposição a ativos líquidos (Campo 6): Campo que informa sobre o limite inferior, para cada perfil de carteira, referente a depósitos à ordem e a prazo e outros instrumentos financeiros de dívida de curto prazo. Deve ser preenchido com o valor percentual correspondente à exposição da carteira a esta categoria de ativo. Caso não esteja definido limite, este campo deverá ser preenchido com "NA".

Limite máximo de exposição a ativos líquidos (Campo 7): Campo que informa sobre o limite superior, para cada perfil de carteira, referente a depósitos à ordem e a prazo e outros instrumentos financeiros de dívida de curto prazo. Deve ser preenchido com o valor percentual correspondente à exposição da carteira a esta categoria de ativo. Caso não esteja definido limite, este campo deverá ser preenchido com "NA".

Limite mínimo de exposição a outros ativos (Campo 8): Campo que informa sobre o limite inferior, para cada perfil de carteira, referente a ativos com exposição ao mercado imobiliário ou outros ativos reais. Deve ser preenchido com o valor percentual correspondente à exposição da carteira a esta categoria de ativo. Caso não esteja definido limite, este campo deverá ser preenchido com "NA".

Limite máximo de exposição a outros ativos (Campo 9): Campo que informa sobre o limite superior, para cada perfil de carteira, referente a ativos com exposição ao mercado imobiliário ou outros ativos reais. Deve ser preenchido com o valor percentual correspondente à exposição da carteira a esta categoria de ativo. Caso não esteja definido limite, este campo deverá ser preenchido com "NA".

(ver documento original)

Bloco de informação n.º 3: Informação sobre critérios de elegibilidade/restrições aplicáveis ao perfil de carteira indicado no campo 1 do bloco de informação n.º 1, de acordo com o definido nos contratos de gestão de carteiras e/ou condições particulares celebrados com os clientes, com os seguintes campos. Caso o campo 1 do bloco de informação n.º 1 tenha sido preenchido com o código "PNP" este bloco de informação não é incluído.

Código de identificação de perfil de carteira (Campo 1): Campo que identifica, de forma unívoca, o código do perfil de carteira definido nos contratos de gestão de carteiras e/ou condições particulares celebrados com os clientes. É preenchido com um código interno definido pela entidade que presta a atividade de gestão de carteiras por conta de outrem e é repetido nos reportes subsequentes enquanto este perfil estiver em vigor. Devem ser utilizados os mesmos códigos utilizados para o preenchimento do campo 1 do bloco de informação n.º 1.

Caraterização de notação de risco (Campo 2): Campo que informa sobre critérios de elegibilidade para cada perfil de carteira, relativas à notação de risco dos emitentes dos respetivos ativos elegíveis. Caso não sejam aplicados critérios de elegibilidade/ restrições, este campo deverá ser preenchido com "NA".

Caraterização de área geográfica (Campo 3): Campo que informa sobre critérios de elegibilidade para cada perfil de carteira, relativas a áreas geográficas de localização dos emitentes dos respetivos ativos elegíveis. Caso não sejam aplicados critérios de elegibilidade/ restrições, este campo deverá ser preenchido com "NA".

Caraterização de sector (Campo 4): Campo que informa sobre critérios de elegibilidade para cada perfil de carteira, relativas aos sectores dos emitentes dos respetivos ativos elegíveis. Caso não sejam aplicados critérios de elegibilidade/ restrições, este campo deverá ser preenchido com "NA".

(ver documento original)

Quanto ao nome do ficheiro:

(ver documento original)

Quanto à estrutura e conteúdo do ficheiro de dados:

As especificações técnicas relativas ao ficheiro "GCO" a enviar à CMVM constam do documento "2020_reporte_GCO_schemas.zip" ou em versões atualizadas do mesmo, disponível no sítio da internet da CMVM."

I - Opção de reporte perante inexistência de informação ("reporte nulo")

Na inexistência de informação a enviar para determinado período de referência, o presente ficheiro é enviado à CMVM com a indicação de "NULO" nos elementos ConteudoReporte do cabeçalho e no elemento identificador de reporte nulo do corpo do ficheiro.

Nesta circunstância todos os restantes elementos do corpo do ficheiro não devem ter conteúdo.

II - Opção de reporte com conteúdo

Existindo conteúdo a reportar o elemento ConteudoReporte do cabeçalho deve conter a indicação "REPO" e o elemento identificador de reporte nulo do corpo do ficheiro não deve ser preenchido, sendo preenchidos os restantes elementos do corpo do ficheiro de acordo com as instruções infra.

Código de identificação de perfil de carteira (Campo 1): Campo que identifica, de forma unívoca, o código do perfil de carteira definido nos contratos de gestão de carteiras e/ou condições particulares celebrados com os clientes. É preenchido com um código interno definido pela entidade que presta a atividade de gestão de carteiras por conta de outrem e é repetido nos reportes subsequentes enquanto este perfil estiver em vigor. Devem ser utilizados os mesmos códigos utilizados para o preenchimento do campo 1 do bloco de informação n.º 1 do ficheiro CCG.

Tipo de ativo (Campo 2): Campo que identifica a tipologia dos ativos, sendo preenchido com um dos seguintes códigos:

"AC", para ações;

"UP", para unidades de participação em organismos de investimento coletivo não admitidas à negociação;

"EF", para unidades de participação em organismos de investimento coletivo admitidas à negociação (ETF);

"DU", para instrumentos de dívida emitidos pelo Estado ou outros entes públicos e equiparados;

"PC", para papel comercial;

"DI", para outros instrumentos de dívida emitidos por entidades privadas;

"ON", para outros instrumentos financeiros não derivados;

"FT", para contratos de futuros;

"CT", para contratos de forward;

"OC", para contratos de opções de compra;

"OV", para contratos de opções de venda;

"CD", para contratos financeiros por diferenças (CFD);

"SW", para contratos de troca (Swap);

"WR", para warrants;

"OD", para outros instrumentos financeiros derivados;

"UL", para unit linked;

"DO", para depósitos à ordem correntes;

"CM" para depósitos associados a contas margem;

"DP", para depósitos a prazo;

"OT", para outros ativos.

Tipo de subjacente (Campo 3): Campo que identifica a tipologia do subjacente do instrumento financeiro derivado, sendo preenchido com um dos seguintes códigos:

"NA", quando o ativo do campo anterior for preenchido com um dos seguintes códigos: "AC", "UP", "EF", "DU", "PC", "DI", "ON", "UL", "DO", "DP" ou "OT";

"AC", para ações;

"IN", para índices;

"TJ", para taxas de juro;

"TC", para taxas de câmbio;

"CR", para crédito;

"MC", para mercadorias e licenças de emissão;

"OT", para outros subjacentes não especificados anteriormente.

Código do ativo que integra a carteira sob gestão (Campo 4): Campo que identifica o código do ativo, sendo preenchido com:

Para instrumentos financeiros:

O International Standard Identification Number (ISIN), nos termos definidos na Norma ISO 6166, sempre que aplicável.

Não existindo ISIN, o Classification of Financial Instruments (CFI), nos termos definidos na Norma ISO 10962.

Para outros ativos que não sejam instrumentos financeiros, este campo deverá ser preenchido com "NA".

Tipo de código do ativo que integra a carteira sob gestão (Campo 5): Campo que identifica o tipo de código do ativo, sendo preenchido com:

Para instrumentos financeiros:

"I", quando o código de instrumento financeiro no campo anterior for preenchido com um código ISIN.

"C", quando o código de instrumento financeiro no campo anterior for preenchido com um código CFI.

Para outros ativos que não sejam instrumentos financeiros, este campo deverá ser preenchido com "NA".

Mercado de admissão (Campo 6): Campo que identifica o mercado onde o instrumento financeiro está admitido à negociação, sendo preenchido com:

O respetivo Market Identifier Code (MIC), nos termos definidos na Norma ISO 10383, para instrumentos financeiros admitidos à negociação em mercado regulamentado, em sistema de negociação multilateral ou em sistema de negociação organizada.

Deve ser preenchido com o MIC Code do primeiro mercado onde o instrumento financeiro foi admitido à negociação. Caso exista mais do que um mercado nestas circunstâncias, deve ser considerado o mercado mais líquido.

"XXXX", para instrumentos financeiros não admitidos à negociação em plataforma de negociação.

Para outros ativos não sejam instrumentos financeiros, este campo deve ser preenchido com "NA".

Designação do ativo que integra a carteira sob gestão (Campo 7): Campo relativo à designação do ativo.

Moeda (Campo 8): Campo que identifica a moeda em que o preço dos ativos originariamente se encontram expressos, sendo preenchido nos termos da norma ISO 4217.

Quantidade/Valor nominal (Campo 9): Campo que identifica a quantidade ou valor nominal de cada ativo.

Preço unitário (Campo 10): Campo que é preenchido com valor unitário do ativo em carteira na moeda em que se encontra expresso ou em percentagem quando se trate de um instrumento representativo de dívida.

Indicação de preço unitário (Campo 11): Campo preenchido com "V", caso o campo anterior tenha sido preenchido com valor, "P", caso tenha sido preenchido em percentagem.

Montante sob gestão (Campo 12): Campo que identifica o valor sob gestão, expresso em euros.

Exposição (Campo 13): Campo que identifica a exposição inerente aos instrumentos financeiros derivados, expresso em euros. As posições vendedoras deverão ser precedidas de sinal negativo.

Caraterização dos ativos em função da exposição da carteira (Campo 14): Campo que carateriza o ativo em função da exposição, de acordo com o referido no bloco de informação n.º 2 do ficheiro CCG, sendo preenchido com:

"AC", para ações, fundos de ações, unit linked ou outros ativos com exposição a ações;

"OB", para obrigações, fundos de obrigações, unit linked ou outros ativos com exposição a risco de crédito e de taxa de juro;

"LQ", depósitos à ordem e a prazo e outros instrumentos financeiros de dívida de curto prazo;

"AR", ativos com exposição ao mercado imobiliário ou outros ativos reais;

"OU" ativos com outras exposições.

Tipo de investidor (Campo 15): Campo que identifica o tipo de investidor que corresponde ao primeiro titular da carteira individual sob gestão, sendo preenchido com um dos seguintes códigos:

"NP", se for investidor não profissional.

"PR", se for investidor profissional.

"CE", se for contraparte elegível.

Notação de risco da emissão ou do emitente (Campo 16): Campo que é preenchido com:

A notação de risco da emissão do título de dívida, ou na sua inexistência, notação do risco do emitente à data da carteira, atribuído por agências internacionalmente reconhecidas. No caso da existência de duas ou mais notações, corresponde à notação mais baixa.

"NA", no caso de inexistência de notação de risco da emissão ou do emitente.

Tipo de notação de risco (Campo 17): Campo que é preenchido com:

"O", se o campo anterior tiver sido preenchido com notação de risco da emissão;

"E", se o campo anterior tiver sido preenchido com notação de risco do emitente;

"NA", se o campo anterior tiver sido preenchido com "NA".

País do emitente (Campo 18): Campo que identifica o país do emitente do instrumento financeiro. Caso não seja aplicável, este campo deverá ser preenchido com "NA".

Código do emitente (Campo 19): Campo que identifica o código LEI do emitente, sendo preenchido com nos termos da norma ISO 17442, apenas quando aplicável. Caso não seja aplicável, este campo deverá ser preenchido com "NA".

Descrição do emitente (Campo 20): Campo que identifica o nome ou denominação do emitente do instrumento financeiro. Caso não seja aplicável, este campo deverá ser preenchido com "NA".

(ver documento original)

Quanto ao nome do ficheiro:

(ver documento original)

Quanto à estrutura e conteúdo do ficheiro de dados:

As especificações técnicas relativas ao ficheiro "OPR" a enviar à CMVM constam do documento "2020_reporte_OPR_schemas.zip" ou em versões atualizadas do mesmo, disponível no sítio da internet da CMVM."

I - Opção de reporte perante inexistência de informação ("reporte nulo")

Na inexistência de informação a enviar para determinado período de referência, o presente ficheiro é enviado à CMVM com a indicação de "NULO" nos elementos ConteudoReporte do cabeçalho e no elemento identificador de reporte nulo do corpo do ficheiro.

Nesta circunstância todos os restantes elementos do corpo do ficheiro não devem ter conteúdo.

II - Opção de reporte com conteúdo

Existindo conteúdo a reportar o elemento ConteudoReporte do cabeçalho deve conter a indicação "REPO" e o elemento identificador de reporte nulo do corpo do ficheiro não deve ser preenchido, sendo preenchidos os restantes elementos do corpo do ficheiro de acordo com as instruções infra.

Data da operação (Campo 1): Campo que identifica a data da operação, nos termos da norma ISO 8601, verificada nas carteiras sob gestão. Deve ser preenchido para todos os dias do período de referência em que se verificaram operações com impacto nas carteiras sob gestão, agregando todas as operações de determinado dia.

Tipo de operação (Campo 2): Campo que identifica o tipo de operação verificada, sendo preenchido com um dos seguintes códigos:

"C", para aquisições e outras operações similares, incluindo subscrições de OIC;

"V", para alienações e outras operações similares, incluindo resgates de OIC;

"L" para levantamento de ativos e/ou numerário;

"D", para reforços de ativos e/ou numerário.

Código da origem da operação (Campo 3): Campo que identifica a origem da operação verificada na carteira sob gestão, sendo preenchido com:

"GC", para operações com origem no contrato de gestão de carteiras e/ou condições particulares celebrado com o cliente decididos pelo gestor;

"OV", para operações com origem em ordens vinculativas transmitidas pelo cliente.

Código do instrumento financeiro objeto da operação (Campo 4): Campo que identifica o código do instrumento financeiro objeto da operação, sendo preenchido com:

O International Standard Identification Number (ISIN), nos termos definidos na Norma ISO 6166, sempre que aplicável.

Não existindo ISIN, o Classification of Financial Instruments (CFI), nos termos definidos na Norma ISO 10962.

Para operações sobre outros ativos que não sejam instrumentos financeiros, este campo deverá ser preenchido com "NA".

Tipo de código do instrumento financeiro objeto da operação (Campo 5): Campo que identifica o tipo de código do instrumento financeiro objeto da operação identificado no campo 4, sendo preenchido com:

"I", quando o código de instrumento financeiro no campo 4 for preenchido com um código ISIN;

"C", quando o código de instrumento financeiro no campo 4 for preenchido com um código CFI.

Se o campo 4 tiver sido preenchido com "NA", este campo deverá ser preenchido com "NA".

Tipo de ativo (Campo 6): Campo que identifica a tipologia dos ativos, sendo preenchido com um dos seguintes códigos:

"AC", para ações;

"UP", para unidades de participação em organismos de investimento coletivo não admitidas à negociação;

"EF", para unidades de participação em organismos de investimento coletivo admitidas à negociação (ETF);

"DU", para instrumentos de dívida emitidos pelo Estado ou outros entes públicos e equiparados;

"PC", para papel comercial;

"DI", para outros instrumentos de dívida emitidos por entidades privadas;

"ON", para outros instrumentos financeiros não derivados;

"FT", para contratos de futuros;

"CT", para contratos de forward;

"OC", para contratos de opções de compra;

"OV", para contratos de opções de venda;

"CD", para contratos financeiros por diferenças (CFD);

"SW", para contratos de troca (Swap);

"WR", para warrants;

"OD", para outros instrumentos financeiros derivados;

"UL", para unit linked;

"DO", para depósitos à ordem correntes;

"CM", para depósitos associados a contas margem;

"DP", para depósitos a prazo;

"OT", para outros ativos.

Mercado de admissão (Campo 7): Campo que identifica o mercado onde o instrumento financeiro identificado no campo 4 está admitido à negociação, sendo preenchido com:

O respetivo Market Identifier Code (MIC), nos termos definidos na Norma ISO 10383, para instrumentos financeiros admitidos à negociação em mercado regulamentado, em sistema de negociação multilateral ou em sistema de negociação organizada.

Deve ser preenchido com o MIC Code do primeiro mercado onde o instrumento financeiro foi admitido à negociação. Caso exista mais do que um mercado nestas circunstâncias, deve ser considerado o mercado mais líquido.

"XXXX", para instrumentos financeiros não admitidos à negociação em plataforma de negociação.

Se o campo 4 tiver sido preenchido com "NA", este campo deverá ser preenchido com "NA".

Local de Execução (Campo 8): Campo que identifica o local onde ocorreu a operação sobre o instrumento financeiro identificado no campo 4, sendo preenchido com:

O respetivo Market Identifier Code (MIC), nos termos definidos na Norma ISO 10383, para as transações executadas em mercado regulamentado, em sistema de negociação multilateral ou em sistema de negociação organizada.

"OECP", para as operações executadas fora de plataformas de negociação e contra a carteira própria da entidade que presta a atividade de gestão de carteiras por conta de outrem (internalização).

"OEFM", para as operações executadas fora de plataformas de negociação e em que a entidade que presta a atividade de gestão de carteiras por conta de outrem, isenta de risco, intermedia o encontro entre a ordem do comprador e a do vendedor, não sendo ambos clientes da atividade de gestão de carteiras por conta de outrem.

"OEGC", para as operações executadas fora de plataformas de negociação e em que a entidade que presta a atividade de gestão de carteiras por conta de outrem, isenta de risco, intermedia o encontro entre a ordem do comprador e a do vendedor, sendo ambos clientes da atividade de gestão de carteiras por conta de outrem.

Este campo apenas deve ser preenchido se o campo 2 tiver sido preenchido com o código "C" ou "V".

Para outros ativos/operações, incluindo subscrições e resgates de unidades de participação, este campo deve ser preenchido com "NA".

Código LEI da entidade que executou a transação (Campo 9): Campo que identifica o código LEI da entidade que executou a operação ou efetuou a subscrição ou resgate sobre o instrumento financeiro identificado no campo 4.

Este campo apenas deve ser preenchido se o campo 2 foi preenchido com o código "C" ou "V".

Para outros ativos/ operações, este campo deve ser preenchido com "NA".

Quantidade (Campo 10): Campo que identifica a quantidade do ativo transacionado na operação, se aplicável. Este campo deve ser preenchido com "NA" se o campo 2 tiver sido preenchido com os códigos "L" e "D".

Não havendo ativos envolvidos na operação, este campo deve ser preenchido com "NA".

Preço unitário médio (Campo 11): Campo que é preenchido com o preço unitário médio do ativo objeto da operação, sendo preenchido em valor, na moeda da operação, ou em percentagem, Este campo deve ser preenchido com "NA" se o campo 2 tiver sido preenchido com os códigos "L" e "D".

Indicação de preço unitário médio (Campo 12): Campo preenchido com "V", caso o campo anterior tenha sido preenchido com valor, "P", caso tenha sido preenchido em percentagem. Este campo deve ser preenchido com "NA" se o campo 2 tiver sido preenchido com os códigos "L" e "D".

Moeda (Campo 13): Campo que identifica a moeda da operação.

Montante (Campo 14): Campo que identifica o montante de cada operação, incluindo juros corridos se aplicável, expresso na moeda da operação.

(ver documento original)

- *Aditado pelo/a Artigo 3.º do/a [Regulamento da CMVM n.º 6/2020 - Diário da República n.º 243/2020, Série II de 2020-12-16](https://diariodarepublica.pt/dr/detalhe/regulamento-cmvm/6-2020-151322794), em vigor a partir de 2021-07-01*

## Anexo 26 — Informação relativa ao registo e depósito de unidades de participação por conta de outrem

O presente Anexo é preenchido nos termos do Regulamento da CMVM n.º 3/2016.

Quanto ao nome do ficheiro:

(ver documento original)

Quanto à estrutura e conteúdo do ficheiro de dados:

As especificações técnicas relativas ao ficheiro "RUP" a enviar à CMVM constam do documento "2020_reporte_RUP_schemas.zip" ou em versões atualizadas do mesmo, disponível no sítio da internet da CMVM."

I - Opção de reporte perante inexistência de informação ("reporte nulo")

Na inexistência de informação a enviar para determinado período de referência, o presente ficheiro é enviado à CMVM com a indicação de "NULO" nos elementos ConteudoReporte do cabeçalho e no elemento identificador de reporte nulo do corpo do ficheiro.

Nesta circunstância todos os restantes elementos do corpo do ficheiro não devem ter conteúdo.

II - Opção de reporte com conteúdo

Existindo conteúdo a reportar o elemento ConteudoReporte do cabeçalho deve conter a indicação "REPO" e o elemento identificador de reporte nulo do corpo do ficheiro não deve ser preenchido, sendo preenchidos os restantes elementos do corpo do ficheiro de acordo com as instruções infra.

Código do instrumento financeiro (Campo 1): Campo que identifica o código da unidade de participação, sendo preenchido com:

O International Standard Identification Number (ISIN), nos termos definidos na Norma ISO 6166, sempre que aplicável

Não existindo ISIN, o código LEI do organismo de investimento coletivo, nos termos definidos na Norma ISO 17442.

Tipo de código do instrumento financeiro (Campo 2): Campo que identifica o tipo de código da unidade de participação, sendo preenchido com:

"I", quando o código de instrumento financeiro no campo anterior for preenchido com um código ISIN;

"L", quando o código de instrumento financeiro no campo anterior for preenchido com um código LEI.

Designação do instrumento financeiro (Campo 3): Campo que identifica a designação da unidade de participação.

Mercado de admissão (Campo 4): Campo que identifica o mercado onde a unidade de participação está admitida à negociação, sendo preenchido com:

O Market Identifier Code (MIC), nos termos definidos na Norma ISO 10383, para instrumentos financeiros admitidos em mercado regulamentado, em sistema de negociação multilateral ou em sistema de negociação organizada.

Deve ser preenchido com o MIC Code do primeiro mercado onde o instrumento financeiro foi admitido à negociação. Caso exista mais do que um mercado nestas circunstâncias, deve ser considerado o mercado mais líquido.

"XXXX", para instrumentos financeiros não admitidos à negociação em plataformas de negociação.

Central de valores mobiliários (Campo 5): Campo que identifica o código LEI da central de valores mobiliários onde estão integradas as unidades de participação, sendo preenchido apenas quando aplicável. Caso não seja aplicável, este campo deverá ser preenchido com "NA".

Código do emitente (Campo 6): Campo que identifica o código LEI do emitente, sendo preenchido apenas quando aplicável. Caso não seja aplicável, este campo deverá ser preenchido com "NA".

Descrição do emitente (Campo 7): Campo que identifica a denominação do emitente. Caso não seja aplicável, este campo deverá ser preenchido com "NA".

País do emitente (Campo 8): Campo que identifica o país do emitente. Caso não seja aplicável, este campo deverá ser preenchido com "NA".

Residência do titular (Campo 9): Campo que identifica a residência do primeiro titular da conta da unidade de participação e deve ser preenchido com um dos seguintes códigos:

"R", para titulares residentes;

"N", para titulares não residentes.

Tipo de titular (Campo 10): Campo que identifica o tipo do primeiro titular da conta da unidade de participação, sendo preenchido com um dos seguintes códigos:

"NP", se for investidor não profissional;

"PR", se for investidor profissional;

"CE", se for contraparte elegível.

Quantidade (Campo 11): Campo que identifica a quantidade de instrumentos financeiros, sendo preenchido com o número de unidades de participação.

Montante (Campo 12): Campo que identifica o montante das unidades participação, em euros.

(ver documento original)

- *Aditado pelo/a Artigo 3.º do/a [Regulamento da CMVM n.º 6/2020 - Diário da República n.º 243/2020, Série II de 2020-12-16](https://diariodarepublica.pt/dr/detalhe/regulamento-cmvm/6-2020-151322794), em vigor a partir de 2021-07-01*

## Anexo 27 — Modelo de divulgação da carteira de organismos de investimento coletivo em valores mobiliários de organismos de investimento alternativo em valores mobiliários e de organismos de investimento em ativos não financeiros

1 - Instrumentos financeiros admitidos, em processo de admissão ou não admitidos à negociação em plataformas de negociação:

1.1 - Instrumentos Financeiros admitidos à negociação em Plataformas Negociação (PN):

1.1.1 - Títulos de dívida pública;

1.1.2 - Outros fundos públicos e equiparados;

1.1.3 - Obrigações diversas;

1.1.4 - Ações;

1.1.5 - Unidades de participação/ações de OIC que não OII (ETFs);

1.1.6 - Direitos;

1.1.7 - Warrants autónomos;

1.1.8 - Opções;

1.1.9 - Unidades de participação/ações de OII (ETFs);

1.1.10 - Ações emitidas por sociedades imobiliárias;

1.1.11 - Papel comercial;

1.1.12 - Outros instrumentos de dívida de curto prazo;

1.1.13 - Outros instrumentos financeiros;

1.2 - Instrumentos Financeiros em processo de admissão à negociação em PN:

1.2.1 - Títulos de dívida pública;

1.2.2 - Outros fundos públicos e equiparados;

1.2.3 - Obrigações diversas;

1.2.4 - Ações;

1.2.5 - Unidades de participação/ações de OIC que não OII (ETFs);

1.2.6 - Direitos;

1.2.7 - Warrants autónomos;

1.2.8 - Opções;

1.2.9 - Unidades de participação/ações de OII (ETFs);

1.2.10 - Ações emitidas por sociedades imobiliárias;

1.2.11 - Papel comercial;

1.2.12 - Outros instrumentos de dívida de curto prazo;

1.2.13 - Outros instrumentos financeiros;

1.3 - Instrumentos Financeiros não admitidos à negociação em PN:

1.3.1 - Títulos de dívida pública;

1.3.2 - Outros fundos públicos e equiparados;

1.3.3 - Obrigações diversas;

1.3.4 - Ações;

1.3.5 - Unidades de participação/ações de OIC que não OII;

1.3.6 - Direitos;

1.3.7 - Warrants autónomos;

1.3.8 - Opções;

1.3.9 - Unidades de participação/ações de OII;

1.3.10 - Ações emitidas por sociedades imobiliárias;

1.3.11 - Papel comercial;

1.3.12 - Outros instrumentos de dívida de curto prazo;

1.3.13 - Outros instrumentos financeiros.

2 - Ativos não financeiros da carteira:

2.1 - Outros Ativos da Carteira:

2.1.1 - Ativos Não Financeiros;

2.1.2 - Imóveis;

2.1.3 - Outros Ativos.

3 - Outros ativos e passivos da carteira:

3.1 - Liquidez:

3.1.1 - Numerário;

3.1.2 - Depósitos à Ordem;

3.1.3 - Aplicações nos mercados monetários;

3.1.4 - Depósitos a prazo;

3.2 - Empréstimos:

3.2.1 - Empréstimos obtidos;

3.2.2 - Descobertos;

3.3 - Outros Valores a Regularizar:

3.3.1 - Valores ativos;

3.3.2 - Valores passivos.

4 - Valor líquido global (VLGF).

5 - N.º Unidades de participação total:

5.1 - Categoria C1;

5.2 - Categoria C2;

[...]

5.3 - Categoria Cn.

6 - Ativo sob gestão.

7 - Ativos líquidos.

8 - Valor de posições equivalentes nos ativos subjacentes relativamente a instrumentos financeiros derivados.

9 - Valor do investimento noutros OIC geridos pela entidade responsável pela gestão.

10 - Responsabilidades extrapatrimoniais:

10.1 - Contratos Cambiais admitidos à negociação em PN:

10.1.1 - Futuros;

10.1.2 - Opções;

10.1.3 - Outros;

10.2 - Contratos Cambiais não admitidos à negociação em PN:

10.2.1 - Forwards;

10.2.2 - Opções;

10.2.3 - Swaps;

10.2.4 - Outros;

10.3 - Contratos sobre taxas de juro admitidos à negociação em PN:

10.3.1 - Futuros;

10.3.2 - Opções;

10.3.3 - Outros;

10.4 - Contratos sobre taxa de juro não admitidos à negociação em PN:

10.4.1 - FRA;

10.4.2 - Opções;

10.4.3 - Swaps;

10.4.4 - Outros;

10.5 - Contratos sobre cotações admitidos à negociação em PN:

10.5.1 - Futuros;

10.5.2 - Opções;

10.5.3 - Outros;

10.6 - Contratos sobre cotações não admitidos à negociação em PN:

10.6.1 - Opções;

10.6.2 - Swaps;

10.6.3 - Outros.

- *Aditado pelo/a Artigo 3.º do/a [Regulamento da CMVM n.º 6/2020 - Diário da República n.º 243/2020, Série II de 2020-12-16](https://diariodarepublica.pt/dr/detalhe/regulamento-cmvm/6-2020-151322794), em vigor a partir de 2021-07-01*

## Anexo 28 — Modelo de divulgação da carteira de organismos de investimento imobiliário

1 - Imóveis:

1.1 - Imóveis situados em Estados da União Europeia:

1.1.1 - Terrenos Urbanizados;

1.1.2 - Terrenos Não Urbanizados;

1.1.3 - Projetos de Construção de Reabilitação;

1.1.4 - Outros Projetos de Construção;

1.1.5 - Construções Acabadas Arrendadas;

1.1.6 - Construções Acabadas Não arrendadas;

1.1.7 - Direitos;

1.2 - Imóveis situados fora da União Europeia:

1.2.1 - Terrenos Urbanizados;

1.2.2 - Terrenos Não urbanizados;

1.2.3 - Projetos de Construção de Reabilitação;

1.2.4 - Outros Projetos de Construção;

1.2.5 - Construções Acabadas Arrendadas;

1.2.6 - Construções Acabadas Não arrendadas;

1.2.7 - Direitos.

2 - Participações:

2.1 - UP's Domiciliados em Estados da União Europeia:

2.1.1 - Organismos de investimento imobiliário;

2.1.2 - Outros;

2.2 - UP's Domiciliados fora da União Europeia:

2.2.1 - Organismos de investimento imobiliário;

2.2.2 - Outros;

2.3 - Participações em Sociedades Imobiliárias na UE:

2.3.1 - Ações;

2.3.2 - Quotas;

2.3.3 - Direitos de subscrição;

2.3.4 - Outras participações;

2.4 - Participações em Sociedades Imobiliárias fora da UE:

2.4.1 - Ações;

2.4.2 - Quotas;

2.4.3 - Direitos de subscrição;

2.4.4 - Outras participações.

3 - Outros ativos e passivos:

3.1 - Liquidez:

3.1.1 - Numerário;

3.1.2 - Depósitos à Ordem;

3.1.3 - Organismos do mercado monetário;

3.1.4 - Depósitos com pré-aviso e a prazo;

3.1.5 - Certificados de depósito;

3.1.6 - Valores mobiliários com prazo de vencimento residual inferior a 12 meses;

3.2 - Empréstimos:

3.2.1 - Empréstimos obtidos;

3.2.2 - Descobertos;

3.3 - Valores ativos a regularizar:

3.3.1 - Adiantamentos por conta de imóveis;

3.3.2 - Adiantamentos por conta de sociedades imobiliárias;

3.3.3 - Valores a receber por conta de transações de imóveis;

3.3.4 - Rendas em dívida;

3.3.5 - Outros;

3.4 - Valores passivos a regularizar:

3.4.1 - Recebimentos por conta de imóveis;

3.4.2 - Recebimentos por conta de sociedades imobiliárias;

3.4.3 - Valores a pagar por conta de transações de imóveis;

3.4.4 - Cauções;

3.4.5 - Rendas adiantadas;

3.4.6 - Outros.

4 - Valor líquido global (VLGF).

5 - N.º Unidades de participação total:

5.1 - Categoria C1;

5.2 - Categoria C2;

[...]

5.3 - Categoria Cn.

6 - Ativo sob gestão.

7 - Ativos líquidos.

8 - Valor de posições equivalentes nos ativos subjacentes relativamente a instrumentos financeiros derivados.

9 - Valor do investimento noutros OIC geridos pela entidade responsável pela gestão.

10 - Responsabilidades extrapatrimoniais.

10.1 - Compromissos com e de terceiros:

10.1.1 - Direitos de arrendamento;

10.1.2 - Direitos de concessão;

10.1.3 - Direitos de exploração;

10.1.4 - Direitos de superfície;

10.1.5 - Outros direitos.

- *Aditado pelo/a Artigo 3.º do/a [Regulamento da CMVM n.º 6/2020 - Diário da República n.º 243/2020, Série II de 2020-12-16](https://diariodarepublica.pt/dr/detalhe/regulamento-cmvm/6-2020-151322794), em vigor a partir de 2021-07-01*
