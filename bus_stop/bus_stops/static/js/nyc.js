'use strict';


function get_address(dist, dist_unit){
  navigator.geolocation.getCurrentPosition(function(position){
    find_stops(position.coords.latitude, position.coords.longitude, dist, dist_unit);
  });
};


(function user_actions(){
  var eval_dist = new RegExp('[0-9]+')

  $('#get').on('click touchstart', function(evt){
    var dist = $('#int-distance').val();
    var dist_unit = $('#dist_unit').val();

    if ((eval_dist.test(dist)) && (dist_unit !== 'nill')){
      get_address(dist, dist_unit);
    }else{
      alert("Please select a unit / enter the distance you'd like.")
    }
  });
  $('#given').on('click touchstart', function(evt){
    evt.stopImmediatePropagation();
    evt.preventDefault();

    var dist = $('#int-distance').val();
    var dist_unit = $('#dist_unit').val();

    if((eval_dist.test(dist)) && (dist_unit !== 'nill')){
      geocode_address($('#address').val(), dist, dist_unit);
    }else{
      alert("Please select a unit / enter the distance you'd like.")
    }
  });
})();
