# Intermediate Project Report

## Introduction and Problem Description

Handwriting recognition can be broken up into two main categories: online and offline recognition. In the case of 
online handwriting recognition, handwriting input is analyzed as it is being written. Using a stylus to write on an 
electronic device with a touch screen falls into this category. In offline recognition, however, the text is analyzed 
after it has been written. For example, analysis of a page scanned from a book. Modern handwriting also falls into two 
categories: standard lettering, which is also known as block lettering, manuscript style, or printing, and cursive. 
Generally speaking, characters written in standard lettering are relatively simple to detect through online and offline 
methods: the letters are discrete, so it is easy to distinguish where one character ends and another begins. Cursive, 
on the other hand, poses a tougher challenge. Cursive lettering is continuous, meaning that as a word is being written, 
the utensil with which it is being written doesn’t leave the medium. The result is a chain of characters with no 
distinct separation between them. 

To address the continuity problem in offline cursive handwriting recognition, the most common approach is to segment 
the string into individual characters. The slope of the string characters must also be corrected. The quality of 
segmentation and alignment is crucial because of its impact on successful character recognition. One of the most 
successful methods of segmentation is the Ideal Distance approach, which, when used in the context of a machine 
learning model, has been shown to lead to a 97% rate of success in recognizing characters. 

Our goal with this project is to train a model that can recognize cursive handwritten characters in an image of a word
and probabilistically predict what the word is, based on the confidence of prediction accuracy. This "confidence" will
 simply be a threshold that must be crossed before a character can be assumed to be correct. For example, consider the 
 word "hello" and its segmented form {'h','e','l','l','o'}. Now, let's say that our threshold for assumed correctness 
 is .95 or 95%. Let's also say that the respective "confidence" levels for the individual characters are 
 {.92, .96, .97, .70, .97}. In this case, we will assume that the letters 'e', 'l', 'o' were correctly predicted. This 
 can be represented by:
 
    actual word                     h e l l o
    "confident" prediction          _ e l _ o
    
Based on the "confident" prediction, further predictions will be made regarding what the word is, with consideration for
 its prevalence in the English language.
 
     actual word                     h e l l o
     "confident" prediction          _ e l _ o
     
     Word prediction:
     
        --> h e l l o               highest prevalence
                                            |
        --> c e l l o                       |
                                            |
        --> j e l l o                       |
                                            |
        --> h e l i o               lowest prevalence         
        
        
## Description of the data used in the project                  

The IDIAP dataset we had originally requested to have access to was not ideal for our purposes: the vector 
representations of the images were of many different sizes, and not all of the characters contained in the 
dataset are written in cursive. Additionally, the datatype was not easily integrable with how the project has been 
implemented so far. As a result, we chose to develop our own dataset by leveraging Evernote (a note-taking application 
IOS, macOS, Android, and Microsoft Windows), the Evernote api, python, Image Magick (a command-line-based image 
manipulation software), and a handful of generous volunteers. The general collection/processing pipeline can be 
understood as follows:

* Record handwriting data with Evernote and save all inputs with .png extension
* Pull Evernote data to device leveraging Evernote api
* Using Image Magick, trim, center, resize, and adjust color of .png images
* Convert images to MNIST format for integration into model

Even with the contributions of volunteers, we felt that our dataset was too small to effectively train a model, so, 
again using Image Magick, we made copies of the original images that were then edited and incorporated into the training
set.

#### Example with the letter 'a':

<center>
<p style="text-align:center">
  <img src="MarkdownImages/a-0.png" width="100" height="100" />
  <img src="MarkdownImages/a-blur-233.png" width="100" height="100" />
  <img src="MarkdownImages/a-dilate-1160.png" width="100" height="100" />
  <img src="MarkdownImages/a-gauss-106.png" width="100" height="100" />
  <img src="MarkdownImages/a-morph-cvx-122.png" width="100" height="100" />
  <img src="MarkdownImages/a-rot8l-0.png" width="100" height="100" />
  <img src="MarkdownImages/a-morph-sm-167.png" width="100" height="100" />
</p>
</center>

In order from left to right, the effects are: None (original image), blur, dilate, gauss, octagonal convex hull, 8*degree 
rotation to the left, smooth

As a result of the artificial increase in data, we were left with 379,600 images, which we then split into training and testing sets.
*The resulting training set has:
  *7042 images for each character. That is, ‘a’: 7042 images, ‘A’: 7042 images, ‘b’: 7042 images, etc.
  *Total images in training set: 366184
*The resulting test set has:
  *258 images for each character
  *Total images in test set: 13416






