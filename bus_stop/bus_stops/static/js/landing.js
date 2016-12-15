'use strict';


function create_form_events(){
  // Fields in use
  var $email= $('input[name=email]')
  var $confirm_email = $('input[name=confirm_email]')
  var $zip = $('input[name=zip]')
  var $pass = $('input[name=password]')
  var $confirm_pass = $('input[name=confirm_pass]')

  // regex patterns for validation
  var re_email =/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  var re_pass = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$/;
  var re_zip = /(\d{5})/;

  /* client side field verification
  1. Email verification
  2. Zip code verification
  3. password verification
  */
  /////////////////////////////////////// 1
  $email.on('blur', function(){
    if (re_email.test($email.val())){
      $email.css('background-color', '#4C934C');
    } else{
      $email.css('background-color', '#f63939');
    }
  });
  $confirm_email.on('blur', function(){
    if ($email.val() == $confirm_email.val()){
      $confirm_email.css('background-color', '#4C934C')
    } else{
      $confirm_email.css('background-color', '#f63939')
    }
  });
  ///////////////////////////////////////// 2
  $zip.on('blur', function(){
    if (re_zip.test($zip.val())){
      $zip.css('background-color', '#4C934C')
    } else{
      $zip.css('background-color', '#f63939')
    }
  });
  //////////////////////////////////////// 3
  $pass.on('blur', function(){
    if (re_pass.test($pass.val())){
      $pass.css('background-color', '#4C934C')
    } else{
      $pass.css('background-color', '#f63939')
    }
  });
  $confirm_pass.on('blur', function(){
    if ($confirm_pass.val() == $pass.val()){
      $confirm_pass.css('background-color', '#4C934C')
    } else{
      $confirm_pass.css('background-color', '#f63939')
    }
  })

};


function login_form(){
  $('#land').fadeOut(function(){
    $('#loginform').fadeIn();
  });
};


function guest_form(){
  $('#land').fadeOut(function(){
    $('#guest').fadeIn();
  });
};


function create_form(){
  $('#land').fadeOut(function(){
    $('#createacc').fadeIn();
    create_form_events();
  });
};


(function direction(){
  $('#login').on('click touchstart', function(evt){
    login_form()
  });
  $('#create').on('click touchstart', function(evt){
    create_form()
  });
  $('#continue').on('click touchstart', function(evt){
    guest_form()
  });
})();
