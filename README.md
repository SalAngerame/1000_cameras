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
Although this data contains a lot of information, it doesn't contain much of the important information needed to make a good conclusion on the best camera. One of the things that was wrong with it was that it didn't describe the units of measurment it was using for some of it's data. This involved having to do research beyond the data and correlate with the numbers present and then adding it onto the data. Another key issue found was that it didn't include a lot of physical measurments of the cameras themselves. It included a dimensions column, but after doing some searching trying to decipher what the numbers meant, it only gave the width of the camera itself, lacking the rest of the measurments. It also lacked the sensor size (full-frame, APS-C, micro four thirds, etc.). This lead to many issues on attempting to analize which camera produced a truly high quality image. The only way to get image quality was from the "effective pixels" column (the count of the amount of pixels within a sensor in measurments of megapixels). The count of how many megapixels is only part of what produces a good quality image. Too many megapixels can actually be a negative thing depending if the sensor is small enough, making the photo grainer and less detailed due to smaller pixels recieving less light. Having a lot of pixels that can't recieve a lot of light can give your photos a "static" look to them. The larger sensors, however, can recieve more light, thus, eliminating the potential for that grainy look to the photos. There are equations that can be plugged in to find the sensor size (Senor Size = (Focal Length * Field of View) / Working Distance) Or (Sensor Size (mm) = Pixel Size (um) * Resolution). The problem is that the math requires you to have information about the camera, such as pixel size or field of view. In order to get those, you would need to know the sensor size, so any equation possible on getting any of that data that way is not possible in this case due to the limit data. 











Intro Picture: https://www.amazon.com/s?k=cameras+that+print+pictures&adgrpid=1339205726322904&hvadid=83700428831171&hvbmt=be&hvdev=c&hvlocphy=77889&hvnetw=o&hvqmt=e&hvtargid=kwd-83700700921784%3Aloc-190&hydadcr=18478_10807015&mcid=31b2c672769b3bc1a279fd7a66982f68&msclkid=ba27129d633a110d16377b970fff874c&tag=mh0b-20&ref=pd_sl_491a2okmrh_e
