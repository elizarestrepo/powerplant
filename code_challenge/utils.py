class powerplant:
    def __init__(self,data):
        self.load = data['load']
        self.fuels = data['fuels']

    def order_powerplants(self, plants):
        for plant in plants:
            if plant['type'] == 'windturbine':
                plant['pmax'] = self.get_pmax(plant)
            plant['cost'] = self.feul_cost(plant)
        newlist_powerplants = sorted(plants, key=lambda d: (d['efficiency'],d['cost']),reverse=True)
        return newlist_powerplants
    
    
    def get_pmax(self, plant):
        pmax = plant['pmax'] * self.fuels['wind(%)']/100
        return pmax

    def feul_cost(self,plant):
        if plant['type'] == 'windturbine':
            cost = 0
        elif plant['type'] == 'gasfired':
            cost = self.fuels['gas(euro/MWh)'] / plant['efficiency']
        elif plant['type'] == 'turbojet':
            cost = self.fuels['kerosine(euro/MWh)'] / plant['efficiency']
        else:
            cost = 0
        return cost
    
    def power(self, plants):
        response = []
        total_load = self.load
        for plant in plants:
            res = {}
            if total_load == 0:
                res['name'] = plant['name']
                res['p'] = 0
            elif plant['pmin'] > total_load:
                res['name'] = plant['name']
                res['p'] = 0
            elif plant['pmax'] > total_load and total_load>0:
                res['name'] = plant['name']
                res['p'] = total_load
                total_load=0
            else:
                res['name'] = plant['name']
                res['p'] = plant['pmax']
                total_load -= plant['pmax']
                
            response.append(res)
                
        return response