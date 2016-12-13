'use strict';

function add_stop_markers(mylat, mylng, stops){
  var mycoords = {lat:mylat, lng:mylng};

  map = new google.maps.Map(document.getElementById('map'),{
    zoom: 17,
    center: mycoords
  });

  $.each(stops, function(index, value){
    var $info_string = '<div><p>Address:<br><b>'+ stops[index].street + '</b><br><br>TransitType:<br><b>' + stops[index].type +'</b></p></div>';
    var pos = {lat:parseFloat(stops[index].lat), lng:parseFloat(stops[index].lng)}
    console.log($info_string)
    var marker = new google.maps.Marker({
      position: pos,
      map:map,
      animation:google.maps.Animation.DROP,
      title: stops[index].street + ' || ' + stops[index].type
    });

    var infowindow = new google.maps.InfoWindow({
      content:$info_string
    });

    marker.addListener('click', function(){
      infowindow.open(map, marker);
    });
  });
};

function find_stops(lat, lng, dist, dist_unit){
  $.ajax({url:'/nyc_find_stops/',
          type: 'POST',
          data:{'lat':lat,
               'lng':lng,
               'dist':dist,
               'unit_for_dist':dist_unit},
          success: function(response){
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
    if ((eval_dist.test(dist)) && (dist_unit !== 'nill')){
      get_address(dist, dist_unit);
    }else{
      alert("Please select a unit / enter the distance you'd like.")
    }
  });
  $('#given').on('click touchstart', function(evt){
    evt.stopImmediatePropagation();

    var dist = $('#int-distance').val();
    var dist_unit = document.getElementById('dist_unit sel1').value;

    if((eval_dist.test(dist)) && (dist_unit !== 'nill')){
      geocode_address($('#address').val(), dist, dist_unit);
    }else{
      alert("Please select a unit / enter the distance you'd like.")
    }
  });
})();
