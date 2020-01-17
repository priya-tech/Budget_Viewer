const view_date = $("#viewdate")

const budget_div = $('#replaceable-content')
//const endpoint = ['/budget/', '/budget/monthview', '/budget/yearview']
const endpoint = ['/budget/']
const endpoint1 = ['/budget/monthview']
const endpoint2 = ['/budget/yearview']

const delay_by_in_ms = 700
let scheduled_function = false

let ajax_call = function (endpoint, request_parameters) {
	$.getJSON(endpoint, request_parameters)
		.done(response => {
			// fade out the artists_div, then:
			budget_div.fadeTo('slow', 0).promise().then(() => {
				// replace the HTML contents
				budget_div.html(response['html_from_view'])
				// fade-in the div with new contents
				budget_div.fadeTo('slow', 1)
				// stop animating search icon
			})
		})
}



view_date.on('keyup', function () {

	const request_parameters = {
		viewdate: $(this).val() // value of user_input: the HTML element with ID user-input
	}

	// start animating the search icon with the CSS class

	// if scheduled_function is NOT false, cancel the execution of the function
	if (scheduled_function) {
		clearTimeout(scheduled_function)
	}

	// setTimeout returns the ID of the function to be executed
	scheduled_function = setTimeout(ajax_call, delay_by_in_ms, endpoint, request_parameters)
})
