'use strict';


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
