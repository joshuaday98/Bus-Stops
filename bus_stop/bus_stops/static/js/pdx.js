'use strict';


function bus_markers(response){
  var bus = response.resultSet.vehicle;

  if (bus){$.each(bus, function(index, value){
      var marker = new google.maps.Marker({
        position: {lat:bus[index].latitude, lng:bus[index].longitude},
        map: map,
        animation: google.maps.Animation.DROP,
        title: 'Route: ' + bus[index].routeNumber,
        icon: 'http://maps.google.com/mapfiles/ms/icons/green-dot.png'
      });
    });}else {
      alert('There are no available busses on that route!')
    };
  };


function show_route(route_num){
    $.ajax({url: '/find_route/',
            type: 'POST',
            data: {'route': route_num},
            success: function(resp){
              console.log(route_num)
              bus_markers(resp);
            },
            error: function(resp){
              console.log(resp);
            }
          });
        };

function add_stop_markers(mylat, mylng, ob){
  var mycoords = {lat:mylat, lng:mylng};
  var stops = ob.resultSet.location;

  map = new google.maps.Map(document.getElementById('map'),{
    zoom: 15,
    center: mycoords
  });

  $.each(stops, function(index, value){
      var $info_string = $('<div></div>');

      var marker = new google.maps.Marker({
        position: {lat:stops[index].lat, lng:stops[index].lng},
        map:map,
        animation:google.maps.Animation.DROP,
        title: stops[index].desc + ' || ' + stops[index].dir
      });

      $.each(stops[index].route, function(inde, value){
        var route_num = stops[index].route[inde].route;

        if (route_num.toString().length == 1){
          $info_string.append($('<a><br><p>Route: <a href="http://trimet.org/schedules/r00'+route_num+'.htm">'+route_num+'</a></p></a>').on('click', function(){
            show_route(route_num);
          }));
        } else if(route_num.toString().length == 2){
          $info_string.append($('<a><br><p>Route: <a href="http://trimet.org/schedules/r0'+route_num+'.htm">'+route_num+'</a></p></a>').on('click', function(){
            show_route(route_num);
          }));
        }else {
          $info_string.append($('<a><br><p>Route: <a href="http://trimet.org/schedules/r'+route_num+'.htm">'+route_num+'</a></p></a>').on('click', function(){
            show_route(route_num);
          }));
        };
      });

      var infowindow = new google.maps.InfoWindow({
        content:$info_string[0]
      });

      marker.addListener('click', function(){
        infowindow.open(map, marker);
      });
    });
  };


function find_stops(lat, lng, dist, dist_unit){
  $.ajax({url: '/find_stops/',
          type:'POST',
          data:{'lat': lat,
                'lng': lng,
                'distance': dist,
                'unit_for_dist': dist_unit},
          success: function(response){
            add_stop_markers(lat, lng, response);
          },
          error: function(error){
            $('#results').append('<p>An Error Occured</p>');
          }
        });
      };


function geocode_address(user_address, dist, dist_unit){
  $.ajax({url:'/geocode/',
          type:'POST',
          data:{'address': user_address},
          success: function(response){
            find_stops(response.lat, response.lng, dist, dist_unit)
          },
          error: function(error){
            console.log(error);
            $('#results').append('<p>An Error Occured</p>');
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
