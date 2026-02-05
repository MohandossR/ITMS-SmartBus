async function fetchAI() {
    const res = await fetch("/ai/status");
    const data = await res.json();

    document.getElementById("driver").innerText = data.driver_status;
    document.getElementById("attention").innerText = data.attention_score + "%";
    document.getElementById("passengers").innerText = data.passenger_count;
    document.getElementById("seats").innerText = data.seat_vacancy;

    const alerts = document.getElementById("alerts");
    alerts.innerHTML = "";
    data.decisions.forEach(d => {
        alerts.innerHTML += `<li>${d}</li>`;
    });
}

setInterval(fetchAI, 2000);
fetchAI();
