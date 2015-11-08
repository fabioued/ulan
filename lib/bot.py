import aiml

bot = aiml.Kernel()
bot.learn('brain.aiml')
while True:
    print 'resp -->'+ bot.respond(raw_input('>'))

