# pywerview-json
Update to pywerview main.py to allow for json parsing.

This patch will allow for json output in the pywerview scripts making the output more usable than the default line by line plaintext.
This work for the python3-pywerview package as of 4 April 2025.
If main.py is updated, this may break pywerview. I will attempt to keep up and work on updates if changes come about.

Usage:
- Patch the default main.py in the default location for a pywerview installation.
```
sudo python patch-pywerview.py copy
```
- Restore the default main.py back to default settings.
```
sudo python patch-pywerview.py restore
```
- Regular output for the get-netcomputer command in pywerview
  
![image](https://github.com/user-attachments/assets/9edbc4b1-6da7-4541-b8d2-594d6fb6bf47)


- Here is the output when using the updated --json switch.

![image](https://github.com/user-attachments/assets/3f0d3671-4b44-414b-a019-1382551f1782)

- multi-line field support

![image](https://github.com/user-attachments/assets/c4003292-b334-40c0-aee6-47691579db22)


![image](https://github.com/user-attachments/assets/9a6f4ec2-51cc-4dc7-ae9c-abf75dc4716b)

- Error checking

![image](https://github.com/user-attachments/assets/933a90d8-1e41-412c-9370-013514670ff4)

