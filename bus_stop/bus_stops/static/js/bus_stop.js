'use strict';


function add_markers(mylat, mylng, ob){
  var mycoords = {lat:mylat, lng:mylng};
  var stops = ob.resultSet.location;
  map = new google.maps.Map(document.getElementById('map'),{
    zoom: 15,
    center: mycoords
  });

  $.each(stops, function(index, value){
      var info_string = '';

      var marker = new google.maps.Marker({
        position: {lat:stops[index].lat, lng:stops[index].lng},
        map:map,
        animation:google.maps.Animation.DROP,
        title: stops[index].desc + ' || ' + stops[index].dir
      });

      $.each(stops[index].route, function(inde, value){
        var route_num = stops[index].route[inde].route;

        if (route_num.toString().length == 1){
          info_string += '<br><p>Route: <a href="http://trimet.org/schedules/r00'+route_num+'.htm">'+route_num+'</a></p>';
        } else if(route_num.toString().length == 2){
          info_string += '<br><p>Route: <a href="http://trimet.org/schedules/r0'+route_num+'.htm">'+route_num+'</a></p>';
        }else {
          info_string += '<br><p>Route: <a href="http://trimet.org/schedules/r'+route_num+'.htm">'+route_num+'</a></p>';
        };
      });

      var infowindow = new google.maps.InfoWindow({
        content:info_string
      });

      marker.addListener('click', function(){
        infowindow.open(map, marker);
      });
  });
};


function find_stops(lat, lng){
  $.ajax({url: '/find_stops/',
          type:'POST',
          data:{'lat': lat, 'lng': lng},
          success: function(response){
            add_markers(lat, lng, response);
          },
          error: function(error){
            $('#results').append('<p>An Error Occured</p>');
          }
        });};


function geocode_address(user_address){
  $.ajax({url:'/geocode/',
          type:'POST',
          data:{'address':user_address},
          success: function(response){
            find_stops(response.lat, response.lng)
          },
          error: function(error){
            console.log(error);
            $('#results').append('<p>An Error Occured</p>');
          }
        });};


function get_address(){
  navigator.geolocation.getCurrentPosition(function(position){
    find_stops(position.coords.latitude, position.coords.longitude);
  });
};


(function user_actions(){
  $('#get').on('click', function(evt){
    get_address();
  });
  $('#given').on('click', function(evt){
    evt.stopImmediatePropagation();
    evt.preventDefault();
    var address_string = $('#address').val()
    geocode_address(address_string)
  });
})();
