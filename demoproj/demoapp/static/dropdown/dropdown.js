 
 /*==============================   Models Drop Down  =================================*/


$("#id_brand").change(function () {
    const url = $("#asset").attr("data-models-url");  
    const brandId = $(this).val();   
    $.ajax({                       
        url: url,                
        data: {
            'brand_id': brandId        
        },
        success: function (data) {    
            $("#id_model").html(data);   
          
        }
    });

});

 /*==============================   Location  Drop Down  =================================*/

 $("#id_LocationType").change(function () {
    const url = $("#asset").attr("data-locations-url");  
    const LocationTypeId = $(this).val();  

    $.ajax({                     
        url: url,              
        data: {
            'LocationType_id': LocationTypeId       
        },
        success: function (data) {   
            $("#id_AssignedLocation").html(data);  
        }
    });

});




 /*==============================   Zones  Drop Down  =================================*/

