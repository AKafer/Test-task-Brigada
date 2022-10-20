$(document).ready(function(){
    $.ajax({
    type: 'GET',
    url: 'http://127.0.0.1:8000/api/cities/',
    success: function(response){
      $('#data-box').html(JSON.stringify(response));
      var sel1 = $('#sel1');
      for(let i=0; i<response.length; i++){
        var city_id = response[i].id;
        var city_name = response[i].name;
        sel1.append(`<option value="${city_id}">
                           ${city_name}
                      </option>`);
      }
    }
    });
});
