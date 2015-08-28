$(function() {
  $('.tasks_tabs a').click(function (e) {
    e.preventDefault()
    $(this).tab('show')
  })

  $('.tab-pane:first, li:first, .tasks_tabs a:first').addClass('active')
})

