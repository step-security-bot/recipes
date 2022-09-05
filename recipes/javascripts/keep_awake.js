"use strict";
// https://www.educative.io/answers/how-to-keep-your-screen-awake-using-javascript
class KeepAwake {
	constructor() {
		if ("wakeLock" in navigator) {
			$(function () {
				console.log("wake lock available");
				$(`<form>
					<input id="keepAwake" type="checkbox" />
					<label for="keepAwake">Keep Awake</label>
				</form>`).insertBefore($("header nav .md-header__option").first());
			});
		} else {
			$(function () {
				console.log("wake lock unavailable");
			});
		}
	}
}

new KeepAwake();