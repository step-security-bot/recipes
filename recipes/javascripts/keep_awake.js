"use strict";
// https://www.educative.io/answers/how-to-keep-your-screen-awake-using-javascript
if ("wakeLock" in navigator) {
	createButton();
}

const checkboxSelector = "header nav form.md-header__option input#keepAwake";

function createButton() {
	$(() => {
		$(`<form class="md-header__option">
			<input id="keepAwake" type="checkbox" />
			<label for="keepAwake">Keep Awake</label>
		</form>`).insertBefore($("header nav .md-header__option").first());
		$(checkboxSelector).change(() => {
			const ischecked = $(this).is(":checked");
			console.log(ischecked);
		});
	});
}