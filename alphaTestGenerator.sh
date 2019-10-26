#!/bin/bash

declare -a arr=(a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z)


for i in "${arr[@]}"
do
	cd ~/Desktop/test-images/$i/
	rm $i*
	mkdir orig
	mv *.png orig/
	
	convert orig/*.png -trim -adaptive-sharpen 0x3 -resize 28x28 -gravity Center -extent 28x28 -statistic minimum 2x2 -level 90x100% -colorspace Gray $i.png
	
	convert *.png 	-rotate "2"		-resize 28x28 $i-rot2r.png
	convert *.png 	-rotate "-2"	-resize 28x28 $i-rot2l.png
	convert *.png 	-rotate "4" 	-resize 28x28 $i-rot4r.png
	convert *.png 	-rotate "-4" 	-resize 28x28 $i-rot4l.png

	convert *.png -adaptive-sharpen 0x3 -resize 28x28 $i-gauss.png
	
	convert *.png -adaptive-sharpen 0x3 -morphology Smooth Octagon:1 -resize 28x28 $i-morph-sm.png
	convert *.png -adaptive-sharpen 0x3 -morphology Thicken ConvexHull -resize 28x28 $i-morph-cvx.png
	
	convert *.png -adaptive-sharpen 0x3 -morphology DilateIntensity Octagon:1 -level 60x100% $i-dilate.png
	
done
