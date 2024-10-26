# Every Frame In Order Bot(Twitter)
<h2>Twitter Bot posts every 30 minutes every second of movie or TV series in order such as Spongebob,Breaking Bad and American Psyho</h2>

![image](https://github.com/bahrom04/Sotqin-kinosidan-lavhalar/assets/116780481/f4c249e7-7059-4c0c-86f6-466f89cb46b6)

<h2>Requirements</h2>
<ul>
  <li><code>1.python3 version=>3.8 or later</code></li>
  <li><code>3.ffmpeg</code>You will install it from website.Here is tutorial for <a href="https://youtu.be/qSlxv68Xpkw">Windows</a> and <a href="https://youtu.be/mfTaTmc7Wjo">Ubuntu</a></li>
 </ul>

 <h2>Ffmpeg</h2>
 <p>Create folder and put your <code>mp.4</code> movie inside this folder.You also need to get subtitle file like <code>.srt</code>of this movie and add it by using ffmpeg <a href="https://youtu.be/t8oUOHWufug">tutorial</a></p>
<p>Open terminal(cmd) inside this folder and write <code>ffmpeg -i input_file.mp4 -r fps_number output_file.mp4</code> your movie name and write 1 instead of fps_number to get 1 frame in every second of the movie then your output_file name </p>
<p>Then once you finished you need to split your 1fps movie to frames by this command <code>ffmpeg -i input_file.mp4 image2%.png</code></p>

<p>And results should be like this</p>

![repo](https://github.com/bahrom04/Sotqin-kinosidan-lavhalar/assets/116780481/148979af-f8be-4587-9963-7841102b4f76)

<h2>Code</h2>
<p>Download these two packages </p>
<pre>
pip install -r requirements.txt
</pre>
<p>Create python file for example <code>main.py</code> inside folder which you splitted frames and paste code which is written in<code>bot.py</code> in this <a href="https://github.com/bahrom04/Sotqin-kinosidan-lavhalar/blob/main/bot.py">repository</a></p>
<p>Put your <code>BEARER_TOKEN,CONSUMER_KEY,CONSUMER_SECRET,ACCES_TOKEN,ACCES_TOKEN_SECRET</code>,movie name,total number of frames</p>
<p>These tokens you can get from <a href="https://developer.twitter.com/en">Twitter Developer Portal</a></p>
<br>
<p>That's it!. Use<code>Task scheduler</code> in Windows to automate your run time</p>
<br>
<p>Don't forget to give star and feel free to contact</p>
<p>Special thank's to <a href="https://github.com/pigeonburger">Pigeonburger</a> for the idea</p>

