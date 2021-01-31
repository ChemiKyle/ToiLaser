# Required Hardware

* Any model Raspberry Pi (preferrably one with onboard WiFi)
* A microSD card
* A [**p**yroelectric **i**nfra**r**ed (PIR) motion sensor](https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor)
* An LED laser

# Initial Setup of Raspberry Pi
If you already have a Pi with an OS installed, feel free to skip this section.
<details><summary>Installing Raspbian</summary>

The operating system can be downloaded at the [official Raspberry Pi website](https://www.raspberrypi.org/software/operating-systems/). You'll see 3 options (OS with desktop and recommended software, OS with desktop, and OS Lite), it doesn't matter which one you use. Instructions for installing to an SD card are provided on the Raspberry Pi website.

You will likely want to set up headless operation (make the pi usable without a monitor and keyboard attached to it).
If you're using a Raspberry Pi Zero W and don't have converter cables, you'll _have to_ follow these steps.

<details><summary>Click for Headless Setup</summary>

This section is condensed from [the official documentation](https://www.raspberrypi.org/documentation/configuration/wireless/headless.md).

You will need to create 2 files in the `boot` directory on the SD card.

## Enable SSH
Create a file called `ssh` (with no extension). That's it!

## Enable Wifi
Create a file named `wpa_supplicant.conf`.

```conf
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=<Insert 2 letter ISO 3166-1 country code here>

network={
 ssid="<Name of your wireless LAN>"
 psk="<Password for your wireless LAN>"
}
```

</details> <!-- End headless setup-->

</details><!-- End rpi setup-->
