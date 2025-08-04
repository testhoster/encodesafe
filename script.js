function login() {
  const user = document.getElementById("username").value;
  const pass = document.getElementById("password").value;
  if (user === "admin" && pass === "darksecrets") {
    document.getElementById("loginBox").style.display = "none";
    document.getElementById("mainBox").style.display = "block";
  } else {
    alert("Invalid credentials");
  }
}

async function encodeText() {
  const message = document.getElementById("inputText").value;
  const key = document.getElementById("encryptionKey").value;

  if (!message || !key) {
    alert("Please enter both message and key.");
    return;
  }

  try {
    const res = await fetch('/encode', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message, key })
    });

    const data = await res.json();

    if (data.error) {
      document.getElementById("outputArea").innerText = `Error: ${data.error}`;
    } else {
      document.getElementById("outputArea").innerText =
        `ENCODED:\n${data.encoded}\n\nHASH:\n${data.hash}\n\nENCRYPTED:\n${data.encrypted}`;
    }
  } catch (err) {
    document.getElementById("outputArea").innerText = `Error encoding: ${err}`;
  }
}

async function decodeText() {
  const wrapped = document.getElementById("inputText").value.trim();
  const key = document.getElementById("encryptionKey").value.trim();

  if (!wrapped) {
    alert("Please provide text to decode.");
    return;
  }

  try {
    const res = await fetch('/decode', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ wrapped, key })
    });

    const data = await res.json();

    if (data.result) {
      document.getElementById("outputArea").innerText = data.result;
    } else if (data.error) {
      document.getElementById("outputArea").innerText = `Error: ${data.error}`;
    } else {
      document.getElementById("outputArea").innerText = `[Decode error: Unknown response]`;
    }
  } catch (err) {
    document.getElementById("outputArea").innerText = `[Decode error: ${err}]`;
  }
}

