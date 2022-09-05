"use strict";
// https://www.educative.io/answers/how-to-keep-your-screen-awake-using-javascript
class KeepAwake {
	#checkboxSelector = "header nav form.md-header__option input#keepAwake";
	#screenlock;
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
			$(document).on("visibilitychange", () => {
				if (screenLock !== null && document.visibilityState === 'visible') {
					this.#lockScreen();
				}
			});
			$(this.#checkboxSelector).change(() => {
				$(() => {
					const ischecked = $(this.#checkboxSelector).prop("checked");
					console.log(ischecked);
					if (ischecked) {
						this.#lockScreen();
					} else {
						this.#unlockScreen();
					}
				});
			});
		});
	}

	#lockScreen() {
		try {
			navigator.wakeLock.request("screen").then((lock) => {
				this.#screenlock = lock;
				$(() => {
					$(this.#checkboxSelector).prop("checked", true);
				});
			});
		} catch (error) {
			console.error(error);
			$(() => {
				$(this.#checkboxSelector).prop("checked", false);
			});
		}
	}

	#unlockScreen() {
		if (typeof screenLock !== "undefined" && screenLock != null) {
			this.#screenLock.release().then(() => {
				this.#screenLock = null;
				$(() => {
					$(this.#checkboxSelector).prop("checked", false);
				});
			});
		} else {
			console.error(screenLock);
			$(() => {
				$(this.#checkboxSelector).prop("checked", false);
			});
		}
	}
}

new KeepAwake();