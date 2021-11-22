from py_expression_eval import Parser
import sympy
import discord
from discord.ext import commands
from discord.commands import Option
import requests
from python.Biseccion import Biseccion
from python.BusquedasIncrementales import BusquedasIncrementales
from python.Newton import Newton
from python.PuntoFijo import PuntoFijo
from python.ReglaFalsa import ReglaFalsa
from python.Secante import Secante
from python.RaicesMultiples import RaicesMultiples
from python.gaussPipSim import gaussPipSimp
import asyncio
from python.gaussPipPar import gaussPipPar
from python.gaussPipTot import gaussPipTot
from python.gaussSeidel import gaussSeidel
from python.vandermonde import vandermonde as bb
from python.lagrange import lagrange as lagranja
from python.difdivs import difDivs 
from python.token import TOKEN
class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix = commands.when_mentioned_or("$"),case_insensitive=True)

    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("----------------------------------------------")

bot = Bot()

variable = sympy.Symbol('x')

def Evaluar(funcion,x):
    parser = Parser()
    return parser.parse(funcion).evaluate({'x': x}) 

@bot.slash_command(guild_ids=[908525393152180264])
async def derivar(
    ctx,
    funcion: Option(str, "Pone la funcion pa destruirla"),
    ):
    derivada = str(sympy.diff(funcion,variable))
    if '**' in derivada:
        derivada = derivada.replace('**','^')
    await ctx.respond(f'`{derivada}`')

@bot.slash_command(guild_ids=[908525393152180264])
async def busquedas_incrementales(
    interaction : discord.Interaction,
    funcion: Option(str, "Pone la funcion"),
    x0: Option(float, "Pone un X"),
    delta: Option(float, "Pone un delta"),
    iter: Option(int, "Pone las iteraciones"),
    ):
    datos, grafica = BusquedasIncrementales(funcion,x0,delta,iter)
    if not grafica:
        await interaction.response.send_message(datos)
        return 

    embedVar = discord.Embed(title = "Busquedas Incrementales 🔍📈", color = discord.Color.greyple())
    embedVar.add_field(name = "valores",value = '\n'.join([f'{x} : {y}'for x, y in datos.items()]))
    UwU = discord.File(grafica, filename = 'graf.jpg')
    embedVar.set_image(url = "attachment://graf.jpg")
    await interaction.response.send_message(embed = embedVar,file = UwU)

    

@bot.slash_command(guild_ids=[908525393152180264])
async def biseccion(
    interaction : discord.Interaction,
    funcion: Option(str, "Pone la funcion"),
    x0: Option(float, "Pone un X"),
    x1: Option(float, "Pone un delta"),
    tol: Option(float, "Pone la toleracia"),
    ):
    datos, grafica = Biseccion(x0,x1,tol,funcion)
    if not grafica:
        await interaction.response.send_message(datos)
        return 

    embedVar = discord.Embed(title = "Biseccion 🔀", color = discord.Color.yellow())
    embedVar.add_field(name = "valores",value = '\n'.join([f'{x} : {y}'for x, y in datos.items()]))
    UwU = discord.File(grafica, filename = 'graf.jpg')
    embedVar.set_image(url = "attachment://graf.jpg")
    await interaction.response.send_message(embed = embedVar,file = UwU)


@bot.slash_command(guild_ids=[908525393152180264])
async def regla_falsa(
    ctx,
    funcion: Option(str, "Pone la funcion"),
    x0: Option(float, "Pone un X"),
    x1: Option(float, "Pone un delta"),
    tol: Option(float, "Pone la tolerancia"),
    ):

    datos, error = ReglaFalsa(x0,x1,tol,funcion)
    if error:
       await ctx.respond(datos)
       return 
    embedVar = discord.Embed(title = "Regla Falsa 📏❓", color = discord.Color.brand_red())
    embedVar.add_field(name = "valores",value = '\n'.join([f'{x} : {y}'for x, y in datos.items()]))
    await ctx.respond(embed=embedVar)


@bot.slash_command(guild_ids=[908525393152180264])
async def punto_fijo(
    interaction : discord.Interaction,
    funcion_g: Option(str, "Pone la funcion"),
    x0: Option(float, "Pone un X"),
    tol: Option(float, "Pone un delta"),
    iter: Option(int, "Ponelo xd"),
    ):

        datos,graf = PuntoFijo(x0, tol, iter, funcion_g)
        embedVar = discord.Embed(title = "Punto Fijo ⏺📌", color = discord.Color.blurple())
        embedVar.add_field(name = "valores",value = '\n'.join([f'{x} : {y}'for x, y in datos.items()]))
        UwU = discord.File(graf, filename = 'graf.jpg')
        embedVar.set_image(url = "attachment://graf.jpg")
        await interaction.response.send_message(embed = embedVar,file = UwU)

@bot.slash_command(guild_ids=[908525393152180264])
async def newton(
    interaction : discord.Interaction,
    funcion: Option(str, "Pone la funcion"),
    x0: Option(float, "Pone un X"),
    tol: Option(float, "Pone una delta"),
    iter: Option(int, "Ponelo xd"),
    ):
    derivada = str(sympy.diff(funcion,variable))
    datos,graf = Newton(x0, tol, iter, funcion, derivada)
    if not graf:
        await interaction.response.send_message(datos)
        return
    embedVar = discord.Embed(title = "Newton 🍎", color = discord.Color.brand_red())
    embedVar.add_field(name = "valores",value = '\n'.join([f'{x} : {y}'for x, y in datos.items()]))
    UwU = discord.File(graf, filename = 'graf.jpg')
    embedVar.set_image(url = "attachment://graf.jpg")
    await interaction.response.send_message(embed = embedVar,file = UwU)

@bot.slash_command(guild_ids=[908525393152180264])
async def secante(
    ctx,
    funcion: Option(str, "Pone la funcion"),
    x0: Option(float, "Pone un X"),
    x1: Option(float, "Pone un X"),
    tol: Option(float, "Pone un delta"),
    iter: Option(int, "Ponelo xd"),
    ):
        datos, error = Secante(x0, x1, tol, iter, funcion)
        if error:
            await ctx.respond(datos)
            return
        embedVar = discord.Embed(title = "Secante 🛐", color = discord.Color.brand_red())
        embedVar.add_field(name = "valores",value = '\n'.join([f'{x} : {y}'for x, y in datos.items()]))
        await ctx.respond(embed = embedVar)

@bot.slash_command(guild_ids=[908525393152180264])
async def raices_multiples(
    ctx,
    funcion: Option(str, "Pone la funcion"),
    x0: Option(float, "Pone un X"),
    tol: Option(float, "Pone un tol"),
    iter: Option(int, "Ponelo xd"),
    ):
    """Method"""
    derivada = str(sympy.diff(funcion,variable))
    segunda = str(sympy.diff(derivada,variable))

    datos = RaicesMultiples(x0, tol, iter, funcion, derivada, segunda)
    embedVar = discord.Embed(title = "Raices multiples 🌱♾", color = discord.Color.greyple())
    embedVar.add_field(name = "valores",value = '\n'.join([f'{x} : {y}'for x, y in datos.items()]))
    await ctx.respond(embed = embedVar)

@bot.command()
async def Gauss(ctx,n:int):
    embedVar = discord.Embed(title = 'Gauss')
    embedVar.add_field(name = f'Matriz {n}x{n}', value = 'Ingresa la primera fila')
    mensajeBot = await ctx.send(embed = embedVar)
    matriz,error = await RecibirMatriz(ctx,n,embedVar,mensajeBot)
    if not matriz:
        await ctx.send(error)
    else:
        resultado = gaussPipSimp(n,matriz)
        embedVar.add_field(name = 'Resultado Gauss Simple',value = resultado)
        await mensajeBot.edit(embed = embedVar)

async def RecibirMatriz(ctx,n,embedVar,mensajeBot):
    matriz = []
    def check(msg):
        return msg.author == ctx.author
    for i in range(n):
        try:
            mensaje = await bot.wait_for('message', timeout=120.0, check=check)
        except asyncio.TimeoutError:
            error = 'Te demoraste mucho en ingresar los valores'
            return False,error
        else:
            fila = [float(numero) if check_float(numero) else False for numero in mensaje.content.split(',')]
            print (fila)
            if False in fila or len(fila) != n+1:
                error = 'Ingresaste un valor mas o no ingresaste un valor numerico'
                return False,error
            matriz.append(fila)    
            embedVar.set_field_at(0,name = f'Matriz {n}x{n}',value = '\n'.join([f'**{arreglo}**' for arreglo in matriz]))
            await mensajeBot.edit(embed = embedVar)
            await mensaje.delete()
    return matriz,True

def check_float(potential_float):
    try:
        float(potential_float)
        return True
    except ValueError:
        return False

@bot.command()
async def Gauss_Partial(ctx,n:int):
    embedVar = discord.Embed(title = 'Gauss partial')
    embedVar.add_field(name = f'Matriz {n}x{n}', value = 'Ingresa la primera fila')
    mensajeBot = await ctx.send(embed = embedVar)
    matriz,error = await RecibirMatriz(ctx,n,embedVar,mensajeBot)
    if not matriz:
        await ctx.send(error)
    else:
        b = [fila.pop() for fila in matriz]
        resultado = gaussPipPar(matriz, b)
        embedVar.add_field(name = 'Resultado Gauss Simple',value = resultado)
        await mensajeBot.edit(embed = embedVar)

@bot.command()
async def Gauss_total(ctx,n:int):
    embedVar = discord.Embed(title = 'Gauss total')
    embedVar.add_field(name = f'Matriz {n}x{n}', value = 'Ingresa la primera fila')
    mensajeBot = await ctx.send(embed = embedVar)
    matriz,error = await RecibirMatriz(ctx,n,embedVar,mensajeBot)
    if not matriz:
        await ctx.send(error)
    else:
        resultado = gaussPipTot(matriz, n)
        embedVar.add_field(name = 'Result Gauss total',value = resultado)
        await mensajeBot.edit(embed = embedVar)

@bot.command()
async def Gauss_Seidel(ctx,n:int,tol:float,iter:int):
    embedVar = discord.Embed(title = 'Gauss Seidel')
    embedVar.add_field(name = f'Matriz {n}x{n}', value = 'Ingresa la primera fila')
    mensajeBot = await ctx.send(embed = embedVar)
    matriz,error = await RecibirMatriz(ctx,n,embedVar,mensajeBot)
    if not matriz:
        await ctx.send(error)
    else:
        b = [fila.pop() for fila in matriz]
        resultado = gaussSeidel(matriz, b, tol, iter)
        embedVar.add_field(name = 'Result Gauss Seidel',value = resultado)
        await mensajeBot.edit(embed = embedVar)

@bot.slash_command(guild_ids=[908525393152180264])
async def vandermonde(
    ctx,
    matrizx: Option(str, "Introducr vector x"),
    matrizy: Option(str, "Introducr vector y"),
    ):

    x = [float(numero) if check_float(numero) else None for numero in matrizx.split(',')]
    y = [float(numero) if check_float(numero) else None for numero in matrizy.split(',')]
    if None in x or None in y:
        await ctx.respond("Valores incorrectos")
        return     
    datos = bb(x, y)
    embedVar = discord.Embed(title = "Vandermonde", color = discord.Color.greyple())
    embedVar.add_field(name = 'Resultado Vandermonde',value = datos)
    await ctx.respond(embed = embedVar)

@bot.slash_command(guild_ids=[908525393152180264])
async def lagrange(
    ctx,
    matrizx: Option(str, "Introducr vector x"),
    matrizy: Option(str, "Introducr vector y"),
    xp: Option(float, "ingrese xp")
    ):

    x = [float(numero) if check_float(numero) else None for numero in matrizx.split(',')]
    y = [float(numero) if check_float(numero) else None for numero in matrizy.split(',')]
    if None in x or None in y:
        await ctx.respond("Valores incorrectos")
        return     
    datos = lagranja(x, y, xp)
    embedVar = discord.Embed(title = "lagrange", color = discord.Color.greyple())
    embedVar.add_field(name = 'Resultado lagrange',value = datos)
    await ctx.respond(embed = embedVar)

@bot.slash_command(guild_ids=[908525393152180264])
async def diferencia_divididas(
    ctx,
    matrizx: Option(str, "Introducr vector x"),
    matrizy: Option(str, "Introducr vector y"),
    ):

    x = [float(numero) if check_float(numero) else None for numero in matrizx.split(',')]
    y = [float(numero) if check_float(numero) else None for numero in matrizy.split(',')]
    if None in x or None in y:
        await ctx.respond("Valores incorrectos")
        return     
    datos = difDivs(x, y)
    embedVar = discord.Embed(title = "Diferencias dividas ", color = discord.Color.greyple())
    embedVar.add_field(name = 'Resultado diferencias divididas',value = datos)
    await ctx.respond(embed = embedVar)

bot.run(TOKEN)