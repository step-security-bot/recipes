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
			const checked1 = $(this).is(":checked");
			const checked2 = $(this).prop("checked");
			const checked3 = $(checkboxSelector).is(":checked");
			const checked4 = $(checkboxSelector).prop("checked");
			console.log(checked1, checked2, checked3, checked4);
		});
	});
}