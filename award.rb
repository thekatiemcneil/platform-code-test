class Award
  attr_accessor :name, :expires_in, :quality

  def initialize(name, expires_in, quality)
    @name       = name
    @expires_in = expires_in
    @quality    = quality
  end

  def update_quality(awards)
    awards.each do |award|
      # Blue Distinction Plus awards should not change
      if award.name != 'Blue Distinction Plus'
        case award.name
        when 'Blue First'
          update_bf(award)
        when 'Blue Compare'
          update_bc(award)
        when 'Blue Star'
          update_bs(award)
        else
          update_gen(award)
        end
        award.expires_in -= 1
        fix_overages(award)
      end
    end
  end

  # update Blue Compare award
  def update_bc(award)
    if award.expires_in > 0
      award.quality += 1
    end
    if award.expires_in <= 10
      award.quality += 1
    end
    if award.expires_in <= 5
      award.quality += 1
    end
    if award.expires_in <= 0
      award.quality = 0
    end
  end

  # update Blue First award
  def update_bf(award)
    award.quality += 1
    if award.expires_in <= 0
      award.quality += 1
    end
  end

  # update Blue Star award
  def update_bs(award)
    if award.expires_in > 0
      award.quality -= 2
    else
      award.quality -= 4
    end
  end

  # update all other awards
  def update_gen(award)
    award.quality -= 1
    if award.expires_in <= 0
      award.quality -= 1
    end
  end

  # fix any values that have exceeded quality parameters
  def fix_overages(award)
    if award.quality > 50
      award.quality = 50
    end
    if award.quality < 0
      award.quality = 0
    end
  end

end
