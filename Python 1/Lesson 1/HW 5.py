uzegnii_bagtsiin_too = int(input())
markeriin_bagtsiin_too = int(input())
sambar_tsewerlegch_litriin_too = int(input())
hongololtiin_huwi = int(input())

uzegnii_une = 5.80
markeriin_une = 7.20
sambar_tsewerlegch_une = 1.20

niit_une = (uzegnii_bagtsiin_too * uzegnii_une) + (markeriin_bagtsiin_too * markeriin_une) + (sambar_tsewerlegch_litriin_too * sambar_tsewerlegch_une)
hongololtiin_huwi = (hongololtiin_huwi / 100) * niit_une
toloh_dun = niit_une - hongololtiin_huwi

print(toloh_dun)
