import authz

authz.id("1893701490")  # Buyer's secret 10-digit key

from telegram.ext import ApplicationBuilder

app = ApplicationBuilder().token("7576028578:AAEGN2qk4NUd30yCxXGsnAUTwZMn7l99cRU").build()
# continue as normal...
