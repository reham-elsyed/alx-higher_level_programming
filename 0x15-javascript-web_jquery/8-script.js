$(function(){
    let $movieList = ('#list_movies');
    $.ajax({
        type: 'GET',
        url: 'https://swapi-api.hbtn.io/api/films/?format=json',
        success: function(data){
            $.each(data.results,function(id, film){
                $movieList.append('<li>' + film.title + '</li>')
            });
        }
    });
});
