import math
import enum
import sys

from PIL import Image, ImageDraw, ImageFont, ImageColor

'''
        addField = 1
        addBuilding = 2
        addCross = 3
        addRoadUn = 4
        addRoad = 5
        draw = 6
        Cross = 7
        colors = 8
'''

fields_types = [
    'ellipse',
    'rectangle',
    'polygon',
    'chord',
    'pieslice'
]


def linedashed(x0, y0, x1, y1, draw, dashlen=14, ratio=3):
    dx = x1 - x0  # delta x
    dy = y1 - y0  # delta y
    # check whether we can avoid sqrt
    l = math.sqrt(dx * dx + dy * dy)  # length of line
    xa = dx / l  # x add for 1px line length
    ya = dy / l  # y add for 1px line length
    step = dashlen * ratio  # step to the next dash
    a0 = 0
    while a0 < l:
        a1 = a0 + dashlen
        if a1 > l:
            a1 = l
        draw.line((x0 + xa * a0, y0 + ya * a0, x0 + xa * a1, y0 + ya * a1), fill=(255, 255, 255), width=5)
        a0 += step


def centroid(vertexes):
    _x_list = [vertex[0] for vertex in vertexes]
    _y_list = [vertex[1] for vertex in vertexes]
    _len = len(vertexes)
    _x = sum(_x_list) / _len
    _y = sum(_y_list) / _len
    return _x, _y


class Crossroad:
    def __init__(self, identifier, x, y, diameter, cross):
        self.id = identifier
        self.x = x
        self.y = y
        self.diameter = diameter
        self.cross = cross

        self.toReturn = None


class Road:
    def __init__(self, identifier, pavement, bike_road, road_type,
                 uni_directional, size, start_node, end_node, angle, length):
        self.id = identifier

        self.pavement = pavement
        self.bike_road = bike_road
        self.road_type = road_type
        self.uni_directional = uni_directional

        self.size = size

        self.start_node = start_node
        self.end_node = end_node

        self.angle = angle
        self.length = length


class Building:
    def __init__(self, identifier, narrows, color):
        self.id = identifier
        self.narrows = narrows
        self.color = color


class Field:
    def __init__(self, identifier, parameters, shape, color):
        self.id = identifier
        self.parameters = parameters
        self.shape = shape
        self.color = color


class Space:
    def __init__(self, name, x, y):
        self.name = name
        self.type = "Space"
        self.toReturn = None

        self.x = x
        self.y = y
        self.crossroads = []
        self.roads = []
        self.buildings = []
        self.fields = []

    class FNames(enum.Enum):
        addField = 1
        addBuilding = 2
        addCross = 3
        addRoadUn = 4
        addRoad = 5
        draw = 6
        Cross = 7
        colors = 8

    def methodCall(self, method_name, args):
        for fName in self.FNames:
            if fName.name == method_name:
                doSomething = getattr(OrtHelper, method_name)
                return doSomething(args, self)

    @staticmethod
    def colors():
        ret = ""
        for name, code in ImageColor.colormap.items():
            ret += f'{name:30} : {code}\n'
        return ret

    def add_field(self, identifier, parameters, shape, color):
        if shape not in fields_types:
            print('Invalid field shape')
            sys.exit(-1000)
        else:
            f = Field(identifier, parameters, shape, color)
            self.fields.append(f)

    def add_building(self, identifier, narrows, color):
        b = Building(identifier, narrows, color)
        self.buildings.append(b)

    def add_crossroad(self, identifier, x, y, diameter, cross):
        c = Crossroad(identifier, x, y, diameter, cross)
        self.crossroads.append(c)

    def get_crossroad(self, cr_id):
        for cr in self.crossroads:
            if cr.id == cr_id:
                return cr
        sys.exit(-1000)

    def add_road_con(self, identifier, pavement, bike_road, road_type, uni_directional, size, start_node, end_node):
        r = Road(identifier, pavement, bike_road, road_type, uni_directional, size, start_node, end_node, None, None)
        self.roads.append(r)

    def add_road_un_con(self, identifier, pavement, bike_road, road_type, uni_directional, size, start_node, angle,
                        length):
        r = Road(identifier, pavement, bike_road, road_type, uni_directional, size, start_node, None, angle, length)
        self.roads.append(r)

    def draw(self):
        img = Image.new(mode="RGB", size=(self.x, self.y), color="#939AB6")

        draw = ImageDraw.Draw(img)

        self.__drawRoads__(draw)

        self.__drawCrossRoads__(draw)

        self.__drawBuilding__(draw)

        self.__drawFields__(draw)

        img.show()

    def __drawFields__(self, draw):
        for field in self.fields:
            font = ImageFont.truetype("arial.ttf", 60)
            if field.shape == 'ellipse':
                draw.ellipse(field.parameters,
                             fill=field.color,
                             outline=(0, 0, 0))
            elif field.shape == 'rectangle':
                draw.rectangle(field.parameters,
                               fill=field.color,
                               outline=(0, 0, 0))
            elif field.shape == 'polygon':
                draw.polygon(field.parameters,
                             fill=field.color,
                             outline=(0, 0, 0))
            elif field.shape == 'chord':
                draw.chord(field.parameters[0],
                           start=field.parameters[1],
                           end=field.parameters[2],
                           fill=field.color,
                           outline=(0, 0, 0))
            else:
                draw.pieslice(field.parameters[0],
                              start=field.parameters[1],
                              end=field.parameters[2],
                              fill=field.color,
                              outline=(0, 0, 0))
            draw.text(centroid(field.parameters), str(field.id), (0, 0, 0), font=font)

    def __drawRoads__(self, draw):
        for road in self.roads:
            x_start = road.start_node.x  # + road.start_node.diameter / 2
            y_start = road.start_node.y  # + road.start_node.diameter / 2
            if road.end_node is None:
                sin = math.sin((math.radians(road.angle)))
                cos = math.cos((math.radians(road.angle)))
                length = road.length
                c = 0.5 * (road.size + 15)
                a = sin * c
                b = cos * c

                draw.line((x_start, y_start, x_start + cos * length, y_start - sin * length),
                          fill=(0, 0, 0), width=road.size)
                if not road.uni_directional:
                    linedashed(x_start, y_start, x_start + cos * length, y_start - sin * length, draw)

                if road.pavement and not road.bike_road:
                    draw.line((x_start + int(a), y_start - int(b), x_start + cos * length + int(a),
                               y_start - sin * length - int(b)),
                              fill=(100, 100, 100), width=15)

                if road.bike_road:
                    if road.pavement:
                        draw.line((x_start + int(a), y_start - int(b), x_start + cos * length + int(a),
                                   y_start - sin * length - int(b)),
                                  fill=(255, 0, 255), width=15)
                        c = 0.5 * (70 + 30 + 15)
                        a = sin * c
                        b = cos * c
                        draw.line((x_start + int(a), y_start - int(b), x_start + cos * length + int(a),
                                   y_start - sin * length - int(b)),
                                  fill=(100, 100, 100), width=15)
                    else:
                        draw.line((x_start + int(a), y_start - int(b), x_start + cos * length + int(a),
                                   y_start - sin * length - int(b)),
                                  fill=(100, 100, 100), width=15)
            else:
                x_end = road.end_node.x  # + road.end_node.diameter / 2
                y_end = road.end_node.y  # + road.end_node.diameter / 2

                c = 0.5 * (road.size + 15)
                sin_a = abs(y_end - y_start) / math.sqrt((abs(y_end - y_start) ** 2) + (abs(x_start - x_end) ** 2))
                a = sin_a * c
                b = c
                if y_end - y_start != 0:
                    b = a * (abs(x_start - x_end) / abs(y_end - y_start))

                if road.size == 1:
                    draw.line((x_start, y_start, x_end, y_end),
                              fill=(0, 0, 0), width=road.size)
                    if not road.uni_directional:
                        #linedashed(x_start, y_start, x_end, y_end, draw)
                        dx = 5 * sin_a
                        dy = 0
                        if y_end - y_start != 0:
                            dy = 5 * (abs(x_start - x_end) / abs(y_end - y_start))
                        draw.line((x_start + int(dx), y_start - int(dy), x_end + int(dx), y_end - int(dy)),
                                  fill=(255, 255, 255), width=5)
                        draw.line((x_start - int(dx), y_start + int(dy), x_end - int(dx), y_end + int(dy)),
                                  fill=(255, 255, 255), width=5)
                else:
                    draw.line((x_start, y_start, x_end, y_end),
                              fill=(0, 0, 0), width=road.size)
                    if not road.uni_directional:
                        #linedashed(x_start, y_start, x_end, y_end, draw)
                        dx = 5 * sin_a
                        dy = 5
                        if y_end - y_start != 0:
                            dy = 5 * (abs(x_start - x_end) / abs(y_end - y_start))
                        draw.line((x_start + int(dx), y_start - int(dy), x_end + int(dx), y_end - int(dy)),
                                  fill=(255, 255, 255), width=5)
                        draw.line((x_start - int(dx), y_start + int(dy), x_end - int(dx), y_end + int(dy)),
                                  fill=(255, 255, 255), width=5)

                if road.pavement and not road.bike_road:
                    draw.line((x_start + int(a), y_start - int(b), x_start + int(a), y_start - int(b)),
                              fill=(100, 100, 100), width=15)

                if road.bike_road:
                    if road.pavement:
                        draw.line((x_start + int(a), y_start - int(b), x_end + int(a), y_end - int(b)),
                                  fill=(255, 0, 255), width=15)
                        c = 0.5 * (70 + 30 + 15)
                        sin_a = abs(y_end - y_start) / math.sqrt(
                            (abs(y_end - y_start) ** 2) + (abs(x_start - x_end) ** 2))
                        a = sin_a * c
                        b = c
                        if y_end - y_start != 0:
                            b = a * (abs(x_start - x_end) / abs(y_end - y_start))
                        draw.line((x_start + int(a), y_start - int(b), x_end + int(a), y_end - int(b)),
                                  fill=(100, 100, 100), width=15)
                    else:
                        draw.line((x_start + int(a), y_start - int(b), x_end + int(a), y_end - int(b)),
                                  fill=(100, 100, 100), width=15)

    def __drawCrossRoads__(self, draw):
        # font = ImageFont.truetype("arial.ttf", int(max(self.x, self.y) / 30))
        for c in self.crossroads:
            # draw.ellipse((c.x - c.diameter, c.y - c.diameter, c.x + c.diameter, c.y + c.diameter ), fill=(0, 0, 0), outline=(0, 0, 0))
            if c.cross:
                draw.polygon(((c.x + c.diameter, c.y + c.diameter),
                              (c.x - c.diameter, c.y + c.diameter),
                              (c.x - c.diameter, c.y - c.diameter),
                              (c.x + c.diameter, c.y - c.diameter)),
                             fill=(30, 30, 30), outline=(255, 255, 255))
            else:
                draw.ellipse((c.x - c.diameter, c.y - c.diameter,
                              c.x + c.diameter, c.y + c.diameter),
                             fill=(30, 30, 30), outline=(255, 255, 255))
            # draw.text((int(c.dx0 + c.diameter / 2), int(c.dy0 + c.diameter / 2)), str(c.id), (0, 0, 0), font=font)

    def __drawBuilding__(self, draw):
        font = ImageFont.truetype("arial.ttf", 60)
        for building in self.buildings:
            draw.polygon(building.narrows, fill=building.color, outline=(0, 0, 0))
            draw.text(centroid(building.narrows), str(building.id), (0, 0, 0), font=font)


class VisHelper:
    # This helper is used to check visualisation without OrTex Language
    @staticmethod
    def helpSpaceCreate(x, y):
        return Space("Python", x, y)

    @staticmethod
    def helpAddField(space, identifier, parameters, shape, color):
        space.add_field(identifier, parameters, shape, color)

    @staticmethod
    def helpAddBuilding(space, identifier, narrows, color):
        space.add_building(identifier, narrows, color)

    # scene, X_location, Y_location, size
    @staticmethod
    def helpAddCrossroad(space, x_pos, y_pos, diameter, cross):
        num_of_cross = len(space.crossroads)
        space.add_crossroad(num_of_cross, x_pos, y_pos, diameter, cross)

    @staticmethod
    def helpAddRoadCon(space, identifier, pavement, bike_road, road_type, uni_directional, size, start_node, end_node):
        # from, destination
        space.add_road_con(identifier, pavement, bike_road, road_type, uni_directional, size, start_node, end_node)

    @staticmethod
    def helpAddRoadUnCon(space, identifier, pavement, bike_road, road_type, uni_directional, size, start_node, angle,
                         length):
        # from, angle, length
        space.add_road_un_con(identifier, pavement, bike_road, road_type, uni_directional, size, start_node, angle,
                              length)

    @staticmethod
    def helpSpaceDraw(space):
        space.draw()


class OrtHelper:
    @staticmethod
    def addField(args, space):
        parameters = []
        for i in range(0, len(args[3].list) - 1, 2):
            parameters.append((int(args[3].list[i]), int(args[3].list[i + 1])))

        parameters = tuple(parameters)

        space.add_field(args[0], parameters, args[1], args[2])
        return space

    @staticmethod
    def addBuilding(args, space):
        narrows = []
        for i in range(0, len(args[2].list)-1, 2):
            narrows.append((int(args[2].list[i]), int(args[2].list[i+1])))

        narrows = tuple(narrows)
        space.add_building(args[0], narrows, args[1])
        return space

    @staticmethod
    def addCross(args, space):
        if len(args) == 4:
            num_of_cross = len(space.crossroads)
            # num_of_cross, x_pos, y_pos, diameter, cross
            space.add_crossroad(num_of_cross, args[0], args[1], args[2], args[3])
        return space

    @staticmethod
    def addRoadUn(args, space):
        if len(args) == 5:
            num_of_roads = len(space.roads)

            string = args[0]
            if len(string) == 4:
                pavement = False
                bike_road = False
                road_type = 0
                uni_directional = False
                values = [int(i) for i in string]
                if values[0] == 1:
                    pavement = True
                if values[1] == 1:
                    bike_road = True
                if values[3] == 1:
                    uni_directional = True

                road_type = values[2]

                space.add_road_un_con(num_of_roads, pavement, bike_road, road_type, uni_directional, args[1], args[2],
                                      args[3], args[4])
        return space

    @staticmethod
    def addRoad(args, space):
        if len(args) == 4:
            num_of_roads = len(space.roads)

            string = args[0]
            if len(string) == 4:
                pavement = False
                bike_road = False
                road_type = 0
                uni_directional = False
                values = [int(i) for i in string]
                if values[0] == 1:
                    pavement = True
                if values[1] == 1:
                    bike_road = True
                if values[3] == 1:
                    uni_directional = True

                road_type = values[2]

                space.add_road_con(num_of_roads, pavement, bike_road, road_type, uni_directional, args[1], args[2], args[3])
        return space

    @staticmethod
    def draw(args, space):
        if len(args) == 0:
            space.draw()
        return space

    @staticmethod
    def Cross(args, space):
        if len(args) == 1:
            space.toReturn = space.crossroads[args[0]]
        return space

    @staticmethod
    def colors(args, space):
        if len(args) == 0:
            space.toReturn = space.colors()
        return space
