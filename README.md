<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Crypto Demo Platform</title>
<meta name="viewport" content="width=device-width, initial-scale=1">

<style>
body {
    margin:0;
    font-family:Arial;
    background:#0f172a;
    color:white;
}
header{
    padding:15px;
    background:#111827;
    text-align:center;
}
.balance{
    font-size:18px;
}
.container{
    padding:20px;
}
.card{
    background:#1e293b;
    padding:20px;
    border-radius:12px;
    margin-bottom:20px;
}
button{
    padding:10px 15px;
    border:none;
    border-radius:8px;
    cursor:pointer;
    margin:5px;
    font-weight:bold;
}
.buy{ background:#16a34a; color:white; }
.sell{ background:#dc2626; color:white; }
input{
    padding:8px;
    width:100%;
    margin:8px 0;
    border-radius:6px;
    border:none;
}
.trade{
    border-bottom:1px solid #334155;
    padding:6px 0;
}
</style>
</head>

<body>

<header>
    <h2>🚀 Crypto Demo</h2>
    <div class="balance">Balance: $<span id="balance">1000</span></div>
</header>

<div class="container">

<div class="card">
    <h3>BTC/USDT</h3>
    <h1>$<span id="price">0</span></h1>
    <input type="number" id="amount" placeholder="Amount ($)">
    <button class="buy" onclick="openTrade('BUY')">BUY</button>
    <button class="sell" onclick="openTrade('SELL')">SELL</button>
</div>

<div class="card">
    <h3>Open Trades</h3>
    <div id="trades"></div>
</div>

</div>

<script>
let balance = 1000;
let price = 30000;
let trades = [];

function updatePrice(){
    let change = (Math.random() - 0.5) * 200;
    price += change;
    document.getElementById("price").innerText = price.toFixed(2);
}
setInterval(updatePrice, 2000);
updatePrice();

function openTrade(type){
    let amount = parseFloat(document.getElementById("amount").value);
    if(!amount || amount > balance){
        alert("Invalid amount");
        return;
    }

    balance -= amount;
    document.getElementById("balance").innerText = balance.toFixed(2);

    trades.push({
        type:type,
        entry:price,
        amount:amount
    });

    renderTrades();
}

function renderTrades(){
    let container = document.getElementById("trades");
    container.innerHTML = "";

    trades.forEach((t,index)=>{
        let currentProfit = (price - t.entry) / t.entry * t.amount;
        if(t.type === "SELL"){
            currentProfit = -currentProfit;
        }

        let div = document.createElement("div");
        div.className="trade";
        div.innerHTML = `
        ${t.type} | Entry: $${t.entry.toFixed(2)} |
        P/L: $${currentProfit.toFixed(2)}
        <button onclick="closeTrade(${index})">Close</button>
        `;
        container.appendChild(div);
    });
}

function closeTrade(index){
    let t = trades[index];
    let profit = (price - t.entry) / t.entry * t.amount;
    if(t.type === "SELL"){
        profit = -profit;
    }

    balance += t.amount + profit;
    document.getElementById("balance").innerText = balance.toFixed(2);

    trades.splice(index,1);
    renderTrades();
}
</script>

</body>
</html>
