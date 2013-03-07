UDEV Rule to automount Arduino

    cat /etc/udev/rules.d/10-local.rules 
    ACTION=="add", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6001", SYMLINK+="arduino-tty"
