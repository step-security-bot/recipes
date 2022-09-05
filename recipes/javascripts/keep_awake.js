"use strict";
// https://www.educative.io/answers/how-to-keep-your-screen-awake-using-javascript
class KeepAwake {
	constructor() {
		if ("wakeLock" in navigator) {
			this.#createButton();
		}
	}

	#createButton() {
		$(function () {
			const button = $(`<form class="md-header__option">
				<input id="keepAwake" type="checkbox" />
				<label for="keepAwake">Keep Awake</label>
			</form>`);
			button.insertBefore($("header nav .md-header__option").first());
			button.change(this.#buttonToggle());
		});
	}

	#buttonToggle() {
		$(function () {
			const ischecked = $(this).is(":checked");
			console.log(ischecked);
		});
	}
}

new KeepAwake();