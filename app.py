from flask import Flask, render_template, request, jsonify
import re
from urllib.parse import urlparse

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    message = data.get('text', '').strip()
    url = data.get('url', '').strip()
    
    combined_input = f"{message} {url}".lower()
    
    if not combined_input.strip():
        return jsonify({'error': 'Please provide text, a URL, or both.'}), 400

    score = 0
    reasons = []

    # 1. Check for Urgency & High-Pressure Words
    urgency_words = ['urgent', 'immediate', 'act now', 'expires', 'suspended', 'locked', 'verify now', 'action required']
    found_urgency = [w for w in urgency_words if w in combined_input]
    if found_urgency:
        score += 35
        reasons.append(f"Contains high-pressure/urgency wording: {', '.join(found_urgency)}")

    # 2. Check for Financial / Prize Lures
    lure_words = ['won', 'lottery', 'prize', 'bank', 'account', 'credit card', 'crypto', 'bonus', 'free cash']
    found_lures = [w for w in lure_words if w in combined_input]
    if found_lures:
        score += 30
        reasons.append(f"Contains financial or prize-related triggers: {', '.join(found_lures)}")

    # 3. URL & Phishing Indicators
    if url:
        parsed_url = urlparse(url if url.startswith('http') else 'http://' + url)
        domain = parsed_url.netloc or parsed_url.path
        
        # Check for URL shorteners
        shorteners = ['bit.ly', 'tinyurl.com', 't.co', 'ow.ly', 'goo.gl']
        if any(s in domain for s in shorteners):
            score += 25
            reasons.append("Uses a URL shortener which can hide the true destination.")
        
        # Check for IP address instead of domain
        if re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', domain):
            score += 40
            reasons.append("URL uses a raw IP address instead of a standard domain name.")
            
        # Check if HTTP instead of HTTPS
        if url.startswith('http://'):
            score += 10
            reasons.append("URL uses unencrypted HTTP instead of HTTPS.")

    # Cap score at 100
    score = min(score, 100)

    # 4. Determine Verdict Tier
    if score >= 60:
        verdict = "Likely Scam"
    elif score >= 25:
        verdict = "Needs Review"
    else:
        verdict = "Likely Safe"

    # 5. Required Disclaimer
    disclaimer = "Disclaimer: This tool provides heuristic-based analysis for educational purposes and is never 100% certain. Always verify independently."

    return jsonify({
        'verdict': verdict,
        'score': score,
        'reasons': reasons if reasons else ["No major high-risk indicators detected."],
        'disclaimer': disclaimer
    })

if __name__ == '__main__':
    app.run(debug=True)