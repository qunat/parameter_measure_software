
class price_parameter(object):
    def __init__(self):
        #-----------------------------SML----------------------------------------------------
        self.dict_price_parameter_slm={}#字典初始化
        self.dict_price_parameter_polishing_slm={"普通级":1,"精密级":1.1,"高难级":1.2}#磨抛参数
        #备注 价格单位 元/g 密度单位 g/cm^2
        #铝合金
        dict_material={"material":"AlSi₁₀Mg","price":8.0,"density":3.0,
                       "single__lowset_price":100,"single_group_lowerst_price":500}#金属烧结参数
        self.dict_price_parameter_slm["AlSi₁₀Mg"]=dict_material#将一种材料的参数输入到总参数
        #不锈钢
        dict_material = {"material": "316L", "price": 4.0, "density": 8.0,
                         "single__lowset_price": 100, "single_group_lowerst_price": 500}  # 金属烧结参数
        self.dict_price_parameter_slm["316L"] = dict_material  # 将一种材料的参数输入到总参数
        # 高温合金
        dict_material = {"material": "Inconel718", "price": 8.0, "density": 8.3,
                         "single__lowset_price": 300, "single_group_lowerst_price": 1000}  # 金属烧结参数
        self.dict_price_parameter_slm["Inconel718"] = dict_material  # 将一种材料的参数输入到总参数
        # 钛合金
        dict_material = {"material": "TC4（Ti₆Al₄V）", "price": 15.0, "density": 4.5,
                         "single__lowset_price": 300, "single_group_lowerst_price": 1000}  # 金属烧结参数
        self.dict_price_parameter_slm["TC4（Ti₆Al₄V）"] = dict_material  # 将一种材料的参数输入到总参数
        # 模具刚
        dict_material = {"material": "Ms1（18Ni300）", "price": 4, "density": 8.0,
                         "single__lowset_price": 100, "single_group_lowerst_price": 500}  # 金属烧结参数
        self.dict_price_parameter_slm["Ms1（18Ni300）"] = dict_material  # 将一种材料的参数输入到总参数
        # 锡青铜
        dict_material = {"material": "QSN6.5-0.4", "price": 6.0, "density": 9,
                         "single__lowset_price": 200, "single_group_lowerst_price": 1000}  # 金属烧结参数
        self.dict_price_parameter_slm["QSN6.5-0.4"] = dict_material  # 将一种材料的参数输入到总参数
        # 铬青铜
        dict_material = {"material": "QCr1", "price": 8.0, "density": 9.0,
                         "single__lowset_price": 200, "single_group_lowerst_price": 1000}  # 金属烧结参数
        self.dict_price_parameter_slm["QCr1"] = dict_material  # 将一种材料的参数输入到总参数
        # 钴铬钨合金
        dict_material = {"material": "CoCrW", "price": 8.0, "density": 8.4,
                         "single__lowset_price": 100, "single_group_lowerst_price": 500}  # 金属烧结参数
        self.dict_price_parameter_slm["CoCrW"] = dict_material  # 将一种材料的参数输入到总参数
        # -----------------------------SLS----------------------------------------------------
        self.dict_price_parameter_sls = {}  # 字典初始化
        # 尼龙12
        dict_material = {"material": "ZRPA12", "price": 5.0, "density": 1.3,
                         "single__lowset_price": 100, "single_group_lowerst_price": 300}  # 粉末烧结
        self.dict_price_parameter_sls["ZRPA12"] = dict_material  # 将一种材料的参数输入到总参数
        # TPU软胶
        dict_material = {"material": "TPU", "price": 10.0, "density": 1.3,
                         "single__lowset_price": 100, "single_group_lowerst_price": 300}  # 粉末烧结
        self.dict_price_parameter_sls["TPU"] = dict_material  # 将一种材料的参数输入到总参数
        # -----------------------------SLA----------------------------------------------------
        self.dict_price_parameter_sla = {}  # 字典初始化
        self.dict_price_parameter_polishing_sla = {"普通级": 1, "精密级": 1.1, "高难级": 1.2}  # 磨抛参数
        # 普通白树脂
        dict_material = {"material": "ZR680", "price": 1.0, "density": 1.3,
                         "single__lowset_price": 20, "single_group_lowerst_price": 200}  # 粉末烧结
        self.dict_price_parameter_sla["ZR680"] = dict_material  # 将一种材料的参数输入到总参数
        # 高精度白树脂
        dict_material = {"material": "ZR300", "price": 1.2, "density": 1.3,
                         "single__lowset_price": 20, "single_group_lowerst_price": 300}  # 粉末烧结
        self.dict_price_parameter_sla["ZR300"] = dict_material  # 将一种材料的参数输入到总参数
        # 半透明白树脂
        dict_material = {"material": "ZR820", "price": 1.5, "density": 1.3,
                         "single__lowset_price": 30, "single_group_lowerst_price": 200}  # 粉末烧结
        self.dict_price_parameter_sla["ZR820"] = dict_material  # 将一种材料的参数输入到总参数
        # 强韧白色树脂
        dict_material = {"material": "Somos® Ledo", "price": 2.0, "density": 1.3,
                         "single__lowset_price": 50, "single_group_lowerst_price": 300}  # 粉末烧结
        self.dict_price_parameter_sla["Somos® Ledo"] = dict_material  # 将一种材料的参数输入到总参数
        # 铸造树脂
        dict_material = {"material": "Somos ® WaterShed XC 11122", "price": 3.0, "density": 1.4,
                         "single__lowset_price": 50, "single_group_lowerst_price": 300}  # 粉末烧结
        self.dict_price_parameter_sla["SSomos ® WaterShed XC 11122"] = dict_material  # 将一种材料的参数输入到总参数
        # 蓝黑色强韧树脂
        dict_material = {"material": "Somos® Taurus", "price": 3.0, "density": 1.4,
                         "single__lowset_price": 50, "single_group_lowerst_price": 300}  # 粉末烧结
        self.dict_price_parameter_sla["Somos® Taurus"] = dict_material  # 将一种材料的参数输入到总参数
        # 韧性光敏树脂
        dict_material = {"material": "ZR730", "price": 1.0, "density": 1.4,
                         "single__lowset_price": 20, "single_group_lowerst_price": 200}  # 粉末烧结
        self.dict_price_parameter_sla["ZR730"] = dict_material  # 将一种材料的参数输入到总参数
        #------------------符合所有参数---------------------------------------------------------
        self.manufacture_parameter={}
        self.manufacture_parameter["SLM"]=self.dict_price_parameter_slm
        self.manufacture_parameter["SLS"] = self.dict_price_parameter_sls
        self.manufacture_parameter["SLA"] = self.dict_price_parameter_sla
    def choose_parameter(self,manufacture,material,process,volume):
        pass

    def calculate_price(self,process,volume):
        pass

