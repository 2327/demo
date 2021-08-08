import os, psutil, socket

def check_nginx():
    """
    calculate exit code
    """
    _status = None

    for process in psutil.process_iter():
        try:
            if process.as_dict(attrs=['pid', 'name'])['name'] == 'tinyproxy':
                _status = 'found'
        except psutil.NoSuchProcess:
            pass

    if _status is not None:
        _port = socket.socket(socket.AF_INET)
        try:
            _port.connect(('127.0.0.1',31128))
        except:
            print('WARNING: process ok but port not accessible')
            code = 127
        else:
            print('OK: process ok & port ok')    
            code = 0
    else:
        print('ERROR: process not found')
        code = 127

    return code

if __name__ == '__main__':
    os._exit(check_nginx())

