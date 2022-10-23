"use strict";

// https://www.educative.io/answers/how-to-keep-your-screen-awake-using-javascript
class KeepAwake {
	#checkboxSelector;
	#screenLock = null;

	constructor() {
		// Check feature availability
		if ("wakeLock" in navigator) {
			this.#createButton();
		}
	}

	#createButton() {
		$(() => {
			// Create checkbox and label
			$(`<form class="md-header__option">
				<input id="keepAwake" type="checkbox" />
				<label for="keepAwake">Keep Awake</label>
			</form>`).insertBefore($("header nav .md-header__option").first());
			this.#checkboxSelector = "header nav form.md-header__option input#keepAwake";
			// Browsers release wake lock on loss of visibility, low battery, etc
			// if screen lock was previously on, set it again
			$(document).on("visibilitychange", () => {
				if (this.#screenLock !== null && document.visibilityState === "visible") {
					this.#lockScreen();
				}
			});
			// On checkbox change
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
		// Attempt to wake lock
		try {
			navigator.wakeLock.request("screen").then((lock) => {
				this.#screenLock = lock;
				$(() => {
					$(this.#checkboxSelector).prop("checked", true);
				});
				// call back when system auto releases wake lock
				this.#screenLock.onrelease = () => {
					$(() => {
						$(this.#checkboxSelector).prop("checked", !this.#screenLock.released);
						if (this.#screenLock.released) {
							this.#screenLock = null;
						}
					});
				};
			});
		// Denied wake lock
		} catch (error) {
			console.error(error);
			this.#screenLock = null;
			$(() => {
				$(this.#checkboxSelector).prop("checked", false);
			});
		}
	}

	#unlockScreen() {
		// Make sure wake lock still retained
		if (typeof this.#screenLock !== "undefined" && this.#screenLock != null) {
			// Release wake lock
			this.#screenLock.release();
		}
	}
}

// Run code
new KeepAwake();