// Navigation
function goToDashboard() {
    window.location.href = "dashboard.html";
}

function goToMedicalInfo() {
    window.location.href = "medical_info.html";
}

function goToLogin() {
    window.location.href = "login.html";
}

function registerUser() {
    alert("Registration successful. Redirecting to login...");
    window.location.href = "login.html";
}

// Medical Info Save (TC03 Logic)
function saveMedicalInfo() {
    const weight = Number(document.getElementById("weight").value);
    const ft = document.getElementById("heightFt").value;
    const inch = document.getElementById("heightIn").value;
    const age = Number(document.getElementById("age").value);
    const msg = document.getElementById("msg");

    // TC03 Condition
    if (weight <= 0) {
        msg.innerText = "Error: Weight must be greater than 0.";
        return;
    }

    // Height validation
    if (ft === "" || inch === "") {
        msg.innerText = "Error: Height fields cannot be empty.";
        return;
    }

    // Age validation
    if (!(age > 0 && age < 120)) {
        msg.innerText = "Error: Age must be between 1 and 119.";
        return;
    }

    // If valid, store info
    const data = {
        weight: weight,
        heightFt: ft,
        heightIn: inch,
        age: age
    };

    localStorage.setItem("medicalInfo", JSON.stringify(data));

    msg.innerText = "Information saved successfully.";
}
