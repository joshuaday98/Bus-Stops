'use strict';

function find_stops(lat, lng, dist, dist_unit){
  $.ajax({url:'/nyc_find_stops/',
          type: 'POST',
          data:{'lat':lat,
               'lng':lng,
               'dist':dist,
               'unit_for_dist':dist_unit},
          success: function(response){
            console.log(response)
            add_stop_markers(lat, lng, response)
          },
          error: function(error){
            $('results').append('<p>An Error Occured</p>')
          }
        });
      };


function geocode_address(user_address, dist, dist_unit){
  $.ajax({url:'/geocode/',
          type: 'POST',
          data:{'address':user_address},
          success: function(response){
            find_stops(response.lat, response.lng, dist, dist_unit)
          },
          error: function(error){
            console.log(error);
            $('#results').append('<p>An Error Occured</p>')
          }
        });
      };


function get_address(dist, dist_unit){
  navigator.geolocation.getCurrentPosition(function(position){
    find_stops(position.coords.latitude, position.coords.longitude, dist, dist_unit);
  });
};


(function user_actions(){
  var eval_dist = new RegExp('[0-9]+')

  $('#get').on('click touchstart', function(evt){
    var dist = $('#int-distance').val();
    var dist_unit = document.getElementById('dist_unit sel1').value;
    console.log(dist_unit)
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
    var dist_unit = document.getElementById('dist_unit sel1').value;

    if((eval_dist.test(dist)) && (dist_unit !== 'nill')){
      geocode_address($('#address').val(), dist, dist_unit);
    }else{
      alert("Please select a unit / enter the distance you'd like.")
    }
  });
})();
