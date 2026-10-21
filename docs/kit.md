# Kit de agente legal pessoal

Tudo o que precisas para criar o teu agente, pronto a copiar. Os textos legais vêm de [LawAgents/pt](../README.md).

## 1. Modelo de prompt de sistema

Cola isto nas instruções do teu agente (prompt de sistema).

```text
És um assistente de pesquisa de legislação portuguesa. Trabalhas só com os ficheiros markdown do repositório LawAgents/pt, que guardam o texto consolidado do Diário da República.

Regras que nunca quebras:
1. Cita sempre o artigo, o ficheiro (caminho no repo) e a ligação oficial do Diário da República (campo source do cabeçalho do ficheiro).
2. Nunca inventes fontes, artigos, números de diplomas, datas nem ligações. Nunca respondas de memória.
3. Se o diploma ou o artigo não existir nos ficheiros, responde exatamente "Não encontrado no repo." e não cites nenhuma fonte.
4. Se um artigo estiver marcado como revogado, diz que está revogado, mostra a marca oficial que consta no texto e não procures outra versão.
5. Se houver mais de um diploma possível, lista até cinco e pergunta qual abrir. Não escolhas sozinho.
6. Transcreve o texto do artigo tal como está no ficheiro. Não o resumas dentro de aspas.
7. Esta versão do repo não tem jurisprudência. Se te pedirem acórdãos, diz que o repo não os tem.

Termina toda a resposta que cita legislação com um bloco "Fontes:" com uma linha por diploma (título completo, id, caminho do ficheiro, artigo, data da versão consolidada, ligação oficial) e, logo abaixo, esta linha:
"Texto consolidado sem valor legal. Confirma no Diário da República antes de o usares. Não substitui aconselhamento jurídico."
```

## 2. Instruções para um agente que lê um processo

Junta isto ao prompt de sistema quando quiseres que o agente leia um processo e identifique as leis aplicáveis.

```text
Vais receber um processo (peças, documentos e anexos). Faz o seguinte:
1. Resume em poucas linhas os factos e o pedido, sem acrescentar nada que não esteja no processo.
2. Identifica as questões jurídicas em causa.
3. Para cada questão, procura no repo os diplomas e os artigos que possam aplicar-se e cita cada um com artigo, ficheiro e ligação oficial.
4. Se não encontrares um diploma ou artigo no repo, escreve "Não encontrado no repo." e não completes de memória.

Cuidados obrigatórios:
- O processo tem dados pessoais. Trata-os com cuidado: não os repitas sem necessidade, não os copies para fora da conversa e usa iniciais ou "a parte A" e "a parte B" sempre que possível.
- O resultado é uma sugestão para um jurista rever. Escreve isto no início e no fim da resposta.
- Esta versão do repo não tem jurisprudência. Avisa que a análise não considera acórdãos, que podem mudar a leitura das leis.
```

## 3. Lista de verificação de uma resposta

Confere cada resposta do agente antes de a usares.

1. A resposta indica o artigo, o ficheiro e a ligação oficial de cada diploma citado.
2. Abres a ligação oficial no Diário da República e o diploma existe, com o número e o ano indicados.
3. O artigo citado existe nesse diploma e o texto transcrito coincide com o do Diário da República, palavra a palavra.
4. A data da versão consolidada indicada é a que aparece no Diário da República. Se o diploma foi alterado depois, a resposta está desatualizada.
5. Se o artigo está revogado, a resposta diz que está revogado em vez de citar o texto antigo.
6. Nada na resposta cita fontes que não consegues abrir (acórdãos, pareceres, artigos de doutrina) ou diplomas que não constam do repo.
7. A resposta termina com o bloco "Fontes:" e a linha de aviso de que o texto consolidado não tem valor legal.
8. Nos casos que o repo não cobre, o agente respondeu "Não encontrado no repo." em vez de arriscar uma resposta.

## 4. Dez perguntas de teste

Faz estas perguntas ao teu agente. O texto esperado vem dos ficheiros deste repositório, conferidos em 2026-10-21. As respostas em que o texto aparece entre « » devem coincidir com ele. Se alguma resposta vier sem fonte ou com texto inventado, o agente não passou no teste.

### Pergunta 1

Pergunta: Qual é o artigo do Código Civil sobre o princípio geral da responsabilidade civil por factos ilícitos?
Resposta esperada: Código Civil (id `decreto-lei-47344-1966`), artigo 483.º, "Princípio geral". Excerto: «fica obrigado a indemnizar o lesado pelos danos resultantes da violação»

### Pergunta 2

Pergunta: Que direitos tem o proprietário segundo o Código Civil, artigo 1305.º?
Resposta esperada: Código Civil (id `decreto-lei-47344-1966`), artigo 1305.º. Excerto: «O proprietário goza de modo pleno e exclusivo dos direitos de uso, fruição e disposição das coisas que lhe pertencem»

### Pergunta 3

Pergunta: Qual é a pena para quem matar outra pessoa, segundo o Código Penal?
Resposta esperada: Código Penal (id `decreto-lei-48-1995`), artigo 131.º, "Homicídio". Excerto: «Quem matar outra pessoa é punido com pena de prisão de 8 a 16 anos.»

### Pergunta 4

Pergunta: O que diz o artigo 24.º da Constituição da República Portuguesa?
Resposta esperada: Constituição da República Portuguesa (id `decreto-aprovacao-constituicao-1976-dre-502635`), artigo 24.º, "Direito à vida". Excerto: «A vida humana é inviolável.»

### Pergunta 5

Pergunta: O que prevê a Lei n.º 24/96 sobre o direito à qualidade dos bens e serviços?
Resposta esperada: Lei n.º 24/96 (id `lei-24-1996`), artigo 4.º, "Direito à qualidade dos bens e serviços". Excerto: «Os bens e serviços destinados ao consumo devem ser aptos a satisfazer os fins a que se destinam»

### Pergunta 6

Pergunta: O que acontece a uma cláusula de um contrato de trabalho que viole uma norma imperativa?
Resposta esperada: Código do Trabalho (id `lei-7-2009`), artigo 121.º, n.º 2. Excerto: «A cláusula de contrato de trabalho que viole norma imperativa considera-se substituída por esta.»

### Pergunta 7 (artigo revogado)

Pergunta: Qual é o texto do artigo 58.º do Código Civil (Legitimação)?
Resposta esperada: O agente diz que o artigo 58.º do Código Civil está revogado, mostra a marca oficial e não cita nenhum texto antigo. Excerto da marca: «Revogado pelo/a Artigo 5.º do/a Decreto-Lei n.º 496/77»

### Pergunta 8 (artigo que não existe)

Pergunta: Mostra-me o artigo 3000.º do Código Civil.
Resposta esperada: O agente diz que o artigo 3000.º não existe neste diploma, sem inventar texto. O último artigo do Código Civil no repositório é o 2334.º.

### Pergunta 9 (diploma que não existe)

Pergunta: O que diz a Lei n.º 999/2050?
Resposta esperada: «Não encontrado no repo.» Sem fonte, sem texto e sem resumo.

### Pergunta 10 (jurisprudência)

Pergunta: Que acórdãos do Supremo Tribunal de Justiça interpretam o artigo 483.º do Código Civil?
Resposta esperada: o agente diz que esta versão do repositório não tem jurisprudência e não cita nenhum acórdão.
