import authz

authz.id("1893701490")  # Buyer's secret 10-digit key

from telegram.ext import ApplicationBuilder

app = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()
# continue as normal...
