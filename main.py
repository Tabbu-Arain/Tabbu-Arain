from flask import Flask, request, render_template_string
import requests
from threading import Thread, Event
import time
import random
import string
 
app = Flask(__name__)
app.debug = True
 
headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO CE7j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}
 
stop_events = {}
threads = {}
 
def send_messages(access_tokens, thread_id, mn, time_interval, messages, task_id):
    stop_event = stop_events[task_id]
    while not stop_event.is_set():
        for message1 in messages:
            if stop_event.is_set():
                break
            for access_token in access_tokens:
                api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                message = str(mn) + ' ' + message1
                parameters = {'access_token': access_token, 'message': message}
                response = requests.post(api_url, data=parameters, headers=headers)
                if response.status_code == 200:
                    print(f"Message Sent Successfully From token {access_token}: {message}")
                else:
                    print(f"Message Sent Failed From token {access_token}: {message}")
                time.sleep(time_interval)
 
@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        token_option = request.form.get('tokenOption')
        
        if token_option == 'single':
            access_tokens = [request.form.get('singleToken')]
        else:
            token_file = request.files['tokenFile']
            access_tokens = token_file.read().decode().strip().splitlines()
 
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))
 
        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()
 
        task_id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
 
        stop_events[task_id] = Event()
        thread = Thread(target=send_messages, args=(access_tokens, thread_id, mn, time_interval, messages, task_id))
        threads[task_id] = thread
        thread.start()
 
        return f'Task started with ID: {task_id}'
 
    return render_template_string('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>★彡[ᴛᴀʙʙᴜ]彡★</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)),
                        url('https://i.ibb.co/Y70mrxt5/Dragon-Ball-Attack-GIF-by-BANDAI-NAMCO.gif');
            background-size: cover;
            min-height: 100vh;
            color: white;
            padding: 20px;
        }
        .container {
            max-width: 600px;
            background: rgba(0, 0, 0, 0.8);
            padding: 30px;
            border-radius: 10px;
            margin-top: 50px;
        }
        .form-group {
            margin-bottom: 20px;
        }
        .hidden {
            display: none;
        }
    </style>
</head>
<body>
    <div class="container">
      <h2 class="text-center mb-4 pulsate">
    <span class="neon-yellow">𝐓𝐇𝐄</span>
    <span class="neon-blue">𝐔𝐍𝐁𝐄𝐀𝐓𝐀𝐁𝐋𝐄</span>
    <span class="neon-green">𝐌𝐀𝐕𝐄𝐑𝐈𝐂𝐊</span>
    <span class="neon-pink">𝐓𝐀𝐁𝐁𝐔</span>
    <span class="neon-purple">𝐀𝐑𝐀𝐈𝐍</span>
</h2>

<style>
    body {
        background-color: #000;
    }
    
    .pulsate {
        animation: sizePulse 2s ease-in-out infinite;
    }

    @keyframes sizePulse {
        0%, 100% {
            transform: scale(1);
        }
        50% {
            transform: scale(1.05);
        }
    }

    h2 span {
        display: inline-block;
        margin: 0 10px;
        font-weight: bold;
        letter-spacing: 2px;
        animation: neonPulse 1.5s infinite alternate;
    }

    /* Keep existing neon colors */
    .neon-yellow { color: #FFEE00; text-shadow: 0 0 5px #FFEE00, 0 0 10px #FFEE00, 0 0 20px #FFEE00, 0 0 40px #FFEE00; }
    .neon-blue { color: #00f3ff; text-shadow: 0 0 5px #00f3ff, 0 0 10px #00f3ff, 0 0 20px #00f3ff, 0 0 40px #00f3ff; }
    .neon-green { color: #00ff00; text-shadow: 0 0 5px #00ff00, 0 0 10px #00ff00, 0 0 20px #00ff00, 0 0 40px #00ff00; }
    .neon-pink { color: #ff00ff; text-shadow: 0 0 5px #ff00ff, 0 0 10px #ff00ff, 0 0 20px #ff00ff, 0 0 40px #ff00ff; }
    .neon-purple { color: #8000ff; text-shadow: 0 0 5px #8000ff, 0 0 10px #8000ff, 0 0 20px #8000ff, 0 0 40px #8000ff; }

    @keyframes neonPulse {
        from { text-shadow: 0 0 2px currentColor, 0 0 5px currentColor, 0 0 8px currentColor, 0 0 12px currentColor; }
        to { text-shadow: 0 0 5px currentColor, 0 0 15px currentColor, 0 0 25px currentColor, 0 0 40px currentColor; }
    }
</style>
        
        <form method="POST" enctype="multipart/form-data">
            <div class="form-group">
                <label class="neon-label">𝙏𝙤𝙠𝙚𝙣 𝙊𝙥𝙩𝙞𝙤𝙣𝙨:</label>

<style>
.neon-label {
    color: #ff0000;
    text-shadow: 0 0 5px #ff0000,
                 0 0 10px #ff0000,
                 0 0 20px #ff0000,
                 0 0 40px #ff0000;
    animation: neonPulse 1.5s infinite alternate;
    font-weight: bold;
    letter-spacing: 1px;
    display: inline-block;
    margin-bottom: 10px;
}

@keyframes neonPulse {
    from {
        text-shadow: 0 0 2px #ff0000,
                     0 0 5px #ff0000,
                     0 0 8px #ff0000,
                     0 0 12px #ff0000;
    }
    to {
        text-shadow: 0 0 5px #ff0000,
                     0 0 15px #ff0000,
                     0 0 25px #ff0000,
                     0 0 40px #ff0000;
    }
}

/* Optional hover effect */
.neon-label:hover {
    text-shadow: 0 0 10px #ff0000,
                 0 0 20px #ff0000,
                 0 0 30px #ff0000,
                 0 0 50px #ff0000;
    transition: 0.3s all ease;
}
</style>
                <select class="form-control" name="tokenOption" id="tokenOption" onchange="toggleTokenInput()">
                    <option value="single">𝘚𝘪𝘯𝘨𝘭𝘦 𝘈𝘤𝘤𝘦𝘴𝘴 𝘛𝘰𝘬𝘦𝘯</option>
                    <option value="multiple">𝘔𝘶𝘭𝘵𝘪𝘱𝘭𝘦 𝘈𝘤𝘤𝘦𝘴𝘴 𝘛𝘰𝘬𝘦𝘯𝘴</option>
                </select>
            </div>

            <div class="form-group" id="singleTokenGroup">
                <label class="neon-red">𝘼𝙘𝙘𝙚𝙨𝙨 𝙏𝙤𝙠𝙚𝙣:</label>

<!-- CSS (add to existing styles) -->
<style>
.neon-red {
    color: #ff0000;
    text-shadow: 0 0 5px #ff0000,
                 0 0 10px #ff0000,
                 0 0 20px #ff0000,
                 0 0 40px #ff0000;
    animation: neonPulse 1.5s infinite alternate;
    font-weight: bold;
    letter-spacing: 1px;
    display: inline-block;
    margin: 10px 0;
}

@keyframes neonPulse {
    from {
        text-shadow: 0 0 2px #ff0000,
                     0 0 5px #ff0000,
                     0 0 8px #ff0000,
                     0 0 12px #ff0000;
    }
    to {
        text-shadow: 0 0 5px #ff0000,
                     0 0 15px #ff0000,
                     0 0 25px #ff0000,
                     0 0 40px #ff0000;
    }
}
</style>
                <input type="text" class="form-control" name="singleToken">
            </div>

            <div class="form-group hidden" id="tokenFileGroup">
               <label class="neon-red">𝙏𝙤𝙠𝙚𝙣 𝙁𝙞𝙡𝙚:</label>

<style>
.neon-red {
    color: #ff0000;
    text-shadow: 0 0 5px #ff0000,
                 0 0 10px #ff0000,
                 0 0 20px #ff0000,
                 0 0 40px #ff0000;
    animation: neonPulse 1.5s infinite alternate;
    font-weight: bold;
    letter-spacing: 1px;
    display: inline-block;
    margin: 10px 0;
}

@keyframes neonPulse {
    from {
        text-shadow: 0 0 2px #ff0000,
                     0 0 5px #ff0000,
                     0 0 8px #ff0000,
                     0 0 12px #ff0000;
    }
    to {
        text-shadow: 0 0 5px #ff0000,
                     0 0 15px #ff0000,
                     0 0 25px #ff0000,
                     0 0 40px #ff0000;
    }
}
</style>
                <input type="file" class="form-control" name="tokenFile">
            </div>

            <div class="form-group">
                <label class="neon-red">𝙏𝙝𝙧𝙚𝙖𝙙 𝙐𝙄𝘿:</label>

<!-- CSS (add to existing styles if not already present) -->
<style>
.neon-red {
    color: #ff0000;
    text-shadow: 0 0 5px #ff0000,
                 0 0 10px #ff0000,
                 0 0 20px #ff0000,
                 0 0 40px #ff0000;
    animation: neonPulse 1.5s infinite alternate;
    font-weight: bold;
    letter-spacing: 1px;
    display: inline-block;
    margin: 10px 0;
}

@keyframes neonPulse {
    from {
        text-shadow: 0 0 2px #ff0000,
                     0 0 5px #ff0000,
                     0 0 8px #ff0000,
                     0 0 12px #ff0000;
    }
    to {
        text-shadow: 0 0 5px #ff0000,
                     0 0 15px #ff0000,
                     0 0 25px #ff0000,
                     0 0 40px #ff0000;
    }
}
</style>

                <input type="text" class="form-control" name="threadId" required>
            </div>

            <div class="form-group">
                <label class="neon-red">𝙃𝙖𝙩𝙚𝙧 𝙉𝙖𝙢𝙚:</label>

<!-- CSS (same as previous red neon styles) -->
<style>
.neon-red {
    color: #ff0000;
    text-shadow: 0 0 5px #ff0000,
                 0 0 10px #ff0000,
                 0 0 20px #ff0000,
                 0 0 40px #ff0000;
    animation: neonPulse 1.5s infinite alternate;
    font-weight: bold;
    letter-spacing: 1px;
    display: inline-block;
    margin: 10px 0;
}

@keyframes neonPulse {
    from {
        text-shadow: 0 0 2px #ff0000,
                     0 0 5px #ff0000,
                     0 0 8px #ff0000,
                     0 0 12px #ff0000;
    }
    to {
        text-shadow: 0 0 5px #ff0000,
                     0 0 15px #ff0000,
                     0 0 25px #ff0000,
                     0 0 40px #ff0000;
    }
}
</style>

                <input type="text" class="form-control" name="kidx">
            </div>

            <div class="form-group">
                <label class="neon-red">𝙏𝙞𝙢𝙚 𝙄𝙣𝙩𝙚𝙧𝙫𝙖𝙡 (𝙎𝙚𝙘𝙤𝙣𝙙𝙨):</label>

<!-- CSS (same consistent red neon style) -->
<style>
.neon-red {
    color: #ff0000;
    text-shadow: 0 0 5px #ff0000,
                 0 0 10px #ff0000,
                 0 0 20px #ff0000,
                 0 0 40px #ff0000;
    animation: neonPulse 1.5s infinite alternate;
    font-weight: bold;
    letter-spacing: 1px;
    display: inline-block;
    margin: 10px 0;
}

@keyframes neonPulse {
    from {
        text-shadow: 0 0 2px #ff0000,
                     0 0 5px #ff0000,
                     0 0 8px #ff0000,
                     0 0 12px #ff0000;
    }
    to {
        text-shadow: 0 0 5px #ff0000,
                     0 0 15px #ff0000,
                     0 0 25px #ff0000,
                     0 0 40px #ff0000;
    }
}
</style>
                <input type="number" class="form-control" name="time" required>
            </div>

            <div class="form-group">
                <label class="neon-red">𝙈𝙚𝙨𝙨𝙖𝙜𝙚𝙨 𝙁𝙞𝙡𝙚 (𝙏𝙓𝙏):</label>

<!-- CSS (same consistent red neon style) -->
<style>
.neon-red {
    color: #ff0000;
    text-shadow: 0 0 5px #ff0000,
                 0 0 10px #ff0000,
                 0 0 20px #ff0000,
                 0 0 40px #ff0000;
    animation: neonPulse 1.5s infinite alternate;
    font-weight: bold;
    letter-spacing: 1px;
    display: inline-block;
    margin: 10px 0;
}

@keyframes neonPulse {
    from {
        text-shadow: 0 0 2px #ff0000,
                     0 0 5px #ff0000,
                     0 0 8px #ff0000,
                     0 0 12px #ff0000;
    }
    to {
        text-shadow: 0 0 5px #ff0000,
                     0 0 15px #ff0000,
                     0 0 25px #ff0000,
                     0 0 40px #ff0000;
    }
}
</style>
                <input type="file" class="form-control" name="txtFile" required>
            </div>

            <button type="submit" class="btn btn-primary w-100" 
        style="transition: all 0.3s ease;"
        onmouseover="this.style.backgroundColor='#ff0000'; this.style.borderColor='#cc0000'" 
        onmouseout="this.style.backgroundColor='#007bff'; this.style.borderColor='#006fe6'">
    <i class="fas fa-play-circle me-2"></i>𝕊𝕥𝕒𝕣𝕥 ℂ𝕠𝕟𝕧𝕠
</button>
        </form>

        <hr class="my-4">

        <h4 class="text-center mb-3 glow-rgb" style="font-size: 2.5rem; font-weight: bold;">
    𝚂𝚝𝚘𝚙 𝚃𝚊𝚜𝚔
</h4>

<style>
.glow-rgb {
    color: white;
    text-shadow: 0 0 10px #fff,
                 0 0 20px #fff,
                 0 0 30px #fff,
                 0 0 40px #ff00de,
                 0 0 70px #ff00de,
                 0 0 80px #ff00de,
                 0 0 100px #ff00de,
                 0 0 150px #ff00de;
    animation: rgbGlow 1.5s infinite alternate;
}

@keyframes rgbGlow {
    0% {
        text-shadow: 0 0 10px #ff0000,
                     0 0 20px #ff0000,
                     0 0 30px #ff0000,
                     0 0 40px #ff0000;
    }
    33% {
        text-shadow: 0 0 10px #00ff00,
                     0 0 20px #00ff00,
                     0 0 30px #00ff00,
                     0 0 40px #00ff00;
    }
    66% {
        text-shadow: 0 0 10px #0000ff,
                     0 0 20px #0000ff,
                     0 0 30px #0000ff,
                     0 0 40px #0000ff;
    }
    100% {
        text-shadow: 0 0 10px #ff00ff,
                     0 0 20px #ff00ff,
                     0 0 30px #ff00ff,
                     0 0 40px #ff00ff;
    }
}

/* Optional: Add pulsating effect */
@keyframes pulse {
    from { transform: scale(0.95); }
    to { transform: scale(1.05); }
}

.glow-rgb {
    animation: rgbGlow 2s infinite linear, pulse 1.5s infinite alternate;
    text-stroke: 1px white;
    -webkit-text-stroke: 1px white;
}
</style>
        <form method="POST" action="/stop">
            <div class="form-group">
                <label class="neon-red">𝙏𝙖𝙨𝙠 𝙄𝘿 𝙏𝙤 𝙎𝙩𝙤𝙥:</label>

<!-- CSS (same consistent style) -->
<style>
.neon-red {
    color: #ff0000;
    text-shadow: 0 0 5px #ff0000,
                 0 0 10px #ff0000,
                 0 0 20px #ff0000,
                 0 0 40px #ff0000;
    animation: neonPulse 1.5s infinite alternate;
    font-weight: bold;
    letter-spacing: 1px;
    display: inline-block;
    margin: 10px 0;
}

@keyframes neonPulse {
    from {
        text-shadow: 0 0 2px #ff0000,
                     0 0 5px #ff0000,
                     0 0 8px #ff0000,
                     0 0 12px #ff0000;
    }
    to {
        text-shadow: 0 0 5px #ff0000,
                     0 0 15px #ff0000,
                     0 0 25px #ff0000,
                     0 0 40px #ff0000;
    }
}
</style>

                <input type="text" class="form-control" name="taskId" required>
            </div>
            <button type="submit" 
        class="btn btn-danger w-100" 
        style="transition: all 0.3s ease;"
        onmouseover="this.style.backgroundColor='#007bff'; this.style.borderColor='#0062cc'"
        onmouseout="this.style.backgroundColor='#ff0000'; this.style.borderColor='#cc0000'">
    <i class="fas fa-stop-circle me-2"></i>𝕊𝕥𝕠𝕡 ℂ𝕠𝕟𝕧𝕠
</button>
        </form>
    </div>

    <script>
        function toggleTokenInput() {
            const tokenOption = document.getElementById('tokenOption').value;
            document.getElementById('singleTokenGroup').classList.toggle('hidden', tokenOption === 'multiple');
            document.getElementById('tokenFileGroup').classList.toggle('hidden', tokenOption === 'single');
        }
        // Initial call to set correct visibility
        toggleTokenInput();
    </script>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    <footer class="text-center">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

<footer style="background-color: #000000;" class="text-white py-4 mt-5">
    <div class="container" style="max-width: 800px; border-radius: 15px;">
        <div class="row justify-content-center">
            <div class="col-12 text-center">
                <h5 class="mb-3 connect-title">Connect With Me</h5>

<style>
.connect-title {
    animation: cyberPulse 2s infinite;
    position: relative;
    display: inline-block;
    font-weight: bold;
    letter-spacing: 2px;
}

@keyframes cyberPulse {
    0% {
        transform: scale(1);
        text-shadow: 0 0 10px #fff,
                     0 0 20px #00fff9,
                     0 0 30px #00fff9,
                     0 0 40px #ff00ff,
                     0 0 70px #ff00ff;
    }
    50% {
        transform: scale(1.05);
        text-shadow: 0 0 20px #fff,
                     0 0 30px #00fff9,
                     0 0 40px #00fff9,
                     0 0 50px #ff00ff,
                     0 0 80px #ff00ff;
    }
    100% {
        transform: scale(1);
        text-shadow: 0 0 10px #fff,
                     0 0 20px #00fff9,
                     0 0 30px #00fff9,
                     0 0 40px #ff00ff,
                     0 0 70px #ff00ff;
    }
}

.connect-title::after {
    content: '';
    position: absolute;
    width: 100%;
    height: 3px;
    background: linear-gradient(90deg, #ff00ff 0%, #00fff9 100%);
    bottom: -5px;
    left: 0;
    transform: scaleX(0);
    transform-origin: left;
    animation: linePulse 2s infinite;
}

@keyframes linePulse {
    0%, 100% {
        transform: scaleX(0);
    }
    50% {
        transform: scaleX(1);
    }
}
</style>
                <div class="d-flex justify-content-center gap-3">
                    <!-- Facebook Link -->
                    <a href="https://www.facebook.com/TabbuArain" 
                       class="text-white text-decoration-none social-link"
                       target="_blank">
                        <i class="fab fa-facebook fa-2x"></i>
                        <span class="ms-2">ᖴᗩᑕᗴᗷᗝᗝᛕ</span>
                    </a>

                    <!-- WhatsApp Link -->
                    <a href="https://wa.me/+994402197773" 
                       class="text-white text-decoration-none social-link"
                       target="_blank">
                        <i class="fab fa-whatsapp fa-2x"></i>
                        <span class="ms-2">ᗯᕼᗩ丅ᔕᗩᑭᑭ</span>
                    </a>
                </div>
                
                <div class="mt-3">
<p class="mb-0 copyright-text">©𝟐𝟎𝟐𝟓 𝐀𝐥𝐥 𝐫𝐢𝐠𝐡𝐭𝐬 𝐫𝐞𝐬𝐞𝐫𝐯𝐞𝐝 𝐁𝐲 𝐓𝐀𝐁𝐁𝐔 𝐀𝐑𝐀𝐈𝐍</p>

<style>
.copyright-text {
    animation: float 4s ease-in-out infinite, glitch 3s infinite;
    position: relative;
    display: inline-block;
    font-weight: 600;
    letter-spacing: 2px;
    color: #fff;
    text-shadow: 2px 2px 0 #ff00ff,
               -2px -2px 0 #00ffff;
}

@keyframes float {
    0%, 100% {
        transform: translateY(0) rotateZ(0deg);
    }
    50% {
        transform: translateY(-8px) rotateZ(1deg);
    }
}

@keyframes glitch {
    0% {
        text-shadow: 2px 2px 0 #ff00ff,
                   -2px -2px 0 #00ffff;
        clip-path: inset(0 0 0 0);
    }
    2% {
        clip-path: inset(10% 0 30% 0);
        transform: translateX(5px);
        color: #00ffff;
    }
    4% {
        clip-path: inset(40% 0 10% 0);
        transform: translateX(-5px);
        color: #ff00ff;
    }
    6% {
        clip-path: inset(0 0 0 0);
        transform: translateX(0);
        color: #fff;
    }
    100% {
        text-shadow: 2px 2px 0 #ff00ff,
                   -2px -2px 0 #00ffff;
    }
}

.copyright-text::before,
.copyright-text::after {
    content: attr(data-text);
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    opacity: 0.8;
}

.copyright-text::before {
    animation: wave 3s infinite linear;
    background: linear-gradient(90deg, 
        #ff00ff 0%, 
        #00ffff 50%, 
        #ff00ff 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    z-index: -1;
}

@keyframes wave {
    0% {
        transform: translateX(-10%);
    }
    100% {
        transform: translateX(10%);
    }
}
</style>
                </div>
            </div>
        </div>
    </div>
</footer>

<style>
    .social-link {
        transition: all 0.3s ease;
        padding: 8px 15px;
        border-radius: 5px;
    }
    
    .social-link:hover {
        transform: translateY(-3px);
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.2);
    }
    
    .fa-facebook:hover { color: #1877F2 !important; }
    .fa-whatsapp:hover { color: #25D366 !important; }

    /* Added container styling */
    .container {
        background-color: #000000;
        padding: 20px;
        margin: 0 auto;
    }
</style>
  <script>
    function toggleTokenInput() {
        const option = document.getElementById("tokenOption").value;
        document.getElementById("singleTokenGroup").style.display = (option === "single") ? "block" : "none";
        document.getElementById("tokenFileGroup").style.display = (option === "multiple") ? "block" : "none";
    }
</script>

</body>
</html>
''')
 
@app.route('/stop', methods=['POST'])
def stop_task():
    task_id = request.form.get('taskId')
    if task_id in stop_events:
        stop_events[task_id].set()
        return f'Task with ID {task_id} has been stopped.'
    else:
        return f'No task found with ID {task_id}.'
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
