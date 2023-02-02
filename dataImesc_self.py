class dataImesc:
    def __init__(self):
        self.dicio={129:"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/2018|2019|2020|2021/variaveis/143?localidades=N1[all]|N2[all]|N3[21]|N6[2100055,2100808,2101400,2101509,2101608,2101806,2102002,2102036,2102200,2102309,2102325,2102358,2102556,2102804,2103000,2103174,2103208,2103257,2103307,2103406,2103752,2104057,2104073,2104552,2104800,2105302,2105427,2105500,2106102,2106607,2107308,2107803,2109007,2109502,2109551,2109700,2110005,2110104,2110807,2110856,2110906,2111052,2111532,2111573,2111607,2111805,2112001,2112605,2112852]&classificacao=194[0]"}

    def procurar_tabela(self,numero_Tabela):
        import requests as rq
        self.Tabela=self.dicio[numero_Tabela]
        self.Resposta=rq.get(self.Tabela)
        return ((self.Resposta).json())
        