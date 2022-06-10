let planet;
let R,C;
const UNSELECTED_COLOR = "rgba(0, 0, 0, 0.05)";
const SELECTED_COLOR = "rgba(255, 153, 0, 0.7)";

function display(){
    getPlanet();
    showMap();
}

function showMap(){
    console.log(planet);
    if(planet!=null){
    R=planet.size.x;
    C=planet.size.y;
    let row,column,r,c,img,building;
    let map = document.getElementById("map");
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
                    case "habitation" : img.src="../assets/buildings3D/habitation.png"; break;
                    case "crystalMine" : img.src="../assets/buildings3D/crystalMine.png"; break;
                    case "uranimMine" : img.src="../assets/buildings3D/uranimMine.png"; break;
                    case "stealMine" : img.src="../assets/buildings3D/stealMine.png"; break;
                    case "commandCenter" : img.src="../assets/buildings3D/commandCenter.png"; break;
                    case "stealDepot" : img.src="../assets/buildings3D/stealDepot.png"; break;
                    case "defenseTurret" : img.src="../assets/buildings3D/defenseTurret.png"; break;
                    case "crystalDepot" : img.src="../assets/buildings3D/crystalDepot.png"; break;
                    case "garage" : img.src="../assets/buildings3D/garage.png"; break;
                    case "spaceShipYard" : img.src="../assets/buildings3D/spaceShipYard.png"; break;
                    case "solarPanel" : img.src="../assets/buildings3D/solarPanel.png"; break;
                    case "nuclearPlant" : img.src="../assets/buildings3D/nuclearPlant.png"; break;
                }
                img.id="figure"+r+"-"+c;
                img.className="column1x1";
                img.style.height = "70px";
                img.style.width = "44px";
                img.draggable=false;
                column.append(img);
            }
            setEventListeners(column);
            row.append(column);
        }
        map.append(row);
    }
    }
}

function getPlanet(){
    $.ajax({
        type: "GET",
        url: "Planet.json", /* temp url */
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

function setEventListeners(column){

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
