function getramval(){
    var uiram = document.getElementsByName("uiram");
    for(var i in uiram){
        if (uiram[i].checked){
            return parseInt(uiram[i].value);
        }
    }
    return -1
}

function getdiskval(){
    var uidisk = document.getElementsByName("uidisk");
    for(var i in uidisk){
        if (uidisk[i].checked){
            return parseInt(uidisk[i].value);
        }
    }
    return -1
}

function onClickedEstimatePrice(){
    console.log("Estimate Price Button clicked!")
    var screen_size = document.getElementById("uiscreen");
    var ram = getramval();
    var disk_size = getdiskval();
    var brand = document.getElementById("uibrands");
    var cpu = document.getElementById("uicpus");
    var estPrice = document.getElementById("uiEstimatedPrice");

    var url = "/api/predict_laptop_price";

    $.post(url, {
        screen_size: parseFloat(screen_size.value),
        ram: ram,
        disk_size: disk_size,
        brand: brand.value,
        cpu: cpu.value
    }, function(data,status){
        console.log(data);
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Rupees</h2>";
        console.log(status);
    });
}


function onPageLoad(){
    console.log("document loaded");
    var url1 = "/api/get_brands";
    $.get(url1,function(data1,status){
        console.log("got response for get_brands request");
        if (data1){
            var brands = data1.brands;
            var uibrands= document.getElementById("uibrands");
            $('#uibrands').empty();
            for(var i in brands){
                var opt = new Option(brands[i]);
                $('#uibrands').append(opt);
            }
        }
    });
    var url2 = "/api/get_cpus";
    $.get(url2,function(data2,status){
        console.log("got response for get_cpus request");
        if (data2){
            var cpus = data2.cpus;
            var uicpus= document.getElementById("uicpus");
            $('#uicpus').empty();
            for(var i in cpus){
                var opt = new Option(cpus[i]);
                $('#uicpus').append(opt);
            }
        }
    });

}

window.onload= onPageLoad;