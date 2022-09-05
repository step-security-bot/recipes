"use strict";
// https://www.educative.io/answers/how-to-keep-your-screen-awake-using-javascript
if ("wakeLock" in navigator) {
	createButton();
}

function createButton() {
	$(() => {
		const form = $(`<form class="md-header__option"></form>`);
		const label = $(`<input id="keepAwake" type="checkbox" />`);
		const input = $(`<input id="keepAwake" type="checkbox" />`);
		form.append(label);
		form.append(input);
		form.insertBefore($("header nav .md-header__option").first());
		input.change(() => {
			const ischecked = $(this).prop("checked");
			console.log(ischecked);
		});
	});
}