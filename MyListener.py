from patitoListener import patitoListener

class MyListener(patitoListener):
    def enterEveryRule(self, ctx):
        print("Enter rule:", type(ctx).__name__)

    def exitEveryRule(self, ctx):
        print("Exit rule:", type(ctx).__name__)

