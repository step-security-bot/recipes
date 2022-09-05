"use strict";
// https://www.educative.io/answers/how-to-keep-your-screen-awake-using-javascript
class KeepAwake {
	#checkboxSelector = "header nav form.md-header__option input#keepAwake";
	constructor() {
		if ("wakeLock" in navigator) {
			this.#createButton();
		}
	}

	#createButton() {
		$(() => {
			$(`<form class="md-header__option">
				<input id="keepAwake" type="checkbox" />
				<label for="keepAwake">Keep Awake</label>
			</form>`).insertBefore($("header nav .md-header__option").first());
			$(this.#checkboxSelector).change(this.#buttonToggle());
		});
	}

	#buttonToggle() {
		$(() => {
			const ischecked = $(this.#checkboxSelector).prop("checked");
			console.log(ischecked);
		})
	}
}

new KeepAwake();