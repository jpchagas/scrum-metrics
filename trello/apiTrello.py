import requests
import json as js

class trello:

    def __init__ (self):
        self.key = 'b81b5034af037e281b66b0e3003aed54'
        self.token = 'b245830c847a571a888ee4b948f66ab8ba385342284e32d6ab11e647b1c55635'
        self.board = 'UBfMCuQF'


    def getBoard(self):
        url = "https://api.trello.com/1/boards/" + self.board

        querystring = {"actions":"all","boardStars":"none","cards":"none","card_pluginData":"false","checklists":"none","customFields":"false","fields":"name,desc,descData,closed,idOrganization,pinned,url,shortUrl,prefs,labelNames","lists":"open","members":"none","memberships":"none","membersInvited":"none","membersInvited_fields":"all","pluginData":"false","organization":"false","organization_pluginData":"false","myPrefs":"false","tags":"false","key":self.key,"token":self.token}

        response = requests.request("GET", url, params=querystring)

        print(response.text)

    def getCards(self):
        self.limit = '1000'
        url = 'https://api.trello.com/1/boards/' + self.board + '/cards/?limit=' + self.limit + '&fields=name&members=true&member_fields=fullName&key=' + self.key + '&token=' + self.token
        
        headers = {
            'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
        }

        call = requests.get(url , headers=headers)
        dic = js.loads(call.text)
        cards = {}
        for cardindex in range(len(dic)):
            card = dic[cardindex]
            cards.update({card['id']:card['name']})
        
        return cards


    def getCardID(self,cardId):
        self.idCard = cardId
        
        url = 'https://trello.com/1/boards/' + self.board + '/cards/' + self.idCard + '?key=' + self.key + '&token=' + self.token

        headers = {
            'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
        }

        call = requests.get(url , headers=headers)
        dic = js.loads(call.text)
        card_detail={}
        card_detail.update({'cardid':dic['id']})
        card_detail.update({'listid':dic['idList']})
        return card_detail

    def getMember(self):
        self.member = '550a1457c58a3212b6851477'

        url = "https://api.trello.com/1/members/" + self.member

        querystring = {"boardBackgrounds":"none","boardsInvited_fields":"name,closed,idOrganization,pinned","boardStars":"false","cards":"none","customBoardBackgrounds":"none","customEmoji":"none","customStickers":"none","fields":"all","organizations":"none","organization_fields":"all","organization_paid_account":"false","organizationsInvited":"none","organizationsInvited_fields":"all","paid_account":"false","savedSearches":"false","tokens":"none","key": self.key,"token":self.token}

        response = requests.request("GET", url, params=querystring)

        print(response.text)

    def getLists(self):
        url = 'https://api.trello.com/1/boards/' + self.board + '/lists/' + '?key=' + self.key + '&token=' + self.token
        headers = {
            'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
        }

        call = requests.get(url , headers=headers)
        dic = js.loads(call.text)
        lanes = list()
        for laneindex in range(len(dic)):
            laneinfo = {}
            lane = dic[laneindex]
            laneinfo.update({'laneid':lane['id']})
            laneinfo.update({'lanename':lane['name']})
            lanes.append(laneinfo)
        return lanes