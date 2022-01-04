let calc_button = document.querySelector("#calculate-button")
let L_result = document.querySelector("#L-result")
let LQ_result = document.querySelector("#LQ-result")
let W_result = document.querySelector("#W-result")
let WQ_result = document.querySelector("#WQ-result")
let rho_result = document.querySelector("#rho-result")
let PO_result = document.querySelector("#PO-result")
let PN_result = document.querySelector("#PN-result")
let mu_title = document.querySelector("#muTitle")
let unit = document.querySelectorAll(".unit")

let select = document.querySelector("#units")

function changeUnit() {
    console.log(select.value)
    unit[0].innerText = select.value
    unit[1].innerText = select.value
}
calc_button.addEventListener("click", async () => {
    let c = parseFloat(document.getElementById("c").value);
    let mu = parseFloat(document.getElementById("Mu").value);
    let lambda = parseFloat(document.getElementById("Lambda").value);
    let n = parseFloat(document.getElementById("n").value);

    if (isNaN(c) || isNaN(mu) || isNaN(lambda)) {
        alert("Please Fill All Required Field With Number");
    } else {
        await window.pywebview.api.calc(c, lambda, mu, n)
        L_result.innerText = `${await window.pywebview.api.getL()} Pelanggan`
        LQ_result.innerText = `${await window.pywebview.api.getLQ()} Pelanggan`
        W_result.innerText = `${await window.pywebview.api.getW()} ${select.value}`
        WQ_result.innerText = `${await window.pywebview.api.getWQ()} ${select.value}`
        rho_result.innerText = await window.pywebview.api.getRho()
        PO_result.innerText = await window.pywebview.api.getP0()
        PN_result.innerText = await window.pywebview.api.getPN()
    }
})
