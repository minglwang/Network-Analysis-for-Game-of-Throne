# Network-Analysis-for-Game-of-Throne

Game of Thrones is the hugely popular television series by HBO based on the (also) hugely popular book series <em>A Song of Ice and Fire</em> by George R.R. Martin. In this notebook, I will analyze the co-occurrence network of the characters in the  Game of Thrones books. Here, two characters are considered to co-occur if their names appear in the vicinity of 15 words from one another in the books. </p>
The dataset is extracted using the bookworm and stored in CSV files which can be download from 
https://github.com/mathbeveridge/asoiaf/tree/master/data.

The data constitutes a network and is given as a text file describing the <em>edges</em> between characters, with some attributes attached to each edge.


The goal is to find homogeneous regions in the images which hopefully belong to objects or object parts. Below is one of the test images and an example segmentation using K-means (In the right image, each segment is colored based on the average color within the segment).

<p align = "center">
<img width ="800" height="180", src = 
https://user-images.githubusercontent.com/45757826/57579422-c972af00-749b-11e9-99ca-8847a548e730.png>
</p>

# Table of Content
- [Data Description](#data-description)
- [Clustering Methods](#clustering-methods)
  - [K Means](#k-means)
  - [Gaussian Mixture Models](#gaussian-mixture-models)
  - [Mean Shift](#mean-shift)
  - [Modification](#modification)
- [Results](#results)
- [How To Use](#how-to-use)

