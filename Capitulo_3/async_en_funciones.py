import asyncio
import datetime
import random
from asyncio import sleep


async def respondedor(nombre):
    frases = ['si', 'no']
    elegida = random.choice(frases)
    await sleep(random.choice([0.5, 1, 2]))
    fecha = datetime.datetime.utcnow().strftime('%H:%M:%S')
    return f'{nombre} - {fecha}: {elegida}'


async def preguntador(nombre):
    frases = ['¿Quiere agua?', '¿Vamos al parque?', '¿Quiere comer?', '¿Le gusta el color azul?',
              '¿Hizo buen dia ayer?', '¿Le gustan los perros?', '¿Le gustan los gatos?']
    elegida = random.choice(frases)
    await sleep(random.choice([0.5, 1, 2]))
    fecha = datetime.datetime.utcnow().strftime('%H:%M:%S')
    return f'{nombre} - {fecha}: {elegida}'


async def chat(nombre_pregunta, nombre_respuesta, chat_id):
    for _ in range(5):
        nombre_pregunta, nombre_respuesta = nombre_respuesta, nombre_pregunta
        pregunta = await preguntador(nombre_pregunta)
        print(f'chat {chat_id}: {pregunta}')
        respuesta = await respondedor(nombre_respuesta)
        print(f'chat {chat_id}: {respuesta}')
    return True


async def main(participantes):
    chats = []
    for idx, (part1, part2) in enumerate(participantes):
        chats.append(chat(part1, part2, idx + 1))
    await asyncio.gather(
        *chats
    )


if __name__ == '__main__':
    asyncio.run(chat('Juan', 'Juana', 1))
    print('Terminado el chat simple')

    asyncio.run(main([('Ana', 'Antonio'), ('Mario', 'María'), ('Pepe', 'Pepa'), ('Juan', 'Josefa')]))
