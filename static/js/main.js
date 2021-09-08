// select course between suggest and choice div
function select(id, bool) {
    if (bool === true) {
        let course = $('#' + id).remove()
        course.attr('onclick', `select(${id}, false)`)
        $('#choice').append(course)


    } else {
        let course = $('#' + id).remove()
        course.attr('onclick', `select(${id}, true)`)
        $('#choice > div').css('background-color', 'white')
        course.css('background-color', 'white')
        $('#suggest').append(course)
    }
}

// function for create search results div
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


// select courses from search field to suggest field
function select_from_results(course) {
    let selected_div = $(`#${course.id}`)
    let result_field = $('#fields_results')
    if (selected_div.html() === undefined) {
        let course_div = $(`<div id="${course.id}" class="card w-100 row course-select" style="width: 70rem!important;"/>`)
        course_div.html(make_select_html(course))
        course_div.attr('onclick', `select(${course.id}, true)`)
        $('#suggest').append(course_div)


    }
    $("#field_name").val('')
    result_field.html('')
}


// get results of courses query from api

function get_courses_results(url) {

    let text = $("#field_name").val()
    let result_field = $('#fields_results')
    if (text !== '') {
        console.log(url.slice(0, 27) + text)
        $.get(url.slice(0, 27) + text, function (data, status) {
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
        })
    } else {
        result_field.html('')
    }
}


// books rent search ajax

// convert true or false to 'ناموجود' and 'موجود'
function available_book(bool) {
    if (bool === false) {
        return 'موجود'
    } else {
        return 'ناموجود'
    }
}


// function for create search results div
function show_selected_book_data(id_num) {
    let alert_info = $('#books-limits')
    $(`#${id_num}`).remove();
    let text = `شما ${6 - document.getElementById('book_results_div').children.length + 1} کتاب دیگر میتوانید انتخاب کنید`
    alert_info.html(`<p>${text}</p>`)
}


function make_select_book_html(book) {
    return `
            <div class="row">
                <div class="card-text text-right col-2"><p class="mr-1">${book.id}</p></div>
                <div class="card-text text-right col-3"><p>${book.name}</p></div>
                <div class="card-text text-right col-3"><p>${book.study_field.name}</p></div>
                <div class="card-text text-right col-3"><p>${available_book(book.rented)}</p></div>
                <div class="card-text text-right col-1"><i onclick="show_selected_book_data(${book.id})" style="font-size: 150%" class="fa fa-trash-o text-danger mt-1 delete-book" aria-hidden="true"></i></div>
        </div>
    `
}


// select books from search field to choice field
function select_book_from_results(book) {
    let selected_div = $(`#${book.id}`)
    let books_results = $('#books_results')
    let alert_info = $('#books-limits')

    if (selected_div.html() === undefined) {
        if (6 - document.getElementById('book_results_div').children.length <= 0) {
            alert_info.html(`<p>شما دیگر نمیتوانید کتاب انتخاب کنید</p>`)
        } else {
            let text = `شما ${6 - document.getElementById('book_results_div').children.length} کتاب دیگر میتوانید انتخاب کنید`
            alert_info.html(`<p>${text}</p>`)
        }
        if (document.getElementById('book_results_div').children.length > 6) {
            alert('شما بیشتر از 5 کتاب نمیتوانید انتخاب کنید')
        } else {
            let book_div = $(`<div id="${book.id}" class="card w-100 course-select"/>`)
            book_div.html(make_select_book_html(book))
            book_div.data('key', book)
            $(`#${book.id} i`).data('key', book_div.data('key'))
            $('#book_results_div').append(book_div)
            $('#book_name').val('')
        }
    }
    books_results.html('')
}


// get results of courses query from api
function get_books_results(url) {

    let text = $("#book_name").val()
    let books_results = $('#books_results')
    if (text !== '') {
        $.get(url.slice(0, 23) + text, function (data, status) {

            if (data.length === 0) {
                books_results.html('')
                let h5 = $('<h5/>').html('نتیجه ای یافت نشد')
                books_results.append(h5)
            } else {
                books_results.html('')
                let title = `
                        <div class="w-75">
                             <div class="row results-div">
                                 <div class="col-7"><h5 class="mr-5">نام کتاب</h5></div>
                                 <div class="col-3"><h5 class="mr-5">نام رشته</h5></div>
                                 <div class="col-2"><h5>وضعیت</h5></div>
                             </div>
                         </div>
                    `
                books_results.append(title)
                for (let res of data) {
                    let div = $(`<div id="l-${res.id}" class="w-75" onclick="select_book_from_results($(this).data('key'))" />`)
                    let content = `
                         <div class="row results-div">
                             <div class="col-7"><h5 class="mr-5">${res.name}</h5></div>
                             <div class="col-3"><h5 class="mr-5">${res.study_field.name}</h5></div>
                             <div class="col-2"><h5>${available_book(res.rented)}</h5></div>
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
                    books_results.append(div)
                }


            }
        })
    } else {
        books_results.html('')
    }
}

// get ids of all books

function show_final_books(url, token, next_url) {
    let parentDiv = []
    $("#book_results_div > div").each((index, elem) => {
        parentDiv.push(elem.id);
    });
    let allowed_ids = parentDiv.slice(1,)

    $.post(url, {'results': allowed_ids, 'csrfmiddlewaretoken': token}, function (data, status) {
        location.replace(next_url);
    })

}

// register student courses
function register_courses(url_check, url_submit, token, std_id, next_url) {
    let choice_field = document.getElementById('choice').children
    const courses_id = Object.keys(choice_field).slice(2,).reduce((result, key) => {
        result[key] = choice_field[key].id;
        return result;
    }, {});

    // check for courses conflicts
    let check_conflicts;
    $.ajax({
        url: url_check,
        type: "POST",
        data: Object.assign({}, courses_id, {csrfmiddlewaretoken: token}),
        dataType: 'json',
        success: function (data) {
            check_conflicts = data[0]
            if (check_conflicts['status'] !== 'ok') {
                // there is conflict
                for (let id in check_conflicts['courses']) {
                    let id_num = check_conflicts['courses'][id];
                    $(`#${id_num}`).css('background-color', 'red');
                }
                let message = `دروس قرمز شده باهم تداخل دارند... لطفا بررسی کنید`
                alert(message)
            } else {
                // there is no conflict
                // submit courses
                for (let i in courses_id) {
                    let data = {
                        "score": null,
                        "course": Number(courses_id[i]),
                        "student": std_id,
                        csrfmiddlewaretoken: token
                    }
                    $.ajax({
                        url: url_submit,
                        type: "POST",
                        data: data,
                        dataType: 'json',
                        error: function (xhr, status, error) {
                            let message = 'در ثبت دروس مشکلی پیش آمده دوباره سعی کنید'
                            alert(message)
                        },
                        success: function (data) {
                            location.replace(next_url);
                        }
                    });


                }
            }
        }
    });


}