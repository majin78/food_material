material_list=[
    ['花菜','菜花'],
    ['虾'],
    ['木耳'],
    ['番茄','西红柿'],
    ['鸡蛋'],
    ['柠檬'],
    ['南瓜 '],
    ['炒肉','肉丝','肉片'],
    ['牛肉'],
    ['蕨菜'],
    ['炒蛋','炒鸡蛋'],
    ['炒肉'],
    ['米线'],
    ['猪蹄'],
    ['鸡爪'],
    ['鸭肠'],
    ['魔芋'],
    ['海带'],
    ['冬瓜'],
    ['山药'],
    ['白菜'],
    ['茶树菇'],
    ['紫菜'],
    ['青瓜'],
    ['生菜'],
    ['木耳'],
    ['杏鲍菇'],
    ['回锅肉'],
    ['肉末'],
    ['豆腐'],
    ['茄子'],
    ['土豆'],
    ['肥肠','大肠'],
    ['胡萝卜'],
    ['排骨'],
    ['草头'],
    ['腰花'],
    ['菠菜'],
    ['青椒'],
    ['四季豆','豆角'],
    ['莴笋'],
    ['菠萝'],
    ['八爪鱼'],
    ['豆皮'],
    ['叉烧'],
    ['鸡丁'],
    ['苦瓜'],
    ['玉米'],
    ['莲白','莲花白','卷心菜','包菜'],
    ['狮子头'],
    ['鱼头'],
    ['花甲'],
    ['藕'],
    ['空心菜'],
    ['鸡翅'],
    ['鸡腿'],
    ['洋葱'],
    ['鱿鱼'],
    ['豇豆'],
    ['平菇'],
    ['西芹'],
    ['西葫芦'],
    ['韭菜'],
    ['莴笋'],
    ['丝瓜'],
    ['豆芽'],
    ['火腿肠','香肠'],
    ['豆干'],
    ['鳗鱼'],
    ['肥牛'],
    ['腰果'],
    ['黄瓜'],
    ['丸子','肉丸'],
    ['金针菇'],
    ['粉条'],
    ['香菇'],
    ['带鱼'],
    ['牛腩'],
    ['西兰花'],
    ['腊肉'],
    ['蒜苔'],
    ['豌豆','青豆'],
    ['芋儿'],
    ['鸡块'],
    ['芦笋'],
    ['鸡丝'],
    ['蘑菇'],
    ['葱蒜'],
    ['百合'],
    ['竹笋'],
    ['芥兰'],
    ['鱼块'],
    ['里脊'],
    ['海参'],
    ['酥肉'],
    ['腐竹'],
    ['茭白'],
    ['花生'],
    ['培根'],
    ['萝卜丝'],
    ['肚'],
    ['百叶']
]


def get_matarray_num(mat_array, mat_name):
    '''
    根据食材的名称获取食材的编号
    :param mat_array: 食材数组
    :param mat_name: 食材的名称
    :return: 食材的编号
    '''
    for i in mat_array:
        if mat_name in i:
            return mat_array.index(i)
    return None


