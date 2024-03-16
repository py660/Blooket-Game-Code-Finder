# How to run (updated by py660)
First, log into blooket. Then, open DevTools > Application > Cookies > https://dashboard.blooket.com
Then find the value corresponding to `bsid`, and copy it. That's your account token. DO NOT SHARE IT! KEEP IT PRIVATE.

Run the following code:
```
BSID=your_account_token_here python main.py
```
It will notify you once a game pin is found. IF YOU FIND A GAME PIN AND WANT TO CONNECT, YOU MUST FIRST STOP THE PROGRAM.
To stop the program, spam CTRL-C until the program stops.

# NEW! Bookmarklet/javascript version
Create a new bookmark with the following URL:
```
javascript: new Promise(async ()=>{let iframe = document.createElement("iframe");iframe.style.display="none";document.body.appendChild(iframe);window.alert = iframe.contentWindow.alert;var code=Math.floor(Math.random()*8999999+1000000);console.log(setInterval(()=>{console.log(code);fetch("https://fb.blooket.com/c/firebase/id?id=1234567", {credentials: "include"}).then(res => {if(res.ok){code=Math.floor(Math.random()*9000000+1000000);return res.text()}else{return '{"success":false,"errType":"429"}'}}).then(res=>{console.log(res);return JSON.parse(res);}).then(res=>{  if(res.success){alert("SUCCESS");alert(code);resolve()}  })},101))})
```

**OR**

Go to `play.blooket.com` and paste the following code into the devtools console
```
new Promise(async ()=>{let iframe = document.createElement("iframe");iframe.style.display="none";document.body.appendChild(iframe);window.alert = iframe.contentWindow.alert;var code=Math.floor(Math.random()*8999999+1000000);console.log(setInterval(()=>{console.log(code);fetch("https://fb.blooket.com/c/firebase/id?id=1234567", {credentials: "include"}).then(res => {if(res.ok){code=Math.floor(Math.random()*9000000+1000000);return res.text()}else{return '{"success":false,"errType":"429"}'}}).then(res=>{console.log(res);return JSON.parse(res);}).then(res=>{  if(res.success){alert("SUCCESS");alert(code);resolve()}  })},101))})
```

# Working blooket game finder

**Not recommended to self host as this takes up a LOT of resources (if you think you can make this more optimized, please open a PR!)**

### If you just want to get game codes to troll people, [join our discord](https://discord.gg/36sgQJ3pcH)! 
*you can also find some really good, working hacks in the discord*
  
This is a blooket game finder that works right now! There are many older version of this but blooket changed the api url. I was able to intercept a request using devtools and get the url!    
   
**In case you are intrested, the api url is `https://fb.blooket.com/c/firebase/id?id=` where you put your ~~6~~ 7 dight game code after `id=`**  

To use the finder, look at the config in main.py and run main.py! You can edit the number of threads used to find codes in main.py! I find that over 50 threads the codes per second is similar. On replit (where I run this), I am using 25 threads with `2 vCPU` (hacker plan default).      

This is not the fastest finder, but it is very simple! *~7 codes per minute using 25 threads*

*I am working on a game flooder!*
