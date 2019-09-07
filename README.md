# Network-Analysis-for-Game-of-Throne

Game of Thrones is the hugely popular television series by HBO based on the (also) hugely popular book series <em>A Song of Ice and Fire</em> by George R.R. Martin. In this notebook, I will analyze the co-occurrence network of the characters in the  Game of Thrones books. Here, two characters are considered to co-occur if their names appear in the vicinity of 15 words from one another in the books. </p>
The dataset is extracted using the bookworm and stored in CSV files which can be download from 
https://github.com/mathbeveridge/asoiaf/tree/master/data.

The data constitutes a network and is given as a text file describing the <em>edges</em> between characters, with some attributes attached to each edge.



<p align = "center">
<img width ="800" height="800", src = https://github.com/minglwang/Network-Analysis-for-Game-of-Throne/blob/master/Figures/GM_book1.png>
</p>
<p align = "center">
<img width ="800" height="800", src = https://github.com/minglwang/Network-Analysis-for-Game-of-Throne/blob/master/Figures/GM_book2.png>
</p>
<p align = "center">
<img width ="800" height="800", src = https://github.com/minglwang/Network-Analysis-for-Game-of-Throne/blob/master/Figures/GM_book3.png>
</p>
<p align = "center">
<img width ="800" height="800", src = https://github.com/minglwang/Network-Analysis-for-Game-of-Throne/blob/master/Figures/GM_book4.png>
</p>
<p align = "center">
<img width ="800" height="800", src = https://github.com/minglwang/Network-Analysis-for-Game-of-Throne/blob/master/Figures/GM_book5.png>
</p>


<p>Is it Jon Snow, Tyrion, Daenerys, or someone else? Let's see! Network science offers us many different metrics to measure the importance of a node in a network. Note that there is no "correct" way of calculating the most important node in a network, every metric has a different meaning.</p>
<p>First, let's measure the importance of a node in a network by looking at the number of neighbors it has, that is, the number of nodes it is connected to. For example, an influential account on Twitter, where the follower-followee relationship forms the network, is an account which has a high number of followers. This measure of importance is called <em>degree centrality</em>.</p>
<p>Using this measure, let's extract the top ten important characters from the first book (<code>book[0]</code>) and the fifth book (<code>book[4]</code>).</p>

