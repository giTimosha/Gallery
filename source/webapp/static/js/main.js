function jqueryParseData (response, status) {
    location.reload(true);

    console.log(response);
    console.log(status);
}

function jqueryAjaxError(response, status) {
    console.log(response);
    console.log(status);
    console.log('error');
}


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');


function createTasksLoadIndex() {
    $.ajax({
        url: 'http://localhost:8000/api/v1/comments/',
        method: 'POST',
        contentType: 'application/json',
        headers: {'X-CSRFToken': csrftoken},
        data: JSON.stringify({text: 'test', author_name: 'admin', photo: 3}),
        dataType: 'json',
        success: jqueryParseData,
        error: jqueryAjaxError
    })
}


function deleteTasksLoadIndex(comment_id) {
    $.ajax({
        url: 'http://localhost:8000/api/v1/comments/' + comment_id,
        method: 'DELETE',
        contentType: 'application/json',
        headers: {'X-CSRFToken': csrftoken},
        dataType: 'json',
        success: jqueryParseData,
        error: jqueryAjaxError
    })
}

$(document).ready(function () {
});