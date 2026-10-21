- Portuguese legislation as markdown, one file per act, taken from the consolidated texts of the Diario da Republica (INCM).
- Covers only what the Diario da Republica consolidates, plus original acts that were never amended. No case law in v1.
- A Claude Code plugin (LawAgents/legislacao-pt-plugin) reads this repo and cites the official source in every answer.
- Step-by-step guides in European Portuguese for non-programmers, plus a ready-made kit to build your own personal legal agent.
- Consolidated texts have no legal value: always confirm in the Diario da Republica. Scripts and plugin are MIT; the legal texts carry no licence of their own.

# Legislação portuguesa em markdown (LawAgents/pt)

## O que é este repositório, o que cobre e o que não cobre

Cada diploma é um ficheiro markdown, com os metadados no topo e cada artigo como título próprio (por exemplo "Artigo 12.º"). Os textos vêm do Diário da República eletrónico. A base de partida tem cerca de 4.800 diplomas. Os códigos grandes ficam divididos por livro ou título dentro da pasta `codigos/`.

O repositório é pensado para servir de conhecimento a agentes de IA, que leem os ficheiros e citam o artigo, o ficheiro e a ligação oficial.

Cobre. Os diplomas em vigor que o Diário da República disponibiliza como consolidados, de todos os tipos de ato (Constituição, códigos, leis, decretos-lei, portarias, resoluções e restantes tipos, incluindo a legislação regional dos Açores e da Madeira), mais os originais que nunca foram alterados. Cada ficheiro traz a ligação ao ato no Diário da República, a data da versão consolidada e um aviso de que o texto consolidado não tem valor legal.

Não cobre:

- Jurisprudência. A versão 1 não tem acórdãos.
- Regulamentos municipais.
- Direito da União Europeia (a fonte própria é o EUR-Lex).
- Atos da 2.ª série do Diário da República sem consolidação pública.
- Diplomas revogados. Saem da pasta principal; o texto fica no histórico do git e a lista `revogados.md` guarda o id, o título, a data da revogação e a ligação oficial.
- Versões anteriores de um diploma. O histórico de alterações fica no git, com um commit por atualização.
- Qualquer diploma fora do conjunto acima. Para esses, o texto oficial consulta-se no Diário da República.

Limite conhecido: alguns anexos e quadros do Diário da República são um único bloco de texto e, por isso, não se dividem. 92 ficheiros ficam acima de 90 KB (a maioria tem um só artigo) e os agentes podem ter dificuldade em lê-los de uma vez. Os códigos e os restantes diplomas dividem-se em partes até 70 KB.

Os ficheiros de índice na raiz do repositório (`nomes-comuns.md`, `indice.md`, `revogados.md` e os índices por tipo de ato) ajudam o agente a encontrar o diploma certo sem ler tudo.

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
