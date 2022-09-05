"use strict";
// https://www.educative.io/answers/how-to-keep-your-screen-awake-using-javascript
class KeepAwake {
	#checkboxSelector = "header nav form.md-header__option input#keepAwake";
	#screenLock;
	constructor() {
		$(() => {
			$(`<form class="md-header__option">
				<input id="keepAwake" type="checkbox" disabled />
				<label for="keepAwake">Keep Awake</label>
			</form>`).insertBefore($("header nav .md-header__option").first());
		});
		if ("wakeLock" in navigator) {
			this.#setupButton();
		}
	}

	#setupButton() {
		$(() => {
			$(this.#checkboxSelector).prop("disabled", false);
			$(document).on("visibilitychange", () => {
				if (this.#screenLock !== null && document.visibilityState === "visible") {
					this.#lockScreen();
				}
			});
			$(this.#checkboxSelector).change(() => {
				$(() => {
					const ischecked = $(this.#checkboxSelector).prop("checked");
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
				this.#screenLock = lock;
				$(() => {
					$(this.#checkboxSelector).prop("checked", true);
				});
				this.#screenLock.onrelease = () => {
					this.#screenLock = null;
					$(() => {
						$(this.#checkboxSelector).prop("checked", false);
					});
				};
			});
		} catch (error) {
			console.error(error);
			this.#screenLock = null;
			$(() => {
				$(this.#checkboxSelector).prop("checked", false);
			});
		}
	}

	#unlockScreen() {
		if (typeof this.#screenLock !== "undefined" && this.#screenLock != null) {
			this.#screenLock.release().then(() => {
				this.#screenLock = null;
				$(() => {
					$(this.#checkboxSelector).prop("checked", false);
				});
			});
		} else {
			console.error(screenLock);
			this.#screenLock = null;
			$(() => {
				$(this.#checkboxSelector).prop("checked", false);
			});
		}
	}
}

new KeepAwake();