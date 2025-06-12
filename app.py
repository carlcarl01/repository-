import difflib
from flask import Flask, request, session, redirect, url_for, abort

# Database ng mga pangalan at unit
name_database = {
    "DH MARICEL": "10E",
    "DH DONNA": "21A",
    "MS MITCH": "24A",
    "DH MALOU": "21B",
    "MS KARIN": "12A",
    "MS SANTOS": "16C",
    "DH HEZIEL": "21C",
    "MS PASCUAL": "11A",
    "MR QUIRON": "22B",
    "DH LOLITA": "10E",
    "DH EDNA": "2A",
    "MR RYAN": "5G",
    "MR JOJO DRIVER": "19A",
    "MR DANIEL BROTHER DAVID": "26D",
    "MR VALDEZ": "11C",
    "MR GONZALEZ": "3F",
    "MR ALARCON": "3D",
    "DH VALDEROZA": "12A",
    "MR GEORGE": "14C",
    "MR ANTHONY": "7E",
    "DH JENNIFER": "11C",
    "DH CONNIE": "11D",
    "MR STORGION": "18E",
    "DH JOSSIE": "10F",
    "DH VERGIE": "19B",
    "MS CARIÑO": "3C",
    "MR LOCSIN": "21A",
    "DH MARRIEL": "9F",
    "MR SAM DRIVER": "11D",
    "DH CONANAN": "25B",
    "MR DANIEL DRIVER": "9E",
    "DH EVA": "25A",
    "MR DEMETRIO": "2B",
    "MS DOYYEN": "18A",
    "DH LIERA": "15C",
    "DH MARJORIE": "23C",
    "MS COROMINA DOCTORA": "15A",
    "DH LESLIE": "16A",
    "MR TRINIDAD": "21C",
    "DH ANNA": "8D",
    "DH MARIO": "10C",
    "MR ALEX DRIVER": "21D",
    "DH MM": "9D",
    "MR BEGA": "24A",
    "DH LEDIA": "18A",
    "DH GRACE": "7A",
    "DH LENA": "7AF",
    "MR ROMMY DRIVER": "10C",
    "MR JOSSE LOCIDO DRIVER": "18D",
    "MR ERNESTO DRIVER": "25A",
    "MR NIMUCO": "17A",
    "MR EDWIN": "9D",
    "DH MELODY": "26D", 
    "DH BING":   "8D",
    "DH JENNYFER": "10C",
    "MS KARIN": "12A",
    "MR LIMUCO": "17A",
    "DH MARY GRACE SLIMP": "9C",
    "MS KOROMINA": "15B",
    "DH SOUL": "23",
    "MR TRINIDAD": "21C",
    "MR ANTHONY": "7C",
    "MR ALARCON": "3D",
    "MR JAKE": "26A",
    "MS CARIÑO": "3C",
    "MR MARIO DRIVER": "7A",
    "DH MARITES": "10A",
    "DH VERGIE": "19B",
    "DH VANGIE": "19D",
    "DH MARRIEL": "9F",
    "DH VANGIE RECTO": "22A",
    "MR TAKA/DICAI": "20E",
    "DH LENA": "7AF",
    "MR SAM DRIVER": "11D",
    "SAMYA ABAY": "26D",
    "MR GARCIA": "22D",
    "MR1 ANG": "22A",
    "MR2 ANG": "23D",
    "MS MARIVEL": "14L",
    "MS OSIAS": "9F",
    "MR SUTTON": "7D",
    "DH NORA": "26C",
    "DH CONNIE": "11B",
    "MS REALYN": "14K",
    "DH VILMA": "8D",
    "MS HANNA ACONA": "4C",
    "MS SERVERRO": "26",
    "MR CANOY D": "10B",
    "DH LINA": "10B",
    "DH BEBE": "11B",
    "MR LOCIDO DRIVER": "18D",
    "DH KRISTINE": "10F",
    "DH AILEN": "7AF",
    "DH GRETCHELL": "16A",
    "DH MARLYN": "8D",
    "DH NORA": "26A",
    "DH JULIET": "9C",
    "DH CRISTINA RAMIREZ": "21B",
    "MR LAUREL": "4J",
    "DH SEZIEL MABABA NA BABAE": "5G",
    "DH JONNA": "2A",
    "MR BIGA": "24A",
    "DH NELPA": "9C",
    "DH MERIAN": "11B",
    "DH MICA": "21B",
    "DH BRENDA": "22B",
    "MS BIANGCA/MARK": "23A",
    "MS CALIDA": "6F",
    "DH MINA": "6B",
    "DH JOY BAKET": "16A",
    "MR AMATIA": "10F",
    "DH GRACE MAY SALAMIN": "9C",
    "MR JHOSUA": "14E",
    "MR VERGARA": "7A",
    "MS DELIA": "6F",
    "MR LEPIN SUBOSTABA": "3G",
    "MS SHERREL": "6B",
    "PUCH": "8B",
    "MR MATSOMUTO": "8A",
}

def get_unit_by_name(name):
    normalized_name = name.strip().upper()
    if not normalized_name:
        return None, []
    if normalized_name in name_database:
        return name_database[normalized_name], []
    else:
        close_matches = difflib.get_close_matches(normalized_name, name_database.keys(), n=3, cutoff=0.6)
        return None, close_matches

def add_or_update_entry(name, unit):
    normalized_name = name.strip().upper()
    normalized_unit = unit.strip().upper()
    if not normalized_name or not normalized_unit:
        print("❌ Pakilagay ang tamang pangalan at unit.\n")
        return
    name_database[normalized_name] = normalized_unit
    print(f"✅ Nadagdag o na-update: '{normalized_name}' -> '{normalized_unit}'\n")

def print_database():
    print("\n--- Lahat ng Entries sa Database ---")
    for name, unit in sorted(name_database.items()):
        print(f"{name}: {unit}")
    print("-------------------------------------\n")

def cli_main():
    print("Welcome to the Unit Lookup & Verification Program!")
    print("Instructions:")
    print(" - Para maghanap ng unit, ilagay lang ang pangalan (e.g. MR LOCIDO)")
    print(" - Para magdagdag o mag-update, ilagay ang pangalan at unit (e.g. MS CARIÑO 3C)")
    print(" - I-type ang 'printdb' para makita lahat ng entries.")
    print(" - I-type ang 'exit' para lumabas.\n")
    while True:
        try:
            user_input = input("Enter name (or 'printdb'/'exit'): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting program.")
            break

        if not user_input:
            continue

        cmd = user_input.lower()

        if cmd == "exit":
            print("Exiting program.")
            break
        elif cmd == "printdb":
            print_database()
            continue

        parts = user_input.strip().rsplit(" ", 1)
        if len(parts) == 2 and any(char.isdigit() for char in parts[1]) and len(parts[1]) <= 5:
            name, unit = parts
            add_or_update_entry(name, unit)
            continue

        name = user_input.strip()
        unit, suggestions = get_unit_by_name(name)
        if unit:
            print(f"✅ Unit para kay '{name.upper()}': {unit}\n")
        else:
            print(f"❌ Walang unit na nahanap para kay '{name.upper()}'.")
            if suggestions:
                print(f"  Baka ito ang ibig mong sabihin: {', '.join(suggestions)}\n")
            else:
                print("  Walang malapit na match.\n")

# WEB APP SECTION

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Set a real secret key for production

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'gio22' and password == 'gio22':
            session['logged_in'] = True
            return redirect(url_for('lookup'))
        else:
            return '''
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <title>Login</title>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
                    <style>
                        body {
                            background: #f8f9fa;
                            height: 100vh;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                        }
                        .login-box {
                            background: #fff;
                            padding: 2rem;
                            border-radius: 8px;
                            box-shadow: 0 0.5rem 1rem rgba(0,0,0,0.1);
                            width: 350px;
                        }
                        .form-title {
                            text-align: center;
                            margin-bottom: 1.5rem;
                            color: #0d6efd;
                        }
                        .btn-primary {
                            width: 100%;
                        }
                        .alert {
                            margin-top: 1rem;
                        }
                    </style>
                </head>
                <body>
                    <div class="login-box">
                        <h3 class="form-title">Unit Lookup System</h3>
                        <form method="post">
                            <div class="mb-3">
                                <label for="username" class="form-label">Username</label>
                                <input type="text" class="form-control" id="username" name="username" required>
                            </div>
                            <div class="mb-3">
                                <label for="password" class="form-label">Password</label>
                                <input type="password" class="form-control" id="password" name="password" required>
                            </div>
                            <button type="submit" class="btn btn-primary">Login</button>
                        </form>
                        <div class="alert alert-danger mt-3" role="alert">
                            Invalid username or password!
                        </div>
                    </div>
                </body>
                </html>
            ''', 401
    return '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Login</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
            <style>
                body {
                    background: #f8f9fa;
                    height: 100vh;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                }
                .login-box {
                    background: #fff;
                    padding: 2rem;
                    border-radius: 8px;
                    box-shadow: 0 0.5rem 1rem rgba(0,0,0,0.1);
                    width: 350px;
                }
                .form-title {
                    text-align: center;
                    margin-bottom: 1.5rem;
                    color: #0d6efd;
                }
                .btn-primary {
                    width: 100%;
                }
            </style>
        </head>
        <body>
            <div class="login-box">
                <h3 class="form-title">Unit Lookup System</h3>
                <form method="post">
                    <div class="mb-3">
                        <label for="username" class="form-label">Username</label>
                        <input type="text" class="form-control" id="username" name="username" required>
                    </div>
                    <div class="mb-3">
                        <label for="password" class="form-label">Password</label>
                        <input type="password" class="form-control" id="password" name="password" required>
                    </div>
                    <button type="submit" class="btn btn-primary">Login</button>
                </form>
            </div>
        </body>
        </html>
    '''

@app.route('/lookup', methods=['GET', 'POST'])
def lookup():
    if not session.get('logged_in'):
        abort(401)
    result = ''
    suggestions = []
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        if name:
            unit, suggestions = get_unit_by_name(name)
            if unit:
                result = f"<div class='alert alert-success'>Unit para kay '{name.upper()}': {unit}</div>"
            else:
                result = f"<div class='alert alert-warning'>Walang unit na nahanap para kay '{name.upper()}'</div>"
                if suggestions:
                    result += f"<div class='alert alert-info'>Baka ito ang ibig mong sabihin: {', '.join(suggestions)}</div>"
    return f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Lookup</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
            <style>
                body {{
                    background: #f8f9fa;
                    padding-top: 2rem;
                }}
                .container {{
                    max-width: 600px;
                    background: #fff;
                    padding: 2rem;
                    border-radius: 8px;
                    box-shadow: 0 0.5rem 1rem rgba(0,0,0,0.1);
                }}
                .form-title {{
                    text-align: center;
                    margin-bottom: 1.5rem;
                    color: #0d6efd;
                }}
                .btn-primary {{
                    width: 100%;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h3 class="form-title">Unit Lookup</h3>
                <form method="post">
                    <div class="mb-3">
                        <label for="name" class="form-label">Pangalan</label>
                        <input type="text" class="form-control" id="name" name="name" required>
                    </div>
                    <button type="submit" class="btn btn-primary">Hanapin</button>
                </form>
                {result}
                <div class="mt-3">
                    <a href="/logout" class="btn btn-outline-danger">Logout</a>
                </div>
            </div>
        </body>
        </html>
    '''

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

def web_main():
    app.run(port=3000, debug=True)

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 and sys.argv[1].lower() == 'web':
        web_main()
    else:
        cli_main()
