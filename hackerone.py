#!/usr/bin/python3
#-*- coding: utf-8 -*-

from os import system
from requests import get
from requests.structures import CaseInsensitiveDict
from json import loads
from urlextract import URLExtract
from time import sleep
from sys import argv

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Basic aDF1Z3Jvb246YVlVZ1hDazNUSGtNNTRmbWRsUHhrZXk4clhxc1VFalpWWXNjc1lwWm1Kaz0="

for dululu in range(argv[1], int(argv[1] + 1)):
    url1 = str("https://api.hackerone.com/v1/hackers/programs?page%5Bsize%5D=100&page%5Bnumber%5D=" + str(dululu))

    b = loads(get(url1, headers=headers).text)

    for i in range(argv[2], argv[3]):
        handle = b['data'][i]['attributes']['handle']

        while handle is not None:
            url2 = str("https://api.hackerone.com/v1/hackers/programs/" + str(handle))

            c = loads(get(url2, headers=headers).text)

            uzunluk = c["relationships"]['structured_scopes']['data']

            for pompala in range(len(uzunluk)):
                try:
                    tip = c["relationships"]['structured_scopes']['data'][pompala]['attributes']['asset_type']
                    asset = c["relationships"]['structured_scopes']['data'][pompala]['attributes']['asset_identifier']
                    instruction = c["relationships"]['structured_scopes']['data'][pompala]['attributes']['instruction']

                    try:
                        tip2 = c["relationships"]['structured_scopes']['data'][pompala]['attributes']['availability_requirement']
                        gecer = True

                    except:
                        gecer = False


                    if "," in asset:
                        asset = URLExtract().find_urls(asset)

                        pijlik = True

                    else:
                        pijlik = False


                    if pijlik == True:
                        for pij in asset:
                            if gecer != False:
                                if tip == "OTHER" and str(tip2) != "none":
                                    pompalareis = URLExtract().find_urls(instruction)

                                    blacklist = ["google", "apple", "android", "appstore"]

                                    for pompaliyorumreis in pompalareis:
                                        if pompaliyorumreis not in blacklist:

                                            asset = pompaliyorumreis

                                            if pij.count("*") > 1:
                                                continue

                                            elif str(pij[:1]) == "*":
                                                system("ayikla " + str(pij[2:]))

                                            elif str(pij[:9]) == "https://*":
                                                system("ayikla " + str(pij[10:]))

                                            elif str(pij[:8]) == "http://*":
                                                system("ayikla " + str(pij[9:]))

                                            elif str(pij[:1]) != "*" and "*" in pij:
                                                pass

                                            elif str(pij[:9]) != "https://*" and "*" in pij:
                                                pass

                                            elif str(pij[:8]) != "http://*" and "*" in pij:
                                                pass


                                            elif str(pij[:8]) == "https://":
                                                system("echo \"" + pij + "\"")


                                            elif str(pij[:7]) == "http://":
                                                system("echo \"" + pij + "\"")

                                            else:
                                                system("echo \"" + "https://" + pij + "\"")


                                elif tip == "URL" and str(tip2) != "none":
                                    if pij.count("*") > 1:
                                        pass

                                    elif str(pij[:1]) == "*":
                                        system("ayikla " + str(pij[2:]))

                                    elif str(pij[:9]) == "https://*":
                                        system("ayikla " + str(pij[10:]))

                                    elif str(pij[:8]) == "http://*":
                                        system("ayikla " + str(pij[9:]))

                                    elif str(pij[:1]) != "*" and "*" in pij:
                                        pass

                                    elif str(pij[:9]) != "https://*" and "*" in pij:
                                        pass

                                    elif str(pij[:8]) != "http://*" and "*" in pij:
                                        pass


                                    elif str(pij[:8]) == "https://":
                                        system("echo \"" + pij + "\"")


                                    elif str(asset[:7]) == "http://":
                                        system("echo \"" + pij + "\"")

                                    else:
                                        system("echo \"" + "https://" + pij + "\"")

                            elif gecer != True:
                                if tip == "URL":
                                    if pij.count("*") > 1:
                                        pass

                                    elif str(pij[:1]) == "*":
                                        system("ayikla " + str(pij[2:]))


                                    elif str(pij[:9]) == "https://*":
                                        system("ayikla " + str(pij[10:]))

                                    elif str(pij[:8]) == "http://*":
                                        system("ayikla " + str(pij[9:]))


                                    elif str(pij[:1]) != "*" and "*" in pij:
                                        pass

                                    elif str(pij[:9]) != "https://*" and "*" in pij:
                                        pass

                                    elif str(pij[:8]) != "http://*" and "*" in pij:
                                        pass


                                    elif str(pij[:8]) == "https://":
                                        system("echo \"" + pij + "\"")


                                    elif str(pij[:7]) == "http://":
                                        system("echo \"" + pij + "\"")

                                    else:
                                        system("echo \"" + "https://" + pij + "\"")


                    else:
                        if gecer != False:
                            if tip == "URL" and str(tip2) != "none":
                                if asset.count("*") > 1:
                                    pass

                                elif str(asset[:1]) == "*":
                                    system("ayikla " + str(asset[2:]))

                                elif str(asset[:9]) == "https://*":
                                    system("ayikla " + str(asset[10:]))

                                elif str(asset[:8]) == "http://*":
                                    system("ayikla " + str(asset[9:]))

                                elif str(asset[:1]) != "*" and "*" in asset:
                                    pass

                                elif str(asset[:9]) != "https://*" and "*" in asset:
                                    pass

                                elif str(asset[:8]) != "http://*" and "*" in asset:
                                    pass


                                elif str(asset[:8]) == "https://":
                                    system("echo \"" + asset.replace(",", "\n") + "\"")


                                elif str(asset[:7]) == "http://":
                                    system("echo \"" + asset.replace(",", "\n") + "\"")

                                else:
                                    system("echo \"" + "https://" + asset + "\"")

                        elif gecer != True:
                            if tip == "URL":
                                if asset.count("*") > 1:
                                    pass

                                elif str(asset[:1]) == "*":
                                    system("ayikla " + str(asset[2:]))


                                elif str(asset[:9]) == "https://*":
                                    system("ayikla " + str(asset[10:]))

                                elif str(asset[:8]) == "http://*":
                                    system("ayikla " + str(asset[9:]))


                                elif str(asset[:1]) != "*" and "*" in asset:
                                    pass

                                elif str(asset[:9]) != "https://*" and "*" in asset:
                                    pass

                                elif str(asset[:8]) != "http://*" and "*" in asset:
                                    pass


                                elif str(asset[:8]) == "https://":
                                    system("echo \"" + asset + "\"")


                                elif str(asset[:7]) == "http://":
                                    system("echo \"" + asset + "\"")

                                else:
                                    system("echo \"" + "https://" + asset + "\"")

                except:
                    sleep(10)

            break
