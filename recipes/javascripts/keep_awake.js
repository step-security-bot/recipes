"use strict";
// https://www.educative.io/answers/how-to-keep-your-screen-awake-using-javascript
class KeepAwake {
	constructor() {
		if ("wakeLock" in navigator) {
			$(function () {
				console.log("wake lock available");
			});
		}
	}
}