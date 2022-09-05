"use strict";
// https://www.educative.io/answers/how-to-keep-your-screen-awake-using-javascript
class KeepAwake {
	#checkboxSelector = "header nav form.md-header__option input#keepAwake";
	#screenLock;
	constructor() {
		// Create as disabled, enable on function availability
		$(() => {
			$(`<form class="md-header__option">
				<input id="keepAwake" type="checkbox" disabled />
				<label for="keepAwake">Keep Awake</label>
			</form>`).insertBefore($("header nav .md-header__option").first());
		});
		// Check feature availability
		if ("wakeLock" in navigator) {
			this.#setupButton();
		}
	}

	#setupButton() {
		$(() => {
			// Enable
			$(this.#checkboxSelector).prop("disabled", false);
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
					this.#screenLock = null;
					$(() => {
						$(this.#checkboxSelector).prop("checked", false);
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
			this.#screenLock.release().then(() => {
				this.#screenLock = null;
				$(() => {
					$(this.#checkboxSelector).prop("checked", false);
				});
			});
		// Wake lock lost somehow, just drop it all
		} else {
			console.error(screenLock);
			this.#screenLock = null;
			$(() => {
				$(this.#checkboxSelector).prop("checked", false);
			});
		}
	}
}

// Run code
new KeepAwake();