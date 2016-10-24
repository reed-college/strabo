// Initialize custom GPS location icon
var locateIcon = L.icon({
    iconUrl: '/static/locationDot.png',
    iconSize: [20,20]
});

// Create custom leaflet icons
var ColorIcon = L.Icon.extend({
    options: {
        shadowUrl: '/static/MapPinShadow.png',
        iconSize:     [30, 50],
        shadowSize:   [30, 32],
        iconAnchor:   [15, 50],
        shadowAnchor: [2, 30],
        popupAnchor:  [-3, -50]
    }
});

var iconObjs = function(){
    var icon_objs = {};
    for (icon_name in straboconfig["COLOR_ICON"]){
            icon_file = straboconfig["COLOR_ICON"][icon_name];
            icon_objs[icon_name] = new ColorIcon({iconUrl:'/static/map_icons/' + icon_file});
        }
    return icon_objs;

}();

// creates leaflet map object
function make_map(map_container_id){
    var map = L.map(map_container_id, {}).setView([straboconfig["LAT_SETTING"], straboconfig["LONG_SETTING"]], straboconfig["INITIAL_ZOOM"]);
    return map;
}
function add_tile_to(map){
    L.tileLayer(straboconfig["MAP_TILE_SRC"],straboconfig["LEAFLET_ATTRIBUTES"]).addTo(map);
}
function make_all_layers_group(interest_point_geojson_list){
    return L.geoJson(interest_point_geojson_list)
}
function is_point(layer){
    return layer.feature.geometry.type == "Point"
}
function is_zone(layer){
    return layer.feature.geometry.type == "Polygon"
}

// sets icon object for points and styling for zones
function set_styles(all_layers_group){
    var all_layers = all_layers_group.getLayers();

    var points = all_layers.filter(is_point);
    var zones = all_layers.filter(is_zone);

    zones.forEach(function(zone){
        zone.setStyle({
              weight: 1,
              color: straboconfig["COLOR_HEX"][zone.feature.properties.style],
              dashArray: '',
              fillOpacity: 0.3
        });
    });

    points.forEach(function(point){
        point.setIcon(icon_objs[point.feature.properties.style]);
    })
}
function place_overlays_on(all_layers_group,map){
    // Set layers and add toggle control menu for each layer,
    //NOTE: will not work if all_layers_group is added to the map elsewhere
    var all_layers = all_layers_group.getLayers();
    var overlays = {};
    for(var lay_num in straboconfig["LAYER_FIELDS"]){
        var lays = all_layers.filter(function(lay){return lay.feature.properties.layer == lay_num});
        var laygroup = L.layerGroup(lays);
        laygroup.addTo(map);
        var lay_name = straboconfig["LAYER_FIELDS"][lay_num];
        overlays[lay_name] = laygroup;
    }
    L.control.layers(null, overlays).addTo(map);
}

// Popups with the interest point name appear when clicked
function bind_popups(all_layers_group){
    var all_layers = all_layers_group.getLayers();

    all_layers.forEach(function(layer){
        layer.bindPopup(layer.feature.properties.name);
    });
}
