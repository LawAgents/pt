- Portuguese legislation as markdown, one file per act, taken from the consolidated texts of the Diario da Republica (INCM).
- Covers only what the Diario da Republica consolidates, plus original acts that were never amended. No case law in v1.
- A Claude Code plugin (LawAgents/legislacao-pt-plugin) reads this repo and cites the official source in every answer.
- Step-by-step guides in European Portuguese for non-programmers, plus a ready-made kit to build your own personal legal agent.
- Consolidated texts have no legal value: always confirm in the Diario da Republica. Scripts and plugin are MIT; the legal texts carry no licence of their own.

# Legislação portuguesa em markdown

A legislação portuguesa em vigor que o Diário da República disponibiliza consolidada, convertida para markdown, com
cabeçalho estruturado e ligação oficial em cada ficheiro. Cada artigo tem o seu título, para um agente de IA ou uma
pessoa chegar ao texto certo e citar a fonte.

O repositório existe para quem precisa de ter a certeza de que o artigo que lê é o que está em vigor e de saber de onde vem:
investigadores, juristas e agentes de IA. O texto da União Europeia está no repositório irmão
[LawAgents/ue-pt](https://github.com/LawAgents/ue-pt).

Para consultar com o Claude Code só precisas de instalar o plugin [legislacao-pt](https://github.com/LawAgents/legislacao-pt-plugin).
Os dados não se instalam: o plugin lê os ficheiros deste repositório diretamente e cita a fonte em cada resposta.

> [!IMPORTANT]
> Os textos consolidados não têm valor legal e não substituem a publicação no Diário da República. Confirma sempre na ligação
> oficial do cabeçalho antes de citar.

---

## O que contém

4.968 diplomas em vigor, em 11.223 ficheiros (os códigos e os diplomas grandes estão divididos em partes).

| Texto | Diplomas |
| --- | ---: |
| Consolidado | 4.525 |
| Original, nunca alterado | 443 |
| **Total** | **4.968** |

Por tipo de ato:

| Tipo | Diplomas | | Tipo | Diplomas |
| --- | ---: | --- | --- | ---: |
| Decreto-Lei | 1.695 | | Decreto Regulamentar | 71 |
| Portaria | 1.438 | | Decreto | 66 |
| Lei | 536 | | Resolução da Assembleia da República | 56 |
| Resolução do Conselho de Ministros | 298 | | Decreto do Presidente da República | 37 |
| Decreto Legislativo Regional | 265 | | Declaração | 36 |
| Aviso | 190 | | Outros tipos | 178 |
| Decreto Regulamentar Regional | 102 | | | |

Os tipos incluem a Constituição, os códigos, as leis orgânicas, os despachos e a legislação regional dos Açores e da Madeira
(43 tipos no total, em `config/act-types.txt`). As contagens são de 2026-10-21.

### O que fica de fora

- Jurisprudência: esta versão não tem acórdãos.
- Regulamentos municipais.
- Atos da 2.ª série do Diário da República sem consolidação pública.
- Diplomas revogados: saem da pasta principal e a lista `revogados.md` guarda o id, o título, a data da revogação e a ligação oficial. O texto anterior fica no histórico do git.
- Versões anteriores de um diploma: o histórico de alterações fica no git, com um commit por atualização.

Limite conhecido: alguns anexos e quadros do Diário da República são um único bloco de texto e não se dividem. 92 ficheiros
ficam acima de 90 KB (a maioria tem um só artigo) e os agentes podem ter dificuldade em lê-los de uma vez.

`COBERTURA.md` e `estatisticas.html` são gerados por `python -I scripts/estatisticas.py` e não se atualizam sozinhos: refazem-se à mão depois de uma atualização.

---

## Estrutura

```
leis/AAAA/lei-N-AAAA.md                     um ficheiro por diploma, por tipo e por ano do ato
decretos-lei/  portarias/  avisos/  ...     uma pasta por tipo de ato (os mesmos nomes de `config/act-types.txt`)
codigos/<codigo>/                           códigos e diplomas grandes: uma visão geral e partes de até 70 KB
constituicao/                               Constituição da República Portuguesa
nomes-comuns.md                             nomes e siglas (Código Civil, CC) para o id certo, 45 entradas
indice.md  indice-<tipo>-<anos>.md          índices por tipo de ato e ano (ficheiros de até 40 KB)
indice-temas.md                             índice por tema
revogados.md                                diplomas revogados, com a data e a ligação oficial
COBERTURA.md                                números por tipo, década, entidade e pasta
estatisticas.html                           página com gráficos, um único ficheiro para abrir no navegador
config/                                     tipos de ato, nomes comuns e temas
scripts/                                    o código que descarrega, converte, valida e gera os índices e as estatísticas
docs/kit.md                                 kit de agente legal pessoal
```

Os diplomas divididos em partes têm um ficheiro de visão geral (`id.md`, com a tabela `## Estrutura` e o primeiro e o último artigo de cada
parte) e ficheiros `id-<parte>.md`. Um agente começa pela visão geral e abre só a parte de que precisa.

Os ids são estáveis e legíveis: `lei-24-1996`, `decreto-lei-100-2023`, `decreto-lei-47344-1966` (o Código Civil, que `nomes-comuns.md` encontra por "Código Civil" ou "CC").

---

## Formato dos ficheiros

Todo o ficheiro tem cabeçalho YAML e, no corpo, o título em `#` seguido do texto, com um título por artigo:

```markdown
---
id: "lei-24-1996"
dre_id: "406882"
title: "Lei n.º 24/96, de 31 de julho"
type: "Lei"
number: "24/96"
year: 1996
date: 1996-07-31
issuer: "Assembleia da República"
status: "em vigor"
text_version: "consolidado"
last_amended: 2023-07-04
source: "https://diariodarepublica.pt/dr/legislacao-consolidada/lei/1996-34491075"
original_pdf: "https://files.diariodarepublica.pt/1s/1996/07/176a00/21842189.pdf"
retrieved: 2026-10-21
summary: "Estabelece o regime legal aplicável à defesa dos consumidores. ..."
legal_notice: "Texto consolidado sem valor legal. Confirma no Diário da República antes de o usares. Não substitui aconselhamento jurídico."
---

# Lei n.º 24/96, de 31 de julho
```

`source` é a ligação oficial do texto consolidado e `retrieved` a data da descarga. Os artigos revogados mantêm a marca oficial
`*(Revogado)*`. Os ficheiros só mudam quando o Diário da República altera o texto.

---

## Atualização

Uma tarefa do GitHub corre todos os domingos às 03:00 UTC, descarrega o que mudou no Diário da República, valida e faz um commit por
atualização. Se algo falhar, não publica dados parciais e abre uma issue com o erro. Um ensaio completo no GitHub (sem commit)
descarregou de novo os 4.968 diplomas, validou sem erros e confirmou que o repositório publicado é idêntico ao resultado.
Ainda não vi uma atualização real com alterações do Diário da República.

---

## Passo a passo para quem não programa

Escolhe um dos três caminhos. O primeiro é o completo.

### Caminho 1: plugin no Claude Code (o completo)

O plugin tem três comandos e cita sempre a fonte: `/lei`, `/artigo` e `/pesquisar-lei`. Só lê ficheiros públicos do GitHub, não escreve nada no teu computador e não envia as tuas perguntas a nenhum outro serviço.

1. Instala o Claude Code e abre-o numa pasta qualquer.
2. Escreve `/plugin marketplace add LawAgents/legislacao-pt-plugin` e carrega em Enter.
3. Escreve `/plugin install legislacao-pt@legislacao-pt` e carrega em Enter.
4. Experimenta `/artigo Código Civil 483`. A resposta termina com o bloco "Fontes" e a linha de aviso.
5. Opcional: cola o texto abaixo no ficheiro `CLAUDE.md` da tua pasta de trabalho.

```text
Para legislação portuguesa usa sempre o plugin legislacao-pt (comandos /lei, /artigo e /pesquisar-lei).
Cita sempre a fonte: título completo, id do diploma, ficheiro no repo, artigo e ligação oficial do Diário da República.
Nunca inventes artigos, números de diplomas, datas ou ligações, e nunca respondas de memória.
Se o plugin não encontrar o que pedi, responde "Não encontrado no repo." e não cites nada.
Termina com a linha: "Texto consolidado sem valor legal. Confirma no Diário da República antes de o usares. Não substitui aconselhamento jurídico."
```

### Caminho 2: Projeto do Claude.ai com os códigos como conhecimento

1. Abre o claude.ai e cria um Projeto novo.
2. Em https://github.com/LawAgents/pt abre a pasta `codigos/` e descarrega os ficheiros dos códigos de que precisas (em cada ficheiro, botão "Download raw file"). Nos códigos divididos em partes, descarrega a visão geral e só as partes que vais usar.
3. No Projeto, abre a zona de conhecimento (Project knowledge) e carrega esses ficheiros.
4. Nas instruções do Projeto, cola o texto abaixo.

```text
Responde sobre legislação portuguesa usando apenas os ficheiros carregados neste Projeto.
Cita sempre o artigo, o ficheiro de onde o tiraste e a ligação oficial do Diário da República que consta no cabeçalho (campo source) desse ficheiro.
Nunca inventes artigos, números de diplomas, datas ou ligações, e nunca completes de memória.
Se a resposta não estiver nos ficheiros carregados, responde "Não encontrado nos ficheiros carregados." e não cites nada.
Termina sempre com: "Texto consolidado sem valor legal. Confirma no Diário da República antes de o usares. Não substitui aconselhamento jurídico."
```

### Caminho 3: qualquer agente que leia ficheiros markdown ou abra ligações da web

Serve para agentes que leem uma pasta de ficheiros markdown ou que abrem endereços da web.

Forma A, o agente lê ficheiros. Descarrega o repositório (em https://github.com/LawAgents/pt, botão "Code", "Download ZIP"), descomprime e aponta o agente para a pasta.

Forma B, o agente abre ligações. Dá-lhe o endereço https://github.com/LawAgents/pt e diz-lhe que pode abrir os ficheiros pelo endereço "raw" do GitHub (https://raw.githubusercontent.com/LawAgents/pt/main/, seguido do caminho do ficheiro). Pede-lhe que comece por `nomes-comuns.md`, e que só abra os índices e os diplomas de que precisar.

Em ambas as formas, cola nas instruções do agente o texto abaixo.

```text
Tens acesso à legislação portuguesa consolidada no repositório LawAgents/pt (ficheiros markdown, um por diploma).
Para encontrar um diploma lê primeiro nomes-comuns.md; se não o encontrares, lê o índice do tipo de ato; se mesmo assim não existir, lê revogados.md.
Responde só com o que lês nos ficheiros. Cita sempre o artigo, o ficheiro (caminho no repo) e a ligação oficial do Diário da República (campo source do cabeçalho).
Nunca inventes artigos, números de diplomas, datas ou ligações, e nunca respondas de memória.
Se não encontrares, responde "Não encontrado no repo." e não cites nada.
Termina sempre com: "Texto consolidado sem valor legal. Confirma no Diário da República antes de o usares. Não substitui aconselhamento jurídico."
```

O [kit de agente legal pessoal](docs/kit.md) tem um modelo de prompt de sistema mais completo, instruções para ler um processo, uma lista de verificação e dez perguntas de teste.

## Avisos legais do Diário da República

Os textos deste repositório vêm do Diário da República eletrónico (https://diariodarepublica.pt/), gerido pela Imprensa Nacional-Casa da Moeda (INCM). Transcrevem-se os pontos dos avisos legais do site que mais importam aqui:

> O acesso universal e gratuito compreende a possibilidade de impressão, arquivo, pesquisa e livre acesso ao conteúdo dos atos publicados nas 1.ª e 2.ª séries do Diário da República.

> A edição eletrónica do Diário da República faz fé plena e a publicação destes atos vale para todos os efeitos legais, nos termos do n.º 5 do artigo 1.º da Lei n.º 74/98, de 11 de novembro.

> A produção do texto consolidado dos atos publicados, ainda que sem valor legal, de modo a facilitar a consulta e a sistematização do ordenamento jurídico;

> A informação apresentada visa o cumprimento da missão de serviço público inerente à publicação do Diário da República e não constitui um parecer profissional ou jurídico.

> Quaisquer tentativas de alteração de informação, de carregamento de informação ou qualquer outra ação que possa causar dano e pôr em risco a integridade do sistema são estritamente proibidas e punidas de acordo com a legislação em vigor.

O serviço público de acesso é regulado pelo Decreto-Lei n.º 83/2016, de 16 de dezembro, e pelo Despacho Normativo n.º 16/2022, de 30 de dezembro. Os avisos não tratam da republicação do texto consolidado. Por isso o descarregador deste repositório faz no máximo dois pedidos por segundo e identifica-se em cada pedido.

O texto integral dos avisos e os termos do site consultam-se em https://diariodarepublica.pt/.

## Licenças

- Os scripts e o plugin têm a licença MIT.
- Os textos das leis não têm licença própria. São atos oficiais do Diário da República (INCM), e este repositório não reivindica direitos sobre o seu conteúdo.

## Como contribuir

- Pull requests só são aceites para a lista de nomes comuns, a documentação e o kit de agente.
- Os ficheiros de legislação não aceitam edições à mão, porque são gerados a partir do Diário da República.
- Encontraste um erro num diploma? Abre uma issue com o id do diploma e a ligação oficial do Diário da República onde se vê o texto correto.

## Kit de agente legal pessoal

Em [docs/kit.md](docs/kit.md): modelo de prompt de sistema, instruções para um agente que lê um processo, lista de verificação contra o Diário da República e dez perguntas de teste com a resposta esperada.
