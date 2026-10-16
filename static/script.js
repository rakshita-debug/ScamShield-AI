document.getElementById('checkBtn').addEventListener('click', async function() {
    const text = document.getElementById('messageInput').value;
    const url = document.getElementById('urlInput').value;
    const resultDiv = document.getElementById('result');

    if (!text.trim() && !url.trim()) {
        alert('Please enter message text, a URL, or both.');
        return;
    }

    resultDiv.classList.remove('hidden');
    document.getElementById('verdictText').innerText = 'Analyzing...';
    document.getElementById('scoreText').innerText = '-';
    document.getElementById('reasonsList').innerHTML = '';
    document.getElementById('disclaimerText').innerText = '';

    try {
        const response = await fetch('/analyze', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text: text, url: url })
        });

        const data = await response.json();
        
        if (response.ok) {
            document.getElementById('verdictText').innerText = data.verdict;
            document.getElementById('scoreText').innerText = data.score;
            
            const reasonsList = document.getElementById('reasonsList');
            data.reasons.forEach(reason => {
                const li = document.createElement('li');
                li.innerText = reason;
                reasonsList.appendChild(li);
            });

            document.getElementById('disclaimerText').innerText = data.disclaimer;
        } else {
            document.getElementById('verdictText').innerText = 'Error';
            document.getElementById('reasonsList').innerHTML = `<li>${data.error}</li>`;
        }
    } catch (error) {
        document.getElementById('verdictText').innerText = 'Connection Error';
    }
});