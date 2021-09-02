function select(id, bool) {
    if (bool === true) {
        let course = $('#' + id).remove()
        course.attr('onclick', `select(${id}, false)`)
        $('#choice').append(course)


    } else {
        let course = $('#' + id).remove()
        course.attr('onclick', `select(${id}, true)`)
        $('#suggest').append(course)
    }
}


function make_select_html(course) {
    return `
        <div class="card-body col-12">
            <div class="row">
                <p class="card-text text-right col-2">${course.lesson.name}</p>
                <p class="card-text text-right col-2">${course.teacher.last_name}</p>
                <p class="card-text text-right col-2">${course.lesson.unit}</p>
                <div class="col-6">
                    <div class="row">
                        <p class="card-text col-6 text-right">${course.session_1} تا ${course.session_2} </p>
                        <p class="card-text col-3 text-right"
                           style="direction: ltr!important; font-size: 70%">${course.session_start_time}</p>
                        <p class="card-text col-3 text-right"
                           style="direction: ltr!important; font-size: 70%">${course.session_end_time}</p>
                    </div>
                </div>
            </div>
        </div>
    `
}


function select_from_results(course) {
    let selected_div = $(`#${course.id}`)
    let result_field = $('#fields_results')
    if ( selected_div.html() === undefined) {
        let course_div = $(`<div id="${ course.id }" class="card w-100 row course-select" style="width: 70rem!important;"/>`)
        course_div.html(make_select_html(course))
        course_div.attr('onclick', `select(${course.id}, true)`)
        $('#suggest').append(course_div)


    }
    $("#field_name").val('')
    result_field.html('')
}


function get_courses_results(url) {
    let text = $("#field_name").val()
    let result_field = $('#fields_results')
    if (text !== '') {
        $.get(url.slice(0, 23) + text, function (data, status) {
            if (data.length === 0) {
                console.log(data.length)
                result_field.html('')
                let h5 = $('<h5/>').html('نتیجه ای یافت نشد')
                result_field.append(h5)
            } else {
                result_field.html('')
                let title = `
                        <div class="w-75">
                             <div class="row results-div">
                                 <div class="col-8"><h5 class="mr-5">نام درس</h5></div>
                                 <div class="col-4"><h5>دانشکده</h5></div>
                             </div>
                         </div>
                    `
                result_field.append(title)
                for (let res of data) {
                    let div = $(`<div id="l-${res.id}" class="w-75" onclick="select_from_results($(this).data('key'))" />`)
                    let content = `
                         <div class="row results-div">
                             <div class="col-8"><h5 class="mr-5">${res.lesson.name}</h5></div>
                             <div class="col-4"><h5>${res.college.name}</h5></div>
                         </div>
                    `
                    div.html(content)
                    div.data('key', res)
                    div.hover(function () {
                        $(this).css("background-color", "rgb(71, 190, 235)");
                        $(this).css("color", "white");
                        $(this).css("border-radius", "20px");
                        $(this).css("cursor", "pointer");
                    }, function () {
                        $(this).css("background-color", "transparent");
                        $(this).css("color", "black");
                        $(this).css("cursor", "none");
                    });
                    result_field.append(div)
                }


            }
        })}
    else {
        result_field.html('')
    }
}
