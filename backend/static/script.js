async function fetchAIStatus() {
    try {
        const res = await fetch("http://127.0.0.1:5000/ai/status");
        const data = await res.json();
        const statusEl = document.getElementById("driverStatus");

        if (data.driver_status === "ALERT") {
            statusEl.style.color = "#00ff88";
        } else if (data.driver_status?.includes("DROWSY")) {
            statusEl.style.color = "orange";    
        } else {
            statusEl.style.color = "red";
        }
        document.getElementById("driverStatus").innerText =
            data.driver_status || "Waiting...";

        document.getElementById("passengerCount").innerText =
            data.passenger_count ?? "---";

        document.getElementById("seatVacancy").innerText =
            data.seat_vacancy ?? "---";

        const attention = data.attention_score || 0;
        const bar = document.getElementById("attentionBar");
        bar.style.width = attention + "%";

        if (attention > 70) bar.style.background = "green";
        else if (attention > 40) bar.style.background = "orange";
        else bar.style.background = "red";

        const list = document.getElementById("decisions");
        list.innerHTML = "";

        if (data.decisions && data.decisions.length > 0) {
            data.decisions.forEach(d => {
                const li = document.createElement("li");
                li.innerText = d;
                list.appendChild(li);
            });
        } else {
            list.innerHTML = "<li>No alerts</li>";
        }

    } catch (err) {
        console.error("Error fetching AI status:", err);
    }
}

setInterval(fetchAIStatus, 2000);
fetchAIStatus();
