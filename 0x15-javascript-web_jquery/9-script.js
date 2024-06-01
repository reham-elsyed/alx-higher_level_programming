$(function(){
	let $mland = ('#hello');
	$.ajax({
	type: 'GET',
	url: 'https://hellosalut.stefanbohacek.dev/?lang=fr/?format=json',
        success: function(data){
		let helloTranslation = data.hello;
		$mland.text(helloTranslation);
	}
    });
});
