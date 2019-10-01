# Prediction-based Cursive English Handwriting Recognition

## Team members

- Tyler Cummings
- Eric Vo

## Description

Handwriting recognition can be broken up into two main categories: online and offline recognition. In the case of online handwriting recognition, handwriting input is analyzed as it is being written. Using a stylus to write on an electronic device with a touch screen falls into this category. In offline recognition, however, the text is analyzed after it has been written. For example, analysis of a page scanned from a book. 

Modern handwriting also falls into two categories: standard lettering, which is also known as block lettering, manuscript style, or printing, and cursive. Generally speaking, characters written in standard lettering are relatively simple to detect through online and offline methods: the letters are discrete, so it is easy to distinguish where one character ends and another begins. Cursive, on the other hand, poses a tougher challenge. Cursive lettering is continuous, meaning that as a word is being written, the utensil with which it is being written doesn’t leave the medium. The result is a chain of characters with no distinct separation between them. 

## A brief survey of what has been done and how the proposed work is different

Online recognition of cursive has been met with much success. This is largely due to the fact that actively written cursive provides directional and temporal information that aid in recognition. These traits, however, are largely absent in physical documents, and ultimately cannot be used in offline recognition to determine which letter is which. 

While segmentation during the analysis of cursive has shown promising results, it is still far from producing accurate recognitions.

The proposed project will follow the approach of segmenting words into individual characters, but then predict the word based on a number of factors: 
- Characters identified with a high level of certainty above a specific threshold will be assumed to be correct. Based on this assumption, word predictions will be made based on the positively identified letters and the frequency of the word in the English language. A human example of this would be the game Wheel Of Fortune, where contestants guess hidden phrases based on the letters they know the phrase possesses.

## Preliminary plan (milestones)

### 10/1/2019 - 11/1/2019

- A request has been made to IDIAP Research Institute to use their Cursive Character dataset. Approval is currently pending, but, according to the IDIAP website, access will likely be granted within a week of the request.
- A small number of sample documents written in cursive will be collected. Some may be handwritten by team members. 
- Following the acquisition of the character dataset, image pre-processing will need to be performed to remove image noise and enhance contrast for stronger detection.Additionally, skew correction, cropping, and resizing will need to be performed on the dataset.
- Handwritten documents will also need to go through pre-processing similar to that of the character dataset.
- Following the acquisition of the IDIAP dataset, and its subsequent pre-processing, we will train the model of choice and evaluate its results. 

## Dataset

https://www.idiap.ch/dataset/ccc

## References

[Freeform Cursive Handwriting Recognition Using a Clustered Neural Network](https://digital.library.unt.edu/ark:/67531/metadc804845/#description-content-main)

[Cursive Handwriting Recognition System Using Feature Extraction and Artificial Neural Network](https://pdfs.semanticscholar.org/8292/26f8c745645802b7d76ef3587b1c389cc173.pdf)

[Segmentation Of Off-line Cursive Handwriting Using Linear Programming](https://www.sciencedirect.com/science/article/abs/pii/S0031320398000818)

[Online Handwriting Recognition Problem: Issues and Techniques](https://pdfs.semanticscholar.org/f957/3acd8405b5c594314491dedfbeb3bf40750f.pdf)

[Study Of Various Character Segmentation Techniques For Handwritten Off-line Cursive](https://www.semanticscholar.org/paper/STUDY-OF-VARIOUS-CHARACTER-SEGMENTATION-TECHNIQUES-Kaur-Baghla/183ed0b8d77773c22e1f5f455256427b654b2d09)

[Handwriting Recognition – “Offline” Approach](https://cs.stanford.edu/people/adityaj/HandwritingRecognition.pdf)

[Offline cursive handwriting recognition system based on hybrid Markov model and neural networks](https://www.semanticscholar.org/paper/Offline-cursive-handwriting-recognition-system-on-Tay-Khalid/8476059c0d810e252249feffc21c2ea55ee8ee43)

[Off-line Cursive Handwriting Recognition Using Synthetic Training Data](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.92.9920&rep=rep1&type=pdf)

[Recognition of Cursive Roman Handwriting - Past, Present and Future](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.1.1763&rep=rep1&type=pdf)

https://pdfs.semanticscholar.org/2313/9cf6228053980eeffd42573c61fe5d658004.pdf
