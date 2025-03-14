document.addEventListener("DOMContentLoaded", function () {
  const scoreInput = document.getElementById("score");
  const priorityDisplay = document.getElementById("priority");

  if (scoreInput) {
      scoreInput.addEventListener("input", function () {
          const score = parseInt(scoreInput.value) || 0;
          let priority = "Low";

          if (score >= 80) {
              priority = "High";
          } else if (score >= 50) {
              priority = "Medium";
          }

          if (priorityDisplay) {
              priorityDisplay.textContent = `Priority: ${priority}`;
          }
      });
  }
});
