let planet,player,system;
let R,C;
const UNSELECTED_COLOR = "rgba(0, 0, 0, 0.05)";
const SELECTED_COLOR = "rgba(255, 153, 0, 0.7)";
const buildings = ["habitation","crystalMine","uranimMine","stealMine",
    "commandCenter", "stealDepot","defenseTurret","crystalDepot","garage","solarPanel", "nuclearPlant"];

function display(){
    setEventListeners();
    getPlayerById(document.getElementById("id_player").innerHTML);
    if(player!=null){
        if(player.possessions[0].id != null){
            getPlanetById(player.possessions[0].id);
        }
    }
    displayBackground();
    displayMap();
    displayTopBar();
    displayPossessions();
}

function displayMap(){
    if(planet!=null){
    R=planet.size.x;
    C=planet.size.y;
    let row,column,r,c,img,building;
    let map = document.getElementById("map");
    map.innerHTML = "";
    for(r=0;r<R;r++){
        row = document.createElement("div");
        row.className="row";
        for(c=0;c<C;c++) {
            column=document.createElement("div");
            column.id=r+"-"+c;
            column.style.background= "rgba(0,0,0,0.05)";
            column.className="column1x1";
            column.style.height = "70px";
            column.style.width = "44px";
            building=getBuilding(r,c);
            if(building!=null){
                img=document.createElement("img");
                switch (building){
                    case "Habitation" : img.src="../assets/buildings3D/"+buildings[0]+".png"; break;
                    case "Crystal Mine" : img.src="../assets/buildings3D/"+buildings[1]+".png"; break;
                    case "Uranium Mine" : img.src="../assets/buildings3D/"+buildings[2]+".png"; break;
                    case "Steel Mine" : img.src="../assets/buildings3D/"+buildings[3]+".png"; break;
                    case "Research Center" : img.src="../assets/buildings3D/"+buildings[4]+".png"; break;
                    case "Steel Warehouse" : img.src="../assets/buildings3D/"+buildings[5]+".png"; break;
                    case "Defensive Turret" : img.src="../assets/buildings3D/"+buildings[6]+".png"; break;
                    case "Crystal Warehouse" : img.src="../assets/buildings3D/"+buildings[7]+".png"; break;
                    case "Garage" : img.src="../assets/buildings3D/"+buildings[8]+".png"; break;
                    case "Solar Panel" : img.src="../assets/buildings3D/"+buildings[9]+".png"; break;
                    case "Nuclear Plant" : img.src="../assets/buildings3D/"+buildings[10]+".png"; break;
                    case "Uranium Warehouse" : img.src="../assets/buildings3D/"+buildings[10]+".png"; break;
                }
                if(img.src!==""){
                    img.id="figure"+r+"-"+c;
                    img.className="column1x1";
                    img.style.height = "70px";
                    img.style.width = "44px";
                    img.draggable=false;
                    column.append(img);
                }
            }
            setEventColumnListeners(column);
            row.append(column);
        }
        map.append(row);
    }
    }
}

function displayBackground(){
    let html = document.getElementById("html");
    if(html != null){
        if(planet != null){
            if(planet.type==="moon")
                html.style.backgroundImage="url('../assets/backgrounds/moon.jpeg')";
            else
                html.style.backgroundImage="url('../assets/backgrounds/planet.jpeg')";
        }else{
            html.style.backgroundImage="url('../assets/backgrounds/planet.jpeg')";
        }
    }
}

function displayTopBar(){
    if(planet!=null){
        /* planet name */
        document.getElementById("planet-name").innerHTML=planet.name+" "+planet.id;
        /* fleet-value */
        document.getElementById("fleet-value").innerHTML=player.fleets.length;
        document.getElementById("fleet-progress").style.width=parseInt(player.fleets.length*10)+"%";
        /* construction-value */

        /* steel */
        document.getElementById("steel-value").innerHTML=planet.resources.Steel;
        document.getElementById("steel-progress").style.width=parseInt(planet.resources.Steel*100/planet.storage.Steel)+"%";
        /* crystal */
        document.getElementById("crystal-value").innerHTML=planet.resources.Crystal;
        document.getElementById("crystal-progress").style.width=parseInt(planet.resources.Crystal*100/planet.storage.Crystal)+"%";
        /* uranium */
        document.getElementById("uranium-value").innerHTML=planet.resources.Uranium;
        document.getElementById("uranium-progress").style.width=parseInt(planet.resources.Uranium*100/planet.storage.Uranium)+"%";
        /* energy */
        document.getElementById("energy-value").innerHTML=planet.resources.Energy;
        document.getElementById("energy-progress").style.width=parseInt(Math.sqrt(planet.resources.Energy))+"%";
        /* population */
        document.getElementById("population-value").innerHTML=planet.resources.Population.used;
        document.getElementById("population-progress").style.width=parseInt(planet.resources.Population.used*100/planet.resources.Population.total)+"%";
        /* gold */
        document.getElementById("gold-value").innerHTML=player.gold;
        document.getElementById("gold-progress").style.width=parseInt(player.gold*100/(1000000))+"%";
        /* user name */
        document.getElementById("user").innerHTML=player.name;
    }
}

function displayPossessions(){
    if(player.possessions != null){
        let button;
        let possessionArea = document.getElementById("possessionArea");
        for(let i=0;i<player.possessions.length;i++){
            button = document.createElement("button");
            button.innerHTML=player.possessions[i].name;
            button.className = "possessionButton";
            button.onclick = function (){
                getPlanetById(player.possessions[i].id);
            }
            possessionArea.append(button);
        }
    }
}

function getSystem(){
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/system",
        async : false,
        dataType: 'json',
        error: function (data) {
            console.log(data.status + ':' + data.statusText,data.responseText);
        },
        success: function(data) {
            system=data;
            console.log(system);
        }
    });
}

function getPlanetById(id){
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/planet/"+id,
        async : false,
        dataType: 'json',
        error: function (data) {
            console.log(data.status + ':' + data.statusText,data.responseText);
        },
        success: function(data) {
            planet=data;
            console.log(planet);
        }
    });
}

function getPlayerById(id){
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/player/"+id,
        async : false,
        dataType: 'json',
        error: function (data) {
            console.log(data.status + ':' + data.statusText,data.responseText);
        },
        success: function(data) {
            player=data;
            console.log(player);
        }
    });
}

function getBuilding(x,y){
    if(planet!=null){
        let baseTileMap = planet.baseTileMap;
        for(let i= 0; i < baseTileMap.length ; i++){
            if(baseTileMap[i].x===x && baseTileMap[i].y===y) return baseTileMap[i].building;
        }
    }
    return null;
}

function getSelectedColumn(){
    let r,c,column;
    for(r=0;r<R;r++){
        for(c=0;c<C;c++) {
            column = document.getElementById(r+"-"+c);
            if(column != null){
                if (column.style.background===SELECTED_COLOR){
                    return r+"-"+c;
                }
            }
        }
    }
    return null;
}

function getEmptyColumn(){
    let r,c,column;
    for(r=0;r<R;r++){
        for(c=0;c<C;c++) {
            column = document.getElementById(r+"-"+c);
            if(column != null){
                if(column.innerHTML==="") return column;
            }
        }
    }
    return null;
}

function unselectAll(){
    let r,c,column;
    for(r=0;r<R;r++){
        for(c=0;c<C;c++) {
            column = document.getElementById(r+"-"+c);
            if(column!=null){
                column.style.background = UNSELECTED_COLOR;
            }
        }
    }
}

function changeSelection(column){
    if(column.style.background === UNSELECTED_COLOR && document.getElementById("figure"+column.id)!=null){
        unselectAll();
        column.style.background = SELECTED_COLOR;
    }else{
        column.style.background = UNSELECTED_COLOR;
    }
}
function moveSelection(column){
    let selectedColumn = getSelectedColumn();
    let figure = document.getElementById("figure"+column.id);
    if(selectedColumn!=null && figure==null){
        /* one column is selected && destination is empty */
        let selectedImage = document.getElementById("figure"+selectedColumn);
        if (selectedImage != null){
            let img = document.createElement("img");
            let selected = document.getElementById(selectedColumn);
            img.id = "figure"+column.id;
            img.src = document.getElementById("figure"+selectedColumn).src;
            img.className = selected.className;
            img.style.width = selected.style.width;
            img.style.height = selected.style.height;
            img.draggable = selected.draggable;
            column.append(img);
            document.getElementById("figure"+selectedColumn).remove();
            changeSelection(column);
        }
    }
}

function setEventColumnListeners(column){

    column.addEventListener('mousedown', function() {
        moveSelection(column);
        changeSelection(column);
    }, true);

}

function zoom(zoomin){
    let r,c,height,width,img,h,w;
    let column = document.getElementById("0-0");
    if (column!=null){
        h = parseInt(column.style.height.substring(0,column.style.height.length-2));
        w = parseInt(column.style.width.substring(0,column.style.width.length-2));
        if(zoomin){
            if(h>120) return;
            height = h+8+"px";
            width = w+5+"px";
        }else{
            if(h<40) return;
            height = h-8+"px";
            width = w-5+"px";
        }
    }

    for(r=0;r<R;r++){
        for(c=0;c<C;c++) {
            column = document.getElementById(r+"-"+c);
            if(column!=null){
                column.style.width  = width;
                column.style.height  = height;
                img = document.getElementById("figure"+column.id);
                if(img!=null){
                    img.style.width  = width;
                    img.style.height  = height;
                }
            }
        }
    }
    document.getElementById("map").scrollIntoView({block: "center"});
}

function setEventListeners(){
    window.onload = function (){
        /* prev next */
        let prev = document.getElementById("prev");
        let next = document.getElementById("next");
        let upButton = document.getElementById("building-menu-up-down");
        let up = document.getElementById("building-construction");
        for (let i = 1; i <= buildings.length; i++) {
            document.getElementById("building-" + i).style.left = 200*(i-1) + "px";
        }
        if(prev!=null){
            prev.onclick = function () {
                buildingListPrev();
            }
        }
        if(next!=null){
            next.onclick = function (){
                buildingListNext();
            }
        }
        if (upButton!=null) {
            upButton.onclick = function (){
                constructionMenuUpDown();
            }
        }
        if(up!=null) closeConstructionMenu()
        scrollToBottomMsg ();
        /* buy */
        let buy;
        for (let b = 1; b <= buildings.length; b++) {
            temp = document.getElementById("building-" + b).style.left;
            buy = document.getElementById("buy-"+buildings[b-1]);
            if(buy!=null){
                buy.onclick = function (){
                    let emptyColumn = getEmptyColumn();
                    if(emptyColumn === null){
                        alert("Espace plein !")
                    }else{
                        /* price */
                        let price = 10;
                        let gold = document.getElementById("gold-value");
                        if((parseInt(gold.innerHTML)-price)>=0){
                            img=document.createElement("img");
                            img.src="../assets/buildings3D/"+buildings[b-1]+".png";
                            img.id="figure"+emptyColumn.id;
                            img.className="column1x1";
                            img.style.height = "70px";
                            img.style.width = "44px";
                            img.draggable=false;
                            emptyColumn.append(img);
                            gold.innerHTML = (parseInt(gold.innerHTML)-price)+"";
                        }else{
                            alert("Or Insuffisant !")
                        }
                    }
                }
            }
        }
    }
}

function buildingListPrev() {
    let temp;
    if((document.getElementById("building-1").style.left).localeCompare("0px") !== 0) {
        for (let b = 1; b <= buildings.length; b++) {
            temp = document.getElementById("building-" + b).style.left
            document.getElementById("building-" + b).style.left = parseInt(temp.slice(0, temp.length - 2)) + 200 + "px";
        }
    }
}

function buildingListNext() {
    let temp;
    if((document.getElementById("building-" + buildings.length).style.left).localeCompare("600px") !== 0) {
        for (let b = 1; b <= buildings.length; b++) {
            temp = document.getElementById("building-" + b).style.left
            document.getElementById("building-" + b).style.left = parseInt(temp.slice(0, temp.length - 2)) - 200 + "px";
        }
    }
}

function constructionMenuUpDown() {
    if (!constructionMenuUp) openConstructionMenu();
    else closeConstructionMenu();
    //aa
}

function openConstructionMenu() {
    constructionMenuUp = true;
    document.getElementById("building-store").style.transform = "translateY(-180px)";
    document.getElementById("title-bar-icon").innerHTML = '<p>&#709;</p>';

}

function closeConstructionMenu() {
    constructionMenuUp = false;
    document.getElementById("building-store").style.transform = "translateY(0)";
    document.getElementById("title-bar-icon").innerHTML = "<p>&#94;</p>";
}

function scrollToBottomMsg () {
    let chatArea = document.getElementById("chatArea");
    chatArea.scrollTop = chatArea.scrollHeight;
}

function openLeftMenu(id){
    document.getElementById(id).style.display="block";
}

function closeLeftMenu(id){
    document.getElementById(id).style.display="none";
}

function block_spaceship(id){
    document.getElementById(id).style.opacity="0.3";
}

function closeOpenPossessionMenu() {
    if ((document.getElementsByClassName("wrap-menuD")[0].style.right).localeCompare("0px") !== 0) {
        document.getElementsByClassName("wrap-menuD")[0].style.right = "0";
        document.getElementById("closeOpenMenuD").innerText = ">";
    } else {
        document.getElementsByClassName("wrap-menuD")[0].style.right = "-250px";
        document.getElementById("closeOpenMenuD").innerText = "<";
    }
}

(function (root, factory) {
    if (typeof define === 'function' && define.amd) {
        define(['exports'], factory);
    } else if (typeof exports !== 'undefined') {
        factory(exports);
    } else {
        factory((root.dragscroll = {}));
    }
}(this, function (exports) {
    var _window = window;
    var _document = document;
    var mousemove = 'mousemove';
    var mouseup = 'mouseup';
    var mousedown = 'mousedown';
    var EventListener = 'EventListener';
    var addEventListener = 'add'+EventListener;
    var removeEventListener = 'remove'+EventListener;
    var newScrollX, newScrollY;

    var dragged = [];
    var reset = function(i, el) {
        for (i = 0; i < dragged.length;) {
            el = dragged[i++];
            el = el.container || el;
            el[removeEventListener](mousedown, el.md, 0);
            _window[removeEventListener](mouseup, el.mu, 0);
            _window[removeEventListener](mousemove, el.mm, 0);
        }

        // cloning into array since HTMLCollection is updated dynamically
        dragged = [].slice.call(_document.getElementsByClassName('dragscroll'));
        for (i = 0; i < dragged.length;) {
            (function(el, lastClientX, lastClientY, pushed, scroller, cont){
                (cont = el.container || el)[addEventListener](
                    mousedown,
                    cont.md = function(e) {
                        if (!el.hasAttribute('nochilddrag') ||
                            _document.elementFromPoint(
                                e.pageX, e.pageY
                            ) === cont
                        ) {
                            pushed = 1;
                            lastClientX = e.clientX;
                            lastClientY = e.clientY;

                            e.preventDefault();
                        }
                    }, 0
                );

                _window[addEventListener](
                    mouseup, cont.mu = function() {pushed = 0;}, 0
                );

                _window[addEventListener](
                    mousemove,
                    cont.mm = function(e) {
                        if (pushed) {
                            (scroller = el.scroller||el).scrollLeft -=
                                newScrollX = (- lastClientX + (lastClientX=e.clientX));
                            scroller.scrollTop -=
                                newScrollY = (- lastClientY + (lastClientY=e.clientY));
                            if (el === _document.body) {
                                (scroller = _document.documentElement).scrollLeft -= newScrollX;
                                scroller.scrollTop -= newScrollY;
                            }
                        }
                    }, 0
                );
            })(dragged[i++]);
        }
    }


    if (_document.readyState === 'complete') {
        reset();
    } else {
        _window[addEventListener]('load', reset, 0);
    }

    exports.reset = reset;
}));
