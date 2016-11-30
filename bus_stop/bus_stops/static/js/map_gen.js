var map;

function PDXMap() {
  map = new google.maps.Map(document.getElementById('map'),
  {center: {lat: 45.5234, lng: -122.6762},
  zoom: 10});
};

function NYCMap() {
  map = new google.maps.Map(document.getElementById('map'),
   {center: {lat: 40.730610, lng: -73.935242},
   zoom: 11});
 };
