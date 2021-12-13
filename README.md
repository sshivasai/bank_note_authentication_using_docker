# Bank Note Authentication
### Bank Note Authentication Data Set
Download: Data Folder, Data Set Description

Abstract: Data were extracted from images that were taken for the evaluation of an authentication procedure for banknotes.

Data Set Characteristics:

Multivariate

Number of Instances:

1372

Source:

Owner of database: Volker Lohweg (University of Applied Sciences, Ostwestfalen-Lippe, volker.lohweg '@' hs-owl.de) Donor of database: Helene DÃ¶rksen (University of Applied Sciences, Ostwestfalen-Lippe, helene.doerksen '@' hs-owl.de) Date received: August, 2012

Data Set Information:

Data were extracted from images that were taken from genuine and forged banknote-like specimens. For digitization, an industrial camera usually used for print inspection was used. The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 660 dpi were gained. Wavelet Transform tool were used to extract features from images.

Attribute Information:

  1. variance of Wavelet Transformed image (continuous)
  2. skewness of Wavelet Transformed image (continuous)
  3. curtosis of Wavelet Transformed image (continuous)
  4. entropy of image (continuous)
  5. class (integer)


![download](https://user-images.githubusercontent.com/64718250/145863521-ead15b3f-adbc-456c-8455-c2237e127c8c.png)


Used:
  1.Python
  2. Numpy
  3. Pandas
  4. Sklearn
  5. Heroku
  6. Docker for Containerizing.


 ![dockercycle1](https://user-images.githubusercontent.com/64718250/145864388-b0e957a4-92b9-45d6-83cd-0745b70ade06.png)



To run the application on local machine:
  1. Download the zip file and extract
  2. Run pip install requirements.txt
  3. Run theh command "python app.py"


To Dockerrize the Whole Project:
  1. Download Docker for Desktop
  2. using command "docker build" or by clicking the option build image in vscode
  3. After sucessfull building of docker image, deploy the docker image on heroku using Container Registry 


Final Project:
![image](https://user-images.githubusercontent.com/64718250/145864718-edbaf40f-256a-4a78-bf26-bc676cfc6a65.png)

