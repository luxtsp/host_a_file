# host_a_file
A simple flask python script to host a file. Made to pass a file from my main pc to my server through wget

## How to use:
There are two steps you have to do in order to use this  
(very difficult)

1. place your file in the `data/` folder.   
*the first file `os.listdir()` finds in `data` will be the one sent by the script if you give multiple files*



2. run the script using '`python3 -m uv run .`' or by running the provided `run.sh` or `run.bat` depending on OS  
*uv must be installed, you can use `pip install uv` if you dont have it*  
*also script must be started from the project's root*

3. get the file on your other machine  
if you have a GUI on your server you can just go on `{your_host's_ip}:5000` on your web browser  
or you can use `wget {your_host's_ip}:5000` in ur terminal
