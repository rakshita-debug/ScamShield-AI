const messageInput = document.getElementById("message");
const urlInput = document.getElementById("url");
const analyzeBtn = document.getElementById("analyzeBtn");
const inputError = document.getElementById("inputError");
const resultBox = document.getElementById("result");
const verdictText = document.getElementById("verdict");
const scoreText = document.getElementById("score");
const reasonsList = document.getElementById("reasons");

analyzeBtn.addEventListener("click", function () {
  const message = messageInput.value.trim();
  const url = urlInput.value.trim();

  inputError.textContent = "";
  resultBox.classList.add("hidden");

  if (!message && !url) {
    inputError.textContent =
      "Please enter a message, a URL, or both.";
    return;
  }

  const reasons = [];

  if (/\b(urgent|immediately|act now|within 24 hours)\b/i.test(message)) {
    reasons.push("Urgency wording detected in the message.");
  }

  if (/\b(password|otp|pin|bank details)\b/i.test(message)) {
    reasons.push("The message mentions sensitive information.");
  }

  if (url && !/^https?:\/\//i.test(url)) {
    reasons.push(
      "The URL does not start with HTTP or HTTPS. Check its format."
    );
  }

  if (url && /^http:\/\//i.test(url)) {
    reasons.push("The URL uses HTTP rather than encrypted HTTPS.");
  }

  if (reasons.length === 0) {
    reasons.push(
      "No demonstration warning rules were triggered. This does not establish that the input is safe."
    );
  }

  verdictText.textContent = "Needs Review";
  scoreText.textContent = "Risk score: Not available in demo mode";

  reasonsList.replaceChildren();

  reasons.forEach(function (reason) {
    const item = document.createElement("li");
    item.textContent = reason;
    reasonsList.appendChild(item);
  });

  resultBox.classList.remove("hidden");
});