"use strict";
// https://www.educative.io/answers/how-to-keep-your-screen-awake-using-javascript
class KeepAwake {
	constructor() {
		if ("wakeLock" in navigator) {
			$(function () {
				$(`<form>
					<input id="keepAwake" type="checkbox" />
					<label for="keepAwake">Keep Awake</label>
				</form>`).insertBefore($("header nav .md-header__option").first());
			});
		}
	}
}

new KeepAwake();