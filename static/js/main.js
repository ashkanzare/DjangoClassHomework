function select(id, bool) {
    if (bool === true) {
        let course = $('#'+id).remove()
        course.attr('onclick', `select(${id}, false)`)
        $('#choice').append(course)


    }
    else {
        let course = $('#'+id).remove()
        course.attr('onclick', `select(${id}, true)`)
        $('#suggest').append(course)
    }
}