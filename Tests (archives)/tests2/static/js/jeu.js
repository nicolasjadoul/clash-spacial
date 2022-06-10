let planet,player;
let R,C;
const UNSELECTED_COLOR = "rgba(0, 0, 0, 0.05)";
const SELECTED_COLOR = "rgba(255, 153, 0, 0.7)";
const buildings = ["habitation","crystalMine","uranimMine","stealMine",
    "commandCenter", "stealDepot","defenseTurret","crystalDepot","garage",
    "spaceShipYard","solarPanel", "nuclearPlant"];
function display(){
    setEventListeners();

    getPlanet();
    getPlayer();

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
                    case buildings[0] : img.src="static/assets/buildings3D/"+buildings[0]+".png"; break;
                    case buildings[1] : img.src="static/assets/buildings3D/"+buildings[1]+".png"; break;
                    case buildings[2] : img.src="static/assets/buildings3D/"+buildings[2]+".png"; break;
                    case buildings[3] : img.src="static/assets/buildings3D/"+buildings[3]+".png"; break;
                    case buildings[4] : img.src="static/assets/buildings3D/"+buildings[4]+".png"; break;
                    case buildings[5] : img.src="static/assets/buildings3D/"+buildings[5]+".png"; break;
                    case buildings[6] : img.src="static/assets/buildings3D/"+buildings[6]+".png"; break;
                    case buildings[7] : img.src="static/assets/buildings3D/"+buildings[7]+".png"; break;
                    case buildings[8] : img.src="static/assets/buildings3D/"+buildings[8]+".png"; break;
                    case buildings[9] : img.src="static/assets/buildings3D/"+buildings[9]+".png"; break;
                    case buildings[10] : img.src="static/assets/buildings3D/"+buildings[10]+".png"; break;
                    case buildings[11] : img.src="static/assets/buildings3D/"+buildings[11]+".png"; break;
                }
                img.id="figure"+r+"-"+c;
                img.className="column1x1";
                img.style.height = "70px";
                img.style.width = "44px";
                img.draggable=false;
                column.append(img);
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
                html.style.backgroundImage="url('static/assets/backgrounds/moon.jpeg')";
            else
                html.style.backgroundImage="url('static/assets/backgrounds/planet.jpeg')";
        }else{
            html.style.backgroundImage="url('static/assets/backgrounds/planet.jpeg')";
        }
    }
}

function displayTopBar(){
    if(planet!=null){
        /* planet name */
        document.getElementById("planet-name").innerHTML=planet.name+" "+planet.id;
        /* fleet-value */

        /* construction-value */

        /* steal */
        document.getElementById("steel-value").innerHTML=planet.ressources.steal;
        document.getElementById("steel-progress").style.width=parseInt(planet.ressources.steal*100/planet.depot.steal)+"%";
        /* crystal */
        document.getElementById("crystal-value").innerHTML=planet.ressources.crystal;
        document.getElementById("crystal-progress").style.width=parseInt(planet.ressources.crystal*100/planet.depot.crystal)+"%";
        /* uranium */
        document.getElementById("uranium-value").innerHTML=planet.ressources.uranium;
        document.getElementById("uranium-progress").style.width=parseInt(planet.ressources.uranium*100/planet.depot.uranium)+"%";
        /* energy */
        document.getElementById("energy-value").innerHTML=planet.ressources.energy;
        document.getElementById("energy-progress").style.width=parseInt(100+planet.ressources.energy)+"%";
        /* population */
        document.getElementById("population-value").innerHTML=planet.ressources.population.used;
        document.getElementById("population-progress").style.width=parseInt(planet.ressources.population.used*100/planet.ressources.population.total)+"%";
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

function getPlanetById(id){

}

function getSystem(){

}

function getPlanet(){
    $.ajax({
        type: "GET",
        url: "static/JsonTest/Planet.json", /* temp url */
        async : false,
        dataType: 'json',
        error: function (data) {
            console.log(data.status + ':' + data.statusText,data.responseText);
        },
        success: function(data) {
            planet=data;
        }
    });
}

function getPlayer(){
    $.ajax({
        type: "GET",
        url: "static/JsonTest/Player.json", /* temp url */
        async : false,
        dataType: 'json',
        error: function (data) {
            console.log(data.status + ':' + data.statusText,data.responseText);
        },
        success: function(data) {
            player=data;
        }
    });
    console.log(player);
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
            if(h<70) return;
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
                        let price = 50;
                        let gold = document.getElementById("gold-value");
                        if((parseInt(gold.innerHTML)-price)>=0){
                            img=document.createElement("img");
                            img.src="static/assets/buildings3D/"+buildings[b-1]+".png";
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

function show_menuv(){
    document.getElementById('menuv').style.display="block";
}

function show_menuc(){
    document.getElementById('menuc').style.display="block";
}

function show_menua(){
    document.getElementById('menua').style.display="block";
}

function show_menur(){
    document.getElementById('menur').style.display="block";
}

function close_menuv(){
    document.getElementById('menuv').style.display="none";
}

function close_menuc(){
    document.getElementById('menuc').style.display="none";
}

function close_menua(){
    document.getElementById('menua').style.display="none";
}

function close_menur(){
    document.getElementById('menur').style.display="none";
}


function block_Colonizer(){
    let block;
    const station_spacial = Boolean("false");
    if(station_spacial){
        block = Boolean("true");
    }
    else if(station_spacial===false){
        block=false;
    }
    if(block){
        document.getElementById('Colonizer').style.opacity="0.1";
        //document.getElementById('choix5').style.display="none";
    }
}

function block_LightTransportShip(){
    let block;
    const station_spacial = Boolean("false");
    if(station_spacial){
        block = Boolean("true");
    }
    else if(station_spacial===false){
        block=false;
    }
    if(block){
        document.getElementById('LightTransportShip').style.opacity="0.3";
        //document.getElementById('choix6').style.display="none";
    }
}

function block_HeavyTransportShip(){
    let block;
    const station_spacial = Boolean("false");
    if(station_spacial){
        block = Boolean("true");
    }
    else if(station_spacial===false){
        block=false;
    }
    if(block){
        document.getElementById('HeavyTransportShip').style.opacity="0.1";
        //document.getElementById('choix1').style.display="none";
    }
}

function block_Destroyer(){
    let station_spacial = Boolean("false");
    let block
    if(station_spacial){
        block = Boolean("true");
    }
    else if(station_spacial===false){
        block=false;
    }
    if(block){
        document.getElementById('Destroyer').style.opacity="0.1";
        //document.getElementById('choix2').style.display="none";
    }
}

function block_BattleCruiser(){
    let block = Boolean("true");
    if(block){
        document.getElementById('BattleCruiser').style.opacity="0.1";
        //document.getElementById('choix3').style.display="none";
    }
}

function block_BattleShip(){
    const block = Boolean("true");
    if(block){
        document.getElementById('BattleShip').style.opacity="1";
        document.getElementById('BattleShip').style.color="black";
        //document.getElementById('choix4').style.display="none";
    }
}
