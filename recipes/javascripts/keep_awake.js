"use strict";
// https://www.educative.io/answers/how-to-keep-your-screen-awake-using-javascript
export class KeepAwake {
	constructor() {
		if ("wakeLock" in navigator) {
			$(function () {
				console.log("wake lock available");
			});
		} else {
			$(function () {
				console.log("wake lock unavailable");
			});
		}
	}
}