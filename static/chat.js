
document.getElementById('negotiation-form').onsubmit = async (e) => {
    e.preventDefault();
    const buyerOffer = document.getElementById('buyer-offer').value.split(',').map(Number);

    const response = await fetch('/negotiate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ buyer_offer: buyerOffer })
    });

    const data = await response.json();
    document.getElementById('results').innerText = JSON.stringify(data.negotiation_results, null, 2);
};
