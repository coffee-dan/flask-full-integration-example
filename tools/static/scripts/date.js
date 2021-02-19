//
const getDateButton = document.getElementById("getDateButton");
const dateText = document.getElementById("date");
const image = document.getElementById("kek");

getDateButton.addEventListener("click", () => {
	console.log("button pressed");

	dateText.innerHTML = Date();
	image.style.display = "block";
});
