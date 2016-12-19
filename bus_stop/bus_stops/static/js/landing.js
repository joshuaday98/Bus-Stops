(function main(){
    'use strict';


    (function enable_pops(){
      $(document).ready(function(){
        $('[data-toggle=popover]').popover();
      });
    })();


    function change_border(html_element, change){
      if (change !== 0){
        html_element.css('border-color', 'rgb(48, 172, 22)');
        html_element.css('box-shadow', '0 0 5px rgba(48, 172, 22, 0.74)');
        html_element.css('border-radius', '5px')
      } else{
        html_element.css('border-color', 'rgb(181, 16, 16)');
        html_element.css('box-shadow', '0 0 5px rgba(181, 16, 16, 0.74)');
        html_element.css('border-radius', '5px')
      }
    };


    function create_form_events(states){
    // Fields in use
    var field_array = [$('input[name=email]'),//0
                       $('input[name=confirm_email]'),//1
                       $('input[name=zip]'),//2
                       $('input[name=password]'),//3
                       $('input[name=confirm_pass]'),//4
                       $('input[name=state]'),//5
                       $('input[name=fname]'),//6
                       $('input[name=lname]'),//7
                       $('#create_acc'),//8
                       $('input[name=gender]'),//9
                       $('input[name=street]')]//10

    // regex patterns for validation
    var re_email =/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    var re_pass = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,16}$/;
    var re_zip = /(\d{5})/;
    var re_name = /^[A-Za-z]+$/;

    /* client side field verification
    1. Email verification
    2. address verification
    3. password verification
    4. Arbitrary verification
    */

    /////////////////////////////////////// 1
    field_array[0].on('blur', function(){
      if (re_email.test(field_array[0].val())){
        change_border(field_array[0],1);
      } else{
        change_border(field_array[0],0);
      }
    });
    field_array[1].on('blur', function(){
      if (field_array[0].val() == field_array[1].val()){
        change_border(field_array[1],1);
      } else{
        change_border(field_array[1],0);
      }
    });
    ///////////////////////////////////////// 2
    field_array[2].on('blur', function(){             // Zip
      if (re_zip.test(field_array[2].val())){
        change_border(field_array[2],1);
      } else{
        change_border(field_array[2],0);
      }
    });
    field_array[5].on('blur', function(){              // State
      if ($.inArray(field_array[5].val(), states) != -1){
         change_border(field_array[5],1);
      } else{
        change_border(field_array[5],0);
      }
    });
    field_array[10].on('blur', function(){            // Street
      $.ajax({url:'/geocode/',
              type:'GET',
              data:{'address':field_array[10].val()},
              success: function(response){
                if (response.validity == 1){
                  change_border(field_array[10],1);
                } else{
                  change_border(field_array[10],0);
                }
              },
              error: function(error){
                console.log(error);
              }
            });
          });
    //////////////////////////////////////// 3
    field_array[3].on('blur', function(){
      if (re_pass.test(field_array[3].val())){
        change_border(field_array[3],1);
      } else{
        change_border(field_array[3],0);
      }
    });
    field_array[4].on('blur', function(){
      if (field_array[4].val() == field_array[3].val()){
        change_border(field_array[4],1);
      } else{
        change_border(field_array[4],0);
      }
    });
    ///////////////////////////////////////////// 4
    field_array[6].on('blur', function(){               //first name
      if (re_name.test(field_array[6].val())){
        change_border(field_array[6],1);
      } else{
        change_border(field_array[6],0);
      }
    });
    field_array[7].on('blur', function(){               //last name
      if(re_name.test(field_array[7].val())){
        change_border(field_array[7],1);
      } else{
        change_border(field_array[7],0);
      }
    });
    field_array[9].on('blur', function(){               //gender
      if (re_name.test(field_array[9].val())){
        change_border(field_array[9],1);
      } else{
        change_border(field_array[9],0);
      }
    });
  };


  (function direction(){
    var states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
                  "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
                  "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
                  "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
                  "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"];

    $('#login').on('click touchstart', function(evt){
      $('#land').fadeOut(function(){
        $('#loginform').fadeIn();
      });
    });
    $('#create').on('click touchstart', function(evt){
      $('#land').fadeOut(function(){
        $('#createacc').fadeIn(function(){
          create_form_events(states);
        });
      });
    });
    $('#continue').on('click touchstart', function(evt){
      $('#land').fadeOut(function(){
        $('#guest').fadeIn();
      });
    });
    $('#back').on('click touchstart', function(evt){
      $('#guest').fadeOut()
      $('#createacc').fadeOut()
      $('#loginform').fadeOut(function(){
        $('#land').fadeIn()
      });
    });

    $('input[name=state]').autocomplete({
      source:states
    });
  })();
})();
