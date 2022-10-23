$(document).ready(function() {
    var sel1 = $('#sel1');
    var sel2 = $('#sel2');
    var sel3 = $('#sel3');
    var opt1 = localStorage.getItem('opt1')
    var opt2 = localStorage.getItem('opt2')
    var opt3 = localStorage.getItem('opt3')


    sel1.change(function() {
        var flag = 0
        opt1 = $(this).val();
        localStorage.setItem('opt1', opt1);
        $('#name').html("");
        $('#head').html("");
        $('#amount_people').html("");
        $('#qualification').html("");
        sel2.empty();
        sel2.append(`<option value="0">-Выбрать-</option>`);
        sel3.empty();
        sel3.append(`<option value="0">-Выбрать-</option>`);
        $.ajax({
            type: 'GET',
            url: 'api/brigades/from_city/' + opt1,
            success: function(response) {
                for (let i = 0; i < response.length; i++) {
                    var brigada_id = response[i].id;
                    var brigada_name = response[i].name;
                    sel2.append(`<option value="${brigada_id}">${brigada_name}</option>`);
                    if (brigada_id == opt2) {
                      flag = 1;
                    }
                }
                if (flag == 1) {
                    sel2.val(opt2);
                    console.log(sel2.change());
                }
            }
        });
    });

    sel2.change(function() {
        var flag = 0
        opt2 = $(this).val()
        localStorage.setItem('opt2', opt2);
        $('#name').html("");
        $('#head').html("");
        $('#amount_people').html("");
        $('#qualification').html("");
        sel3.empty();
        sel3.append(`<option value="0">-Выбрать-</option>`);
        $.ajax({
            type: 'GET',
            url: 'api/objects/from_brigada/' + opt2,
            success: function(response) {
                for (let i = 0; i < response.length; i++) {
                    var object_id = response[i].id;
                    var object_name = response[i].name;
                    sel3.append(`<option value="${object_id}">${object_name}</option>`);
                    if (object_id == opt3) {
                      flag = 1;
                    }
                }
                if (flag == 1) {
                    sel3.val(opt3);
                    sel3.change();
                }
            }
        });
        $.ajax({
            type: 'GET',
            url: 'api/brigades/' + opt2,
            success: function(response) {
                $('#name').html(response.name);
                $('#head').html(response.head);
                $('#amount_people').html(response.amount_people);
                $('#qualification').html(response.qualification);
                name = response.name;
                head = response.head;
                amount_people = response.amount_people;
                qualification = response.qualification;
            }
        });
    });

    sel3.change(function() {
        opt3 = $(this).val();
        localStorage.setItem('opt3', opt3);
        $('#name').html(name);
        $('#head').html(head);
        $('#amount_people').html(amount_people);
        $('#qualification').html(qualification);
        $.ajax({
            type: 'GET',
            url: 'api/objects/' + opt3,
            success: function(response) {
                $('#name').html(response.name);
                $('#head').html(response.head);
                $('#amount_people').html(response.amount_people);
                $('#qualification').html(response.qualification);;
            }
        });
    });

    var name;
    var head;
    var amount_people;
    var qualification;
    sel1.append(`<option value="0">-Выбрать-</option>`);
    sel2.append(`<option value="0">-Выбрать-</option>`);
    sel3.append(`<option value="0">-Выбрать-</option>`);
    $.ajax({
        url:  'api/cities/',
        success: function(response) {
            for (let i = 0; i < response.length; i++) {
                var city_id = response[i].id;
                var city_name = response[i].name;
                sel1.append(`<option value="${city_id}">${city_name}</option>`);
            }
            sel1.val(opt1);
            sel1.change();
        }
    });
});
