# KOMP22-OrTex -- How to Use

1. Simply download repository and use ortex.exe app as given:
```
    ortex.exe <path-to-OrTex-script>
``` 
2. In Documentation section you can find more informations about our language.

# KOMP22-OrTex -- How to Contribute

## Antlr:

1. Make folder containing [Files](https://drive.google.com/drive/folders/15JZDp0L1ISP9jjXBvJZtFfyfe1MF612L?usp=sharing).
    <br />
    <br />    
2. Create new User environment [variable](https://prnt.sc/aSE0s4fdDsvy:)
    - CLASSPATH
    - **{YOUR FOLDER PATH}**\antlr-4.9.3-complete.jar
    <br />
3. Add two new environment variables to your user [Path variable ](https://prnt.sc/9OrH8QeL7yIM:)
    - %CLASSPATH%
    - **{YOUR FOLDER PATH}**
    <br />
4. Run cmd and check your antlr:
    - where antlr
        - **{YOUR FOLDER PATH}**\antlr.bat
    - antlr
        - ANTLR Parser Generator  Version 4.9.3
        - -o ___              specify output directory where all output is generated
        - -lib ___            specify location of grammars, tokens files
        - -atn                generate rule augmented transition network diagrams
        - -encoding ___       specify grammar file encoding; e.g., euc-jp
        - -message-format ___ specify output style for messages in antlr, gnu, vs2005
        - -long-messages      show exception details when available for errors and warnings
        - -listener           generate parse tree listener (default)
        - -no-listener        don't generate parse tree listener
        - -visitor            generate parse tree visitor
        - -no-visitor         don't generate parse tree visitor (default)
        - -package ___        specify a package/namespace for the generated code
        - -depend             generate file dependencies
        - -D<option>=value    set/override a grammar-level option
        - -Werror             treat warnings as errors
        - -XdbgST             launch StringTemplate visualizer on generated code
        - -XdbgSTWait         wait for STViz to close before continuing
        - -Xforce-atn         use the ATN simulator for all predictions
        - -Xlog               dump lots of logging info to antlr-timestamp.log
        - -Xexact-output-dir  all output goes into -o dir regardless of paths/package

## Update visitor:

1. In ur Pycharm terminal write:
    - **{Repository Path}**\komp22-ortex> antlr -Dlanguage=Python3 .\OrTex\OrTex.g4 -visitor -o .\OrTex

## Install antlr to ur Pycharm:
1. Enter your interpretter settings and click "+" to install new [Package](https://prnt.sc/WORlpd7l05nw)
    <br />
    <br />
2. Install [antlr4-python3-runtime](https://prnt.sc/RGZVNOJiHcjk) (my version 4.9.3)

## Setup Pycharm to help you with .ot file:
1. Edit your File Types [add OrTex](https://prnt.sc/qTLxHQfYlYBo):
    - Name: OrTex
    - Description: OrTex
    - Line comment # (only at line start)
    - Support paired braces
    - Support paired parens
    - Support paired brackets
    - Support string escapes
    - keywords:
        | 1 | 2 | 3 | 4 |
        | ------ | ------ | ------ | ------ |
        | ; | != | Space() | @ |
        | and | % | write |  |
        | else | * | List() |  |
        | false | + | Dict() |  |
        | for | - |  |  |
        | func | / |  |  |
        | if | < |  |  |
        | null | <= |  |  |
        | or | = |  |  |
        | true | == |  |  |
        | while | > |  |  |
        | xor | >= |  |  |
        | new | [ |  |  |
        | class | ] |  |  |
        |  | { |  |  |
        |  | } |  |  |
2. Make sure that ur file name pattern for ortex is *.ot!!
    <br />
    <br />
3. Instead of adding new project edit [existing file templates](https://prnt.sc/um0tu84mSlmo)
    <br />
    <br />
4. Add [OrTex](https://prnt.sc/RX9wox4_OIkG):
    - Name: OrTex
    - Extension: ot
    - style:
        ```
        # ${FILE_NAME}
        # MADE BY: ${USER}
        # ${DATE} ${TIME}


        func helloWorld(programmer){
            write("Hello ", programmer, "! Its nice to see you!");
        }

        func MAIN(){
            name = "OrTexDev ${USER}";
            helloWorld(name);
        }
        ```

## Write your CODE!!! Examples are below

#### [TemplateGen.ot](https://prnt.sc/cX5z7mqLNqE1)
```
    # TemplateGen.ot
    # MADE BY: Michał
    # 14.04.2022 13:23


    func helloWorld(programmer){
        write("Hello ", programmer, "! Its nice to see you!");
    }

    func MAIN(){
        name = "OrTexDev Michał";
        helloWorld(name);
    }
```



<details><summary>code snippets</summary>

###. Prog1.ot
```
    # Prog1.ot

    func myFunction(str, int, limit) {
        i = 7;

        write("hey, its my function! (", str, ")");
        secondFunction("index: ", int, limit);
    }

    func secondFunction(str, int, limit) {
        write(str, int, " limit: ", limit);
    }

    func MAIN(){
        i = 1;
        write("i: ", i);

        i = 1 * 2;
        write("i: ", i);

        e = i + 1;
        write("e: ", e);

        while (i < 6) {
            myFunction("Its working...", i, 6);
            i = i + 1;
        }
    }
```

###. Prog2.ot
```
    # Prog2.ot

    func increment(index, stop){
        printInfo(index, stop);

        index = index + 1;

        nextStopInfo(index, stop);
    }

    func nextStopInfo(nextIndex, stop){

        nextStop = stop - nextIndex;

        write("next index: ", nextIndex, " next stop: ", nextStop);
        write("#####################");
    }

    func printInfo(index, stop){
        write("current index is: ", index, " current stop value: ", stop);
    }

    func calcStop(stop, reduce){
        stop = stop - reduce;
    }

    func MAIN(){
        i = 1;
        stop = 50;

        while(i < stop){
            increment(@i, stop);
            calcStop(@stop, i);
        }
    }
```

###. Prog3.ot
```
    # Prog3.ot

    func MAIN(){

        i = 0;
        j = 0;

        str = "hej";

        while(i < 10){
            str = "";
            while(j < 10){
                str = str + "(" + i + "," + j + ")";
                j = j + 1;
            }
            write(str);
            i = i + 1;
            j = 0;
        }
    }
```

###. ClassDemo.ot
```
    # ClassDemo.ot
    # MADE BY: Michał
    # 08.06.2022 21:41


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

    class PointMaker{
        constr (){}

        func makePoint(x, y){
            ret = new Point(x, y);
        }->ret;
    }

    func myF(){
        ret = new Point(3,4);
    }->ret;

    func MAIN(){
        list = new List();
        mp = new Point(2, 3);
        list.pushB(mp);
        list.get(0).writeOut();
        list.get(0).swapXAndY();
        list.get(0).writeOut();

        write("\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n");
        myF().writeOut();

        write("\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n");
        X = mp.xCord;
        Y = mp.yCord;
        mp.pointName = "firstPoint";
        write(mp.pointName + ": " + X + ", " + Y);
        if (mp.isYBigger(5)){
            write("y is bigger");
        } else {
            write("y is smaller");
        }

        write("\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n");
        write(myF().yCord);

        write("\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n");
        pMaker = new PointMaker();
        write(pMaker.makePoint(1,6).yCord);
    }
```

###. VisDemo.ot
```
    
    # VisDemo.ot
    # MADE BY: Michał
    # 11.05.2022 12:52


    func mkList(){
        lst = new List();
    }->lst;

    func mkSpace(){
    #   x size, y size
        sp = new Space(3000, 3000);
    }->sp;

    func mkCrosses(sp){
        for (y = 500, y<=2500, +1000){
            for (x = 500, x<=2500, +1000){
                if (x != 500 or y != 1500){
    #               x, y, size, (says if its roundabout or not)
                    sp.addCross(x, y, 70, true);
                }
            }
        }

        sp.addCross(500, 1500, 80, false);
    }

    func mkConnections(sp){
        road_size = 70;
    #   string: pavement, bike road, road type (num of crossing 1->9), uni directional
    #   string, size, from, angle, len
        sp.addRoadUn("0010", road_size, sp.Cross(8), 180, 500);
        sp.addRoadUn("0010", road_size, sp.Cross(1), 90, 500);


        sp.addRoad("1120", road_size, sp.Cross(0), sp.Cross(8));
        sp.addRoad("1111", road_size, sp.Cross(0), sp.Cross(1));
        sp.addRoad("1110", road_size, sp.Cross(1), sp.Cross(2));
        sp.addRoad("0010", road_size, sp.Cross(2), sp.Cross(4));
        sp.addRoad("0011", road_size, sp.Cross(2), sp.Cross(3));
        sp.addRoad("0010", road_size, sp.Cross(8), sp.Cross(3));
        sp.addRoad("0010", road_size, sp.Cross(8), sp.Cross(6));
        sp.addRoad("0010", road_size, sp.Cross(5), sp.Cross(6));
        sp.addRoad("0010", road_size, sp.Cross(6), sp.Cross(7));
    }

    func mkBuildings(sp){

        sp.addBuilding("Bank", "thistle",
                                mkList().pushB(1450, 1450, 1450, 1100, 1200, 1100, 1200, 1450));

        sp.addField("Football", "polygon", "green",
                                mkList().pushB(1200, 1450, 700, 1450, 700, 700, 1200, 700));

        sp.addField("Rossman", "polygon", "red",
                                mkList().pushB(1550, 1350, 1550, 1050, 2000, 600, 2000, 900));
    }

    func MAIN(){
        sp = mkSpace();

        mkCrosses(@sp);
        mkConnections(@sp);
        mkBuildings(@sp);

        sp.draw();
    }
```
</details>
