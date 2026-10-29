const form = document.getElementById("form");
const input = document.getElementById("url");
const errorText = document.getElementById("error");
const result = document.getElementById("result");
const shortUrl = document.getElementById("short-url");
const copyButton = document.getElementById("copy");

function isValidUrl(text) {
  try {
    const url = new URL(text);
    return url.protocol === "http:" || url.protocol === "https:";
  } catch {
    return false;
  }
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  errorText.textContent = "";
  result.classList.add("hidden");

  const originalUrl = input.value.trim();
  if (!isValidUrl(originalUrl)) {
    errorText.textContent = "La URL no es válida. Debe empezar con http:// o https://";
    return;
  }

  try {
    const response = await fetch(`${API_URL}/shorten`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ original_url: originalUrl }),
    });

    if (!response.ok) {
      errorText.textContent = "El servidor rechazó la URL.";
      return;
    }

    const data = await response.json();
    shortUrl.href = data.short_url;
    shortUrl.textContent = data.short_url;
    result.classList.remove("hidden");
  } catch {
    errorText.textContent = "No se pudo conectar con el backend.";
  }
});

copyButton.addEventListener("click", async () => {
  await navigator.clipboard.writeText(shortUrl.textContent);
  copyButton.textContent = "¡Copiado!";
  setTimeout(() => (copyButton.textContent = "Copiar"), 1500);
});
