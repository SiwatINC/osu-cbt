import json, requests
class osuapi:
    def __init__(self):
        data = self.fetchAPI()
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
        data = requests.get("http://localhost:10800/api/ortdp/playing/info")
        return json.loads(data.text)