def modifier_for_attribute(_attribute):
    if _attribute == 9:
        return -1
    return (int(_attribute) - 10) // 2


def health_by_class(_class):
    return [None, 12, 6, 8, 8, 10, 8, 10, 8, 6, 4, 4][_class]


def health_by_class_and_level(_class, _level, _const):
    _mod = modifier_for_attribute(_const)
    _base_health = health_by_class(_class) + _mod
    if _base_health <= 0:
        _base_health = 1
    return _base_health * _level


def damage(_str):
    _mod = modifier_for_attribute(_str)
    if _mod <= 1:
        return 1
    else:
        return _mod


def base_attack_bonus_by_class(_class):
    return [None, 4, 3, 3, 3, 4, 3, 4, 4, 3, 2, 2][_class]


def base_attack_bonus_by_class_and_level(_class, _level):
    return _level * base_attack_bonus_by_class(_class) // 4


def attack_bonus(_class, _str, _level):
    return base_attack_bonus_by_class_and_level(_class, _level) + modifier_for_attribute(_str)


def to_hit_ac(_attack_bonus):
    return _attack_bonus > 2


def armor_class(_dex):
    return modifier_for_attribute(_dex)


def sim_reward(_str, _dex, _const, _level, _class):
    _health = health_by_class_and_level(_class, _level, _const)
    _dungeon_health = 10
    _damage = damage(_str)
    _attack_bonus = attack_bonus(_class, _str, _level)
    _to_hit_ac = to_hit_ac(_attack_bonus)
    _hit_ac = armor_class(_dex)
    if _to_hit_ac:
        for reward in [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]:
            _dungeon_health -= _damage
            if _dungeon_health <= 0:
                break
            if _hit_ac:
                _health -= _dungeon_health
            if _health <= 0:
                return 0
        return reward
    return 0


def attr(score):
    if score <= 14:
        return score - 8
    else:
        return ((score - 8)**2)//6


if __name__=='__main__':
    for a in range(9, 23):
        for b in range(9, 23):
            for c in range(9, 23):
                for d in range(9, 23):
                    for e in range(9, 23):
                        for f in range(9, 23):
                            if attr(a)+attr(b)+attr(c)+attr(d)+attr(e)+attr(f) > 32:
                                break
                            if attr(a)+attr(b)+attr(c)+attr(d)+attr(e)+attr(f) != 32:
                                continue
                            r = sim_reward(a, b, c, 1, 1)
                            if r == 0:
                                break
                            print(a, b, c, d, e, f, r)
