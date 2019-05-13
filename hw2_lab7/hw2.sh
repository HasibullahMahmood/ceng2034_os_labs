#!/bin/bash

# Read MBR and write it into a file.
hd -n 512 /dev/sda > MyMbr.txt

# Enter a new entry in GRUB with an iso under your home directory.
# https://www.howtogeek.com/196933/how-to-boot-linux-iso-images-directly-from-your-hard-drive/

echo 'menuentry "ubuntu-18.10-desktop-amd64.iso" {
set isofile="/home/hasibullah/ubuntu-18.10-desktop-amd64.iso"
loopback loop (hd0,5)$isofile
linux (loop)/casper/vmlinuz boot=casper iso-scan/filename=${isofile} quiet splash
initrd (loop)/casper/initrd
}' >> /etc/grub.d/40_custom
update-grub
reboot
