
import os

def generate_file_tree_html(folder_path):
    txt = '''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pastas Indexadas</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background: #F5E8B1;
        }

        header {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: end;
            background: #B0CC99;
            height: 84px;
            margin: 32px 64px;
            border-radius: 32px;
            box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
        }
        .logo {
            position: relative;
            left: -28px;
            width: 237px;
            height: 71px;
            background: #D9D9D9;
        }

        ul {
            list-style: none;
        }

        li {
            display: flex;
            align-items: center;
            justify-content: start;
        }

        p {
            color: #88725B;
            font-family: Lora;
            font-size: 16px;
            font-style: normal;
            font-weight: 400;
            line-height: normal;
        }

        .folder {
            width: 30px;
            height: 30px;
            background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='30' height='30' viewBox='0 0 30 30' fill='none'%3E%3Cpath d='M4.61979 13.1133L0 22.0195V5.625C0 3.55664 1.49479 1.875 3.33333 1.875H9.45312C10.3385 1.875 11.1875 2.26758 11.8125 2.9707L13.1927 4.52344C13.8177 5.22656 14.6667 5.61914 15.5521 5.61914H21.6667C23.5052 5.61914 25 7.30078 25 9.36914V11.2441H7.5C6.3125 11.2441 5.21875 11.9531 4.61979 13.1074V13.1133ZM6.05729 14.0566C6.35938 13.4766 6.90625 13.125 7.5 13.125H28.3333C28.9323 13.125 29.4792 13.4824 29.776 14.0684C30.0729 14.6543 30.0729 15.3691 29.7708 15.9492L23.9375 27.1992C23.6406 27.7734 23.0938 28.125 22.5 28.125H1.66667C1.06771 28.125 0.520833 27.7676 0.223958 27.1816C-0.0729166 26.5957 -0.0729167 25.8809 0.229167 25.3008L6.0625 14.0508L6.05729 14.0566Z' fill='%23687E4F'/%3E%3C/svg%3E") no-repeat left center;
            padding-left: 20px;
            background-size: contain;
            display: inline-block;
        }

        .file {
            width: 30px;
            height: 30px;
            background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='20' height='26' viewBox='0 0 20 26' fill='none'%3E%3Cg clip-path='url(%23clip0_17_75)'%3E%3Cpath d='M0 3.25C0 1.45742 1.49479 0 3.33333 0H11.6667V6.5C11.6667 7.39883 12.4115 8.125 13.3333 8.125H20V22.75C20 24.5426 18.5052 26 16.6667 26H3.33333C1.49479 26 0 24.5426 0 22.75V3.25ZM20 6.5H13.3333V0L20 6.5Z' fill='%2388725B'/%3E%3C/g%3E%3Cdefs%3E%3CclipPath id='clip0_17_75'%3E%3Crect width='20' height='26' fill='white'/%3E%3C/clipPath%3E%3C/defs%3E%3C/svg%3E") no-repeat left center;
            padding-left: 20px;
            background-size: contain;
            display: inline-block;
        }
    </style>
</head>
<body>
    <header>
        <div class="logo">

        </div>
    </header>
    <div class="content">
    '''
    txt += ('<ul>\n')
    txt += list_folders(folder_path)
    txt += ('</ul>\n')
    txt += '''
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
    '''
    return txt

def list_folders(folder_path):
    txt = ''
    folders = []
    files = []
    txt += ('<ul>\n')
    for item in os.listdir(folder_path):
        if item.startswith(".") and not item.startswith("./"):
            continue
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            folders.append(item)
        else:
            files.append(item)
    
    for folder in folders:
        item_path = os.path.join(folder_path, folder)
        txt += (f'<li data-bs-toggle="collapse" data-bs-target="#{folder}"><div class="{verify_class_type(item_path)}"></div><p>{folder}</p></li>\n')
        txt += (f'<div id="{folder}" class="collapse">')
        txt += list_folders(item_path)
        txt += ('</div>')
    
    for file in files:
        item_path = os.path.join(folder_path, file)
        txt += (f'<li ><div class="{verify_class_type(item_path)}"></div><p>{file}</p></li>\n')
    txt += ('</ul>\n')
    return txt

def verify_class_type(filename: str):
    # if filename.startswith("/") or filename.startswith("./"):
    if os.path.isdir(filename):
        class_type = "folder"
    else:
        class_type = "file"
    return class_type

def save_html(txt, output_name):
    with open(output_name, 'w') as f:
        f.write(txt)

def main():
    current_working_directory = os.getcwd()
    txt = generate_file_tree_html(current_working_directory)
    save_html(txt, current_working_directory + "/files_indexed.html")

if __name__ == '__main__':
    pass
