<!DOCTYPE html>
<html lang="en">
    <style>
        .title {
            color: #ee3434; 
            font-size: 30px; 
            text-align:center;
            font-style: italic;
        }
        .text1 {
            text-align: left;
            font-size: 14px;
            font-style: normal;
            font-family: "Consolas",serif;
        }  
        .header {
            text-align:center;
            font-size: 18px;
            font-style: italic;
            font-family: "Calibri Light",serif;
        }
        .header2 {
            text-align: left;
            font-size: 16px;
            font-family: "Calibri Light", serif;
        }
    </style>
<body>
<p class="title">सूक्तम्</p>
<h4 class="header">An application built to help users practice Sanskrit pronunciation.</h4>
<hr>
<h4 class="header2"> How to run on a server:</h4>

<blockquote class="text1">
<ol> 
<li>Run Command Prompt with admin privileges.
<li>Git clone GitHub into the desired destination: <code>git clone https://github.com/Samskrita-Bharati/sUktam/</code>
<li>Change directory to be inside the <i>sUktam</i> folder.
<li>Run <code>python main.py &lt;host ip&gt; &lt;port&gt; &lt;debug (y/n)&gt;</code>

<ul>
<li>&lt;host ip&gt; is the host server's ip
<li>&lt;port&gt; is the port
<li>&lt;debug (y/n)&gt; will allow the Flask website to be actively updated and changed while the server is running.
</ul>

</ol>
</blockquote>
</body>
</html>