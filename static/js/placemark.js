ymaps.ready(init);

function init(){
    var myMap = new ymaps.Map("map", {
        center: [41.015, 70.074],
        zoom: 15
    },{
       searchControlProvider: 'yandex#search'
    });

    myMap.geoObjects
    .add(new ymaps.Placemark([41.015248, 70.074561],
       {
          balloonContent: 'цвет <strong>воды пляжа бонди</strong>'
       }, {
          preset: 'islands#icon',
          iconColor: '#0095b6'
       })
    );
}
