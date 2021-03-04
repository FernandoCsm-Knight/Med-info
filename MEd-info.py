import discord
from keep_alive import keep_alive
import requests
from bs4 import BeautifulSoup

intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'O bot está logado como {client.user}!')


@client.event
async def on_message(message):

    if message.author.bot:
        return

    if message.guild.id != [id do seu servidor]:
        return

    canalmed = client.get_channel([id do canal onde o comando irá funcionar])
    if message.channel == canalmed:
        alo = message.content.split()
        if alo[0] not in ['>p', '[outro comando que você quer permitir no canal]']:
            alo1 = await message.channel.send(
                f'{message.author.mention} nesse canal você só pode utilizar o comando >p[pesquisa]. Para saber mais sobre esse comando utilize =>help no canal de texto `grupo de estudos 1` da biblioteca medicina.'
            )
            await message.delete()
            await alo1.delete(delay=4)

        if message.content.startswith('>p'):
            args = message.content.split()
            args.pop(0)
            lista = []
            listaart = []
            embedtitle = ' '.join(args)
            b = len(args)
            try:
                if b // 2:
                    div = b // 2
                    for x in range(1, div + 1):
                        valor = (2 * x) - 1
                        args[valor] = args[valor].upper()
                        resposta = ')+'.join(args[valor - 1:valor + 1])
                        lista.append(resposta)
                    lista.append(args[b - 1])
                    lil = '+'.join(lista)
                    busca = '(' * div + lil
                    site = requests.get(
                        f'https://www.ncbi.nlm.nih.gov/pmc/?term={busca}')
                    content = site.content
                    sitenovo = BeautifulSoup(content, 'html.parser')
                    artigo = sitenovo.find_all('div', attrs={'class': 'rprt'})
                    for x in range(0, 8):
                        titulolink = artigo[x].find('div',
                                                    attrs={'class': 'title'})
                        link = titulolink.find('a')
                        link2 = link['href']
                        titulo = link.text
                        detalhes = artigo[x].find('div',
                                                  attrs={'class': 'details'})
                        detalhes1 = detalhes.text
                        listaart.append(
                            f'__**{titulo}**__ \n  {detalhes1}  \n \n LINK: https://www.ncbi.nlm.nih.gov/{link2} \n'
                        )
                    embedpub = discord.Embed(
                        title=f'🔎 Artigos no Pubmed sobre ```{embedtitle}``` 🔍',
                        description='',
                        color=0x133458)
                    embedpub.set_author(
                        name='Ir para o Pubmed',
                        url=f'https://www.ncbi.nlm.nih.gov/pmc/?term={busca}',
                        icon_url='[link da imagem do autor do embed]')
                    for arquivo in range(0, len(listaart)):
                        embedpub.add_field(name=f'📖 Artigo {arquivo + 1}',
                                           value=f'{listaart[arquivo]}',
                                           inline=False)
                    embedpub.set_thumbnail(url='[link da imagem da sua thumbnail]')
                    embedpub.set_footer(
                        text='Staff do servidor [nome do seu servidor].',
                        icon_url='[link da imagem do seu footer]')
                    await message.channel.send(embed=embedpub)
                else:
                    busca = args[0]
                    site = requests.get(
                        f'https://www.ncbi.nlm.nih.gov/pmc/?term={busca}')
                    content = site.content
                    sitenovo = BeautifulSoup(content, 'html.parser')
                    artigo = sitenovo.find_all('div', attrs={'class': 'rprt'})
                    for x in range(0, 8):
                        titulolink = artigo[x].find('div',
                                                    attrs={'class': 'title'})
                        link = titulolink.find('a')
                        link2 = link['href']
                        titulo = link.text
                        detalhes = artigo[x].find('div',
                                                  attrs={'class': 'details'})
                        detalhes1 = detalhes.text
                        listaart.append(
                            f'__**{titulo}**__ \n  {detalhes1}  \n \n LINK: https://www.ncbi.nlm.nih.gov/{link2} \n'
                        )
                    embedpub = discord.Embed(
                        title=f'🔎 Artigos no Pubmed sobre ```{embedtitle}``` 🔍',
                        description='',
                        color=0x133458)
                    embedpub.set_author(
                        name='Ir para o Pubmed',
                        url=f'https://www.ncbi.nlm.nih.gov/pmc/?term={busca}',
                        icon_url='[link da iumagem do autor do embed]')
                    for arquivo in range(0, len(listaart)):
                        embedpub.add_field(name=f'📖 Artigo {arquivo + 1}',
                                           value=f'{listaart[arquivo]}',
                                           inline=False)
                    embedpub.set_thumbnail(url='[link da imagem da sua thumbnail]')
                    embedpub.set_footer(
                        text='Staff do servidor [nome do seu servidor].',
                        icon_url='[link da imagem do seu footer]')
                    await message.channel.send(embed=embedpub)
            except IndexError as erro:
                msgpub = await message.channel.send(
                    f'{message.author.mention} **não há resultados para essa pesquisa no Pubmed.** `{erro}`'
                )
                await message.delete()
                await msgpub.delete(delay=3)

    a = client.get_channel([canal onde os comandos abaixo irão funcionar])
    if message.channel == a:
        if message.content.startswith('=>bibliografia'):
            embed = discord.Embed(title='', description='', color=0x4150C3)
            embed.set_author(
                name='Bibliografias-Medicina',
                url='[link do drive onde está a bibliografia]',
                icon_url='[link da imagem do autor do embed]')
            embed.set_footer(text='Staff do servidor [nome do seu servidor]',
                             icon_url='[link da imagem do seu footer]')
            await message.channel.send(embed=embed)
            await message.delete()

        if message.content.startswith('=>help'):
            embedhelp = discord.Embed(
                title='Bem vindo ao embed de ajuda do Med-info!',
                description='',
                color=0xFFFAFA)
            embedhelp.set_thumbnail(url='[link da imagem da sua thumbnail]')
            embedhelp.set_footer(text='Staff do servidor [nome do seu servidor].',
                                 icon_url='[link da imagem do seu footer]')
            embedhelp.add_field(
                name='=>bibliografia',
                value=
                'Ao utilizar esse comando você receberá um link para um Drive com a bibliografia do curso de medicina (até o terceiro semestre do curso)',
                inline=False)
            embedhelp.add_field(
                name='>p',
                value=
                'Esse comando só pode ser utilizado no canal de texto `pubmed` da categoria biblioteca medicina. Ao utilizar esse comado você deve escrever a pesquisa que deseja realizar no pubmed: >p [pesquisa]. A pesquisa pode ser feita com os operadores booleanos AND, OR, NOT. Exemplo: \n ``` >p covid \n >p covid and spike protein \n >p anxiety disorder not depression \n >p anxiety disorder or depression```',
                inline=False)
            await message.channel.send(embed=embedhelp)

    if message.content.startswith('=>ping'):
        args = message.content.split()
        if len(args) == 1:
            p = (client.latency) * 1000
            await message.channel.send(f'Pong! [{p:.0f}ms]')


keep_alive()
client.run('O TOKEN vai aqui!')
