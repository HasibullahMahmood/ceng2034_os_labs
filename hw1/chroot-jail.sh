
#!/bin/bash

sudo mkdir /bashjail
sudo mkdir /bashjail/{bin,etc}
sudo mkdir -p /bashjail/{lib/x86_64-linux-gnu,lib64}
sudo cp /bin/bash /bashjail/bin/
sudo cp /bin/ls /bashjail/bin/
for i in /lib/x86_64-linux-gnu/libtinfo.so.6 /lib/x86_64-linux-gnu/libdl.so.2 /lib/x86_64-linux-gnu/libc.so.6 /lib64/ld-linux-x86-64.so.2 ; do sudo cp $i /bashjail/lib/x86_64-linux-gnu/; done
sudo cp /lib64/ld-linux-x86-64.so.2  /bashjail/lib64/
for i in /lib/x86_64-linux-gnu/libselinux.so.1 /lib/x86_64-linux-gnu/libc.so.6 /lib/x86_64-linux-gnu/libpcre.so.3 /lib/x86_64-linux-gnu/libdl.so.2 /lib/x86_64-linux-gnu/libpthread.so.0 ; do sudo cp $i /bashjail/lib/x86_64-linux-gnu/; done
echo "PS1=' JAIL $ ' " | sudo tee /bashjail/etc/bash.bashrc
sudo chroot /bashjail /bin/bash
