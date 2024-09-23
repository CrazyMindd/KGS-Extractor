import datetime

def get_datetime_str():
    now = datetime.datetime.now()
    return now.strftime("%Y%m%d%H%M%S")

def create_html_file(file_name, batch_name, contents):
    tbody = ''
    parts = contents.split('\n')
    for part in parts:
        split_part = [item.strip() for item in part.split(':', 1)]
    
        text = split_part[0] if split_part[0] else 'Untitled'
        url = split_part[1].strip() if len(split_part) > 1 and split_part[1].strip() else 'No URL'

        tbody += f'<tr><td>{text}</td><td><a href="{url}" target="_blank">{url}</a></td></tr>'

    with open('Extractor/core/template.html', 'r') as fp:
        file_content = fp.read()
    title = batch_name.strip()
    with open(file_name, 'w') as fp:
        fp.write(file_content.replace('{{tbody_content}}', tbody).replace('{{batch_name}}', title))
