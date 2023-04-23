from datetime import datetime

def logging(message):
    timestamp_format = '%y-%h-%d-%H-%M-%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open('log_file.txt','a') as f :
        f.write(timestamp + ',' + message + '\n') 