import json, requests, config, logging
class osuapi:
    logger = logging.getLogger('osuapi')
    def __init__(self):
        data = self.fetchAPI()
        if data != None:
            data = data['list'][0]
            self.hit300 =['count300']
            self.hit100 = data['count100']
            self.hit50 = data['count50']
            self.hitgeki = data['countGeki']
            self.hitkatu = data['countKatu']
            self.miss = data['countMiss']
            self.combo = data['combo']
            self.health = data['healthPoint']
            self.accuracy = data['accuracy']
            self.score = data['score']
    def fetchAPI(self) -> json:
        try:
            data = requests.get(config.API_URL+"/api/ortdp/playing/info")
            return json.loads(data.text)
        except:
            self.logger.error("Failed to connect to osu! API")
            return None