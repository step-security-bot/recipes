"use strict";
// https://www.educative.io/answers/how-to-keep-your-screen-awake-using-javascript
if ("wakeLock" in navigator) {
	createButton();
}

function createButton() {
	$(() => {
		$(`<form class="md-header__option">
			<input id="keepAwake" type="checkbox" />
			<label for="keepAwake">Keep Awake</label>
		</form>`).insertBefore($("header nav .md-header__option").first());
		$('header nav .md-header__option form input#keepAwake[type="checkbox"]').change(() => {
			const ischecked = $(this).is(":checked");
			console.log(ischecked);
		});
	});
}

function buttonToggle() {
	
}