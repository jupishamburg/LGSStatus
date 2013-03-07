UDEV Rule to automount Arduino

    cat /etc/udev/rules.d/10-local.rules 
    ACTION=="add", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6001", SYMLINK+="arduino-tty"

Supervisord

1. Add config

    [include]
    files = /etc/supervisor.d/*.ini

    [program:lgs_status]
    environment=PYTHONPATH=/root/LGSStatus/raspberrypi
    command=/root/LGSStatus/raspberrypi/run.py --prod
    user=root
    autostart=true
    autorestart=true
    redirect_error=true
    startretries = 0
    stdout_logfile = /var/log/lgs_status_out.log
    stderr_logfile = /var/log/lgs_status_err.log

2. Start Supervisor on boot

    systemctl enable supervisord.service

This will automagically start the LGS Status

3. Manual starting and stopping of supervisor

    supervisorctl start lgs_status
    supervisorctl stop lgs_status
