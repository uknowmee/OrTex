# Project Documentation

As we planned at the beginning we wanted to create object-oriented
programming language to generate city maps.


Our base objective was generating it in 2D, and it ended up successfully.

## Using OrTex
To use OrTex you can just download repo and run 
```
ortex.exe <path-to-OrTex-script>
```
this will execute example program that
creates basic visualization.

Some examples of OrTex scripts are placed in OrTex/Projects/.


## According to our plan we delivered functionalities listed below:
### 1. Primitive types and operations such as:
   - int
   - string
   - double
   - bool
   - null 

<br>

   - \+
   - \/
   - \-
   - %

You don't need to declare variable type, for instance:
```
a = 5;
```

Our language supports dynamic typing, it means that:
```
a = "something"
a = 4
```
won't cause any error.

Course all comparisons between them are also provided.
### 2. Functions:
Everything you want to execute has to be placed inside MAIN() function.
You can declare functions in such way:
```
func newList(){
    nList = new List();
    nList.pushB(1,2,3);
}->nList;    
```
Last line "}-->nList;" tells that function returns nList variable.

You can also pass variable reference to function using: "@":
```
makeLists(@list, @list2d);
```
You can use objects returned from function "inplace". (newList function was created above)
```
write(newList().pushB(3,4).popF)
```
### 3. Classes:
Because it's object-oriented programming language you can use builtin and declare your own classes.

Example:
```    
class Point{
    constr (x, y){
        write("in constr");
        this.pointName;
        this.xCord = x;
        this.yCord = y;
        x = 4;
        x = x + 2;
    }

    func writeOut(){
        write("x coord: ", this.xCord, ", y coord: ", this.yCord);
    }
    func swapXAndY(){
        temp = this.yCord;
        this.yCord = this.xCord;
        this.xCord = temp;
    }
    func isXBigger(x){
        ret = false;
        if (this.xCord > x){
            ret = true;
        }
    }->ret;
    func isYBigger(y){
        ret = false;
        if (this.yCord > y){
            ret = true;
        }
    }->ret;
}
```
Constructor is "constr".

Class variables are just like in Python prefixed with "this." and you declare them in constructor.

Class methods can be used everywhere, if u want to use method inside method specify method call with "this" keyword.

You can use both methods and variables inplace just like normal function calls.

### 4. Scopes:
Scopes are defined in two ways:
- by declaring classes, functions, for, if etc. by using "{ }"
- by explicit declaration using "[ ]"

Variables can be accessed only in their scopes and scopes that are placed in current scope.

If you declare variable with the same name in external scope and internal scope inside this scope, variable will be replaced in internal scope,
but after executing this scope it will get back to previous value in external scope.
```
func scopes(){
    [
        x = 2; <- this and next variables are defined in function scope so they dont interfere with variables from MAIN()
        [
            y = x;
            write(y);
        ]
        write(x);
        # write(y); <- this will produce error, variable y is not defined in current scope
    ]
    # write(x); <- this will produce error, variable x is not defined in current scope

    x = 2;
    write(x);
}

func MAIN(){
    x = 3;
    scopes();
}
```

### 5. Conditional statements:
- if statement
```
func writeSomething(shouldKnow){

    maybe = false;
    if(!shouldKnow){
    	write("i dont know where im going");
    } else if (maybe){
        write("maybe i know where im going");
    } else{
        write("i know where im going");
    }

}

func recFun1(num){
    if (num == 1 or num == 0){
        num = 1;
    } else {
        num = num * recFun(num - 1);
    }
}
```

You can use standard If, Else If, Else pattern

We provide "and" and "or" keywords, which you can put with whatever configuration needed inside If statement.

Inside "If statement" you can use all functions which returns something. Same goes for thing such as class methods or variables.

### 6. Loops:
- for statement: 

What is unusual we don't put expression in 3rd place of "for loop".

This is a spot for "operation" and its step

```
x = 1;
for (i = 0, i<20, +x){
    i = i + 1;
    x = x + 1;
    write("i: " + i + ", " + "x: " + x);
}
```
- while statement 

```
i = 0;
stop = 5;
while(i < stop){
    i = i + 1;
    x = i;
    write(x);
}
```

### 7. Comments:
You can comment whichever line you want by specifying "#" at it's beginning.

### 8. Builtin classes:
- List
- Dict
- Space

#### Data containers (supporting chain function calls):
- List
```
    - myL = new List();
        - Creates new List, can be used without variable definition
        - Returns new List
    - myL.pushF(arg1, arg2);
        - Pushes an argument in from of the list, you can define more than one and separate them with comma.
        - Returns self
    - myL.pushB(arg1, arg2); 
        - Pushes an argument to the back of the list, you can define more than one and separate them with comma.
        - Returns self
        - Deepcopy!
    - myL.popF(); 
        - Pops first item from list
        - Returns popped element
    - myL.popB(); 
        - Pops last item from list
        - Returns popped element
    - myL.clear(); 
        - Removes all elements from list
        - Returns self
    - myL.get(0); or myL.get(0,1); 
        - Returns specified element from a list, if you use 2 parameters it works as for 2dArray
    - myL.set(0, arg1); or myL.set(0, 0, arg1); 
        - Set value (its not deepcopy) of specified list element, if you use 3 parameters it works as for 2dArray
        - Returns self
    - myL.size(); 
        - Returns size of a list
```
- Dictionary
```
    - myD = new List();
        - Creates new List, can be used without variable definition
        - Returns new List
    - myD.clear(); 
        - Removes all elements from dict
        - Returns self
    - myD.get(key); 
        - Returns specified element from a dict
    - myD.set(key, value);
        - Set value of specified element which already exists in dict
        - Returns self
    - MyD.add(key, value);
        - Adds new item to a dict
        - Returns self
    - myD.delete(arg1, arg2);
        - Deletes all argument based on specified keys
        - Returns self
    - myD.size(); 
        - Returns size of a dict
```
#### VisualisationClasses (supporting chain function calls):
- Space
```
    - sp = new Space(xSize, ySize);
    - sp.addField(fieldName, fieldType, color, coords);
        - fieldName string
        - fieldType :'ellipse', 'rectangle', 'polygon', 'chord', 'pieslice'
        - color rgb or string
        - coords list of points, should be consequently: mkList().pushB(x1, y1, x2, y2, x3, y3) ect
    - sp.addBuilding(fieldName, color, coords);
        - fieldName string
        - color rgb or string
        - coords list of points, should be consequently: mkList().pushB(x1, y1, x2, y2, x3, y3) ect
    - sp.addCross(xCoord, yCoord, size, ifRoundabout);
        - ifRoundabout boolean describing if cross should be roundabout
    - sp.addRoadUn(roadType, roadSize, startCrossroad, angle, length);
        - roadType is a string in format "ttnt" where t is 0 or 1 and n is number between 1 and 9
            - string: pavement, bike road, road type (num of crossing 1->9), uni directional
        - roadSize just normal int
        - startCrossroad you can get it by using sp.Cross(crossId); method
        - angle classic angle 0 -> 360, describes the direction of the road
        - length just normal int
    - sp.addRoad(roadType, roadSize, startCrossroad, endCrossroad);
        - roadType is a string in format "ttnt" where t is 0 or 1 and n is number between 1 and 9
            - string: pavement, bike road, road type (num of crossing 1->9), uni directional
        - roadSize just normal int
        - startCrossroad you can get it by using sp.Cross(crossId); method
        - endCrossroad you can get it by using sp.Cross(crossId); method
    - sp.draw();
        - Draws current space as .jpg
    - sp.Cross(crossId);
        - Returns Crossroad object based on given crossId
    - sp.colors();
        - Returns string with all existing colors you can use
```
### 8. Builtin functions:
- write(arg1, arg2, arg3);
```
"Write" function recive as much arguments as you want but it dont need to recive any.
As argument you can pass a constant or variable.
If needed "write " function can also recive function call as parameter or another type of expression sucha as compare or arythemtical one.
```



    
