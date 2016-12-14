'use strict';


function login_form(){
  
}


function guest_form(){

}


(function direction(){
  $('#login').on('click touchstart', function(evt){
    login_form()
  });
  $('#continue').on('click touchstart', function(evt){
    guest_form()
  });
})();
