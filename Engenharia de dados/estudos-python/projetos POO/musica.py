class Musica:
    nome = ''
    artista = ''
    duracao = int

musica1 = Musica()
musica1.nome = 'helena'
musica1.artista = 'my chemical romance'
musica1.duracao = 355

musica2 = Musica()
musica2.nome = 'king for a day'
musica2.artista = 'pierce the veil'
musica2.duracao = 225

musicas = [musica1, musica2]

print(musicas)
print(vars(musica1))
print(vars(musica2))

print(f'Música: {musica1.nome} - Banda: {musica1.artista} - {musica1.duracao} segundos')
print(f'musica: {musica2.nome} - banda: {musica2.artista} - {musica2.duracao} segundos')