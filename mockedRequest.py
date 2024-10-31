def getChaptersName(tema):
    return ['Introdução ao mundo do bonsai',
 'História e origem do bonsai',
 'Princípios básicos do bonsai',
 'Cuidados e manejo das plantas para bonsai',
 'Técnicas de poda e modelagem',
 'Escolha do vaso e substrato ideal',
 'Estilos e formas de bonsai',
 'Galeria de espécies adequadas para transformação em bonsai']

def getChaptersContent(tema,titulo):
    return """
Ao longo dos séculos, os bonsais têm encantado pessoas ao redor do mundo com sua beleza e elegância. A arte de transformar plantas em bonsais tem suas origens na China, por volta de 200 a.C. A palavra "bonsai" é uma combinação de dois termos japoneses: "bon", que significa bandeja, e "sai", que significa planta. Essa prática milenar era inicialmente reservada para a elite chinesa, que cultivava pequenas árvores em vasos como forma de contemplação.

Com a disseminação do budismo na China, por volta do século VI d.C., os monges passaram a cultivar bonsais como forma de meditação e conexão com a natureza. Foi somente durante a dinastia Tang (618-907 d.C.) que a arte do bonsai se difundiu para o Japão, juntamente com a cultura e a religião budista. Os japoneses adotaram e aprimoraram a técnica chinesa de cultivar árvores em bandejas, tornando-a uma forma de expressão artística e espiritual.

No Japão, o cultivo de bonsais foi associado à simbologia e aos valores do país, como a busca pela perfeição, a simplicidade e a harmonia com a natureza. Os bonsais eram e ainda são considerados obras de arte vivas, que refletem a passagem do tempo e a paciência do artista em moldar a natureza de forma delicada e equilibrada. A estética japonesa do wabi-sabi, que valoriza a beleza imperfeita e transitória, também influenciou a forma como os bonsais são apreciados e cultivados.

Com o passar dos séculos, a arte do bonsai se espalhou pelo mundo, conquistando admiradores em diversos países e continentes. Hoje em dia, há uma comunidade global de entusiastas que se dedicam ao cultivo e à criação de bonsais, trocando experiências e conhecimentos para aprimorar suas técnicas e apreciar a beleza singular de cada árvore.

A história e a origem do bonsai revelam não apenas uma tradição ancestral de cultivo de plantas em miniatura, mas também os valores e a sensibilidade estética das culturas chinesa e japonesa. A prática do bonsai transcende a simples jardinagem, sendo uma forma de expressão artística, espiritual e filosófica que nos convida a contemplar a essência da natureza e a nossa relação com ela. Cada bonsai conta uma história única, carregando consigo a sabedoria e a beleza de gerações passadas, e conectando-nos com a eternidade da vida em seu ciclo contínuo de renovação.
"""

def getBookContent(tema):
    chapters_name = getChaptersName(tema)
    chapters_content = []
    for n in chapters_name:
        chapters_content.append(getChaptersContent(tema,n))
    return [chapters_name,chapters_content]