#!/bin/bash

declare -a arr=(a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z)


for i in "${arr[@]}"
do
	cd ~/charSet/$i/
	rm $i*
	mkdir orig
	mv *.png orig/
	
	convert orig/*.png -trim -adaptive-sharpen 0x3 -resize 28x28 -gravity Center -extent 28x28 -statistic minimum 2x2 -level 90x100% -colorspace Gray $i.png
	convert $i-"[0-9]".png 	-rotate "2"		-resize 28x28 $i-rot2r.png
	convert $i-"[0-9]".png 	-rotate "-2"	-resize 28x28 $i-rot2l.png
	convert $i-"[0-9]".png 	-rotate "4" 	-resize 28x28 $i-rot4r.png
	convert $i-"[0-9]".png 	-rotate "-4" 	-resize 28x28 $i-rot4l.png
	convert $i-"[0-9]".png 	-rotate "6"		-resize 28x28 $i-rot6r.png
	convert $i-"[0-9]".png 	-rotate "-6"	-resize 28x28 $i-rot6l.png
	convert $i-"[0-9]".png 	-rotate "8" 	-resize 28x28 $i-rot8r.png
	convert $i-"[0-9]".png 	-rotate "-8"	-resize 28x28 $i-rot8l.png
	convert $i-"[0-9]".png 	-rotate "10"	-resize 28x28 $i-rot10r.png
	convert $i-"[0-9]".png 	-rotate "-10"	-resize 28x28 $i-rot10l.png
	
	convert *.png -morphology Thicken '3x1+2+0:1,0,0'	-resize 28x28 $i-morph-th.png
	convert *.png -adaptive-sharpen 0x3 -resize 28x28 $i-gauss.png
	
	convert *.png -adaptive-sharpen 0x3 -morphology Smooth Octagon:1 -resize 28x28 $i-morph-sm.png
	convert *.png -adaptive-sharpen 0x3 -morphology Thicken ConvexHull -resize 28x28 $i-morph-cvx.png
	
	convert *.png -blur 1x0.9 -resize 28x28 $i-blur.png
	
	convert *.png -morphology DilateIntensity Octagon:1 -level 60x100% $i-dilate.png

	
	
	
done



