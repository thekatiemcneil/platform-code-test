class Award(object):
    def __init__(self, name=None, expires_in=None, quality=None):
        self.name = name
        self.expires_in = expires_in
        self.quality = quality

    def update_quality(self, awards):
            for award in awards:
                if award.name != 'Blue First' and award.name != 'Blue Compare':
                    if award.quality > 0:
                        if award.name == 'Blue Star':
                            if award.quality > 1:
                                award.quality -=2
                            else:
                                award.quality = 0
                        elif award.name != 'Blue Distinction Plus':
                            award.quality -= 1
                else:
                    if award.quality < 50:
                        if award.name != 'Blue Star':
                            award.quality += 1
                            if award.name == 'Blue Compare':
                                if award.expires_in < 11:
                                    if award.quality < 50:
                                        award.quality += 1
                                if award.expires_in < 6:
                                    if award.quality < 50:
                                        award.quality += 1

                if award.name != 'Blue Distinction Plus':
                    award.expires_in -= 1

                if award.expires_in < 0:
                    if award.name == 'Blue Star':
                        if award.quality > 1:
                            award.quality -=2
                        else:
                            award.quality = 0
                    elif award.name != 'Blue First':
                        if award.name != 'Blue Compare':
                            if award.quality > 0:
                                if award.name != 'Blue Distinction Plus':
                                    award.quality -= 1
                        else:
                            award.quality = award.quality - award.quality
                    else:
                        if award.quality < 50:
                            award.quality += 1
