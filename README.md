# Finding The Best Camera Overall

![Intro Background Slide](https://github.com/user-attachments/assets/8f5b0b6a-3fe6-4bc7-80dc-e2a40079b2fb)
## Overview
Photography can look like a dounting hobby to get into. There are many variables to consider when wanting to take up on the art of capturing a photo, such as quality of the camera, the kind of lens to use, what kind of pictures you're trying to take, and much more. When it comes to photography, there are many ways to pursue it. For some people, it involves buying multiple cameras and multiple lenes for different subjects they want to take a picture of. Whether it's landscape photos, close-ups of animals, portraits, moon photography, etc. Having one camera, however, is the go-to option for some people, for a lot of good reasons. That's why in this repository the goal is to find one camera that can do a little bit of everything, and do it well at the same time.
The objective here is to break it down and find a camera that is the best overall in terms of its specs. This uses a dataset that contains 1000 rows (each row a different camera) and 13 columns giving the specs of each of the camera.
## The Questions Being Tackled:
- Which camera can produce high quality images?
- Which camera has verstile uses?
- Out of the last two questions, which camera has both?
- Is there both an expensive option and a cheaper option?
## Data Drawbacks
![istockphoto-178974109-612x612](https://github.com/user-attachments/assets/8672e732-ab56-4b98-8c75-6ce9104b7815)

Although this data contains a lot of information, it doesn't contain much of the important information needed to make a good conclusion on the best camera. One of the things that was wrong with it was that it didn't describe the units of measurment it was using for some of it's data. This involved having to do research beyond the data and correlate with the numbers present and then adding it onto the data. Another key issue found was that it didn't include a lot of physical measurments of the cameras themselves. It included a dimensions column, but after doing some searching trying to decipher what the numbers meant, it only gave the width of the camera itself, lacking the rest of the measurments. It also lacked the sensor size (full-frame, APS-C, micro four thirds, etc.). This lead to many issues on attempting to analize which camera produced a truly high quality image. The only way to get image quality was from the "effective pixels" column (the count of the amount of pixels within a sensor in measurments of megapixels). The count of how many megapixels is only part of what produces a good quality image. Too many megapixels can actually be a negative thing depending if the sensor is small enough, making the photo grainer and less detailed due to smaller pixels recieving less light. Having a lot of pixels that can't recieve a lot of light can give your photos a "static" look to them. The larger sensors, however, can recieve more light, thus, eliminating the potential for that grainy look to the photos. There are equations that can be plugged in to find the sensor size (Senor Size = (Focal Length * Field of View) / Working Distance) Or (Sensor Size (mm) = Pixel Size (um) * Resolution). The problem is that the math requires you to have information about the camera, such as pixel size or field of view. In order to get those, you would need to know the sensor size, so any equation possible on getting any of that data that way is not possible in this case due to the limit data. 

## Camera Image Quality
The quality of a camera's image was determined by the megapixel count. A bar graph was made on the top 10 cameras (out of 1000) with the highest megapixel count, and then manually adding in their sensor sizes. The prices of each of the camera were also determined, giving a range on what the cost would look like for one of these cameras.
<img width="984" height="989" alt="Top 10 Camera Models With Highest Amount of Megapixels Compared to Their Prices" src="https://github.com/user-attachments/assets/a7a544c9-aaae-4a94-8b1f-518a537d8bfe" />

Here gives a representation on what sensor sizes looks like in a camera.
<img width="610" height="274" alt="common-camera-sensor-sizes-610x274" src="https://github.com/user-attachments/assets/fa4e16c0-f823-46bf-8c12-4753a7657b59" />

## Versatiliy Of The Cameras
The versatility of the cameras was determined by their ​focal lengths. Some lenses​ allow the user to change​ the focal length, allowing for more versatility ​compared to lenes that have a fixed focal length. The graph takes those same 10 cameras and shows their focal length capability. The single red bars represent cameras with a fixed focal length, giving them limited shooting capabilities. The cameras with both red and orange bars show that they can change their focal length, giving them more of a range of environments they can shoot at.​
<img width="1189" height="1189" alt="The Cameras&#39; Focal Length Range" src="https://github.com/user-attachments/assets/668d51c2-926c-46ed-aac6-da1fbb2c3dfb" /> 

Here gives a representation on what focal length looks like in a camera.
![what-is-focal-length-1-1200x675](https://github.com/user-attachments/assets/0121a4ea-f0dd-4e6a-a9f2-0d5d91356cfd)

##Conclusion
The first graph establishes the price range of the top 10 cameras with the highest megapixel count. The Canon EOS-1Ds Mark III has the best quality, but is the most expensive at a price of $7999, while the Kodak DCS SLR/n, Kodak DCS SLR/c, and Kodak DCS 14n are the cheapest options with great quality at $129.​ The Canon Powershot A650 IS has the most versatility, with the ability to change its focal length.​ Out of both the graphs measuring quality and versatility, the Canon Powershot A650 IS is the best camera overall, with a count of 12 megapixels, a sensor size of 7.53 x 5.64 mm, and a focal length range of  35 mm to 210 mm, all for the price of $399. This camera demonstrates a balance between producing great quality images while also having the ability to shoot in different types of environments.​ The images below show the camera itself and pictures taken from that same camera.
![il_1080xN 6480940916_dptq](https://github.com/user-attachments/assets/36c72565-f728-43be-897d-9c4855694558)
![Sample Photo 1](https://github.com/user-attachments/assets/65a5f505-6a4e-478b-8111-208582111e13)
![Sample Photo 2](https://github.com/user-attachments/assets/813a342d-548c-472a-b1b5-57fbe4db678e)
![Sample Photo 3](https://github.com/user-attachments/assets/e789a4ea-a2af-4549-931c-83340a29b40b)

Work Cited
Intro Background Image - https://www.amazon.com​
Data Drawbacks Image – 1,500+ Broken Camera Lens Stock Photos, Pictures & Royalty-Free Images - iStock​
Camera Sensors Sizes Image - Camera Sensor Sizes Explained - Full-Frame vs APS-C​
Focal Length Image - FOCAL LENGTH COMPARISON - What is focal length?​
Canon Powershot A650 IS Image - https://i.etsystatic.com​
Canon Powershot A650 IS Sample Photos - Canon POWERSHOT A650 IS sample photo - qa3nY6Qcl0 - ExploreCams​
