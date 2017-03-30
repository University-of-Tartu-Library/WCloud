
//update slider
$("#limit_input").on("input", function(e) {
	$("#limit_output").text($(e.target).val())
});

//word_obj
function WordFreq(name, count){
	this.name = name;
	this.count = count;
}

// Convert python Counter to bubble format
function counterToBubble(cnt) {
	var wordObjs = [];
	cnt = JSON.parse(cnt);
	for (var key in cnt) {
		if (cnt.hasOwnProperty(key)) {
			wordObjs.push(new WordFreq(key, cnt[key]));
		}
	}
	return wordObjs;
}


//doc ready
$(function() {
    // Submit post on submit
    $('#lem-submit').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        submit_form();
    });

    // AJAX for submitting
    function submit_form() {
        console.log("create_bubbles is working!") // sanity check
        $.ajax({
            url : $("#lem-submit").attr("action"), // the endpoint
            type : "POST", // http method
            data : JSON.stringify({ text : $('#text-input').val() }, null, '\t'), // data sent with the post request
            dataType: 'jsonp',
            contentType: 'application/json;charset=UTF-8',
            // handle a successful response
            success : function(json) {
            	var text_freq = counterToBubble(json);
                d3_chart = drawBubbles(text_freq, $("#limit_input").val());
            },
            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                $('#vis').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    };

})

