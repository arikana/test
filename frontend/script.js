const form = document.getElementById('menu-form');

form.addEventListener('submit', async (event) => {
    event.preventDefault();
    const budget = document.getElementById('budget').value;

    try {
        const response = await fetch('https://my-flask-app.up.railway.app/recommend', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ budget: parseInt(budget) }),
        });

        const data = await response.json();
        document.getElementById('result').textContent = `추천 메뉴: ${data.name} (${data.price}원)`;
    } catch (error) {
        document.getElementById('result').textContent = '서버에 연결할 수 없습니다. 다시 시도해주세요.';
        console.error('Error:', error);
    }
});
