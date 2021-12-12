# X-ray-PreProcessing

## -Vivek Sharma

## Denoising of X-Ray using Adaptive Median filter

Improved version of traditional median filtering
Having two parts:
Noise detection and median filtering\n
To determine the
noise pixels, we defined a simple criterias
It is being called adaptive because it changes it property after each iterations

![image](https://user-images.githubusercontent.com/87460369/145703523-8050efb0-7a82-4aa4-8b31-c395c6083b75.png)
![image](https://user-images.githubusercontent.com/87460369/145703528-5512e13a-91bd-4b2a-a773-fd163b6d0487.png)


# Contrast Enhancement using CLAHE

## Normal Histogram Equalization
Histogram equalization is a basic image processing technique that
adjusts the global contrast of an image by updating the image
histogram’s pixel intensity distribution. Doing so enables areas of low
contrast to obtain higher contrast in the output image.
Essentially, histogram equalization works by:
• Computing a histogram of image pixel intensities
• Evenly spreading out and distributing the most frequent pixel values
(i.e., the ones with the largest counts in the histogram)
• Giving a linear trend to the cumulative distribution function (CDF)

![image](https://user-images.githubusercontent.com/87460369/145703578-b605469f-f88d-40e0-9dcd-dacc3e6b3f37.png)

## X-Ray Original vs X-Ray histogram equalized plot

![image](https://user-images.githubusercontent.com/87460369/145703930-50a18c91-2bc4-4ac1-ba13-96ef57415aa3.png)   ![image](https://user-images.githubusercontent.com/87460369/145703934-08428f5a-c00e-4d8d-8a84-d600e6694b50.png)


## Contrast limited Adaptive Histogram equalization(CLAHE)
• CLAHE limits the amplification by clipping the histogram at a predefined value before computing
the CDF. <br>
• In this we limit the slope of transformation function by a so called clip limit.<br>
• It is advantageous not to discard the part of the histogram that exceeds the clip limit but to
redistribute it equally among all histogram bins

## X-Ray Original vs X-Ray CLAHE equalized

![image](https://user-images.githubusercontent.com/87460369/145704003-2e726577-39b0-4d40-a4b2-6fad1768287a.png)

## X-Ray Original vs X-Ray CLAHE equalized plot

![image](https://user-images.githubusercontent.com/87460369/145704022-99a218c8-98fe-447f-8fda-043ee943eab5.png)
![image](https://user-images.githubusercontent.com/87460369/145704030-f6ff6851-94ed-4a2b-bd0d-4dd594b75d5a.png)


