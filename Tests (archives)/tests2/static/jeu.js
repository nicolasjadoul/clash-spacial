

function showMap(){
    let row,column,r,c,img;
    let map = document.getElementById("map");
    for(r=0;r<8;r++){
        row = document.createElement("div");
        row.className="row";
        for(c=0;c<8;c++) {
            column=document.createElement("div");
            column.className="column";
            img=document.createElement("img");
           img.src="static/assets/bat1.png";
            img.className="column";
            column.append(img);
            row.append(column);
        }
        map.append(row);
    }

}