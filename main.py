import webview
import math


class App:
    def __init__(self):
        self.rho = 0
        self.L = 0
        self.LQ = 0
        self.W = 0
        self.WQ = 0
        self.P0 = 0
        self.Pn = 0

    def calc(self, s, la, mu, n):
        rho = la / (s*mu)

        # calculating probability that there are no customers in the system (P0)
        i = 0
        kiri = 0

        while i <= s-1:
            apanih = ((la/mu)**i) / (math.factorial(int(i)))
            kiri += apanih
            i += 1

        tengah = ((la/mu)**s) / (math.factorial(int(s)))
        kanan = 1 / (1 - (rho))
        p0 = 1 / (kiri + tengah * kanan)
        # calculating average number of customer in waiting line for service
        lq = p0 * (((la/mu)**s) / math.factorial(int(s))) * \
            ((rho) / ((1-rho)**2))
        # calculating average time a customer spends in waiting line for service
        wq = lq/la
        # calculating average number of customer in the system (in waiting line and being served)
        l = lq + la/mu
        # calculating average time a consumer spends in the system (in waiting line and being service)
        w = wq + 1/mu
        # calculating probability that there are n customers in the system
        if s <= n:
            cn = ((la/mu)**n) / ((math.factorial(int(s)) * s**(n-s)))
        else:
            cn = ((la/mu)**n) / (math.factorial(int(n)))

        pn = cn * p0

        self.rho = rho
        self.L = l
        self.LQ = lq
        self.W = w
        self.WQ = wq
        self.P0 = p0
        self.Pn = pn

    def getRho(self):
        return "{:.4f}".format(self.rho)

    def getL(self):
        return "{:.4f}".format(self.L)

    def getLQ(self):
        return "{:.4f}".format(self.LQ)

    def getW(self):
        return "{:.4f}".format(self.W)

    def getWQ(self):
        return "{:.4f}".format(self.WQ)

    def getP0(self):
        return "{:.4f}".format(self.P0)

    def getPN(self):
        return "{:.4f}".format(self.Pn)


app = App()

window = webview.create_window(
    "Queue M/M/C",
    "index.html",
    js_api=App(),
    width=1200,
    height=800
)
webview.start()
