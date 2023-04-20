import PIL.ImageColor

from ortex.Visualisation import VisHelper, Crossroad, Road, Building, Field, Space


def colors():
    ret = ""
    for name, code in PIL.ImageColor.colormap.items():
        ret += f'{name:30} : {code}\n'
    return ret


def ex1():
    space = VisHelper.helpSpaceCreate(3000, 3000)
    VisHelper.helpAddCrossroad(space, 100, 100, 50, True)
    VisHelper.helpAddCrossroad(space, 500, 500, 50, True)
    VisHelper.helpAddRoadCon(space, 0, True, True, True, True, 10, space.crossroads[0],
                             space.crossroads[1])
    VisHelper.helpAddRoadUnCon(space, 1, True, True, False, False, 20,
                               space.crossroads[1], 0, 1000)
    # "1500, 1500; 1000, 1500; 1000, 550; 1500, 550"
    VisHelper.helpAddBuilding(space, 'Bank', ((1500, 1500), (1000, 1500), (1000, 550), (1500, 550)), "thistle")

    space.draw()


def ex2():
    space = VisHelper.helpSpaceCreate(3000, 3000)
    for y in [500, 1500, 2500]:
        for x in [500, 1500, 2500]:
            if y != 1500 or x != 500:
                VisHelper.helpAddCrossroad(space, x, y, 70, True)

    VisHelper.helpAddCrossroad(space, 500, 1500, 80, False)

    road_size = 70

    VisHelper.helpAddRoadUnCon(space, 0, False, False, 1, False, road_size, space.crossroads[8], 180, 500)
    VisHelper.helpAddRoadUnCon(space, 1, False, False, 1, False, road_size, space.crossroads[1], 90, 500)

    VisHelper.helpAddRoadCon(space, 2, True, True, 2, False, road_size, space.crossroads[0], space.crossroads[8])
    VisHelper.helpAddRoadCon(space, 3, True, True, 1, True, road_size, space.crossroads[0], space.crossroads[1])
    VisHelper.helpAddRoadCon(space, 4, True, True, 1, False, road_size, space.crossroads[1], space.crossroads[2])
    VisHelper.helpAddRoadCon(space, 5, False, False, 1, False, road_size, space.crossroads[2], space.crossroads[4])
    VisHelper.helpAddRoadCon(space, 6, False, False, 1, True, road_size, space.crossroads[2], space.crossroads[3])
    VisHelper.helpAddRoadCon(space, 7, False, False, 1, False, road_size, space.crossroads[8], space.crossroads[3])
    VisHelper.helpAddRoadCon(space, 8, False, False, 1, False, road_size, space.crossroads[8], space.crossroads[6])
    VisHelper.helpAddRoadCon(space, 9, False, False, 1, False, road_size, space.crossroads[5], space.crossroads[6])
    VisHelper.helpAddRoadCon(space, 10, False, False, 1, False, road_size, space.crossroads[6], space.crossroads[7])

    space.draw()


if __name__ == "__main__":
    # print(colors())
    ex1()
    #ex2()
