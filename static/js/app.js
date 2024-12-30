document.getElementById('predict-button').addEventListener('click', async () => {
    const area = document.getElementById('area').value;
    const location = document.getElementById('location').value;
    const bedrooms = document.getElementById('bedrooms').value;
    const bathrooms = document.getElementById('bathrooms').value;
    const yearsAhead = document.getElementById('years_ahead').value;

    const response = await fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ area, location, bedrooms, bathrooms, years_ahead: yearsAhead }),
    });

    const result = await response.json();
    document.getElementById('result').innerHTML = `
        <p><strong>Current Price:</strong> ${result.current_price}</p>
        <p><strong>Future Price:</strong> ${result.future_price}</p>
    `;
});
