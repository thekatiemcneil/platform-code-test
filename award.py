class Award(object):
    def __init__(self, name=None, expires_in=None, quality=None):
        self.name = name
        self.expires_in = expires_in
        self.quality = quality

    def update_quality(self, awards):
            for award in awards:
                # Blue Distinction Plus awards should not change
                if award.name != 'Blue Distinction Plus':
                    if award.name == 'Blue First':
                        self.update_bf(award)
                    elif award.name == 'Blue Compare':
                        self.update_bc(award)
                    elif award.name == 'Blue Star':
                        self.update_bs(award)
                    else:
                        self.update_gen(award)
                    award.expires_in -= 1
                    self.fix_overages(award)

    # update Blue Compare award
    def update_bc(self, award):
        if award.expires_in > 0:
            award.quality += 1
        if award.expires_in <= 10:
            award.quality += 1
        if award.expires_in <= 5:
            award.quality += 1
        if award.expires_in <= 0:
            award.quality = 0

    # update Blue First award
    def update_bf(self, award):
        award.quality += 1
        if award.expires_in <= 0:
            award.quality += 1

    # update Blue Star award
    def update_bs(self, award):
        if award.expires_in > 0:
            award.quality -= 2
        else:
            award.quality -= 4

    # update all other awards
    def update_gen(self, award):
        award.quality -= 1
        if award.expires_in <= 0:
            award.quality -= 1

    # fix any values that have exceeded quality parameters
    def fix_overages(self, award):
        if award.quality > 50: award.quality = 50
        if award.quality < 0: award.quality = 0
